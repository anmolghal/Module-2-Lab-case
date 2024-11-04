# Author: Anmol Ghale
# File Name: student_qualification_app.py
# Description: This app accepts student names and GPAs, checks if they qualify for the Dean's List or Honor Roll,
#              and displays the appropriate message. The app stops taking inputs when the last name "ZZZ" is entered.

def main():
    while True:
        # Accept student's last name
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            print("Exiting program.")
            break
        
        # Accept student's first name
        first_name = input("Enter student's first name: ")
        
        # Accept student's GPA
        try:
            gpa = float(input("Enter student's GPA: "))
        except ValueError:
            print("Invalid GPA. Please enter a valid number.")
            continue
        
        # Check qualifications
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

# Run the app
main()
