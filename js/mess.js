const addForm=document.querySelector('.peoples-mesg-box #add');
 const list=document.getElementById('liste');
function nv(){
    let imput_file = document.getElementById("fileContainer");
    if(imput_file.value == ''){
        const tache=document.getElementById('test').value;
        if(tache.length){
            const generateTemplate = (todo) => {               
             const html = `<li class="me">
             <figure><img src="images/resources/userlist-1.jpg" alt=""></figure>
             <p>${todo}</p>
         </li>`;
             list.innerHTML = html + list.innerHTML;
           };
           let writ = document.getElementById("test");
            writ.value ='';
            list.appendChild(generateTemplate(tache));  
       }
    }
      
        const tache=document.getElementById('test').value;
         
         let profil_pic = URL.createObjectURL(imput_file.files[0]);
         
             const generateTemplate = (todo) => {
              const html =`<li class="me">
              <figure><img src="images/resources/userlist-1.jpg" alt=""></figure>
              <img src=${profil_pic} alt="" height="350" width="300">
              <p>${todo}</p>
          </li>`; 
            list.innerHTML = html + list.innerHTML;
        };
        let writ = document.getElementById("test");
        writ.value ='';
        list.appendChild(generateTemplate(tache))
 }

 const userList = document.querySelector('peoples');
 const chat_header = document.querySelector('conversation-head');
 const chat_message = document.querySelector('chatting-area');
 userList.addEventListener('click',(even)=>{
    if(even.target.classList.contains('user'))
    {
        const selectUser = even.target;
        const username = selectUser.querySelector('span').innerText;
        const userProfile = selectUser.querySelector('img').src;
        chat_header.innerHTML =` <div class="conversation-head" >
        <figure><img src= ${userProfile} alt=""></figure>
        <span>${username} <i>online</i></span>
    </div>`;
        chat_message.innerHTML=''; 
    }
 });

 