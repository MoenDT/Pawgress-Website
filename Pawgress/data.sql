USE pawgress_db;

INSERT INTO Users (Name, Username, Email, PasswordHash)
VALUES ('John Doe', 'johndoe', 'john@example.com', 'test_hash_placeholder');

INSERT INTO Pets (UserID, PetName, Species, Breed, Age, Weight, Sex, Birthday, DateRegistered)
VALUES (1, 'Zeus', 'Dog', 'Golden Retriever', 5, 80, 'Male', '2021-01-23', '2026-11-23');

INSERT INTO Medications (PetID, MedicationName, Dosage, Instructions, Duration)
VALUES (1, 'Amoxi', '1/2 tablet', 'Give with food, twice daily (Every 12 hours)', 'Until bottle is empty');

INSERT INTO VetVisits (PetID, VisitDate, Veterinarian, Reason, Status, Notes)
VALUES (1, '2026-11-12', 'Dr. Galle', 'Injured paw', 'Completed', 'Make follow-up if condition worsens'),
       (1, '2026-11-23', 'Dr. Galle', 'Annual vaccines', 'Completed', 'Bring vaccination records'),
       (1, '2026-06-21', 'Dr. Galle', 'Check up', 'Completed', 'Routing care. Zeus exhibits a healthy weight and is up to date on vaccines. Recommend flea/tick/worm prevention.');

INSERT INTO Vaccinations (PetID, VaccineName, LastDate, NextDate)
VALUES (1, 'Rabies', '2026-07-15', '2029-07-15');

INSERT INTO Reminders (PetID, ReminderType, ReminderDate, Description, Recurring, Enabled)
VALUES (1, 'Vet Visit', '2027-07-15', 'Annual vaccines', FALSE, TRUE);

INSERT INTO Activities (PetID, ActivityType, ActivityDate, ActivityTime, DurationMinutes, Notes)
VALUES (1, 'Walk', '2026-11-23', '10:00:00', 30, 'Met the neighbors dog :)');

INSERT INTO Documents (PetID, Title, DocumentType, FilePath, UploadDate)
VALUES (1, 'Rabies Certificate', 'Vaccination', 'uploads/rabies.pdf', '2026-11-23');
