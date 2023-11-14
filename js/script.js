jQuery(document).ready(function($) {
	
	"use strict";
	
//------- Notifications Dropdowns
  $('.top-area > .setting-area > li').on("click",function(){
	$(this).siblings().children('div').removeClass('active');
	$(this).children('div').addClass('active');
	return false;
  });
//------- remove class active on body
  $("body *").not('.top-area > .setting-area > li').on("click", function() {
	$(".top-area > .setting-area > li > div").removeClass('active');		
 });
	

//--- user setting dropdown on topbar	
$('.user-img').on('click', function() {
	$('.user-setting').toggleClass("active");
	return false;
});	
	
//--- side message box	
$('.friendz-list > li, .chat-users > li').on('click', function() {
	$('.chat-box').addClass("show");
	return false;
});	
	$('.close-mesage').on('click', function() {
		$('.chat-box').removeClass("show");
		return false;
	});	
	
//------ scrollbar plugin
	if ($.isFunction($.fn.perfectScrollbar)) {
		$('.dropdowns, .twiter-feed, .invition, .followers, .chatting-area, .peoples, #people-list, .chat-list > ul, .message-list, .chat-users, .left-menu').perfectScrollbar();
	}

/*--- socials menu scritp ---*/	
	$('.trigger').on("click", function() {
	    $(this).parent(".menu").toggleClass("active");
	  });
	
/*--- emojies show on text area ---*/	
	$('.add-smiles > span').on("click", function() {
	    $(this).parent().siblings(".smiles-bunch").toggleClass("active");
	  });

// delete notifications
$('.notification-box > ul li > i.del').on("click", function(){
    $(this).parent().slideUp();
	return false;
  }); 	

/*--- socials menu scritp ---*/	
	$('.f-page > figure i').on("click", function() {
	    $(".drop").toggleClass("active");
	  });

//===== Search Filter =====//
	(function ($) {
	// custom css expression for a case-insensitive contains()
	jQuery.expr[':'].Contains = function(a,i,m){
	  return (a.textContent || a.innerText || "").toUpperCase().indexOf(m[3].toUpperCase())>=0;
	};

	function listFilter(searchDir, list) { 
	  var form = $("<form>").attr({"class":"filterform","action":"#"}),
	  input = $("<input>").attr({"class":"filterinput","type":"text","placeholder":"Search Contacts..."});
	  $(form).append(input).appendTo(searchDir);

	  $(input)
	  .change( function () {
		var filter = $(this).val();
		if(filter) {
		  $(list).find("li:not(:Contains(" + filter + "))").slideUp();
		  $(list).find("li:Contains(" + filter + ")").slideDown();
		} else {
		  $(list).find("li").slideDown();
		}
		return false;
	  })
	  .keyup( function () {
		$(this).change();
	  });
	}

//search friends widget
	$(function () {
	  listFilter($("#searchDir"), $("#people-list"));
	});
	}(jQuery));	

//progress line for page loader
	$('body').show();
	NProgress.start();
	setTimeout(function() { NProgress.done(); $('.fade').removeClass('out'); }, 2000);
	
//--- bootstrap tooltip	
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip();
	});
	
// Sticky Sidebar & header
	if($(window).width() < 769) {
		jQuery(".sidebar").children().removeClass("stick-widget");
	}

	if ($.isFunction($.fn.stick_in_parent)) {
		$('.stick-widget').stick_in_parent({
			parent: '#page-contents',
			offset_top: 60,
		});

		
		$('.stick').stick_in_parent({
		    parent: 'body',
            offset_top: 0,
		});
		
	}
	
/*--- topbar setting dropdown ---*/	
	$(".we-page-setting").on("click", function() {
	    $(".wesetting-dropdown").toggleClass("active");
	  });	
	  
/*--- topbar toogle setting dropdown ---*/	
$('#nightmode').on('change', function() {
    if ($(this).is(':checked')) {
        // Show popup window
        $(".theme-layout").addClass('black');	
    }
	else {
        $(".theme-layout").removeClass("black");
    }
});

//chosen select plugin
if ($.isFunction($.fn.chosen)) {
	$("select").chosen();
}

//----- add item plus minus button
if ($.isFunction($.fn.userincr)) {
	$(".manual-adjust").userincr({
		buttonlabels:{'dec':'-','inc':'+'},
	}).data({'min':0,'max':20,'step':1});
}	
	
if ($.isFunction($.fn.loadMoreResults)) {	
	$('.loadMore').loadMoreResults({
		displayedItems: 3,
		showItems: 1,
		button: {
		  'class': 'btn-load-more',
		  'text': 'Load More'
		}
	});	
}
	//===== owl carousel  =====//
	if ($.isFunction($.fn.owlCarousel)) {
		$('.sponsor-logo').owlCarousel({
			items: 6,
			loop: true,
			margin: 30,
			autoplay: true,
			autoplayTimeout: 1500,
			smartSpeed: 1000,
			autoplayHoverPause: true,
			nav: false,
			dots: false,
			responsiveClass:true,
				responsive:{
					0:{
						items:3,
					},
					600:{
						items:3,

					},
					1000:{
						items:6,
					}
				}

		});
	}
	
// slick carousel for detail page
	if ($.isFunction($.fn.slick)) {
	$('.slider-for-gold').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		slide: 'li',
		fade: false,
		asNavFor: '.slider-nav-gold'
	});
	
	$('.slider-nav-gold').slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		asNavFor: '.slider-for-gold',
		dots: false,
		arrows: true,
		slide: 'li',
		vertical: true,
		centerMode: true,
		centerPadding: '0',
		focusOnSelect: true,
		responsive: [
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				infinite: true,
				vertical: false,
				centerMode: true,
				dots: false,
				arrows: false
			}
		},
		{
			breakpoint: 641,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				infinite: true,
				vertical: true,
				centerMode: true,
				dots: false,
				arrows: false
			}
		},
		{
			breakpoint: 420,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				infinite: true,
				vertical: false,
				centerMode: true,
				dots: false,
				arrows: false
			}
		}	
		]
	});
}
	
//---- responsive header
	
$(function() {

	//	create the menus
	$('#menu').mmenu();
	$('#shoppingbag').mmenu({
		navbar: {
			title: 'General Setting'
		},
		offCanvas: {
			position: 'right'
		}
	});

	//	fire the plugin
	$('.mh-head.first').mhead({
		scroll: {
			hide: 200
		}
		
	});
	$('.mh-head.second').mhead({
		scroll: false
	});

	
});		

//**** Slide Panel Toggle ***//
	  $("span.main-menu").on("click", function(){
	     $(".side-panel").addClass('active');
		  $(".theme-layout").addClass('active');
		  return false;
	  });

	  $('.theme-layout').on("click",function(){
		  $(this).removeClass('active');
	     $(".side-panel").removeClass('active');
		  
	     
	  });

	  
// login & register form
	$('button.signup').on("click", function(){
		$('.login-reg-bg').addClass('show');
		return false;
	  });
	  
	  $('.already-have').on("click", function(){
		$('.login-reg-bg').removeClass('show');
		return false;
	  });
	
//----- count down timer		
	if ($.isFunction($.fn.downCount)) {
		$('.countdown').downCount({
			date: '11/12/2018 12:00:00',
			offset: +10
		});
	}
	
/** Post a Comment **/
jQuery(".post-comt-box textarea").on("keydown", function(event) {

	if (event.keyCode == 13) {
		var comment = jQuery(this).val();
		var parent = jQuery(".showmore").parent("li");
		var comment_HTML = '	<li><div class="comet-avatar"><img src="images/resources/comet-1.jpg" alt=""></div><div class="we-comment"><div class="coment-head"><h5><a href="time-line.html" title="">Jason borne</a></h5><span>1 year ago</span><a class="we-reply" href="#" title="Reply"><i class="fa fa-reply"></i></a></div><p>'+comment+'</p></div></li>';
		$(comment_HTML).insertBefore(parent);
		jQuery(this).val('');
	}
}); 
/** Post a publication **/	

//inbox page 	
//***** Message Star *****//  
    $('.message-list > li > span.star-this').on("click", function(){
    	$(this).toggleClass('starred');
    });


//***** Message Important *****//
    $('.message-list > li > span.make-important').on("click", function(){
    	$(this).toggleClass('important-done');
    });

    

// Listen for click on toggle checkbox
	$('#select_all').on("click", function(event) {
	  if(this.checked) {
	      // Iterate each checkbox
	      $('input:checkbox.select-message').each(function() {
	          this.checked = true;
	      });
	  }
	  else {
	    $('input:checkbox.select-message').each(function() {
	          this.checked = false;
	      });
	  }
	});


	$(".delete-email").on("click",function(){
		$(".message-list .select-message").each(function(){
			  if(this.checked) {
			  	$(this).parent().slideUp();
			  }
		});
	});

// change background color on hover
	$('.category-box').hover(function () {
		$(this).addClass('selected');
		$(this).parent().siblings().children('.category-box').removeClass('selected');
	});
	
	
//------- offcanvas menu 

	const menu = document.querySelector('#toggle');  
	const menuItems = document.querySelector('#overlay');  
	const menuContainer = document.querySelector('.menu-container');  
	const menuIcon = document.querySelector('.canvas-menu i');  

	function toggleMenu(e) {
		menuItems.classList.toggle('open');
		menuContainer.classList.toggle('full-menu');
		menuIcon.classList.toggle('fa-bars');
		menuIcon.classList.add('fa-times');
		e.preventDefault();
	}

	if( menu ) {
		menu.addEventListener('click', toggleMenu, false);	
	}
	
// Responsive nav dropdowns
	$('.offcanvas-menu li.menu-item-has-children > a').on('click', function () {
		$(this).parent().siblings().children('ul').slideUp();
		$(this).parent().siblings().removeClass('active');
		$(this).parent().children('ul').slideToggle();
		$(this).parent().toggleClass('active');
		return false;
	});	
	


});//document ready end


function setCookie(cname, cvalue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
	let expires = "expires="+d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
  
function getCookie(cname) {
	let name = cname + "=";
	let ca = document.cookie.split(';');
	for(let i = 0; i < ca.length; i++) {
	  let c = ca[i];
	  while (c.charAt(0) == ' ') {
		c = c.substring(1);
	  }
	  if (c.indexOf(name) == 0) {
		return c.substring(name.length, c.length);
	  }
	}
	return "";
}
  
function checkCookie() {
	let user = getCookie("username");
	if (user != "") {
	  alert("Welcome again " + user);
	} else {
	  user = prompt("Please enter your name:", "");
	  if (user != "" && user != null) {
		setCookie("username", user, 365);
	  }
	}
} 

function load_auth_container(id, id2){
	let container = document.getElementById(id);
	let container2 = document.getElementById(id2);
	var temp = container2.innerHTML
	container2.innerHTML = container.innerHTML
	container.innerHTML = temp
}

function sendAuthRequest(url, formData, errorZone) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");

	xhr.onreadystatechange = function() {
		if (xhr.readyState === XMLHttpRequest.DONE) {
			if (xhr.status === 200 || xhr.status === 201) {
			var response = JSON.parse(xhr.responseText);
			var authToken = response.token;
			var userData = response.user;

			setCookie("token", authToken, 365);
			setCookie("id", userData.id, 365);
			setCookie("username", userData.username, 365);
			setCookie("first_name", userData.first_name, 365);
			setCookie("last_name", userData.last_name, 365);
			setCookie("status", userData.status, 365);
			setCookie("profile_picture", userData.profile_picture, 365);

			window.location.href = "index.html";

			} else {
				var response = JSON.parse(xhr.responseText);
				var errorMessage = document.getElementById(errorZone);
				errorMessage.innerHTML = response.message;
			}
		}
	}
	xhr.send(JSON.stringify(formData));
}

function getCoursesData(invoker, url, choice_name){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");


	xhr.onreadystatechange = function() {
		if (xhr.readyState === XMLHttpRequest.DONE) {
			if (xhr.status === 200 || xhr.status === 201) {
			var response = JSON.parse(xhr.responseText);
			
			response.forEach(element => {
				var new_div = `<div class="d-flex"  style="font-size: 0.75em; padding: 0.5em 0em">
					<div style="width: 70%;">
						${element.course.course_code} - 
						${element.course.course_name} - 
						${element.level.level} -
						department of : ${element.department.department_of}
					</div>
					<i class="mtrl-select"></i>
					<input type="checkbox" id="${choice_name}-${element.id}" name="courses" value=${element.id} required="required" style="width: 20%;"/>
				</div>`

				invoker.innerHTML += new_div
			}); 

			} else {
				var response = JSON.parse(xhr.responseText);
				invoker.innerHTML = response.message
			}
		}
	}
	xhr.send();
}

function displayChoiceContent(id){
	if (id == "student-regis-radio"){
		document.getElementById("student-regis").style.display = "block"
		var stud_div = document.getElementById("courses-list-1")
		stud_div.innerHTML = ""
		document.getElementById("se-regis").style.display = "none"
		document.getElementById("lecturer-regis").style.display = "none"

		getCoursesData(stud_div, "http://127.0.0.1:8000/api/courses/details/", "courses_attending")
	}
	else if (id == "se-regis-radio"){
		document.getElementById("se-regis").style.display = "block"
		var stud_div = document.getElementById("courses-list-2")
		stud_div.innerHTML = ""
		document.getElementById("student-regis").style.display = "none"
		document.getElementById("lecturer-regis").style.display = "none"

		getCoursesData(stud_div, "http://127.0.0.1:8000/api/courses/details/", "courses_attending")
	}
	else{
		document.getElementById("lecturer-regis").style.display = "block"
		var stud_div = document.getElementById("courses-list-3")
		stud_div.innerHTML = ""
		document.getElementById("student-regis").style.display = "none"
		document.getElementById("se-regis").style.display = "none"

		getCoursesData(stud_div, "http://127.0.0.1:8000/api/courses/details/", "lectures")
	}
}

var  pp = null

function uploadImageRegis(event){
	const file = event.target.files[0];
	const reader = new FileReader();

	if (! event.target.files || ! event.target.files.length){
		const defaultProfilePicture = fetch("/images/profile_default.png")
		.then(response => response.blob())
		.then(blob => new File([blob], 'profile_default.png'));
		pp = defaultProfilePicture
	}
	else{
		reader.onload = (event) => {
			pp = event.target.result;
		};
	}

	reader.readAsDataURL(file);
}

var regisForm = document.querySelector("div#regis_container form");

function registration(){
	
	var  username =  document.getElementById("regis-username").value;
	var  password =  document.getElementById("regis-password").value;
	var  password_confirm =  document.getElementById("password_confirm").value;
	var  first_name =  document.getElementById("first_name").value;
	var  last_name =  document.getElementById("last_name").value;
	var  date_of_birth =  document.getElementById("date_of_birth").value;
	var  sex =  document.querySelector("input[name='sex']:checked").value
	var  email =  document.getElementById("email").value;
	var  registration_number =  document.getElementById("registration_number").value;
	var  phone_number =  document.getElementById("phone_number").value;
	var  address =  document.getElementById("address").value;
	var  profile_picture =  document.getElementById("profile_picture").files[0];
	var  status =  document.querySelector("input[name='status']:checked").value
	
	var today = new Date();
	var err = document.getElementById("errorMessage-regis")
	err.innerHTML = "";

	var dob = new Date(date_of_birth)
	var numregex = /^[0-9]+$/ ;

	if ((password != password_confirm)||(password.length < 6)){
		err.innerHTML = "password too short or passwords unidentical"
		return;
	}
	if (!numregex.test(phone_number) || phone_number.length != 9){
		err.innerHTML = "Invalid phone number. 9 numeric digits required"
		return;
	}
	if (isNaN(dob.getTime()) || dob >= today){
		err.innerHTML = "Invalid date of birth"
		return;
	}
	if (username.length < 5){
		err.innerHTML = "Invalid username, atleast 5 characters"
		return;
	}
	if (registration_number.length < 6){
		err.innerHTML = "Invalid registration number, atleast 6 characters"
		return;
	}

	var formData = {
		"username" : username,
		"password" : password,
		"first_name" : first_name,
		"last_name" : last_name,
		"sex" : sex,
		"date_of_birth" : date_of_birth,
		"registration_number" : registration_number,
		"phone_number" : phone_number,
		"email" : email,
		"address" : address,
		"status" : status,
		"profile_picture" : pp
	}

	if (status == "student"){
		var array = document.querySelectorAll("input[name='courses']:checked");
		var courses_attending = Array.from(array).map(function(array) {return Number(array.value);});
		if (courses_attending.length)
			formData["courses_attending"] = courses_attending;
	}
	else if (status == "school_elder"){
		var array = document.querySelectorAll("input[name='courses']:checked");
		var courses_attending = Array.from(array).map(function(array) {return Number(array.value);});
		var bachelor_graduate_since = document.getElementById("bachelor_graduate_since_se").value;
		var master_graduate_since = document.getElementById("master_graduate_since_se").value;
		var bgs = new Date(bachelor_graduate_since)
		var mgs = new Date(master_graduate_since)
		if (mgs && ( mgs < bgs)){
			err.innerHTML = "mismatching certificate dates"
			return;
		}
		if ((mgs && (mgs > today) )||( bgs > today)){
			err.innerHTML = "mismatching certificate dates"
			return;
		}
		if (courses_attending.length)
			formData["courses_attending"] = courses_attending;
		formData["bachelor_graduate_since"] = bachelor_graduate_since;
		if (master_graduate_since)
			formData["master_graduate_since"] = master_graduate_since;
	}
	else {
		var bachelor_graduate_since = document.getElementById("bachelor_graduate_since").value;
		var master_graduate_since = document.getElementById("master_graduate_since").value;
		var phd_graduate_since = document.getElementById("phd_graduate_since").value;
		var field_of_research = document.getElementById("field_of_research").value;
		var biography = document.getElementById("biography").value;
		var array = document.querySelectorAll("input[name='courses']:checked");
		var lectures = Array.from(array).map(function(array) { Number(array.value); });
		var bgs = new Date(bachelor_graduate_since)
		var mgs = new Date(master_graduate_since)
		var pgs = new Date(phd_graduate_since); alert(master_graduate_since);
		if ((pgs < mgs)|| (mgs < bgs)){
			err.innerHTML = "mismatching certificate dates"
			return;
		}
		if ((pgs > today)|| (mgs > today) ||( bgs > today)){
			err.innerHTML = "mismatching certificate dates"
			return;
		}
		if (lectures.length)
			formData["lectures"] = lectures;
		formData["bachelor_graduate_since"] = bachelor_graduate_since;
		formData["master_graduate_since"] = master_graduate_since;
		formData["phd_graduate_since"] = phd_graduate_since;
		formData["field_of_research"] = field_of_research;
		if (biography)
			formData["biography"] = biography;
	}
	console.log("formData : " + JSON.stringify(formData));

	formD = new FormData()

	sendAuthRequest("http://127.0.0.1:8000/api/auth/signup/", formData, "errorMessage-regis");
}
