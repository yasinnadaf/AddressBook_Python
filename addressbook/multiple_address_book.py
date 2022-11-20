import logging

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
            if self.contact_dict == {}:
                print("No contacts to display")
            else:
                for key, value in self.contact_dict.items():
                    print(key)
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
            if self.contact_dict == {}:
                print("No contacts to display")
            else:
                for key, value in self.contact_dict.items():
                    print("First Name : {}\nLast Name : {}\nAddress : {}\nCity : {}\nState : {}\n"
                          "PIN : {}\nPhone : {}\nEmail : {}\n"
                          .format(value.first_name, value.last_name, value.address, value.city, value.state,
                                  value.pin, value.phone, value.email))
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


class MulAddressBooks:

    def __init__(self):
        self.address_book_dict = {}

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
                print(key)
        except Exception as e:
            logging.exception(e)

    def delete_address_book(self, name):
        """
        Function to delete address_book
        """
        self.address_book_dict.pop(name, "Address Book not present")


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
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = mul_address_book.get_address_book_object(address_book_name)
        name = input("Enter contact name to update : ")
        contact_object = address_book_object.get_contact_object(name)
        if not contact_object:
            print("Contact not present")
        else:
            update_address = input("Enter new address to update : ")
            update_city = input("Enter new city to update : ")
            update_state = input("Enter new state to update : ")
            update_pin = int(input("Enter new pin to update : "))
            update_phone = int(input("Enter new phone to update : "))
            update_email = input("Enter new email id to update : ")

            update_dict = {"update_address": update_address, "update_city": update_city, "update_state": update_state,
                           "update_pin": update_pin, "update_phone": update_phone,
                           "update_email": update_email}

            address_book_object.update_contact(contact_object, update_dict)
    except Exception as e:
        print(e)
        logging.exception(e)


def delete_contact():
    """
    Function to remove a contact
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = mul_address_book.get_address_book_object(address_book_name)
        name = input("Enter first name to delete contact : ")
        address_book_object.delete_contact(name)
    except Exception as e:
        logging.exception(e)


def display_address_book_names():
    """
    Function to display address book names
    """
    mul_address_book.display_address_book_names()


def delete_address_book():
    """
    Function to delete address book
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        mul_address_book.delete_address_book(address_book_name)
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    try:
        mul_address_book = MulAddressBooks()

        while True:
            choice = int(input("1. Add contact into address book\n2. Display names in address book\n"
                               "3. Display contact info\n4. Update contact\n5. Delete contact\n"
                               "6. Display address book names\n7. Delete an Address Book\n8. 0 to Exit\nEnter your choice: "))

            choice_dictionary = {1: add_contact, 2: display_names, 3: display_contacts, 4: update_contact,
                                 5: delete_contact, 6: display_address_book_names, 7: delete_address_book}
            if choice == 0:
                break
            elif choice > 8:
                print("Please enter correct choice")
            else:
                choice_dictionary.get(choice)()

    except Exception as err:
        print(err)
        logging.exception(err)
