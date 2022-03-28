database = {'entries': []}


def database_length_check():
    return len(database['entries']) + 1


def add_entry(user_entry):
    entry = {
        'serial #': database_length_check(),
        'name': user_entry['name'],
        'age': user_entry['age'],
        'gender': user_entry['gender'],
        'registration #': user_entry['registration#']
    }
    database['entries'].append(entry)


def delete(which_entry):
    for entry in enumerate(database['entries']):
        if entry[which_entry[0]] == which_entry[1]:
            database['entries'].remove(entry)


def select_and_get_value():
    print("Please Enter serial Number On which number you search.")
    value_type = ''
    value = ''
    print("1.Serial #")
    print("2.name")
    print("3.age")
    print("4.gender")
    print("5.registration")
    choice = int(input("Enter Your Choice:"))
    if 1 < choice > 5:
        print("Invalid Input... Please Enter Valid Number")
    else:
        if choice == 1:
            SR = 'serial #'
            value_type = SR
            value = input("Enter serial Number:")
            return (value_type, value)
        elif choice == 2:
            value_type = 'name'
            value = input("Enter name :")
            return (value_type, value)
        elif choice == 3:
            value_type = 'age'
            value = input("Enter age :")
            return (value_type, value)
        elif choice == 2:
            value_type = 'gender'
            value = input("Enter gender :")
            return (value_type, value)
        elif choice == 2:
            value_type = 'registration #'
            value = input("Enter registration Number :")
            return (value_type, value)


def enter_student_details():
    print("Please Enter Details..")
    output = {}
    output['name'] = input("Enter Name : ")
    output['age'] = input("Enter age : ")
    output['gender'] = input("Enter gender : ")
    output['registration#'] = input("Enter registration #: ")
    return output


def display_all_entries():
    for entry in database['entries']:
        print(f"SerNo : {entry['serial #']}")
        print(f"Name : {entry['name']}")
        print(f"Age : {entry['age']}")
        print(f"Gender : {entry['gender']}")
        print(f"Registration # : {entry['registration #']}\n")


print("=========Welcome to student management system========")
while True:
    print("\n What would you like to do:")
    print("1. Add entry")
    print("2. Update entry")
    print("3. delete entry")
    print("4. Search entry")
    print("5. See All entries")
    print("6. Exiting...")
    choice = int(input("Please Enter Your choice : "))
    if choice == 1:
        entry = enter_student_details()
        add_entry(entry)
        print("Data Successfully inserted.")
    elif choice == 5:
        display_all_entries()
    elif choice == 3:
        entry = select_and_get_value()
        delete(entry)
        print("Entry Delete Successfully")
    elif choice == 6:
        print("Exiting.....")
        break
