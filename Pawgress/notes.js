document.querySelectorAll(".viewnotesbutton").forEach(function(button) {
    button.addEventListener("click", function() {
        // Opens the notes modal when clicked
        const notesModal = document.getElementById("notesModal");
        notesModal.style.display = "block";
    });
});

document.querySelector("#notesModal .modalContent span").addEventListener("click", function() {
    // Closes the notes modal when the close button is clicked

    const contentBox = document.getElementsByClassName("modalContent")[0];
    contentBox.classList.remove("zoomIn");
    contentBox.classList.add("zoomOut");

    const notesModal = document.getElementById("notesModal");
    setTimeout(function() {
        notesModal.style.display = "none";
        contentBox.classList.replace("zoomOut", "zoomIn");
    }, 500);
});

// Optional: Close the modal when clicking outside of it
window.addEventListener("click", function(event) {
    const notesModal = document.getElementById("notesModal");
    if (event.target === notesModal) {
        notesModal.style.display = "none";
    }
});
