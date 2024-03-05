FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pillow
COPY . /app/
EXPOSE 8000
EXPOSE 8001
CMD ["daphne", "core.asgi:application", "-p", "8001", "-b", "127.0.0.1"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]