"""
search.py
Handles searching for a patient and listing all patients.
"""

from patient import display_patient


def search_patient(patients, patient_id):
    """Return the patient dict matching patient_id, or None if not found."""
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None


def search_and_display(patients):
    """Prompt for a patient ID and display the matching record, if any."""
    print("\n--- Search Patient ---")
    patient_id = input("Enter Patient ID to search: ").strip()
    patient = search_patient(patients, patient_id)
    if patient:
        display_patient(patient)
    else:
        print(f"No patient found with ID '{patient_id}'.")
    return patient


def display_all_patients(patients):
    """Print a summary table of every registered patient."""
    print("\n--- All Registered Patients ---")
    if not patients:
        print("No patients registered yet.")
        return

    print(f"{'ID':<8}{'Name':<20}{'Age':<5}{'Department':<18}{'Status':<15}")
    print("-" * 66)
    for p in patients:
        print(f"{p['id']:<8}{p['name']:<20}{p['age']:<5}{p['department']:<18}{p['status']:<15}")