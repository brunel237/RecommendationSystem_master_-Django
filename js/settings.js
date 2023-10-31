function handleCheckboxChange(id) {
    var checkbox = document.getElementById(id);
    var checkboxState = checkbox.checked ? "on" : "off";
    
    switch(id){
        case "==  'nightmodel'": {
            changeThemeMode();
            break;
        }
        case "==  'switch22'": {
            notifications();
            break;
        }
        case "==  'switch33'": {
            notificationsSound();
            break;
        }
        //etc
    }

  }

function changeThemeMode(state) {}
function notifications(state) {}
function notificationsSound(state) {}
//etc