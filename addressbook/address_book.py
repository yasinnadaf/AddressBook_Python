import logging


class Contact:
    def __init__(self, contact_dict):
        self.first_name = contact_dict.get('first_name')
        self.last_name = contact_dict.get('last_name')
        self.address = contact_dict.get('address')
        self.city = contact_dict.get('city')
        self.state = contact_dict.get('state')
        self.pin = contact_dict.get('pin')
        self.phone = contact_dict.get('phone')
        self.email = contact_dict.get('email')


class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contact_dict = {}

    def add_contact(self, contact_obj):
        """
        Function to add contact_object into dictionary

        """
        self.contact_dict.update({contact_obj.first_name: contact_obj})

    def display_contact(self):
        """
        Function to display contact names in address book

        """
        try:
            if self.contact_dict == {}:
                print("No contact to display")
            else:
                for key, value in self.contact_dict.items():
                    print("First name: {}\nLast name: {}\nCity: {}\nState: {}\nPin {}\nPhone: {}\nemail: {}"
                          .format(value.first_name, value.last_name, value.city, value.state, value.pin,
                                  value.phone, value.email))

        except Exception as e:
            print(e)
            logging.exception(e)

    def update_contact(self, contact_obj, data_dict):
        """
        Function to update contact

        """
        try:
            contact_obj.address = data_dict.get("update_address")
            contact_obj.city = data_dict.get("update_city")
            contact_obj.state = data_dict.get("update_state")
            contact_obj.pin = data_dict.get("update_pin")
            contact_obj.phone = data_dict.get("update_phone")
            contact_obj.email = data_dict.get("update_email")
        except Exception as e:
            print(e)
            logging.exception(e)

    def show_names(self):
        try:
            if self.contact_dict == {}:
                print("name not found: ")
            else:
                for k, v in self.contact_dict.items():
                    print(k)
        except Exception as e:
            print(e)
            logging.exception(e)

    def get_cont(self, cont_name_to_update):
        """
         Function to get contact object
        """
        return self.contact_dict.get(cont_name_to_update)

    def delete_cont(self, cont_name):
        """
        Function to delete contact name
        """
        self.contact_dict.pop(cont_name)


def add_contacts():
    """
    Function to add contacts in address book
    """
    try:
        first_name = input("Enter first name : ")
        last_name = input("Enter last name : ")
        address = input("Enter address : ")
        city = input("Enter city : ")
        state = input("Enter state : ")
        pin = int(input("Enter zip code : "))
        phone = int(input("Enter phone number : "))
        email = input("Enter email id : ")

        cont_parameters = {'first_name': first_name, 'last_name': last_name, 'address': address, 'city': city,
                           'state': state, "pin": pin, "phone": phone, "email": email}

        contact = Contact(cont_parameters)
        addr_obj.add_contact(contact)
    except Exception as e:
        print(e)
        logging.exception(e)


def display_contacts():
    """
    Function to display contacts
    """
    addr_obj.display_contact()


def update():
    """
    Function to update details
    """
    try:
        cont_name_to_update = input("Enter contact name to update")
        cont_obj = addr_obj.get_cont(cont_name_to_update)
        if not cont_obj:
            print("contact not exist")
        else:
            update_address = input("Enter address to update: ")
            update_city = input("Enter city to update: ")
            update_state = input("Enter state to update: ")
            update_pin = int(input("Enter pin code: "))
            update_phone = int(input("Enter phone to update: "))
            update_email = input("Enter email to update: ")

            contact_dict = {'update_address': update_address, 'update_city': update_city, 'update_state': update_state,
                            'update_pin': update_pin, 'update_phone': update_phone, 'update_email': update_email}
            addr_obj.update_contact(cont_obj, contact_dict)

    except Exception as e:
        print(e)
        logging.exception(e)
   

def show_all_names():
    """
    Function to display all names in address book
    """
    addr_obj.show_names()


def delete_contact():
    """
    Function to delete contact
    """
    cont_name = input("Enter person name of address book to delete")
    addr_obj.delete_cont(cont_name)


if __name__ == '__main__':
    addr_book_name = input("Enter Address Book name: ")
    addr_obj = AddressBook("addr_book_name")
    while True:
        choice = int(input("Enter your choice:\n1)add contacts\n2)display contacts\n3)show all names in address book"
                           "\n4)update contact\n5)delete contact\nenter 0 to exit: "))
        choice_dict = {1: add_contacts, 2: display_contacts, 3: show_all_names, 4: update, 5: delete_contact}
        if choice == 0:
            break
        elif choice > 5:
            print("Please enter correct choice")
        else:
            choice_dict.get(choice)()