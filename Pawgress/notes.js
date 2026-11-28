document.querySelectorAll(".viewnotesbutton").forEach(function(button) {
    button.addEventListener("click", function() {
        // Opens the notes modal when clicked
        const notesModal = document.getElementById("notesModal");
        notesModal.style.display = "block";
    });
});

document.querySelector("#notesModal .modalContent span").addEventListener("click", function() {
    // Closes the notes modal when the close button is clicked
    const notesModal = document.getElementById("notesModal");
    notesModal.style.display = "none";
});

// Optional: Close the modal when clicking outside of it
window.addEventListener("click", function(event) {
    const notesModal = document.getElementById("notesModal");
    if (event.target === notesModal) {
        notesModal.style.display = "none";
    }
});
