"""
doctor.py
Handles assigning a doctor and department to a patient.
"""

DEPARTMENTS = {
    "1": "General Medicine",
    "2": "Cardiology",
    "3": "Orthopedics",
    "4": "Pediatrics",
}


def assign_doctor(patient):
    """Ask for a doctor's name and department, then update the patient."""
    if patient is None:
        print("No patient selected. Search for a patient first.")
        return

    print("\n--- Assign Doctor & Department ---")
    doctor_name = input("Doctor's name: ").strip()

    print("Departments:")
    for key, name in DEPARTMENTS.items():
        print(f"  {key}. {name}")

    while True:
        choice = input("Choose department number: ").strip()
        if choice in DEPARTMENTS:
            department = DEPARTMENTS[choice]
            break
        print("  Invalid choice. Pick a number from the list.")

    patient["doctor"] = doctor_name if doctor_name else "Not specified"
    patient["department"] = department
    print(f"Dr. {patient['doctor']} ({department}) assigned to {patient['name']}.")