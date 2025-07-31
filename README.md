# Patient_Database

🏥 Patient Medical Record Management System
📌 Overview
This Python project is a terminal-based patient management system that allows users to:

Store patient demographic and medical test information

Add, delete, and modify patient records

View individual or all patient records

Generate simple medical statistics (e.g., anemia/diabetes prevalence by gender)

It demonstrates object-oriented programming (OOP), file reading, and basic CRUD operations using Python dictionaries.

🗂️ Features
✅ Add New Patient: Enter demographic details and test results

✅ Delete Patient: Remove patient record by ID

✅ Modify Test Results: Update any patient’s medical test data

✅ View Records: Display individual or all patient records

✅ View Specific Test: Retrieve specific test result for a patient

✅ Statistics Module: Calculate anemia/diabetes percentages by gender

✅ Interactive Menu: Easy-to-navigate terminal menu

🏗️ Project Structure
css
Copy
Edit
📁 patients-database-tab.txt
📄 patient_management_system.py (main script)
patients-database-tab.txt: Sample dataset in tab-separated format

patient_management_system.py: Main Python script with full functionality

▶️ How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/patient-management.git
cd patient-management
Ensure your patient data file is named patients-database-tab.txt and is in the correct directory.

Run the program:

bash
Copy
Edit
python patient_management_system.py
Follow the on-screen interactive menu.

💡 Example Functionalities
Add Patient → Add demographics + test results with auto-generated ID

Modify Test → Update any individual test without overwriting full record

View Statistics → See what % of men/women have anemia/diabetes

📈 Potential Improvements
💻 Convert into a GUI application using Tkinter or PyQt

🖥️ Implement file saving/loading for persistent records

📊 Use CSV/JSON formats for more structured data management

🩺 Add more medical tests and advanced analytics

👨‍💻 Author
Developed by Jason Finkle for educational purposes on OOP and data management in Python.


