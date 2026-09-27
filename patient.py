"""
patient.py
Handles adding new patients and displaying a single patient's details.
"""

from validation import (
    validate_patient_id,
    validate_name,
    validate_age,
    validate_gender,
    validate_contact,
)


def get_valid_input(prompt, validator, *extra_args):
    """Keep asking until the entered value passes the validator."""
    while True:
        value = input(prompt).strip()
        is_valid, message = validator(value, *extra_args)
        if is_valid:
            return value
        print(f"  Invalid input: {message}")


def add_patient(patients):
    """Collect patient details from the user and add a new record."""
    print("\n--- Add New Patient ---")
    existing_ids = [p["id"] for p in patients]

    patient_id = get_valid_input("Patient ID: ", validate_patient_id, existing_ids)
    name = get_valid_input("Patient name: ", validate_name)
    age = get_valid_input("Age: ", validate_age)
    gender = get_valid_input("Gender (Male/Female/Other): ", validate_gender)
    contact = get_valid_input("Contact number (10 digits): ", validate_contact)
    address = input("Address: ").strip()
    symptoms = input("Symptoms / reason for visit: ").strip()

    new_patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender.capitalize(),
        "contact": contact,
        "address": address,
        "symptoms": symptoms,
        "doctor": "Not assigned",
        "department": "Not assigned",
        "status": "Pending",
    }
    patients.append(new_patient)
    print(f"\nPatient '{name}' added successfully with ID {patient_id}.")
    return new_patient


def display_patient(patient):
    """Print one patient's details in a readable format."""
    print("\n----- PATIENT DETAILS -----")
    print(f"Patient ID   : {patient['id']}")
    print(f"Name         : {patient['name']}")
    print(f"Age          : {patient['age']}")
    print(f"Gender       : {patient['gender']}")
    print(f"Contact      : {patient['contact']}")
    print(f"Address      : {patient['address']}")
    print(f"Symptoms     : {patient['symptoms']}")
    print(f"Doctor       : {patient['doctor']}")
    print(f"Department   : {patient['department']}")
    print(f"Status       : {patient['status']}")