document.getElementById("loginButton").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Perform your login logic here (e.g., send a request to the server)
    // For demonstration purposes, let's assume a simple check
    if (username === "admin" && password === "password") {
        alert("Login successful!");
        // Redirect to another page or perform other actions
        window.location.href = "dashboardpage.html";
    } else {
        alert("Invalid username or password.");
    }
});
