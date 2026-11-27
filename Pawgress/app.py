from flask import Flask, send_from_directory, abort, request, redirect
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    db = get_connection()
    db.close()
    return "Pawgress database connected"

@app.route("/pets")
def pets():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Pets")
    results = cursor.fetchall()

    cursor.close()
    db.close()

    return str(results)

@app.route("/medications")
def medications():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT Pets.PetName,
            Medications.MedicationName,
            Medications.Dosage,
            Medications.Instructions,
            Medications.Duration
        FROM Medications
        JOIN Pets ON Medications.PetID = Pets.PetID
    """)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return str(results)

@app.route("/vet-visits")
def vet_visits():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT Pets.PetName,
               VetVisits.VisitDate,
               VetVisits.Veterinarian,
               VetVisits.Reason,
               VetVisits.Status
        FROM VetVisits
        JOIN Pets ON VetVisits.PetID = Pets.PetID
    """)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return str(results)

@app.route("/vaccinations")
def vaccinations():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT Pets.PetName,
               Vaccinations.VaccineName,
               Vaccinations.LastDate,
               Vaccinations.NextDate
        FROM Vaccinations
        JOIN Pets ON Vaccinations.PetID = Pets.PetID
    """)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return str(results)

@app.route("/reminders")
def reminders():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT Pets.PetName,
               Reminders.ReminderType,
               Reminders.ReminderDate,
               Reminders.Description
        FROM Reminders
        JOIN Pets ON Reminders.PetID = Pets.PetID
    """)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return str(results)

@app.route("/activities")
def activities():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT Pets.PetName,
               Activities.ActivityType,
               Activities.ActivityDate,
               Activities.ActivityTime,
               Activities.DurationMinutes,
               Activities.Notes
        FROM Activities
        JOIN Pets ON Activities.PetID = Pets.PetID
    """)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return str(results)

@app.route("/documents")
def documents():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT Pets.PetName,
               Documents.Title,
               Documents.DocumentType,
               Documents.FilePath,
               Documents.UploadDate
        FROM Documents
        JOIN Pets ON Documents.PetID = Pets.PetID
    """)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return str(results)

@app.route("/<filename>")
def website(filename):
    allowed = (".html", ".css", ".js", ".png", ".jpg", ".jpeg")

    if not filename.endswith(allowed):
        abort(404)

    return send_from_directory(".", filename)

@app.route("/add-pet", methods=["POST"])
def add_pet():
    name = request.form["petname"]
    breed = request.form["breed"]
    age = request.form["age"]
    weight = request.form["weight"]
    sex = request.form["sex"]
    birthday = request.form["birthday"]

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO Pets
        (UserID, PetName, Breed, Age, Weight, Sex, Birthday)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (1, name, breed, age, weight, sex, birthday))

    db.commit()
    cursor.close()
    db.close()

    return redirect("/petprofilespage.html")

@app.route("/add-medication", methods=["POST"])
def add_medication():
    pet_name = request.form["petname"]
    name = request.form["medname"]
    dosage = request.form["dosage"]
    instructions = request.form["instructions"]
    duration = request.form["duration"]

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT PetID FROM Pets
        WHERE PetName = %s AND UserID = %s
    """, (pet_name, 1))

    pets = cursor.fetchall()

    if len(pets) != 1:
        cursor.close()
        db.close()
        return "Pet not found or multiple pets have this name", 400

    pet_id = pets[0][0]

    cursor.execute("""
        INSERT INTO Medications
        (PetID, MedicationName, Dosage, Instructions, Duration)
        VALUES (%s, %s, %s, %s, %s)
    """, (pet_id, name, dosage, instructions, duration))

    db.commit()
    cursor.close()
    db.close()

    return redirect("/medicationhistorypage.html")

@app.route("/add-vet-visit", methods=["POST"])
def add_vet_visit():
    pet_name = request.form["petname"]
    visit_date = request.form["visitdate"]
    veterinarian = request.form["vet"]
    reason = request.form["reason"]
    status = request.form["status"]

    db = get_connection()
    cursor = db.cursor()
    
    cursor.execute("""
        SELECT PetID FROM Pets
        WHERE PetName = %s AND UserID = %s
    """, (pet_name, 1))

    pets = cursor.fetchall()

    if len(pets) != 1:
        cursor.close()
        db.close()
        return "Pet not found or multiple pets have this name", 400

    pet_id = pets[0][0]

    cursor.execute("""
        INSERT INTO VetVisits
        (PetID, VisitDate, Veterinarian, Reason, Status)
        VALUES (%s, %s, %s, %s, %s)
    """, (pet_id, visit_date, veterinarian, reason, status))

    db.commit()
    cursor.close()
    db.close()

    return redirect("/vetvisitspage.html")

@app.route("/add-vaccination", methods=["POST"])
def add_vaccination():
    pet_name = request.form["petname"]
    vaccine_name = request.form["vacname"]
    last_date = request.form["lastdate"]
    next_date = request.form["nextdate"]

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT PetID FROM Pets
        WHERE PetName = %s AND UserID = %s
    """, (pet_name, 1))

    pets = cursor.fetchall()

    if len(pets) != 1:
        cursor.close()
        db.close()
        return "Pet not found or multiple pets have this name", 400

    pet_id = pets[0][0]

    cursor.execute("""
        INSERT INTO Vaccinations
        (PetID, VaccineName, LastDate, NextDate)
        VALUES (%s, %s, %s, %s)
    """, (pet_id, vaccine_name, last_date, next_date))

    db.commit()
    cursor.close()
    db.close()

    return redirect("/vaccinationspage.html")

# update route
@app.route("/edit-pet", methods=["POST"])
def edit_pet():
    pet_id = request.form["petid"]
    name = request.form["petname"]
    breed = request.form["breed"]
    age = request.form["age"]
    weight = request.form["weight"]
    sex = request.form["sex"]
    birthday = request.form["birthday"]

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE Pets
        SET PetName = %s,
            Breed = %s,
            Age = %s,
            Weight = %s,
            Sex = %s,
            Birthday = %s
        WHERE PetID = %s AND UserID = %s
    """, (name, breed, age, weight, sex,
          birthday, pet_id, 1))

    db.commit()
    cursor.close()
    db.close()

    return redirect("/petprofilespage.html")
    
# delete route
@app.route("/delete-pet", methods=["POST"])
def delete_pet():
    pet_id = request.form["petid"]

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT PetID FROM Pets
        WHERE PetID = %s AND UserID = %s
    """, (pet_id, 1))

    if cursor.fetchone() is None:
        cursor.close()
        db.close()
        return "Pet not found", 404

    tables = ["Medications", "VetVisits", "Vaccinations",
              "Reminders", "Activities", "Documents"]

    for table in tables:
        cursor.execute(
            f"DELETE FROM {table} WHERE PetID = %s", (pet_id,)
        )

    cursor.execute(
        "DELETE FROM Pets WHERE PetID = %s AND UserID = %s",
        (pet_id, 1)
    )

    db.commit()
    cursor.close()
    db.close()

    return redirect("/petprofilespage.html")

# delete med
@app.route("/delete-medication", methods=["POST"])
def delete_medication():
    medication_id = request.form["medicationid"]

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        DELETE Medications
        FROM Medications
        JOIN Pets ON Medications.PetID = Pets.PetID
        WHERE Medications.MedicationID = %s
        AND Pets.UserID = %s
    """, (medication_id, 1))

    db.commit()
    cursor.close()
    db.close()

    return redirect("/medicationhistorypage.html")

if __name__ == "__main__":
    app.run(debug=True)
