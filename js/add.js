const addForm=document.querySelector('.loadMore #addForm');
const list=document.getElementById('list');

//add
function na(){
    const tache=document.getElementById('text').value;
    if(tache.length){
        const generateTemplate = (todo) => {
            const html = `
                                    <div class="central-meta item">

                                            <div class="user-post">
                                                <div class="friend-info">
                                                    <figure>
                                                        <img src="images/resources/friend-avatar10.jpg" alt="">
                                                    </figure>
                                                    <div class="friend-name">
                                                        <ins><a href="time-line.html" title="">Janice Griffith</a></ins>
                                                        <span>published: june,2 2018 19:PM</span>
                                                    </div>
                                                    <div class="description">

                                                        <p>
                                                            ${todo}
                                                        </p>
                                                    </div>
                                                    <div class="post-meta">
                                                        <div class="we-video-info">
                                                            <ul>

                                                                <li>
                                                                    <span class="views" data-toggle="tooltip" title="views">
																	<i class="fa fa-eye"></i>
																	<ins>1.2k</ins>
																</span>
                                                                </li>
                                                                <li>
                                                                    <span class="comment" data-toggle="tooltip" title="Comments">
																	<i class="fa fa-comments-o"></i>
																	<ins>52</ins>
																</span>
                                                                </li>
                                                                <li>
                                                                    <span class="like" data-toggle="tooltip" title="like">
																	<i class="ti-heart"></i>
																	<ins>2.2k</ins>
																</span>
                                                                </li>
                                                                <li>
                                                                    <span class="dislike" data-toggle="tooltip" title="dislike">
																	<i class="ti-heart-broken"></i>
																	<ins>200</ins>
																</span>
                                                                </li>
                                                                <li class="social-media">
                                                                    <div class="menu">
                                                                        <div class="btn trigger"><i class="fa fa-share-alt"></i></div>
                                                                        <div class="rotater">
                                                                            <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-html5"></i></a></div>
                                                                        </div>
                                                                        <div class="rotater">
                                                                            <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-facebook"></i></a></div>
                                                                        </div>
                                                                        <div class="rotater">
                                                                            <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-google-plus"></i></a></div>
                                                                        </div>
                                                                        <div class="rotater">
                                                                            <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-twitter"></i></a></div>
                                                                        </div>
                                                                        <div class="rotater">
                                                                            <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-css3"></i></a></div>
                                                                        </div>
                                                                        <div class="rotater">
                                                                            <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-instagram"></i></a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="rotater">
                                                                            <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-dribbble"></i></a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="rotater">
                                                                            <div class="btn btn-icon"><a href="#" title=""><i class="fa fa-pinterest"></i></a>
                                                                            </div>
                                                                        </div>

                                                                    </div>
                                                                </li>
                                                            </ul>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
              `;
            list.innerHTML = html + list.innerHTML;
        };
        list.appendChild(generateTemplate(tache))
    }
}

//remove
/*list.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete")) {
        e.target.parentElement.remove();
    }
});

//edit
list.addEventListener("click", (e) => {
    if (e.target.classList.contains("modif")) {
        let inp=document.getElementsByTagName("input");
        for (let i = 0; i < inp.length; i++) {
            if(inp[i].className=="mo"){
                inp[i].removeAttribute("disabled")
            }
        }
        alert('Vous pouvez modifier vos informations')
    }
});*/