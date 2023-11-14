
//-----------------------------------------------------------------------------------------------------------------
//-----------------------------------------------------------------------------------------------------------------
var post_media = [];

function handleFileUpload(event, fileType) {
    const file = event.target.files[0];
    const reader = new FileReader();
    
    reader.onload = function() {
      const fileContent = reader.result;
      let temp = {
        "file": fileContent,
        "file_type": fileType
      }
      post_media.push({"file_name":file.name, "data":temp});
      const uploadedFilesDiv = document.getElementById('loadedContent');
      
      const fileDisplay = document.createElement('p');
      fileDisplay.textContent = `File Name: ${file.name}, File Type: ${fileType}`;
      fileDisplay.id=`${file.name}`
      fileDisplay.class=`${file.name}`
      
      const removeButton = document.createElement('button');
      removeButton.textContent = 'Remove';
      removeButton.addEventListener('click', function() {
        uploadedFilesDiv.removeChild(fileDisplay);
        for (let i=0; i<post_media.length; i++) {
            if (fileDisplay.id==post_media[i].file_name && fileDisplay.class==post_media[i].data.file_type){
                post_media.splice(i, 1);
            }
        }
      });
      
      fileDisplay.appendChild(removeButton);
      uploadedFilesDiv.appendChild(fileDisplay);
    }
    
    reader.readAsDataURL(file);
  }

function getFileExtension(fileName) {
    const parts = fileName.split('.');
    return parts[parts.length - 1];
}

function EmbededPdfFile(file) {
    const fileReader = new FileReader();
    fileReader.onload = () => {
        const iframe = document.createElement('iframe');
        iframe.src = URL.createObjectURL(new Blob([fileReader.result], { type: 'application/pdf' }));
        iframe.width = '100%';
        return iframe
    };
    fileReader.readAsArrayBuffer(file);
}

function sendPostToServer(method, url, data){
    var xhr = new XMLHttpRequest();
	xhr.open(method, url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("Authorization", "Token " +getCookie("token"))

	xhr.onreadystatechange = function() {
		if (xhr.readyState === XMLHttpRequest.DONE) {
			if (xhr.status === 200 || xhr.status === 201) {
                var response = JSON.parse(xhr.responseText);
                pushPost(response.message)
			} 
            else {
				var response = JSON.parse(xhr.responseText);
				console.log(JSON.stringify(response))
			}
		}
	}
    xhr.send(JSON.stringify(data));
}

function loadMedia(event){
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
        const fileContents = e.target.result;
        setCookie("loadedMedia", fileContents, 365)
        };

        reader.readAsDataURL(file);
    }
}

function getFile(file){

}

function na(){
    const list = document.getElementById('list');
    const tache = document.getElementById('text').value;
    const file = document.getElementById("imageContainer").files[0];
    let files = []
    if (post_media.length)
        for (let i=0; i<post_media.length; i++) {
            files.push(post_media[i].data);
        }
    let post_data = {
        "message" : tache,
        "media" : files
    }

    sendPostToServer("POST", "http://127.0.0.1:8000/api/posts/new/", post_data);

}

function checkFileType(file) {
    if (!file) return;
    const fileReader = new FileReader();

  fileReader.onload = () => {
    const fileType = fileReader.result.type;
    if (/image\//.test(fileType)) {
        const img = document.createElement('img')
        img.scr =  file;
        img.alt = "Posted Image"
        img.style = "width:100%;"
        return img;
    } else if (/video\//.test(fileType)) {
        const video = document.createElement('video')
        video.scr = file;
        video.style = "width:100%;"
        return video
    } else {
        const iframe = document.createElement('iframe');
        iframe.src = file;
        iframe.width = '100%';
        return iframe
    }
  };
  fileReader.readAsDataURL(file.blob());
}

function displayMedia(media){
    if (media.file_type == "Image")
    	return `<div class="${media.file}" id="" style="width: 90%;">
                <img src=${media.file} alt="a posted image" style="width: 100%">
                </div>`
    else if (media.file_type == "Video")
	    return `<div class="" id="" style="width: 90%;">
                <video src=${media.file} style="width: 100%"></video>
                </div>`
    else if (media.file_type == "Music")
	    return `<div class="" id="" style="width: 90%;">
                <audio src=${media.file} style="width: 100%"></audio>
                </div>`
    else 
	    return `<div class="" id="" style="width: 90%;">
                <iframe src=${media.file} frameborder="0" style="width: 100%"></iframe>
                </div>`
}

function displayComment(comment){
    return `<div class="comments" id="comment-${comment.id} style="padding-top: 0.25em; border:1px solid #9c9c9c5e; border-radius: 1em; ">
                <div style="font-size: 0.85em">${comment.author.first_name} ${comment.author.last_name}</div>
                <div style="font-size: 0.75em">@${comment.author.username}</div>
                <div style="font-size: 1em">${comment.content}</div>
                <div style="font-size: 0.65em">${comment.created_at}</div> 
            </div>`
}

function pushPost(post) {   // post est en format json
    let  post_list = document.getElementById("list");

    let new_post = `<div class="friend-info" style="background-color: white; padding: 1em 1em 0em 1.5em; margin-bottom: 1em;">
        <figure>
            <img src=${post.author.profile_picture} alt="profile_picture" style="width:60px; height:60px">
        </figure>
        <div class="friend-name">
            <ins><a href="time-line.html" title="">${post.author.last_name} ${post.author.first_name}</a></ins>
            <span>@${post.author.username}</span>
            <span>published: ${post.created_at}</span>
        </div>
        <div class="post-meta">
            <div class="description">
                <p> ${post.message} </p>
            </div>
            <div style="width:90%;">`

        if (post.media.length){
            for (let i=0; i<post.media.length; i++){
                new_post += displayMedia(post.media[i])
            }
        }

        let new_post_end = `</div>
            <div class="we-video-info">
                <ul>
                    <li>
                        <span class="comment" data-toggle="tooltip" title="Comments">
                        <i class="fa fa-comments-o"></i>
                        <ins>${post.comment_count}</ins>
                        </span>
                    </li>
                    <li>
                        <span class="like" data-toggle="tooltip" title="like">
                        <i class="ti-heart"></i>
                        <ins>${post.likes_count}</ins>
                        </span>
                    </li>
                </ul>
            </div>
            </div>
            <div class="collapse show" aria-labelledby="show comments" id="" >`;

        new_post += new_post_end

        if (post.comments.length){
            for (let i=0; i<post.comments.length; i++){
                new_post += displayComment(post.comments[i])
            }
        }

        new_post += `</div> </div>`

    var temp = post_list.innerHTML
    post_list.innerHTML = new_post;
    post_list.innerHTML += temp;
}
