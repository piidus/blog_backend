// uid
// const uid = $("#blog_uid").val();
const currentUrl = window.location.pathname;
// console.log(currentUrl.split("/")[2]);
const uid = currentUrl.split("/")[2];
// save image
function saveImage() {
    const imageInput = document.getElementById('imageInput1');
    const imageFile = imageInput.files[0];
    // console.log(imageInput);

    if (imageFile) {
        const formData = new FormData();
        formData.append('image', imageFile);
        formData.append('uid', uid);

        fetch('/save-image', {
            method: 'POST',
            body: formData,
        }).then(response => response.json()).then(data => {
            if (data['success'] === true) {
                alert('Image saved successfully!');
            } else {
                alert('An error occurred: ' + data['message']);
            }
        }).catch(error => {
            console.error('Error:', error);
        });
    } else {
        alert('Please select an image file.');
    }
}



// Handle Submit Button Click
const normalizeContent = (text) => text.normalize("NFC");

$('#submitContent').click(function() {
    const content = normalizeContent($('#text-input').html());
    fetch('/submit-content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: content, uid: uid }),
    }).then(response => response.json()).then(data => {
        if (data['success'] === false) {
            alert('An error occurred: ' + data['message']);
        } else {
            alert('Content submitted successfully!');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
});


// $('#submitContent').click(function() {
//     const content = $('#text-input').html();
//     console.log(content);
//     fetch('/submit-content', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ content: content, uid: uid }),
//     }).then(response => response.json()).then(data => {
//         if (data['success'] == false) {
//             alert('An error occurred: ' + data['error']);
//         } else {
//             alert('Content submitted successfully!');
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });





// save address
function addressSave() {
    var pincode = $("#pincode").val();
    var postOffice = $("#postOffice").val();
    var village = $("#Village").val();
    // alert(pincode + postOffice + village);
    fetch("/save-address", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ pincode: pincode, postOffice: postOffice, village: village, uid: uid }),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // if success = false alert
        if (data['success'] == false) {
            alert(data['message']);
        }
    });
}




// on pincode change call all post office
function pincodeChange() {
    
    var pincode = $("#pincode").val();
    // alert(pincode);
    // fetch all post office
    fetch("/get-postoffice", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ pincode: pincode, uid: uid }),
    })
    .then((response) => response.json())
    .then((data) => {
        //console.log(data);
        var postOffices = data[0]['offices'];
        // console.log(postOffices);
        // remove previous optons
        $("#postOffice").empty();
        // Get a reference to the select element
        var selectElement = $("#postOffice");
        // Create and append options to the select element
            postOffices.forEach(postOffice => {
                const option = $("<option ></option>")
                    .val(postOffice)
                    .text(postOffice);
                   
                selectElement.append(option);
            });
        
        // Add the change event listener to the select element
            selectElement.on('change', function() {
                var selectedPostOffice = $(this).val();
                postOfficeChange(selectedPostOffice);
            });
        // update the chosen dropdown
        selectElement.trigger('chosen:updated');
        
    })
    .catch((error) => {
        console.error("Error:", error);
    });
    
}

// post office change   
function postOfficeChange(postOffice) {
    alert(postOffice);
}


// dropdown selection
$(document).ready(function () {
    $(".ch").chosen({
      width: "30%",
      no_results_text: "Oops, nothing found!",
      allow_single_deselect: true,
    });
    // run the month Dropdown
    // monthDropdown();
  });
  