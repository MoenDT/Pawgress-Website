function closeNotesModal() {
    const contentBox = document.getElementsByClassName("modalContent")[0];
    contentBox.classList.remove("zoomIn");
    contentBox.classList.add("zoomOut");

    const notesModal = document.getElementById("notesModal");
    setTimeout(function () {
        notesModal.style.display = "none";
        contentBox.classList.replace("zoomOut", "zoomIn");
    }, 500);
}

document.getElementById("visitBody").addEventListener("click", function (event) {
    const button = event.target.closest(".viewnotesbutton");
    if (!button) return;

    // Populates the notes text and opens the modal when clicked
    const notesModal = document.getElementById("notesModal");
    const modalNotesText = document.getElementById("modalNotesText");
    if (modalNotesText && button.dataset.notes) {
        modalNotesText.textContent = button.dataset.notes;
    }

    notesModal.style.display = "block";
});

document.querySelector("#notesModal .modalContent span").addEventListener("click", function () {
    // Closes the notes modal with animation when the close button is clicked
    closeNotesModal();
});

// Close the modal with animation when clicking outside of it
window.addEventListener("click", function (event) {
    const notesModal = document.getElementById("notesModal");
    if (event.target === notesModal) {
        closeNotesModal();
    }
});
