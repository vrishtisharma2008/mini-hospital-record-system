"""
consultation.py
Handles updating a patient's consultation status.
"""

STATUS_OPTIONS = {
    "1": "Pending",
    "2": "In Consultation",
    "3": "Completed",
}


def update_consultation_status(patient):
    """Ask for a new status and update the patient's record."""
    if patient is None:
        print("No patient selected. Search for a patient first.")
        return

    print("\n--- Update Consultation Status ---")
    for key, status in STATUS_OPTIONS.items():
        print(f"  {key}. {status}")

    while True:
        choice = input("Choose new status number: ").strip()
        if choice in STATUS_OPTIONS:
            patient["status"] = STATUS_OPTIONS[choice]
            break
        print("  Invalid choice. Pick a number from the list.")

    print(f"Status for {patient['name']} updated to '{patient['status']}'.")