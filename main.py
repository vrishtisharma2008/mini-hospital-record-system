"""
main.py
Mini Hospital Record System - main menu and program entry point.
"""

from patient import add_patient, display_patient
from search import search_and_display, display_all_patients
from doctor import assign_doctor
from consultation import update_consultation_status


def print_menu():
    print("\n===== MINI HOSPITAL RECORD SYSTEM =====")
    print("1. Add Patient")
    print("2. Search Patient")
    print("3. Display Patient Details")
    print("4. Assign Doctor & Department")
    print("5. Update Consultation Status")
    print("6. Display All Patients")
    print("7. Exit")


def main():
    patients = []
    last_found_patient = None

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_patient(patients)

        elif choice == "2":
            last_found_patient = search_and_display(patients)

        elif choice == "3":
            if last_found_patient:
                display_patient(last_found_patient)
            else:
                print("Search for a patient first (option 2).")

        elif choice == "4":
            assign_doctor(last_found_patient)

        elif choice == "5":
            update_consultation_status(last_found_patient)

        elif choice == "6":
            display_all_patients(patients)

        elif choice == "7":
            print("Exiting Mini Hospital Record System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()