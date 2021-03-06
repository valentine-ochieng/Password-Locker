#!/usr/bin/env python3.9
from credential import Credential
from user import User
import random
import string

# credential methods


def create_credential(site_name, user_name, password):
    '''
    Function to create a new user credentials
    '''
    new_credential = Credential(site_name, user_name, password)
    return new_credential


def save_credential(credential):
    '''
    Funtion to save the credential
    '''
    credential.save_credential()


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def find_credential(site_name):
    '''
    Function to find a credential
    '''
    return Credential.locate_account(site_name)


def check_existing_credentials(account_name):
    '''
    Function to check whether a credential exists
    '''
    return Credential.credential_exist(account_name)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()


# Users method
def create_user(first_name, last_name, password):
    '''
   To generate a new user credential, use this function.
    '''
    new_user = User(first_name, last_name, password)
    return new_user


def save_users(user):
    '''
    The user credential is saved using this function.
    '''
    user.save_users()


def main():

    print("HELLO, WELCOME TO PASSWORD LOCKER.")
    usr_name = input("Please enter your name:")

    while True:
        print(
            f"Hello {usr_name}, Kindly use these short codes to either sign up or login to your account.")
        print("sn - sign up to new users")
        print("lg - log into your account")
        short_code = input("Enter short code:").upper()

        if short_code == 'SN':
            print("Enter  first_name: ")
            fst_name = input()

            print("Enter  last_name: ")
            lst_name = input()

            print("Enter password")
            fpin = input()
            print('*' * 60)

            print("You've successfully completed the registration process.")
            print("Kindly, proceed by logging into your account",)
            print('\n')

        elif short_code == 'LG':
            print("Enter your username")
            username = input()

            print("Enter your password")
            pin = input()
            if f"{username } = {pin}":
                print('*' * 60)

                print(f"{username}, you've succesfully logged into your account")
                print('\n')

                pass
                while True:
                    print("Use these short codes: \n sc - Save credentials \n, cc - Create new credentials \n, dc - display credentials \n, lc - locate saved credential \n, del - delete credentials \n, ex - exit the account")

                    short_code = input()

                    if short_code == 'cc':
                        print(" Create New Credentials")
                        print("-"*40)

                        print(" Input Site Name: ")
                        site_name = input()

                        print(" Input User Name: ")
                        user_name = input()

                        print(
                            "Would you prefer a password that is customized for you?, respond by  YES or NO")
                        password = input().upper()
                        if password == 'YES':
                            print("What length do you want your password to be?")
                            password_length = int(input())
                            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
                            gen_password = "".join(random.choice(
                                chars) for i in range(password_length))

                        elif password == 'NO':
                            print("Enter the password you would like to use.")
                            gen_password = input()

                        else:
                            print("Wrong input, enter yes or no",)

                        save_credential(create_credential(
                            site_name, user_name, gen_password))
                        print('\n')
                        print('-'*50)
                        print(
                            f"{user_name}, your new password has successfully  been created")
                        print(f" Your generated password is: {gen_password}")
                        print('-'*50)
                        print('\n')

                    elif short_code == 'sc':
                        print("Save Existing credentials")
                        print("-"*50)

                        print(" Input Site Name: ")
                        site_name = input()

                        print(" Input User Name: ")
                        user_name = input()

                        print("Input Password: ")
                        password = input()

                        save_credential(create_credential(
                            site_name, user_name, password))
                        print('\n')
                        print(f"{site_name} credentials successfully saved")
                        print('\n')

                    elif short_code == 'dc':
                        if display_credentials():
                            print(
                                "The following is a list of all of your credentials.")
                            print('\n')

                            for credential in display_credentials():
                                print(f"{credential.account_name}")
                                print("-"*50)
                                print(
                                    f"Username: {credential.first_name} {credential.last_name}")
                                print(f"Password: {credential.user_password}")
                                print('\n')

                        else:
                            print('\n')
                            print("You don't seem to have any stored credentials.")
                            print('\n')

                    elif short_code == 'lc':
                        print(
                            "Please type the name of the site you're looking for into the below.\n")

                        search_site = input("Site Name: ")
                        if check_existing_credentials(search_site):
                            search_site = find_credential(search_site)
                            print(
                                f"{search_site.first_name} {search_site.last_name}")
                            print("-"*50)

                            print(f"Password: {search_site.user_password}")

                        else:
                            print("These credentials aren't available.")
                            print('\n')

                    elif short_code == 'del':
                        print(
                            "Please type the name of the site you wish to remove below.\n")
                        site_delete = input()
                        if check_existing_credentials(site_delete):
                            site_delete = find_credential(site_delete)
                            delete_credential(site_delete)

                            print("Credentials were successfully removed.")

                        else:
                            print("There are no credentials.")

                        print('-'*50)
                    elif short_code == "ex":
                        print("-"*50)

                        print(
                            "THANK YOU FOR USING PASSWORD LOCKER AND WELCOME BACK AGAIN!!",)
                        print('\n')
                        break

if __name__ == '__main__':
    main()
