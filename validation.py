"""
validation.py
Handles input validation for the Mini Hospital Record System.
"""


def validate_patient_id(patient_id, existing_ids):
    """Check that a patient ID is non-empty and not already used."""
    if not patient_id.strip():
        return False, "Patient ID cannot be empty."
    if patient_id in existing_ids:
        return False, "Patient ID already exists. Please use a unique ID."
    return True, ""


def validate_name(name):
    """Check that a name contains only letters and spaces."""
    if not name.strip():
        return False, "Name cannot be empty."
    if not all(part.isalpha() for part in name.split()):
        return False, "Name should contain only letters."
    return True, ""


def validate_age(age_str):
    """Check that age is a whole number within a realistic range."""
    if not age_str.isdigit():
        return False, "Age must be a whole number."
    age = int(age_str)
    if age <= 0 or age > 120:
        return False, "Age must be between 1 and 120."
    return True, ""


def validate_gender(gender):
    """Check that gender is one of the accepted values."""
    if gender.strip().capitalize() not in ("Male", "Female", "Other"):
        return False, "Gender must be Male, Female, or Other."
    return True, ""


def validate_contact(contact_str):
    """Check that a contact number is exactly 10 digits."""
    if not contact_str.isdigit() or len(contact_str) != 10:
        return False, "Contact number must be exactly 10 digits."
    return True, ""