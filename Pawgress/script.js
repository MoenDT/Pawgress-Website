function clearInput(inputId) {  //function to clear inputs from the username and password widgets found on the login screen
    document.getElementById(inputId).value = "";
}


function populatePetTable() { //function for populating tables for respective pages: vaccinations, vetvisits, etc <- TO BE HEAVILY MODIFIED LATER
    const tableBody = document.getElementById("petTableBody");

    tableBody.replaceChildren();

    pets.forEach(pet => {
        const row = tableBody.insertRow();

        row.insertCell().textContent = pet.name;
        row.insertCell().textContent = pet.registered;
        row.insertCell().textContent = pet.lastVetVisit;

        const actionCell = row.insertCell();

        const link = document.createElement("a");
        link.href = `pet-details.html?id=${pet.id}`;
        link.textContent = "→";
        link.setAttribute("aria-label", `View ${pet.name}'s profile`);

        actionCell.appendChild(link);
    });
}

populatePetTable(); //fills the pet table

function addRow(medication, pet, date, time) { //addRow function to add rows to tables found across pages such as vaccinations, vetvisits, etc.
    const table = document.getElementById("medicationBody");

    const row = table.insertRow();

    [medication, pet, date, time].forEach(value => {
        const cell = row.insertCell();
        cell.textContent = value;
    });

    const actionCell = row.insertCell();
    const button = document.createElement("button");

    button.textContent = "Delete";
    button.addEventListener("click", () => row.remove());

    actionCell.appendChild(button);
}

function deleteRow(button) { //delete row function for various tables
    const row = button.closest("tr"); //since the delete key is on each row, locating by "tr" works
    row.remove();
}