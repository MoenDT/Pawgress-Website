CREATE DATABASE IF NOT EXISTS pawgress_db;
USE pawgress_db;

CREATE TABLE IF NOT EXISTS Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL
);

CREATE TABLE Pets (
    PetID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    PetName VARCHAR(50) NOT NULL,
    Species VARCHAR(30),
    Breed VARCHAR(50),
    Age INT,
    Weight DECIMAL(6,2),
    Sex VARCHAR(10),
    Birthday DATE,
    PhotoPath VARCHAR(225),
    DateRegistered DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE Medications (
    MedicationID INT AUTO_INCREMENT PRIMARY KEY,
    PetID INT NOT NULL,
    MedicationName VARCHAR(100) NOT NULL,
    Dosage VARCHAR(100),
    Instructions VARCHAR(255),
    Duration VARCHAR(100),
    DateGiven DATE,
    TimeGiven TIME,
    FOREIGN KEY (PetID) REFERENCES Pets(PetID)
);

CREATE TABLE VetVisits (
    VisitID INT AUTO_INCREMENT PRIMARY KEY,
    PetID INT NOT NULL,
    VisitDate DATE NOT NULL,
    Veterinarian VARCHAR(100),
    Reason VARCHAR(200),
    Status VARCHAR(30),
    Notes VARCHAR(200),
    FOREIGN KEY (PetID) REFERENCES Pets(PetID)
);

CREATE TABLE Vaccinations (
    VaccinationID INT AUTO_INCREMENT PRIMARY KEY,
    PetID INT NOT NULL,
    VaccineName VARCHAR(100) NOT NULL,
    LastDate DATE,
    NextDate DATE,
    FOREIGN KEY (PetID) REFERENCES Pets(PetID)
);

CREATE TABLE Reminders (
    ReminderID INT AUTO_INCREMENT PRIMARY KEY,
    PetID INT NOT NULL,
    ReminderType VARCHAR(50),
    ReminderDate DATE NOT NULL,
    Description VARCHAR (200),
    Recurring BOOLEAN DEFAULT FALSE,
    Enabled BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (PetID) REFERENCES Pets(PetID)
);

CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY,
    PetID INT NOT NULL,
    ActivityType VARCHAR(50) NOT NULL,
    ActivityDate DATE NOT NULL,
    ActivityTime TIME,
    EndDate DATE,
    DurationMinutes INT,
    NextDueDate DATE,
    Notes VARCHAR(200),
    FOREIGN KEY (PetID) REFERENCES Pets(PetID)
);

CREATE TABLE Documents (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY,
    PetID INT NOT NULL,
    Title VARCHAR(100) NOT NULL,
    DocumentType VARCHAR(50),
    FilePath VARCHAR(200) NOT NULL,
    UploadDate DATE,
    FOREIGN KEY (PetID) REFERENCES Pets(PetID)
);
