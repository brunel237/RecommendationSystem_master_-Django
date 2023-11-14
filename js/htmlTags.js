// import {user} from 'script.js';


function header(id) {
    document.getElementById(id).innerHTML = `<div class="topbar stick" >
    <div class="logo">
        <a title="" href="index.html"><img src="images/logo.png" alt=""></a>
    </div>
    
    <div class="top-area">
        <div class="top-search">
            <form method="post" class="">
                <input type="text" placeholder="Search Friend">
                <button data-ripple><i class="ti-search"></i></button>
            </form>
        </div>
        <ul class="setting-area">
            <li><a href="newsfeed.html" title="Home" data-ripple=""><i class="ti-home"></i></a></li>
            <li>
                <a href="#" title="Notification" data-ripple="">
                    <i class="ti-bell"></i><span>20</span>
                </a>
                <div class="dropdowns">
                    <span>4 New Notifications</span>
                    <ul class="drops-menu">
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-1.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>sarah Loren</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag green">New</span>
                        </li>
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-2.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>Jhon doe</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag red">Reply</span>
                        </li>
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-3.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>Andrew</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag blue">Unseen</span>
                        </li>
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-4.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>Tom cruse</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag">New</span>
                        </li>
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-5.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>Amy</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag">New</span>
                        </li>
                    </ul>
                    <a href="notifications.html" title="" class="more-mesg">view more</a>
                </div>
            </li>
            <li>
                <a href="#" title="Messages" data-ripple=""><i class="ti-comment"></i><span>12</span></a>
                <div class="dropdowns">
                    <span>5 New Messages</span>
                    <ul class="drops-menu">
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-1.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>sarah Loren</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag green">New</span>
                        </li>
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-2.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>Jhon doe</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag red">Reply</span>
                        </li>
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-3.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>Andrew</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag blue">Unseen</span>
                        </li>
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-4.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>Tom cruse</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag">New</span>
                        </li>
                        <li>
                            <a href="notifications.html" title="">
                                <img src="images/resources/thumb-5.jpg" alt="">
                                <div class="mesg-meta">
                                    <h6>Amy</h6>
                                    <span>Hi, how r u dear ...?</span>
                                    <i>2 min ago</i>
                                </div>
                            </a>
                            <span class="tag">New</span>
                        </li>
                    </ul>
                    <a href="messages.html" title="" class="more-mesg">view more</a>
                </div>
            </li>
            <li><a href="#" title="Languages" data-ripple=""><i class="fa fa-globe"></i></a>
                <div class="dropdowns languages">
                    <a href="#" title=""><i class="ti-check"></i>English</a>
                    <a href="#" title="">Arabic</a>
                    <a href="#" title="">Dutch</a>
                    <a href="#" title="">French</a>
                </div>
            </li>
        </ul>
        <div class="user-img">
            <img src=${getCookie("profile_picture")} alt="profile_picture" style="width:60px; height:60px">
            <span class="status f-online"></span>
            <div class="user-setting">
                <a href="#" title=""><span class="status f-online"></span>online</a>
                <a href="#" title=""><span class="status f-away"></span>away</a>
                <a href="#" title=""><span class="status f-off"></span>offline</a>
                <a href="#" title=""><i class="ti-user"></i> view profile</a>
                <a href="#" title=""><i class="ti-pencil-alt"></i>edit profile</a>
                <a href="#" title=""><i class="ti-target"></i>activity log</a>
                <a href="#" title=""><i class="ti-settings"></i>account setting</a>
                <a href="login.html" title=""><i class="ti-power-off"></i>log out</a>
            </div>
        </div>
        <span class="ti-menu main-menu" data-ripple=""></span>
    </div>
</div>`
}

function responsiveHeader(id) {
    document.getElementById(id).innerHTML = `<div class="responsive-header">
    <div class="mh-head first Sticky">
        <span class="mh-btns-left">
            <a class="" href="#menu"><i class="fa fa-align-justify"></i></a>
        </span>
        <span class="mh-text">
            <a href="index.html" title=""><img src="images/logo2.png" alt=""></a>
        </span>
        <span class="mh-btns-right">
            <a class="fa fa-sliders" href="#shoppingbag"></a>
        </span>
    </div>
    <div class="mh-head second">
        <form class="mh-form">
            <input placeholder="search" />
            <a href="#/" class="fa fa-search"></a>
        </form>
    </div>
    <nav id="menu" class="res-menu">
        <ul>
            <li><span>Home</span>
                <ul>
                    <li><a href="index-2.html" title="">Home Social</a></li>
                    <li><a href="index2.html" title="">Home Social 2</a></li>
                    <li><a href="index-company.html" title="">Home Company</a></li>
                    <li><a href="landing.html" title="">Login page</a></li>
                    <li><a href="logout.html" title="">Logout Page</a></li>
                    <li><a href="newsfeed.html" title="">news feed</a></li>
                </ul>
            </li>
            <li><span>Time Line</span>
                <ul>
                    <li><a href="time-line.html" title="">timeline</a></li>
                    <li><a href="timeline-friends.html" title="">timeline friends</a></li>
                    <li><a href="timeline-groups.html" title="">timeline groups</a></li>
                    <li><a href="timeline-pages.html" title="">timeline pages</a></li>
                    <li><a href="timeline-photos.html" title="">timeline photos</a></li>
                    <li><a href="timeline-videos.html" title="">timeline videos</a></li>
                    <li><a href="fav-page.html" title="">favourit page</a></li>
                    <li><a href="groups.html" title="">groups page</a></li>
                    <li><a href="page-likers.html" title="">Likes page</a></li>
                    <li><a href="people-nearby.html" title="">people nearby</a></li>
                    
                    
                </ul>
            </li>
            <li><span>Account Setting</span>
                <ul>
                    <li><a href="create-fav-page.html" title="">create fav page</a></li>
                    <li><a href="edit-account-setting.html" title="">edit account setting</a></li>
                    <li><a href="edit-interest.html" title="">edit-interest</a></li>
                    <li><a href="edit-password.html" title="">edit-password</a></li>
                    <li><a href="edit-profile-basic.html" title="">edit profile basics</a></li>
                    <li><a href="edit-work-eductation.html" title="">edit work educations</a></li>
                    <li><a href="messages.html" title="">message box</a></li>
                    <li><a href="inbox.html" title="">Inbox</a></li>
                    <li><a href="notifications.html" title="">notifications page</a></li>
                </ul>
            </li>
            <li><span>forum</span>
                <ul>
                    <li><a href="forum.html" title="">Forum Page</a></li>
                    <li><a href="forums-category.html" title="">Fourm Category</a></li>
                    <li><a href="forum-open-topic.html" title="">Forum Open Topic</a></li>
                    <li><a href="forum-create-topic.html" title="">Forum Create Topic</a></li>
                </ul>
            </li>
            <li><span>Our Shop</span>
                <ul>
                    <li><a href="shop.html" title="">Shop Products</a></li>
                    <li><a href="shop-masonry.html" title="">Shop Masonry Products</a></li>
                    <li><a href="shop-single.html" title="">Shop Detail Page</a></li>
                    <li><a href="shop-cart.html" title="">Shop Product Cart</a></li>
                    <li><a href="shop-checkout.html" title="">Product Checkout</a></li>
                </ul>
            </li>
            <li><span>Our Blog</span>
                <ul>
                    <li><a href="blog-grid-wo-sidebar.html" title="">Our Blog</a></li>
                    <li><a href="blog-grid-right-sidebar.html" title="">Blog with R-Sidebar</a></li>
                    <li><a href="blog-grid-left-sidebar.html" title="">Blog with L-Sidebar</a></li>
                    <li><a href="blog-masonry.html" title="">Blog Masonry Style</a></li>
                    <li><a href="blog-list-wo-sidebar.html" title="">Blog List Style</a></li>
                    <li><a href="blog-list-right-sidebar.html" title="">Blog List with R-Sidebar</a></li>
                    <li><a href="blog-list-left-sidebar.html" title="">Blog List with L-Sidebar</a></li>
                    <li><a href="blog-detail.html" title="">Blog Post Detail</a></li>
                </ul>
            </li>
            <li><span>Portfolio</span>
                <ul>
                    <li><a href="portfolio-2colm.html" title="">Portfolio 2col</a></li>
                    <li><a href="portfolio-3colm.html" title="">Portfolio 3col</a></li>
                    <li><a href="portfolio-4colm.html" title="">Portfolio 4col</a></li>
                </ul>
            </li>
            <li><span>Support & Help</span>
                <ul>
                    <li><a href="support-and-help.html" title="">Support & Help</a></li>
                    <li><a href="support-and-help-detail.html" title="">Support & Help Detail</a></li>
                    <li><a href="support-and-help-search-result.html" title="">Support & Help Search Result</a></li>
                </ul>
            </li>
            <li><span>More pages</span>
                <ul>
                    <li><a href="careers.html" title="">Careers</a></li>
                    <li><a href="career-detail.html" title="">Career Detail</a></li>
                    <li><a href="404.html" title="">404 error page</a></li>
                    <li><a href="404-2.html" title="">404 Style2</a></li>
                    <li><a href="faq.html" title="">faq's page</a></li>
                    <li><a href="insights.html" title="">insights</a></li>
                    <li><a href="knowledge-base.html" title="">knowledge base</a></li>
                </ul>
            </li>
            <li><a href="about.html" title="">about</a></li>
            <li><a href="about-company.html" title="">About Us2</a></li>
            <li><a href="contact.html" title="">contact</a></li>
            <li><a href="contact-branches.html" title="">Contact Us2</a></li>
            <li><a href="widgets.html" title="">Widgts</a></li>
        </ul>
    </nav>
    <nav id="shoppingbag">
        <div>
            <div class="">
                <form method="post">
                    <div class="setting-row">
                        <span>use night mode</span>
                        <input type="checkbox" id="nightmode"/> 
                        <label for="nightmode" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>Notifications</span>
                        <input type="checkbox" id="switch2"/> 
                        <label for="switch2" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>Notification sound</span>
                        <input type="checkbox" id="switch3"/> 
                        <label for="switch3" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>My profile</span>
                        <input type="checkbox" id="switch4"/> 
                        <label for="switch4" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>Show profile</span>
                        <input type="checkbox" id="switch5"/> 
                        <label for="switch5" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                </form>
                <h4 class="panel-title">Account Setting</h4>
                <form method="post">
                    <div class="setting-row">
                        <span>Sub users</span>
                        <input type="checkbox" id="switch6" /> 
                        <label for="switch6" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>personal account</span>
                        <input type="checkbox" id="switch7" /> 
                        <label for="switch7" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>Business account</span>
                        <input type="checkbox" id="switch8" /> 
                        <label for="switch8" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>Show me online</span>
                        <input type="checkbox" id="switch9" /> 
                        <label for="switch9" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>Delete history</span>
                        <input type="checkbox" id="switch10" /> 
                        <label for="switch10" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                    <div class="setting-row">
                        <span>Expose author name</span>
                        <input type="checkbox" id="switch11" /> 
                        <label for="switch11" data-on-label="ON" data-off-label="OFF"></label>
                    </div>
                </form>
            </div>
        </div>
    </nav>
</div>`
}


function slidePanel(id) {
    document.getElementById(id).innerHTML = `<script src="js/settings.js"></script>
	<h4 class="panel-title">General Setting</h4>
	<form method="post">
		<div class="setting-row">
			<span>night mode</span>
			<input type="checkbox" id="nightmode1" onchange="handleCheckboxChange(this.id)"/> 
			<label for="nightmode1" data-on-label="ON" data-off-label="OFF"></label>
		</div>
		<div class="setting-row">
			<span>Notifications</span>
			<input type="checkbox" id="switch22"  onchange="handleCheckboxChange(this.id)"/> 
			<label for="switch22" data-on-label="ON" data-off-label="OFF"></label>
		</div>
		<div class="setting-row">
			<span>Notification sound</span>
			<input type="checkbox" id="switch33"  onchange="handleCheckboxChange(this.id)"/> 
			<label for="switch33" data-on-label="ON" data-off-label="OFF"></label>
		</div>
		<!-- <div class="setting-row">
			<span>My profile</span>
			<input type="checkbox" id="switch44" /> 
			<label for="switch44" data-on-label="ON" data-off-label="OFF"></label>
		</div>
		<div class="setting-row">
			<span>Show profile</span>
			<input type="checkbox" id="switch55" /> 
			<label for="switch55" data-on-label="ON" data-off-label="OFF"></label>
		</div> -->
	</form>
	<h4 class="panel-title">Account Setting</h4>
	<form method="post">
		<!-- <div class="setting-row">
			<span>Sub users</span>
			<input type="checkbox" id="switch66" /> 
			<label for="switch66" data-on-label="ON" data-off-label="OFF"></label>
		</div>
		<div class="setting-row">
			<span>personal account</span>
			<input type="checkbox" id="switch77" /> 
			<label for="switch77" data-on-label="ON" data-off-label="OFF"></label>
		</div>
		<div class="setting-row">
			<span>Business account</span>
			<input type="checkbox" id="switch88" /> 
			<label for="switch88" data-on-label="ON" data-off-label="OFF"></label>
		</div> -->
		<div class="setting-row">
			<span>Show me online</span>
			<input type="checkbox" id="switch99" onchange="handleCheckboxChange(this.id)"/> 
			<label for="switch99" data-on-label="ON" data-off-label="OFF"></label>
		</div>
		<div class="setting-row">
			<span>Delete history</span>
			<input type="checkbox" id="switch101" onchange="handleCheckboxChange(this.id)"/> 
			<label for="switch101" data-on-label="ON" data-off-label="OFF"></label>
		</div>
		<!-- <div class="setting-row">
			<span>Expose author name</span>
			<input type="checkbox" id="switch111" /> 
			<label for="switch111" data-on-label="ON" data-off-label="OFF"></label>
		</div> -->
	</form>`
}

function topArea(id){
    document.getElementById(id).innerHTML = `<section>
    <div class="feature-photo">
        <figure><img src="images/resources/timeline-1.jpg" alt=""></figure>
        <div class="add-btn">
            <span>1205 followers</span>
            <a href="#" title="" data-ripple="">Add Friend</a>
        </div>
        <form class="edit-phto">
            <i class="fa fa-camera-retro"></i>
            <label class="fileContainer">
                Edit Cover Photo
            <input type="file"/>
            </label>
        </form>
        <div class="container-fluid">
            <div class="row merged">
                <div class="col-lg-2 col-sm-3">
                    <div class="user-avatar">
                        <figure>
                        <img src=${user.profile_picture} alt="profile_picture" style="width:60px; height:60px">
                            <form class="edit-phto">
                                <i class="fa fa-camera-retro"></i>
                                <label class="fileContainer">
                                    Edit Display Photo
                                    <input type="file"/>
                                </label>
                            </form>
                        </figure>
                    </div>
                </div>
                <div class="col-lg-10 col-sm-9">
                    <div class="timeline-info">
                        <ul>
                            <li class="admin-name">
                              <h5>Janice Griffith</h5>
                              <span>Group Admin</span>
                            </li>
                            <li>
                                <a class="" href="time-line.html" title="" data-ripple="">time line</a>
                                <a class="" href="timeline-photos.html" title="" data-ripple="">Photos</a>
                                <a class="" href="timeline-videos.html" title="" data-ripple="">Videos</a>
                                <a class="active" href="timeline-friends.html" title="" data-ripple="">Friends</a>
                                <a class="" href="timeline-groups.html" title="" data-ripple="">Groups</a>
                                <a class="" href="about.html" title="" data-ripple="">about</a>
                                <a class="" href="#" title="" data-ripple="">more</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>`
}

function footer(id) {
    document.getElementById(id).innerHTML = `<footer>
    <div class="container">
        <div class="row">
            <div class="col-lg-4 col-md-4">
                <div class="widget">
                    <div class="foot-logo">
                        <div class="logo">
                            <a href="index-2.html" title=""><img src="images/logo.png" alt=""></a>
                        </div>	
                        <p>
                            The trio took this simple idea and built it into the world’s leading carpooling platform.
                        </p>
                    </div>
                    <ul class="location">
                        <li>
                            <i class="ti-map-alt"></i>
                            <p>33 new montgomery st.750 san francisco, CA USA 94105.</p>
                        </li>
                        <li>
                            <i class="ti-mobile"></i>
                            <p>+1-56-346 345</p>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-2 col-md-4">
                <div class="widget">
                    <div class="widget-title"><h4>follow</h4></div>
                    <ul class="list-style">
                        <li><i class="fa fa-facebook-square"></i> <a href="https://web.facebook.com/shopcircut/" title="">facebook</a></li>
                        <li><i class="fa fa-twitter-square"></i><a href="https://twitter.com/login?lang=en" title="">twitter</a></li>
                        <li><i class="fa fa-instagram"></i><a href="https://www.instagram.com/?hl=en" title="">instagram</a></li>
                        <li><i class="fa fa-google-plus-square"></i> <a href="https://plus.google.com/discover" title="">Google+</a></li>
                        resources<li><i class="fa fa-pinterest-square"></i> <a href="https://www.pinterest.com/" title="">Pintrest</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-2 col-md-4">
                <div class="widget">
                    <div class="widget-title"><h4>Navigate</h4></div>
                    <ul class="list-style">
                        <li><a href="about.html" title="">about us</a></li>
                        <li><a href="contact.html" title="">contact us</a></li>
                        <li><a href="terms.html" title="">terms & Conditions</a></li>
                        <li><a href="#" title="">RSS syndication</a></li>
                        <li><a href="sitemap.html" title="">Sitemap</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-2 col-md-4">
                <div class="widget">
                    <div class="widget-title"><h4>useful links</h4></div>
                    <ul class="list-style">
                        <li><a href="#" title="">leasing</a></li>
                        <li><a href="#" title="">submit route</a></li>
                        <li><a href="#" title="">how does it work?</a></li>
                        <li><a href="#" title="">agent listings</a></li>
                        <li><a href="#" title="">view All</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-2 col-md-4">
                <div class="widget">
                    <div class="widget-title"><h4>download apps</h4></div>
                    <ul class="colla-apps">
                        <li><a href="https://play.google.com/store?hl=en" title=""><i class="fa fa-android"></i>android</a></li>
                        <li><a href="https://www.apple.com/lae/ios/app-store/" title=""><i class="ti-apple"></i>iPhone</a></li>
                        <li><a href="https://www.microsoft.com/store/apps" title=""><i class="fa fa-windows"></i>Windows</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</footer>`
}

function profileIntro(id){
    document.getElementById(id).innerHTML = `<div class="widget stick-widget">
    <h4 class="widget-title">Profile intro</h4>
    <ul class="short-profile">
        <li>
            <span>about</span>
            <p>Hi, i am jhon kates, i am 32 years old and worked as a web developer in microsoft company. </p>
        </li>
        <li>
            <span>fav tv show</span>
            <p>Hi, i am jhon kates, i am 32 years old and worked as a web developer in microsoft company. </p>
        </li>
        <li>
            <span>favourit music</span>
            <p>Hi, i am jhon kates, i am 32 years old and worked as a web developer in microsoft company. </p>
        </li>
    </ul>
    </div>`
}

function usersList(id){
    document.getElementById(id).innerHTML = `<div class="col-lg-6">
    <div class="central-meta">
        <div class="frnds">
            <ul class="nav nav-tabs">
                 <li class="nav-item"><a class="active" href="#students-list" data-toggle="tab">Students</a> <span id="student-count">55</span></li>
                 <li class="nav-item"><a class="" href="#elder_students-list" data-toggle="tab">Elder Students</a><span id="elder_student-count">60</span></li>
                 <li class="nav-item"><a class="" href="#lecturers-list" data-toggle="tab">Lecturers</a><span id="lecturer-count">60</span></li>
            </ul>

            <!-- Tab panes -->
            <div class="tab-content">
                  <div class="tab-pane active fade show " id="students-list" >
                <ul class="nearby-contct">
                    <li>
                        <div class="nearly-pepls">
                            <figure>
                                <a href="time-line.html" title=""><img src="images/resources/friend-avatar9.jpg" alt=""></a>
                            </figure>
                            <div class="pepl-info">
                                <h4><a href="time-line.html" title="">jhon kates</a></h4>
                                <span>ftv model</span>
                                <a href="#" title="" class="add-butn more-action" data-ripple="">unfriend</a>
                                <a href="#" title="" class="add-butn" data-ripple="">add friend</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="nearly-pepls">
                            <figure>
                                <a href="time-line.html" title=""><img src="images/resources/nearly1.jpg" alt=""></a>
                            </figure>
                            <div class="pepl-info">
                                <h4><a href="time-line.html" title="">sophia Gate</a></h4>
                                <span>tv actresses</span>
                                <a href="#" title="" class="add-butn more-action" data-ripple="">unfriend</a>
                                <a href="#" title="" class="add-butn" data-ripple="">add friend</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="nearly-pepls">
                            <figure>
                                <a href="time-line.html" title=""><img src="images/resources/nearly2.jpg" alt=""></a>
                            </figure>
                            <div class="pepl-info">
                                <h4><a href="time-line.html" title="">sara grey</a></h4>
                                <span>work at IBM</span>
                                <a href="#" title="" class="add-butn more-action" data-ripple="">unfriend</a>
                                <a href="#" title="" class="add-butn" data-ripple="">add friend</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="nearly-pepls">
                            <figure>
                                <a href="time-line.html" title=""><img src="images/resources/nearly3.jpg" alt=""></a>
                            </figure>
                            <div class="pepl-info">
                                <h4><a href="time-line.html" title="">Sexy cat</a></h4>
                                <span>Student</span>
                                <a href="#" title="" class="add-butn more-action" data-ripple="">unfriend</a>
                                <a href="#" title="" class="add-butn" data-ripple="">add friend</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="nearly-pepls">
                            <figure>
                                <a href="time-line.html" title=""><img src="images/resources/nearly4.jpg" alt=""></a>
                            </figure>
                            <div class="pepl-info">
                                <h4><a href="time-line.html" title="">Sara grey</a></h4>
                                <span>ftv model</span>
                                <a href="#" title="" class="add-butn more-action" data-ripple="">unfriend</a>
                                <a href="#" title="" class="add-butn" data-ripple="">add friend</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="nearly-pepls">
                            <figure>
                                <a href="time-line.html" title=""><img src="images/resources/nearly5.jpg" alt=""></a>
                            </figure>
                            <div class="pepl-info">
                                <h4><a href="time-line.html" title="">Amy watson</a></h4>
                                <span>Study in university</span>
                                <a href="#" title="" class="add-butn more-action" data-ripple="">unfriend</a>
                                <a href="#" title="" class="add-butn" data-ripple="">add friend</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="nearly-pepls">
                            <figure>
                                <a href="time-line.html" title=""><img src="images/resources/nearly6.jpg" alt=""></a>
                            </figure>
                            <div class="pepl-info">
                                <h4><a href="time-line.html" title="">caty lasbo</a></h4>
                                <span>work as dancers</span>
                                <a href="#" title="" class="add-butn more-action" data-ripple="">unfriend</a>
                                <a href="#" title="" class="add-butn" data-ripple="">add friend</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="nearly-pepls">
                            <figure>
                                <a href="time-line.html" title=""><img src="images/resources/nearly2.jpg" alt=""></a>
                            </figure>
                            <div class="pepl-info">
                                <h4><a href="time-line.html" title="">Ema watson</a></h4>
                                <span>personal business</span>
                                <a href="#" title="" class="add-butn more-action" data-ripple="">unfriend</a>
                                <a href="#" title="" class="add-butn" data-ripple="">add friend</a>
                            </div>
                        </div>
                    </li>
                </ul>
                <div class="lodmore"><button class="btn-view btn-load-more"></button></div>
            </div>

            <div class="tab-pane fade" id="elder_students-list" >
                <ul class="nearby-contct">
                <li>
                    <div class="nearly-pepls">
                        <figure>
                            <a href="time-line.html" title=""><img src="images/resources/nearly5.jpg" alt=""></a>
                        </figure>
                        <div class="pepl-info">
                            <h4><a href="time-line.html" title="">Amy watson</a></h4>
                            <span>ftv model</span>
                            <a href="#" title="" class="add-butn more-action" data-ripple="">delete Request</a>
                            <a href="#" title="" class="add-butn" data-ripple="">Confirm</a>
                        </div>
                    </div>
                </li>	

                <li>
                    <div class="nearly-pepls">
                        <figure>
                            <a href="time-line.html" title=""><img src="images/resources/nearly1.jpg" alt=""></a>
                        </figure>
                        <div class="pepl-info">
                            <h4><a href="time-line.html" title="">sophia Gate</a></h4>
                            <span>ftv model</span>
                            <a href="#" title="" class="add-butn more-action" data-ripple="">delete Request</a>
                            <a href="#" title="" class="add-butn" data-ripple="">Confirm</a>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="nearly-pepls">
                        <figure>
                            <a href="time-line.html" title=""><img src="images/resources/nearly6.jpg" alt=""></a>
                        </figure>
                        <div class="pepl-info">
                            <h4><a href="time-line.html" title="">caty lasbo</a></h4>
                            <span>ftv model</span>
                            <a href="#" title="" class="add-butn more-action" data-ripple="">delete Request</a>
                            <a href="#" title="" class="add-butn" data-ripple="">Confirm</a>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="nearly-pepls">
                        <figure>
                            <a href="time-line.html" title=""><img src="images/resources/friend-avatar9.jpg" alt=""></a>
                        </figure>
                        <div class="pepl-info">
                            <h4><a href="time-line.html" title="">jhon kates</a></h4>
                            <span>ftv model</span>
                            <a href="#" title="" class="add-butn more-action" data-ripple="">delete Request</a>
                            <a href="#" title="" class="add-butn" data-ripple="">Confirm</a>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="nearly-pepls">
                        <figure>
                            <a href="time-line.html" title=""><img src="images/resources/nearly2.jpg" alt=""></a>
                        </figure>
                        <div class="pepl-info">
                            <h4><a href="time-line.html" title="">sara grey</a></h4>
                            <span>ftv model</span>
                            <a href="#" title="" class="add-butn more-action" data-ripple="">delete Request</a>
                            <a href="#" title="" class="add-butn" data-ripple="">Confirm</a>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="nearly-pepls">
                        <figure>
                            <a href="time-line.html" title=""><img src="images/resources/nearly4.jpg" alt=""></a>
                        </figure>
                        <div class="pepl-info">
                            <h4><a href="time-line.html" title="">Sara grey</a></h4>
                            <span>ftv model</span>
                            <a href="#" title="" class="add-butn more-action" data-ripple="">delete Request</a>
                            <a href="#" title="" class="add-butn" data-ripple="">Confirm</a>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="nearly-pepls">
                        <figure>
                            <a href="time-line.html" title=""><img src="images/resources/nearly3.jpg" alt=""></a>
                        </figure>
                        <div class="pepl-info">
                            <h4><a href="time-line.html" title="">Sexy cat</a></h4>
                            <span>ftv model</span>
                            <a href="#" title="" class="add-butn more-action" data-ripple="">delete Request</a>
                            <a href="#" title="" class="add-butn" data-ripple="">Confirm</a>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="nearly-pepls">
                        <figure>
                            <a href="time-line.html" title=""><img src="images/resources/friend-avatar9.jpg" alt=""></a>
                        </figure>
                        <div class="pepl-info">
                            <h4><a href="time-line.html" title="">jhon kates</a></h4>
                            <span>ftv model</span>
                            <a href="#" title="" class="add-butn more-action" data-ripple="">delete Request</a>
                            <a href="#" title="" class="add-butn" data-ripple="">Confirm</a>
                        </div>
                    </div>
                </li>
                </ul>	
                  <button class="btn-view btn-load-more"></button>
              </div>
            </div>
        </div>
    </div>	
</div>`
}

function followersListSideBar(id){
    document.getElementById(id).innerHTML = `<div class="widget friend-list stick-widget">
    <h4 class="widget-title">Friends</h4>
    <div id="searchDir"></div>
    <ul id="people-list" class="friendz-list">
        <li>
            <figure>
                <img src="images/resources/friend-avatar.jpg" alt="">
                <span class="status f-online"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">bucky barnes</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="c6b1afa8b2a3b4b5a9aaa2a3b486a1aba7afaae8a5a9ab">[email&#160;protected]</a></i>
            </div>
        </li>
        <li>
            <figure>
                <img src="images/resources/friend-avatar2.jpg" alt="">
                <span class="status f-away"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">Sarah Loren</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="82e0e3f0ece7f1c2e5efe3ebeeace1edef">[email&#160;protected]</a></i>
            </div>
        </li>
        <li>
            <figure>
                <img src="images/resources/friend-avatar3.jpg" alt="">
                <span class="status f-off"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">jason borne</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="6f050e1c00010d2f08020e0603410c0002">[email&#160;protected]</a></i>
            </div>
        </li>
        <li>
            <figure>
                <img src="images/resources/friend-avatar4.jpg" alt="">
                <span class="status f-off"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">Cameron diaz</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="147e75677b7a76547379757d783a777b79">[email&#160;protected]</a></i>
            </div>
        </li>
        <li>
            
            <figure>
                <img src="images/resources/friend-avatar5.jpg" alt="">
                <span class="status f-online"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">daniel warber</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="640e05170b0a06240309050d084a070b09">[email&#160;protected]</a></i>
            </div>
        </li>
        <li>
            
            <figure>
                <img src="images/resources/friend-avatar6.jpg" alt="">
                <span class="status f-away"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">andrew</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d3b9b2a0bcbdb193b4beb2babffdb0bcbe">[email&#160;protected]</a></i>
            </div>
        </li>
        <li>
            
            <figure>
                <img src="images/resources/friend-avatar7.jpg" alt="">
                <span class="status f-off"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">amy watson</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="deb4bfadb1b0bc9eb9b3bfb7b2f0bdb1b3">[email&#160;protected]</a></i>
            </div>
        </li>
        <li>
            
            <figure>
                <img src="images/resources/friend-avatar5.jpg" alt="">
                <span class="status f-online"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">daniel warber</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="bbd1dac8d4d5d9fbdcd6dad2d795d8d4d6">[email&#160;protected]</a></i>
            </div>
        </li>
        <li>
            
            <figure>
                <img src="images/resources/friend-avatar2.jpg" alt="">
                <span class="status f-away"></span>
            </figure>
            <div class="friendz-meta">
                <a href="time-line.html">Sarah Loren</a>
                <i><a href="https://wpkixx.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ff9d9e8d919a8cbf98929e9693d19c9092">[email&#160;protected]</a></i>
            </div>
        </li>
    </ul>
    <div class="chat-box">
        <div class="chat-head">
            <span class="status f-online"></span>
            <h6>Bucky Barnes</h6>
            <div class="more">
                <span><i class="ti-more-alt"></i></span>
                <span class="close-mesage"><i class="ti-close"></i></span>
            </div>
        </div>
        <div class="chat-list">
            <ul>
                <li class="me">
                    <div class="chat-thumb"><img src="images/resources/chatlist1.jpg" alt=""></div>
                    <div class="notification-event">
                        <span class="chat-message-item">
                            Hi James! Please remember to buy the food for tomorrow! I’m gonna be handling the gifts and Jake’s gonna get the drinks
                        </span>
                        <span class="notification-date"><time datetime="2004-07-24T18:18" class="entry-date updated">Yesterday at 8:10pm</time></span>
                    </div>
                </li>
                <li class="you">
                    <div class="chat-thumb"><img src="images/resources/chatlist2.jpg" alt=""></div>
                    <div class="notification-event">
                        <span class="chat-message-item">
                            Hi James! Please remember to buy the food for tomorrow! I’m gonna be handling the gifts and Jake’s gonna get the drinks
                        </span>
                        <span class="notification-date"><time datetime="2004-07-24T18:18" class="entry-date updated">Yesterday at 8:10pm</time></span>
                    </div>
                </li>
                <li class="me">
                    <div class="chat-thumb"><img src="images/resources/chatlist1.jpg" alt=""></div>
                    <div class="notification-event">
                        <span class="chat-message-item">
                            Hi James! Please remember to buy the food for tomorrow! I’m gonna be handling the gifts and Jake’s gonna get the drinks
                        </span>
                        <span class="notification-date"><time datetime="2004-07-24T18:18" class="entry-date updated">Yesterday at 8:10pm</time></span>
                    </div>
                </li>
            </ul>
            <form class="text-box">
                <textarea placeholder="Post enter to post..."></textarea>
                <div class="add-smiles">
                    <span title="add icon" class="em em-expressionless"></span>
                </div>
                <div class="smiles-bunch">
                    <i class="em em---1"></i>
                    <i class="em em-smiley"></i>
                    <i class="em em-anguished"></i>
                    <i class="em em-laughing"></i>
                    <i class="em em-angry"></i>
                    <i class="em em-astonished"></i>
                    <i class="em em-blush"></i>
                    <i class="em em-disappointed"></i>
                    <i class="em em-worried"></i>
                    <i class="em em-kissing_heart"></i>
                    <i class="em em-rage"></i>
                    <i class="em em-stuck_out_tongue"></i>
                </div>
                <button type="submit"></button>
            </form>
        </div>
    </div>
</div>`
}

function whoIsFollowing(id){
    document.getElementById(id).innerHTML = `<div class="widget">
    <h4 class="widget-title">Who's follownig</h4>
    <ul class="followers">
        <li>
            <figure><img src="images/resources/friend-avatar2.jpg" alt=""></figure>
            <div class="friend-meta">
                <h4><a href="time-line.html" title="">Kelly Bill</a></h4>
                <a href="#" title="" class="underline">Add Friend</a>
            </div>
        </li>
        <li>
            <figure><img src="images/resources/friend-avatar4.jpg" alt=""></figure>
            <div class="friend-meta">
                <h4><a href="time-line.html" title="">Issabel</a></h4>
                <a href="#" title="" class="underline">Add Friend</a>
            </div>
        </li>
        <li>
            <figure><img src="images/resources/friend-avatar6.jpg" alt=""></figure>
            <div class="friend-meta">
                <h4><a href="time-line.html" title="">Andrew</a></h4>
                <a href="#" title="" class="underline">Add Friend</a>
            </div>
        </li>
        <li>
            <figure><img src="images/resources/friend-avatar8.jpg" alt=""></figure>
            <div class="friend-meta">
                <h4><a href="time-line.html" title="">Sophia</a></h4>
                <a href="#" title="" class="underline">Add Friend</a>
            </div>
        </li>
        <li>
            <figure><img src="images/resources/friend-avatar3.jpg" alt=""></figure>
            <div class="friend-meta">
                <h4><a href="time-line.html" title="">Allen</a></h4>
                <a href="#" title="" class="underline">Add Friend</a>
            </div>
        </li>
    </ul>
</div>`
}

function shortcuts(id){
    document.getElementById(id).innerHTML = `<div class="widget">
    <h4 class="widget-title">Shortcuts</h4>
    <ul class="naves">
        <li>
            <i class="ti-clipboard"></i>
            <a href="newsfeed.html" title="">News feed</a>
        </li>
        <li>
            <i class="ti-mouse-alt"></i>
            <a href="inbox.html" title="">Inbox</a>
        </li>
        <li>
            <i class="ti-files"></i>
            <a href="fav-page.html" title="">My pages</a>
        </li>
        <li>
            <i class="ti-user"></i>
            <a href="timeline-friends.html" title="">friends</a>
        </li>
        <li>
            <i class="ti-image"></i>
            <a href="timeline-photos.html" title="">images</a>
        </li>
        <li>
            <i class="ti-video-camera"></i>
            <a href="timeline-videos.html" title="">videos</a>
        </li>
        <li>
            <i class="ti-comments-smiley"></i>
            <a href="messages.html" title="">Messages</a>
        </li>
        <li>
            <i class="ti-bell"></i>
            <a href="notifications.html" title="">Notifications</a>
        </li>
        <li>
            <i class="ti-share"></i>
            <a href="people-nearby.html" title="">People Nearby</a>
        </li>
        <li>
            <i class="fa fa-bar-chart-o"></i>
            <a href="insights.html" title="">insights</a>
        </li>
        <li>
            <i class="ti-power-off"></i>
            <a href="landing.html" title="">Logout</a>
        </li>
    </ul>
    </div>`
}

//-------------------------------------------------------------------------------------------------------------

// document.getElementById('mediaInput').addEventListener('change',handleMediaSelect);
// function handleMediaSelect(event){
//     const files = event.target.files;
//     const previewContainer = document.getElementById('previewContainer');
//     previewContainer.innerHTML='';
//     console.log(file);
//     for(let i=0 ; i<files.length;i++){
//         const file = files[i];
//         const fileType = file.type;
        
//         if (fileType.startsWith('image/')){
//             const reader = new FileReader();
//             reader.onload = function(e){
//                 const imageURL = e.target.result;
//                 const imageElement=document.createElement('img');
//                 imageElement.src= imageURL;
//                 previewContainer.appendChild(imageElement);
//             };
//             reader.readAsDataURL(file);
//         }
//     }
    
// }

// document.getElementById('mediaForm').addEventListener('submit',handleMediaSelect);
// function handleFormSubmit(event){
//     event.preventDefault();
//     const files = document.getElementById('mediaInput').files
//     document.getElementById('mediaForm').reset()
//      ` <div class="central-meta item">

//     <div class="user-post">
//         <div class="friend-info">
//             <figure>
//                 <img src="images/resources/friend-avatar10.jpg" alt="">
//             </figure>
//             <div class="friend-name">
//                 <ins><a href="time-line.html" title="">Janice Griffith</a></ins>
//                 <span>published: june,2 2018 19:PM</span>
//             </div>
//             <div class="description">

//                 <p>
//                     bonjour
//                 </p>
//             </div>
//             <div class="post-meta">
//             <div class="linked-image align-left">
//                 <a href="#" title=""><img src="images/imageElement" alt=""></a>
//                 </div>
//                 <div class="detail">
//                     <span>Love Maid - ChillGroves</span>
//                     <p>Lorem ipsum dolor sit amet, consectetur ipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua... </p>
//                     <a href="#" title="">www.sample.com</a>
//                 </div>
//                 <div class="we-video-info">
//                 <div class="we-video-info">
//                     <ul>

//                         <li>
//                             <span class="views" data-toggle="tooltip" title="views">
//                             <i class="fa fa-eye"></i>
//                             <ins>1.2k</ins>
//                         </span>
//                         </li>
//                         <li>
//                             <span class="comment" data-toggle="tooltip" title="Comments">
//                             <i class="fa fa-comments-o"></i>
//                             <ins>52</ins>
//                         </span>
//                         </li>
//                         <li>
//                             <span class="like" data-toggle="tooltip" title="like">
//                             <i class="ti-heart"></i>
//                             <ins>2.2k</ins>
//                         </span>
//                         </li>
//                         <li>
//                             <span class="dislike" data-toggle="tooltip" title="dislike">
//                             <i class="ti-heart-broken"></i>
//                             <ins>200</ins>
//                         </span>
//                         </li>
//                         <li class="social-media">
//                             <div class="menu">
//                                 <div class="btn trigger"><i class="fa fa-share-alt"></i></div>
//                                 <div class="rotater">
//                                     <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-html5"></i></a></div>
//                                 </div>
//                                 <div class="rotater">
//                                     <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-facebook"></i></a></div>
//                                 </div>
//                                 <div class="rotater">
//                                     <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-google-plus"></i></a></div>
//                                 </div>
//                                 <div class="rotater">
//                                     <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-twitter"></i></a></div>
//                                 </div>
//                                 <div class="rotater">
//                                     <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-css3"></i></a></div>
//                                 </div>
//                                 <div class="rotater">
//                                     <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-instagram"></i></a>
//                                     </div>
//                                 </div>
//                                 <div class="rotater">
//                                     <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-dribbble"></i></a>
//                                     </div>
//                                 </div>
//                                 <div class="rotater">
//                                     <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-pinterest"></i></a>
//                                     </div>
//                                 </div>

//                             </div>
//                         </li>
//                     </ul>
//                 </div>
//             </div>
//         </div>
//     </div>
// </div>`
//     //.reset();
// }

//----------------------------------------------------------------------------------------------------------------
//----------------------------------------------------------------------------------------------------------------

function postComment(id){
    document.getElementById(id).innerHTML =
    `<div class="user-post">
        <div class="coment-area">
            <ul class="we-comet">
                <li>
                    <div class="comet-avatar">
                        <img src="images/resources/comet-1.jpg" alt="">
                    </div>
                    <div class="we-comment">
                        <div class="coment-head">
                            <h5><a href="time-line.html" title="">Jason borne</a></h5>
                            <span>1 year ago</span>
                            <a class="we-reply" href="#" title="Reply"><i class="fa fa-reply"></i></a>
                        </div>
                        <p>we are working for the dance and sing songs. this car is very awesome for the youngster. pse vote this car and like our post</p>
                    </div>
                    <ul>
                        <li>
                            <div class="comet-avatar">
                                <img src="images/resources/comet-2.jpg" alt="">
                            </div>
                            <div class="we-comment">
                                <div class="coment-head">
                                    <h5><a href="time-line.html" title="">alexendra dadrio</a></h5>
                                    <span>1 month ago</span>
                                    <a class="we-reply" href="#" title="Reply"><i class="fa fa-reply"></i></a>
                                </div>
                                <p>yes, really very awesome car i see the features of this car in the official website of <a href="#" title="">#Mercedes-Benz</a> and really impressed :-)</p>
                            </div>
                        </li>
                        <li>
                            <div class="comet-avatar">
                                <img src="images/resources/comet-3.jpg" alt="">
                            </div>
                            <div class="we-comment">
                                <div class="coment-head">
                                    <h5><a href="time-line.html" title="">Olivia</a></h5>
                                    <span>16 days ago</span>
                                    <a class="we-reply" href="#" title="Reply"><i class="fa fa-reply"></i></a>
                                </div>
                                <p>i like lexus cars, lexus cars are most beautiful with the awesome features, but this car is really outstanding than lexus</p>
                            </div>
                        </li>
                    </ul>
                </li>
                <li>
                    <div class="comet-avatar">
                        <img src="images/resources/comet-1.jpg" alt="">
                    </div>
                    <div class="we-comment">
                        <div class="coment-head">
                            <h5><a href="time-line.html" title="">Donald Trump</a></h5>
                            <span>1 week ago</span>
                            <a class="we-reply" href="#" title="Reply"><i class="fa fa-reply"></i></a>
                        </div>
                        <p>we are working for the dance and sing songs. this video is very awesome for the youngster. please vote this video and like our channel
                            <i class="em em-smiley"></i>
                        </p>
                    </div>
                </li>
                <li>
                    <a href="#" title="" class="showmore underline">more comments</a>
                </li>
                <li class="post-comment">
                    <div class="comet-avatar">
                        <img src="images/resources/comet-1.jpg" alt="">
                    </div>
                    <div class="post-comt-box">
                        <form method="post">
                            <textarea placeholder="Post your comment"></textarea>
                            <div class="add-smiles">
                                <span class="em em-expressionless" title="add icon"></span>
                            </div>
                            <div class="smiles-bunch">
                                <i class="em em---1"></i>
                                <i class="em em-smiley"></i>
                                <i class="em em-anguished"></i>
                                <i class="em em-laughing"></i>
                                <i class="em em-angry"></i>
                                <i class="em em-astonished"></i>
                                <i class="em em-blush"></i>
                                <i class="em em-disappointed"></i>
                                <i class="em em-worried"></i>
                                <i class="em em-kissing_heart"></i>
                                <i class="em em-rage"></i>
                                <i class="em em-stuck_out_tongue"></i>
                            </div>
                            <button type="submit"></button>
                        </form>
                    </div>
                </li>
            </ul>
        </div>
    </div>
    `
}
