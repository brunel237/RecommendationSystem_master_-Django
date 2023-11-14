// function convertImageToBase64(file, callback) {
//     const reader = new FileReader();
//     reader.onloadend = function () {
//       callback(reader.result);
//     };
//     reader.readAsDataURL(file);
// }
    // const file = ;

    const defaultProfilePicture = fetch("/images/profile_default.png")
    .then(response => response.blob())
    .then(blob => new File([blob], 'profile_default.png'));

    console.log(defaultProfilePicture)
    
    // convertImageToBase64(file, function (base64String) {
    //     console.log(base64String); // Base64 encoded image data
    // });
