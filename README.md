# Pawgress — Local Test Environment Setup

Pawgress is a Python Flask web application backed by a MySQL database. Follow the steps below to configure the database, install dependencies, and run the application locally.

---

## Prerequisites

* **Python 3.10+**
* **MySQL Server 8.0+** (or **Docker Desktop** if running MySQL in a container)

---

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Pawgress
```

---

## 2. Set Up the Python Virtual Environment

Create and activate a virtual environment inside the project root, then install the required Python packages:

### macOS / Linux / Git Bash

```bash
python -m venv venv
source venv/bin/activate
pip install flask mysql-connector-python
```
Note: Use ```venv/Scripts/activate``` for git bash in windows

### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install flask mysql-connector-python
```

---

## 3. Initialize the MySQL Database

You can set up `pawgress_db` with a local MySQL installation

### Local MySQL Installation

1. Install Oracle MySQL ```winget install Oracle.MySql```
2. then run the MySQL Configurator. Ensure your local MySQL Server service is running on `localhost:3306`.
3. Load the database schema (`schema.sql`) first. Then seed data (`data.sql`). Loading `data.sql`.

### Option A: Command Line

   **macOS / Linux / Git Bash:**
   ```bash
   mysql -u root -p < schema.sql
   mysql -u root -p < data.sql
   ```

   **Windows (PowerShell):**
   ```powershell
   Get-Content schema.sql | mysql -u root -p
   Get-Content data.sql | mysql -u root -p
   ```

### Option B: MySQL via MySQL Workbench

If you are unable to get these commands working, you may also initialize the database using MySQL Workbench.

1. Create a new connection in MySQL Workbench to your local database
2. Open the schema.sql file and execute it.
3. Open the data.sql file and execute it.

Your database is now loaded.

---

## 4. Configure Environment Variables

`database.py` reads the MySQL `root` password from the `DB_PASSWORD` environment variable. Set this in the same terminal session you will use to run Flask:

### macOS / Linux / Git Bash

```bash
export DB_PASSWORD="your_mysql_root_password"
```

### Windows (PowerShell)

```powershell
$env:DB_PASSWORD="your_mysql_root_password"
```

---

## 5. Run the Application

Start the Flask development server from inside the `Pawgress/` directory:

```bash
python app.py
```

Once running, open your browser and navigate to:
* **Web App:** [http://127.0.0.1:5000](http://127.0.0.1:5000)
* **Sample API Endpoint:** [http://127.0.0.1:5000/api/pets](http://127.0.0.1:5000/api/pets)
