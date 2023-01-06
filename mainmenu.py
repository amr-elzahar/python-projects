import re
import ast
import os
from datetime import datetime
from tabulate import tabulate


def create_line_break(text):
    print("\n*************************************************************************************\n")
    print(f"\t\t\t\t\t{text}")
    print("\n*************************************************************************************\n")


def name_validation(name_type):

    while True:
        entered_first_name = input(
            f'Enter Your {name_type} Name: ').strip().lower()
        if entered_first_name.isalpha():
            return entered_first_name
        else:
            print('\nNOT a valid name!\n')


def email_validation():
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    while True:
        entered_email = input('Enter Your Email: ')
        if re.fullmatch(regex, entered_email):
            return entered_email

        else:
            print('\nNot a valid email!\n')


def password_validation():
    while True:
        password = input("Enter Your Password: ")
        confirmed_password = input("Confirm Your Password: ")
        if password and password == confirmed_password:
            return password
        else:
            print("\nPasswords are NOT the same!\n")


def phone_number_valdation():

    while True:
        entered_phone = input('Enter Your Phone Number: ')
        regex = re.compile(r'^01[0125][0-9]{8}$')

        if re.fullmatch(regex, entered_phone):
            return entered_phone
        else:
            print('\nNot a valid phone number!\n')


def user_dict_data():
    first_name = name_validation('First')
    last_name = name_validation('Last')
    phone_number = phone_number_valdation()
    email = email_validation()
    password = password_validation()

    return {'first name': first_name, 'last name': last_name, 'phone number': phone_number, 'email': email, 'password': password}


def project_title_validation():
    while True:
        entered_title = input("Enter Your Title (String): ").strip().lower()
        if entered_title.isalpha():
            return entered_title
        else:
            print("\nNOT a valid title!\n")


def project_description_validation():
    while True:
        entered_description = input(
            "Enter Your Description (String): ").strip().lower()
        if entered_description.isalpha():
            return entered_description
        else:
            print("\nNOT a valid describtion!\n")


def project_target_validation():
    while True:
        entered_total = input("Enter Your Total Target (Number): ")
        if entered_total.isnumeric():
            return entered_total
        else:
            print("\nNOT a valid target!\n")


def project_date_validation(date_type):
    format = "%d-%m-%Y"

    while True:

        date = input(
            f"Enter a {date_type} date format such as(05-08-2010): ")
        try:
            bool(datetime.strptime(date, format))
            return date
        except:
            print("\nNOT a valid date format!\n")


def empty_file_check(file):
    if os.stat(file).st_size == 0:
        return True
    else:
        return False


def project_dict_data():

    title = project_title_validation()
    description = project_description_validation()
    target = project_target_validation()
    start_date = project_date_validation('Start')
    end_date = project_date_validation('End')

    return {
        "title": title,
        "description": description,
        "total target": target,
        "start date": start_date,
        "end date": end_date
    }


def create_project():

    with open(f"users_projects/{user_dict_data()['email']}.txt", "a") as file:
        file.write(str(user_dict_data())+"\n")


def view_projects():
    if empty_file_check(f"users_projects/{user_dict_data()['email']}.txt"):
        print("\nNo projects yet!. Try to add some!\n")
    else:
        with open(f"users_projects/{user_dict_data()['email']}.txt", "r") as file:
            for line in file:
                project = ast.literal_eval(line)

                data = [[project['title'], project['description'], project['total target'],
                        project['start date'], project['end date']]]
                col_names = ['Title', 'Description',
                             'Total Target', 'Start Date', 'End Date']
                print(tabulate(data, headers=col_names,
                      tablefmt="github"))
                print('\n\t\t\t*******************************************\n')


def delete_project():
    title = input('Enter Your projct title: ')
    is_existing = False
    try:
        with open(f"users_projects/{user_dict_data()['email']}.txt", 'r') as fr:
            lines = fr.readlines()

            with open(f"users_projects/{user_dict_data()['email']}.txt", 'w') as fw:
                for line in lines:
                    conv_line = ast.literal_eval(line)
                    if title.lower() != conv_line['title']:
                        fw.write(line)
                    else:
                        is_existing = True
                        print('\nSuccessfully Deleted!\n')
                if not is_existing:
                    print('\nNo such a title!\n')
    except:
        print("Oops! Something went wrong")


# EDIT START

def edit_title():
    old_title = project_title_validation()
    new_title = project_title_validation()

    with open(f"users_projects/{user_dict_data()['email']}.txt", 'r') as f:
        for index, line in enumerate(f):
            user = ast.literal_eval(line)
            if user["title"] == old_title:
                user["title"] = new_title
                new_user = user
                user_index = index
                with open(f"users_projects/{user_dict_data()['email']}txt", "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for index, line in enumerate(lines):
                        if index != user_index:
                            file.write(line)
                        else:
                            file.write(str(new_user)+"\n")
            else:
                print('No such a title')
                break


def edit_description():
    old_desc = project_description_validation()
    new_desc = project_description_validation()

    with open(f"users_projects/{user_dict_data()['email']}.txt", 'r') as f:
        for index, line in enumerate(f):
            user = ast.literal_eval(line)
            if user["description"] == old_desc:
                user["description"] = new_desc
                new_user = user
                user_index = index
                with open(f"users_projects/{user_dict_data()['email']}txt", "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for index, line in enumerate(lines):
                        if index != user_index:
                            file.write(line)
                        else:
                            file.write(str(new_user)+"\n")
            else:
                print('\nNo such a description\n')
                break


def edit_target():
    old_target = project_target_validation()
    new_target = project_target_validation()

    with open(f"users_projects/{user_dict_data()['email']}.txt", 'r') as f:
        for index, line in enumerate(f):
            user = ast.literal_eval(line)
            if user["total target"] == old_target:
                user["total target"] = new_target
                new_user = user
                user_index = index
                with open(f"users_projects/{user_dict_data()['email']}txt", "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for index, line in enumerate(lines):
                        if index != user_index:
                            file.write(line)
                        else:
                            file.write(str(new_user)+"\n")
            else:
                print('\nNo such a target\n')
                break


def edit_start_date():
    old_start_date = project_date_validation('Start')
    new_start_date = project_date_validation('Start')

    with open(f"users_projects/{user_dict_data()['email']}.txt", 'r') as f:
        for index, line in enumerate(f):
            user = ast.literal_eval(line)
            if user["start date"] == old_start_date:
                user["start date"] = new_start_date
                new_user = user
                user_index = index
                with open(f"users_projects/{user_dict_data()['email']}txt", "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for index, line in enumerate(lines):
                        if index != user_index:
                            file.write(line)
                        else:
                            file.write(str(new_user)+"\n")
            else:
                print('\nNo such a date\n')
                break


def edit_end_date():
    old_end_date = project_date_validation('End')
    new_end_date = project_date_validation('End')

    with open(f"users_projects/{user_dict_data()['email']}.txt", 'r') as f:
        for index, line in enumerate(f):
            user = ast.literal_eval(line)
            if user["end date"] == old_end_date:
                user["end date"] = new_end_date
                new_user = user
                user_index = index
                with open(f"users_projects/{user_dict_data()['email']}txt", "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for index, line in enumerate(lines):
                        if index != user_index:
                            file.write(line)
                        else:
                            file.write(str(new_user)+"\n")
            else:
                print('\nNOT a valid date!\n')
                break


# EDIT END


def edit_menu():
    create_line_break('Edit Mode')
    print(" Select one of the following choices :- \n")
    print('1. Edit Title\n')
    print('2. Edit Description\n')
    print('3. Edit Total Target')
    print('4. Edit Start Date\n')
    print('5. Edit End Date\n')
    print('6. Exit\n')

    while True:
        entered_choice = input('Enter Your Choice: ')
        try:
            converted_into_number = int(entered_choice)
        except:
            create_line_break('\nNot a number!\n')
            break
            # edit_menu()
        else:

            if converted_into_number == 1:
                edit_title()
            elif converted_into_number == 2:
                edit_description()
            elif converted_into_number == 3:
                edit_target()
            elif converted_into_number == 4:
                edit_start_date()
            elif converted_into_number == 5:
                edit_end_date()
            elif converted_into_number == 6:
                create_line_break('Bye')
                exit()
            else:
                print('\nNot a valid choice!\n')
                break
                # edit_menu()


# PROJECTS END


def login_menu():
    create_line_break('Logged in successfully')
    print(" Select one of the following choices :- \n")
    print('1. View all projects\n')
    print('2. Create a new project\n')
    print('3. Edit Your own project\n')
    print('4. Delete your own project\n')
    print('5. Exit\n')
    create_line_break('There is s bug here i cannot fix. When you try to view  all projects for example, it excutes a completely different function. it\'s something related to a feature in python called tracback. I\'ve spent a couple of days trying to fix that but i failed. Every function of this menu does its own main role of creating or editing or deleting and so on but SEPARATELT. The error comes up when i combined all of them in the same file.')
    while True:
        entered_choice = input('Enter Your Choice: ')
        try:
            converted_into_number = int(entered_choice)
        except:
            create_line_break('\nNot a number!\n')
            break
            # login_menu()
        else:

            if converted_into_number == 1:
                view_projects()
                break
            elif converted_into_number == 2:
                create_project()
                break
            elif converted_into_number == 3:
                edit_menu()
                break
            elif converted_into_number == 4:
                delete_project()
                break
            elif converted_into_number == 5:
                create_line_break('Bye')
                exit()
            else:
                print('\nNot a valid choice!\n')
                break


def signup():

    file = open('users', 'a+')
    file.seek(0)
    data = file.read(100)
    if len(data) > 0:
        file.write("\n")
    file.write(str(user_dict_data()))
    file.close()
    with open(f"users_projects/{user_dict_data()['email']}.txt", 'w'):
        pass
    create_line_break('Successfully signed up')
    return


def login():

    while True:
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        f = open("users", "r")
        for line in f:
            user = ast.literal_eval(line)
            if user["email"] == email and user["password"] == password:
                login_menu()
                break
            else:
                print('\nThis email does not exist\n')
                break


def main_menu():
    create_line_break('Welcome')
    print(" Select one of the following choices :- \n")
    print('1. Login\n')
    print('2. Signup\n')
    print('3. Exit\n')

    while True:
        entered_choice = input('Enter Your Choice: ')
        try:
            converted_into_number = int(entered_choice)
        except:
            print('\nNot a number!\n')
            break
        else:

            if converted_into_number == 1:
                login()

            elif converted_into_number == 2:
                signup()
                break
            elif converted_into_number == 3:
                create_line_break('Bye')
                exit()
            else:
                create_line_break('\nNot valid choice!\n')
                break


main_menu()
