// uid
// const uid = $("#blog_uid").val();
const currentUrl = window.location.pathname;
// console.log(currentUrl.split("/")[2]);
const uid = currentUrl.split("/")[2];

// Delete Tags
function tagDelete(tagName) {
    fetch('/delete-tag', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'tagName': tagName, 'uid': uid }),
    }).then(response => response.json()).then(data => {
        if (data['success'] === true) {
            alert('Tag deleted successfully!');
        } else {
            alert('An error occurred: ' + data['message']);
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}

// save tags
function tagSave(blogId) {
    var tags = $("#tags").val();
    fetch("/save-tags", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ tags: tags, uid: blogId }),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // if success = true alert
        if (data['success'] == true) {
            alert(data['message']);
        }
        // if success = false alert
        if (data['success'] == false) {
            alert(data['message']);
        }
    })
    .catch((error) => {
        console.error("Error:", error);
    })
}
// delete image
function deleteImage(imageName) {
    fetch('/delete-image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'imageName': imageName, 'uid': uid }),
    }).then(response => response.json()).then(data => {
        if (data['success'] === true) {
            alert('Image deleted successfully!');
        } else {
            alert('An error occurred: ' + data['message']);
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}
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
                // reset image input
                imageInput.value = '';
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



// Handle Submit Button Click for content save
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




// save address
function addressSave() {
    var pincode = $("#pincode").val();
    var postOffice = $("#postOffice").val();
    var village = $("#Village").val();
    var district = $("#district").val();
    // alert(pincode + postOffice + village);
    fetch("/save-address", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ pincode: pincode, postOffice: postOffice, village: village, district: district, uid: uid }),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // if success = true alert
        if (data['success'] == true) {
            alert(data['message']);
        }
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
        // console.log(data);
        var postOffices = data[0]['offices'];
        // console.log(postOffices);
        var districts = data[1]['districts'];
        // console.log(districts);
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

        // Get a reference to the select element
        var selectElement1 = $("#district");
        // Create and append options to the select element
            districts.forEach(district => {
                console.log(district);
                const option = $("<option ></option>")
                    .val(district)
                    .text(district);
                   
                selectElement1.append(option);
            });
        
        
        // Add the change event listener to the select element
            selectElement.on('change', function() {
                var selectedPostOffice = $(this).val();
                postOfficeChange(selectedPostOffice);
            });
        // update the chosen dropdown
        selectElement.trigger('chosen:updated');
        selectElement1.trigger('chosen:updated');
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
      width: "100%",
      no_results_text: "Oops, nothing found!",
      allow_single_deselect: true,
    });
    // run the month Dropdown
    // monthDropdown();
  });
  