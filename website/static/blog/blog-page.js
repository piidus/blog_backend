// uid
const uid = $("#blog_uid").val();

// text editor

function applyStyle(command, value = null) {
    const selection = window.getSelection();
    
    if (!selection.rangeCount) return; // Check if there's a selection
    
    const range = selection.getRangeAt(0); // Get the selected range

    // Handle toggle for bold, italic, and underline
    if (command === 'bold' || command === 'italic' || command === 'underline') {
        const isActive = document.queryCommandState(command); // Check if the command is currently active
        
        if (isActive) {
            // If it is active, toggle it off
            document.execCommand('removeFormat', false, null);
        } else {
            // Apply the formatting
            document.execCommand(command, false, null);
        }
        return; // Exit after handling toggle
    }

    // For other commands, just execute them directly
    if (command === 'foreColor') {
        document.execCommand(command, false, value); // Change text color directly
        return;
    }
    
    const span = document.createElement('span'); // Create a span for styling

    // Apply styles based on command
    switch (command) {
        case 'insertUnorderedList':
            document.execCommand('insertUnorderedList', false, null); // Use execCommand here, as it's complex
            return;
        case 'insertOrderedList':
            document.execCommand('insertOrderedList', false, null); // Use execCommand here, as it's complex
            return;
        default:
            return;
    }
}

// Apply command from toolbar to editor using applyStyle
$('.toolbar button[data-command]').click(function() {
    const command = $(this).data('command');
    const value = $(this).data('value') || null;
    
    applyStyle(command, value);
});

// Hyperlink functionality
$('#addLink').click(function() {
    const url = prompt('Enter the hyperlink URL:');
    if (url) {
        const selection = window.getSelection();
        if (!selection.rangeCount) return;
        
        const range = selection.getRangeAt(0);
        const link = document.createElement('a');
        link.href = url;
        link.target = '_blank'; // Open in new tab
        link.style.color = 'blue'; // Set link color
        link.textContent = selection.toString(); // Set link text to the selected text

        range.deleteContents(); // Remove selected text
        range.insertNode(link); // Insert the link at the cursor position
    }
});

// Hashtag functionality
$('#addHashtag').click(function() {
    const hashtag = prompt('Enter the hashtag:');
    if (hashtag) {
        const selection = window.getSelection();
        if (!selection.rangeCount) return;
        
        const range = selection.getRangeAt(0);
        const span = document.createElement('span');
        span.textContent = hashtag;
        span.style.color = 'green'; // Set hashtag color
        span.style.fontWeight = 'bold'; // Optional: Make hashtag bold

        range.deleteContents(); // Remove selected text
        range.insertNode(span); // Insert the hashtag at the cursor position
    }
});

// Capture Tab key press for indent
$('#editor').on('keydown', function(e) {
    if (e.key === 'Tab') {
        e.preventDefault();

        const selection = window.getSelection();
        if (!selection.rangeCount) return;

        const range = selection.getRangeAt(0);
        const tabNode = document.createTextNode('\u00a0\u00a0\u00a0\u00a0'); // Insert 4 non-breaking spaces as indent
        range.insertNode(tabNode);

        // Move the caret position after the inserted spaces
        range.setStartAfter(tabNode);
        range.setEndAfter(tabNode);
        selection.removeAllRanges();
        selection.addRange(range);
    }
});

// Handle Submit Button Click
$('#submitContent').click(function() {
    const content = $('#editor').html();
    console.log(content);
    fetch('/submit-content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: content, uid: uid }),
    }).then(response => response.json()).then(data => {
        if (data['success'] == false) {
            alert('An error occurred: ' + data['error']);
        } else {
            alert('Content submitted successfully!');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});





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
        var postOffices = data[0]['offices'];
        // console.log(postOffices);
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
  