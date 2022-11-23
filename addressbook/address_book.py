import csv
import json
import logging
import os.path

logging.basicConfig(filename='AddressBook_logs.log', encoding='utf-8', level=logging.DEBUG)


class Contact:

    def __init__(self, contacts_dict):
        self.first_name = contacts_dict.get("first_name")
        self.last_name = contacts_dict.get("last_name")
        self.address = contacts_dict.get("address")
        self.city = contacts_dict.get("city")
        self.state = contacts_dict.get("state")
        self.pin = contacts_dict.get("pin")
        self.phone = contacts_dict.get("phone")
        self.email = contacts_dict.get("email")

    def get_cont_dict(self):
        return {'first_name': self.first_name, 'last_name': self.last_name, 'address': self.address, 'city': self.city,
                'state': self.state, 'pin': self.pin, 'phone': self.phone, 'email': self.email}

    def as_string(self):
        return "{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}"\
            .format(self.first_name, self.last_name, self.address, self.city, self.state, self.pin, self.phone, self.email)


class AddressBook:

    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contact_dict = {}

    def add_contact(self, contact_object):
        """
        Function to add contact_object into dictionary
        :param contact_object: Contact object
        """
        try:
            self.contact_dict.update({contact_object.first_name: contact_object})
        except Exception as e:
            logging.exception(e)

    def display_names(self):
        """
        Function to display contact names in address book
        """
        try:
            if len(self.contact_dict) == 0:
                print("No contacts to display")
            else:
                for key, value in self.contact_dict.items():
                    print("{:<10} {:<10}".format('Contact name-->', key))
        except Exception as e:
            print(e)
            logging.exception(e)

    def get_contact_object(self, name):
        """
        Function to get contact object
        :param name: string
        :return: object of Contact
        """
        try:
            return self.contact_dict.get(name)
        except Exception as e:
            logging.exception(e)

    def display_contacts(self):
        """
        Function to display contact details
        """
        try:
            if len(self.contact_dict) == 0:
                print("No contacts to display")
            else:
                print("{:<11} {:<11} {:<11} {:<11} {:<11} {:<11} {:<11} {:<11} ".format
                      ('First Name', 'Last Name', 'Address', 'City', 'State', 'PIN', 'Phone', 'Email'))
                for key, value in self.contact_dict.items():
                    print(value.as_string())
        except Exception as e:
            print(e)
            logging.exception(e)

    def update_contact(self, contact_object, contacts_dictionary):
        """
        Function to update contact
        """
        try:
            contact_object.address = contacts_dictionary.get("update_address")
            contact_object.city = contacts_dictionary.get("update_city")
            contact_object.state = contacts_dictionary.get("update_state")
            contact_object.pin = contacts_dictionary.get("update_pin")
            contact_object.phone = contacts_dictionary.get("update_phone")
            contact_object.email = contacts_dictionary.get("update_email")

        except Exception as e:
            print(e)
            logging.exception(e)

    def delete_contact(self, name):
        """
        Function to remove contact
        :param name:
        """
        try:
            self.contact_dict.pop(name, "Contact name not present")
        except Exception as e:
            logging.exception(e)

    def get_cont_as_dict(self):
        details_dict = {}
        for key, value in self.contact_dict.items():
            details_dict.update({value.first_name: value.get_cont_dict()})
        return details_dict


class MulAddressBooks:

    def __init__(self):
        self.address_book_dict = {}
        self.json_dict = {}

    def add_address_book(self, address_book_object):
        """
        Function to add address_book_object to address_book_dict dictionary
        """
        try:
            self.address_book_dict.update({address_book_object.address_book_name: address_book_object})
        except Exception as e:
            logging.exception(e)

    def get_address_book_object(self, name):
        """
        Function to get address_book_object
        """
        return self.address_book_dict.get(name)

    def display_address_book_names(self):
        """
        Function to show address book names
        """
        try:
            for key, value in self.address_book_dict.items():
                print("{:<15}".format('address book name'))
                print("{:<15}".format(key))
        except Exception as e:
            logging.exception(e)

    def delete_address_book(self, name):
        """
        Function to delete address_book
        """
        self.address_book_dict.pop(name, "Address Book not present")

    def write_to_json(self):
        for cont_name, cont_obj in self.address_book_dict.items():
            cont_dict = cont_obj.get_cont_as_dict()
            self.json_dict.update({cont_name: cont_dict})
            json_obj = json.dumps(self.json_dict, indent=4)
            with open('contact.json', 'w') as writefile:
                writefile.write(json_obj)

    def write_to_csv(self):
        with open('address_book.csv', 'w', newline='') as writefile:
            field_names = ['first_name', 'last_name', 'address', 'city', 'state', 'pin', 'phone', 'email']
            csv_writer = csv.DictWriter(writefile, fieldnames=field_names)
            csv_writer.writeheader()
            for cont_name, cont_obj in self.address_book_dict.items():
                cont_dict = cont_obj.get_cont_as_dict()
                for key, value in cont_dict.items():
                    csv_writer.writerow(value)


def add_contact():
    """
    Function to add a contact
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = mul_address_book.get_address_book_object(address_book_name)
        if not address_book_object:
            address_book_object = AddressBook(address_book_name)
            mul_address_book.add_address_book(address_book_object)
        first_name = input("Enter first name : ")
        if first_name == "":
            print("Please enter first name")
            return
        last_name = input("Enter last name : ")
        if last_name == "":
            print("Please enter last name")
            return
        address = input("Enter address : ")
        city = input("Enter city : ")
        state = input("Enter state : ")
        pin = int(input("Enter zip code : "))
        phone = int(input("Enter phone number : "))
        email = input("Enter email id : ")

        contact_parameters = {"first_name": first_name, "last_name": last_name, "address": address, "city": city,
                              "state": state, "pin": pin, "phone": phone, "email": email}
        contact = Contact(contact_parameters)

        address_book_object.add_contact(contact)

        mul_address_book.write_to_json()
        mul_address_book.write_to_csv()
    except Exception as e:
        print(e)
        logging.exception(e)


def display_names():
    """
    Function to display contacts
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = mul_address_book.get_address_book_object(address_book_name)
        address_book_object.display_names()

    except Exception as e:
        logging.exception(e)


def display_contacts():
    """
    Function to display all contacts in address book
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = mul_address_book.get_address_book_object(address_book_name)
        address_book_object.display_contacts()

    except Exception as e:
        logging.exception(e)


def update_contact():
    """
    Function to update contact
    """
    address_book_name = input("Enter Address Book name : ")
    address_book_object = mul_address_book.get_address_book_object(address_book_name)
    name = input("Enter contact name to update : ")
    contact_object = address_book_object.get_contact_object(name)
    if not contact_object:
        print("Contact not present")
    else:
        update_choice = int(input("1. Update address\n2. Update city\n3. Update state\n"
                                  "4. Update pin\n2. Update phone\n3. Update email\n"
                                  "Enter your choice : "))

        if update_choice == 1:
            update_address = input("Enter new address to update : ")
            contact_object.address = update_address
        elif update_choice == 2:
            update_city = input("Enter new city to update : ")
            contact_object.city = update_city
        elif update_choice == 3:
            update_state = input("Enter new state to update : ")
            contact_object.state = update_state
        elif update_choice == 4:
            update_pin = int(input("Enter new pin to update : "))
            contact_object.pin = update_pin
        elif update_choice == 5:
            update_phone = int(input("Enter new phone to update : "))
            contact_object.phone = update_phone
        elif update_choice == 6:
            update_email = input("Enter new email id to update : ")
            contact_object.email = update_email

    update_dict = {"update_address": 1, "update_city": 2, "update_state": 3,
                   "update_pin": 4, "update_phone": 5,
                   "update_email": 6}
    address_book_object.update_contact(contact_object, update_dict)
    mul_address_book.write_to_json()
    mul_address_book.write_to_csv()


def delete_contact():
    """
    Function to remove a contact
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = mul_address_book.get_address_book_object(address_book_name)
        name = input("Enter first name to delete contact : ")
        address_book_object.delete_contact(name)

        mul_address_book.write_to_json()
        mul_address_book.write_to_csv()
    except Exception as e:
        logging.exception(e)


def display_address_book_names():
    """
    Function to display address book names
    """
    try:
        mul_address_book.display_address_book_names()
    except Exception as e:
        logging.exception(e)


def delete_address_book():
    """
    Function to delete address book
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        mul_address_book.delete_address_book(address_book_name)

        mul_address_book.write_to_json()
        mul_address_book.write_to_csv()
    except Exception as e:
        logging.exception(e)


def read_from_json():
    """
    Function to read from json file
    """
    try:
        if os.path.getsize('contact.json') == 0:
            print("--> File not exist <--")
        else:
            with open('contact.json', 'r') as read_file:
                json_reader = json.load(read_file)
                print(json_reader)

    except Exception as e:
        logging.exception(e)


def read_from_csv():
    """
    Function to read from csv file
    """
    try:
        if os.path.getsize('contact.json') == 0:
            print("--> File not exist <--")
        else:
            with open('address_book.csv', 'r') as csvfile:
                csv_obj = csv.DictReader(csvfile)
                for rows in csv_obj:
                    print(rows)
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    try:
        mul_address_book = MulAddressBooks()

        while True:
            choice = int(input("1. Add contact into address book\n2. Display names in address book\n"
                               "3. Display contact info\n4. Update contact\n5. Delete contact\n"
                               "6. Display address book names\n7. Delete an Address Book\n8. Read from json\n"
                               "9. Read from csv\n10. 0 to Exit\nEnter your choice: "))

            choice_dictionary = {1: add_contact, 2: display_names, 3: display_contacts, 4: update_contact,
                                 5: delete_contact, 6: display_address_book_names, 7: delete_address_book,
                                 8: read_from_json, 9: read_from_csv}
            if choice == 0:
                break
            elif choice > 10:
                print("Please enter correct choice")
            else:
                choice_dictionary.get(choice)()

    except Exception as err:
        print(err)
        logging.exception(err)
