const optionsButtons = document.querySelectorAll(".option-button");

// Function to modify text based on button click
function modifyText(command, value = null) {
    document.execCommand(command, false, value);
}

// Event listeners for format buttons
optionsButtons.forEach(button => {
    button.addEventListener("click", () => {
        modifyText(button.id);
        button.classList.toggle("active");
    });
});

// Prevent default behavior on link button click
document.getElementById("createLink").addEventListener("click", () => {
    const url = prompt("Enter URL:");
    if (url) modifyText("createLink", url);
});

// Initial settings
document.getElementById("fontSize").addEventListener("change", (e) => {
    modifyText("fontSize", e.target.value);
});

document.getElementById("fontName").addEventListener("change", (e) => {
    modifyText("fontName", e.target.value);
});

document.getElementById("formatBlock").addEventListener("change", (e) => {
    modifyText("formatBlock", e.target.value);
});

document.getElementById("text-input").focus();

// add more options

// Language Change
document.getElementById("languageSelect").addEventListener("change", (e) => {
    const selectedLang = e.target.value;
    document.getElementById("text-input").setAttribute("lang", selectedLang);

    // Optional: Set `dir` for specific languages
    if (selectedLang === "ar") {
        document.getElementById("text-input").setAttribute("dir", "rtl");
    } else {
        document.getElementById("text-input").removeAttribute("dir");
    }
});
 // Image Insertion
 document.getElementById("insertImageButton").addEventListener("click", () => {
    document.getElementById("imageInput").click();
});
document.getElementById("imageInput").addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = () => {
            modifyText("insertImage", reader.result);
        };
        reader.readAsDataURL(file);
    }
});

// Font Color and Highlighter
// document.getElementById("fontColor").addEventListener("change", (e) => {
//     modifyText("foreColor", e.target.value);
// });
// document.getElementById("highlightColor").addEventListener("change", (e) => {
//     modifyText("backColor", e.target.value);
// });