import csv
import os

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# List of services (without prices)
services = ["Haircut", "Facial", "Manicure", "Pedicure"]

# Load existing appointments
def load_appointments():
    try:
        with open("appointments.csv", "r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

# List to store appointments
appointments = load_appointments()

print("Salon Appointment System Initialized!")

def display_prices():
    print("\nAvailable Services and Prices:")
    print("Haircut: RS.1000.00")
    print("Facial: RS.3000.00")
    print("Manicure: RS.3500.00")
    print("Pedicure: RS.4000.00")
    input("\nPress Enter to return to the main menu...")  # Pause before returning to menu


# Function to book an appointment
def book_appointment():
    print("\nAvailable Services:")
    for service in services:
        print(f"- {service}")

    name = input("\nEnter Your Name: ")
    contact = input("Enter Contact Number: ")
    date = input("Enter Appointment Date (YYYY-MM-DD): ")
    service = input("Enter Service: ")

    # Validate service
    if service not in services:
        print("Invalid service! Please try again.")
        return

    appointment_id = len(appointments) + 1
    appointments.append({
        "id": appointment_id,
        "name": name,
        "contact": contact,
        "date": date,
        "service": service,
    })
    print("Appointment booked successfully!")
    input("Press Enter to return to the main menu...")  # Pause before returning to menu

# Function to view all appointments
def view_appointments():
    if not appointments:
        print("\nNo appointments found!")
        return

    print("\nUpcoming Appointments:")
    for appointment in appointments:
        print(f"ID: {appointment['id']}, Name: {appointment['name']}, Contact: {appointment['contact']}, Date: {appointment['date']}, Service: {appointment['service']}")

# Function to cancel an appointment
def cancel_appointment():
    contact = input("\nEnter Contact Number to Cancel Appointment: ")
    for appointment in appointments:
        if appointment["contact"] == contact:
            appointments.remove(appointment)
            print("Appointment canceled successfully!")
            return
    print("No appointment found for the given contact!")

# Function to save appointments to a CSV file
def save_appointments():
    print("Saving appointments...")
    with open("appointments.csv", "w", newline="") as file:
        fieldnames = ["id", "name", "contact", "date", "service"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(appointments)
    print("Appointments have been saved to appointments.csv")

# Main menu
def main_menu():
    while True:
        print("\nWelcome to salon Shiny\n---------------------------------")
        print("\nSalon Appointment System")
        print("1. Available Services and Prices")
        print("2. Book an Appointment")
        print("3. View All Appointments")
        print("4. Cancel an Appointment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_prices()
        elif choice == "2":
            book_appointment()   
        elif choice == "3":
            view_appointments()
        elif choice == "4":
            cancel_appointment()
        elif choice == "5":
            save_appointments()
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the main menu
main_menu()


