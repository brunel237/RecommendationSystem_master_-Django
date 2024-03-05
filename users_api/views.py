import json
from django.http import JsonResponse
from rest_framework import generics, viewsets, permissions
from rest_framework.views import APIView
from courses_api.serializers import *

from .models import *
from .serializers import *



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    
    def retrieve(self, request, id):
        school_elder = SchoolElder.objects.get(pk=id)
        serializer = SchoolElderSerializer(school_elder)
        serialized_data = serializer.data
        return JsonResponse(serialized_data)
    
    def user_list(self, request=None, validated_data=None):
        users = User.objects.all()
        resp = []
        for user in users:
            user = user.get_user()
            try:
                if user.user.status == 'student':
                    resp.append(StudentSerializer(user).data)
                elif user.user.status == 'school_elder':
                    resp.append(SchoolElderSerializer(user).data)
                else:
                    resp.append(LecturerSerializer(user).data)
            except Exception as e:
                return JsonResponse(str(e), status=400, safe=False)
        return JsonResponse(resp, safe=False)
    
    def user_retrieve(self,request=None, id=None):
        if id == 0:
            id = request.user.id
        user_data = display_user(id)
        if user_data:
            return JsonResponse({"success":True, "message":user_data})
        return JsonResponse({"success":False, "message":"User not Found"})
    
    def update(self, request, id):
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'success':False, 'message': 'User not found'}, status=404)

        if request.user != user or request.user.is_superuser:
            return JsonResponse({'success':False, 'message': 'Action Denied !'}, status=405)

        serializer = self.get_serializer(data=request.data, instance=user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        if user.status == "student":
            user_type = Student.objects.get(user=user)
            slz = StudentSerializer(instance=user_type, data=request.data, partial=True)
        elif user.status == "school_elder":
            user_type = SchoolElder.objects.get(user=user)
            slz = SchoolElderSerializer(instance=user_type, data=request.data, partial=True)
        else:
            user_type = Lecturer.objects.get(user=user)
            slz = LecturerSerializer(instance=user_type, data=request.data, partial=True)
        
        slz.is_valid(raise_exception=True)
        slz.save()
        
        
        return JsonResponse({'success':True, 'message':slz.data})
    
    def destroy(self, request, id, *args, **kwargs):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'success':False, 'message': 'User not found'}, status=404)

        if not request.user.is_superuser and request.user != user:
            return JsonResponse({'success':False, 'message': 'Action Denied !'}, status=405)

        return super().destroy(request, *args, **kwargs)

    def follow(self, request=None, id=None):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'success':False, 'message': 'User not found'}, status=404)

        if user.status == "school_elder":
            this_user = SchoolElder.objects.get(user=user)
        elif user.status == "lecturer":
            this_user = Lecturer.objects.get(user=user)

        message = request.user.follow(this_user)

        return JsonResponse({"message": message}, status=200)

    def search_user(self, request, search=None):
        query = search
        if query:
            users = User.objects.filter(first_name__icontains=query).values_list('id', flat=True)
            users2 = User.objects.filter(last_name__icontains=query).values_list('id', flat=True)
            results = []
            for u1 in list(users):
                results.append(display_user(u1))
            for u2 in list(users2):
                if u2 not in list(users):
                    results.append(display_user(u2))
        else:
            results = []
        
        return JsonResponse({'success': True, 'message': results})

    

def display_user(id):
    try:
        user = User.objects.get(id=id)
        user = user.get_user()
        if user.user.status=="student":
            serialized_message = StudentSerializer(user)
            courses = serialized_message.data["courses_attending"]
            sm = serialized_message.data
            if len(courses) >0:
                alc = AcademicLevelCourse.objects.filter(course_id__in=courses)
                slz_alc = AcademicLevelCourseSerializer(alc, many=True)
                sm["courses_attending"] = slz_alc.data
        elif user.user.status=="school_elder":
            serialized_message = SchoolElderSerializer(user)
            courses = serialized_message.data["courses_attending"]
            sm = serialized_message.data
            if len(courses) >0:
                alc = AcademicLevelCourse.objects.filter(course_id__in=courses)
                slz_alc = AcademicLevelCourseSerializer(alc, many=True)
                sm["courses_attending"] = slz_alc.data
        else:
            serialized_message = LecturerSerializer(user)
            courses = serialized_message.data["lectures"]
            sm = serialized_message.data
            if len(courses) >0:
                alc = AcademicLevelCourse.objects.filter(course_id__in=courses)
                slz_alc = AcademicLevelCourseSerializer(alc, many=True)
                sm["lectures"] = slz_alc.data
        
        return sm
    except Exception as e:
        return str(e)
