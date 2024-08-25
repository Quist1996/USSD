import requests

def get_student_id():
    ussd = input("Enter USSD code: ")
    if ussd == "*124#":
        school = 'Good Shepherd Academy'
        home = input(f"Welcome to {school}\nPlease enter student ID: ")
        print(home)

        try:
            response = requests.get(f"http://146.190.72.22/verifyStudent/{home}")
            response.raise_for_status()  # Check if the request was successful
            student_data = response.json()  # Parsing the JSON response

            print (student_data)

            if student_data ['Available'] == "Yes":
            #print("true")
            # Display the retrieved data
                print("confirm\n"
                  f"Student Name: {student_data['Name']}")
                print(f"Student Class: {student_data['class']}")

                choice = input("1. Yes\n2. No\nPlease enter 1 or 2: ")
                if choice == "1":
                    print("1.Pay Fees")
                    print("2.E- cards")
                    print("3.Check Student reports")
                    print("4.Check Arrears")
                    next_step = input("Please enter: ")









            else:
                retry = input("Wrong ID\n"
                              "please enter correct student ID: ")
                print(retry)

        except requests.exceptions.RequestException as e:
            print(f"Error retrieving student data: {e}")

    else:
        print("Invalid USSD code")


get_student_id()


