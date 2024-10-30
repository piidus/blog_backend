var code;
function signup() {
    // fetch a code from backend and set it in the modal as hidden input
    fetch("/auth/authcode", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'email': $("#email").val() }),
    })
        .then((response) => response.json())
        .then((data) => {
            code = data['authcode'];
            // console.log("Success:", data);
            // console.log(code);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    // activate modal
    $("#staticBackdrop").modal("show");
}

function checkCode() {
    // get input
    var input = document.getElementById("code").value;
    // check if code is correct
    if (code == input) {
        // if correct, close modal
        $("#staticBackdrop").modal("hide");
        // create post request to backend
        var signupForm = document.getElementById("signupFormid");
        // console.log(signupForm);    

        // Get form data
        const formData = new FormData(signupForm);
        // console.log(formData);
        // Convert FormData to a regular object
        const formObject = Object.fromEntries(formData.entries());
        // console.log(formObject);
        // Send form data to backend as JSON
        fetch("/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formObject), // Convert the object to JSON string
        })
            .then(response => response.json())
            .then(data => {
                // console.log("Success:", data);
                if (data['success'] == true) {
                    window.location.href = "/login";
                }
                // if success = false alert
                if (data['success'] == false) {
                    alert(data['message']);
                }
                // Open the next modal or handle success as needed
            })
            .catch((error) => {
                console.error("Error:", error);
            });
        // });


        // console.log(signupForm);

    }
}
