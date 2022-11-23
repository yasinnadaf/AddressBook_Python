import pytest

from .address_book import Contact, AddressBook, MulAddressBooks


@pytest.fixture
def cont_obj():
    return Contact({'first_name': 'Yasin', 'last_name': 'Nadaf', 'address': 'Lashkar', 'city': 'Solapur',
                    'state': 'Mh', 'pin': '434343', 'phone': '9087612345', 'email': 'y@gmail.com'})


@pytest.fixture
def address_book_obj():
    return AddressBook('Family')


def test_add_contact(cont_obj, address_book_obj):
    assert len(address_book_obj.contact_dict) == 0
    address_book_obj.add_contact(cont_obj)
    assert len(address_book_obj.contact_dict) == 1


def test_cont_obj_is_present_in_cont_dict_or_not(cont_obj, address_book_obj):
    address_book_obj.add_contact(cont_obj)
    assert cont_obj == address_book_obj.get_contact_object('Yasin')


def test_delete_cont_method(cont_obj, address_book_obj):
    address_book_obj.add_contact(cont_obj)
    assert cont_obj != address_book_obj.delete_contact('Yasin')


def test_address_book_dict_length(address_book_obj):
    mul_address_book_obj = MulAddressBooks()
    assert len(mul_address_book_obj.address_book_dict) == 0
    mul_address_book_obj.add_address_book(address_book_obj)
    assert len(mul_address_book_obj.address_book_dict) == 1


def test_address_book_obj_present_in_address_book_dict(address_book_obj):
    mul_address_book_obj = MulAddressBooks()
    mul_address_book_obj.add_address_book(address_book_obj)
    assert address_book_obj == mul_address_book_obj.get_address_book_object('Family')


def test_delete_address_book_method(address_book_obj):
    mul_address_book_obj = MulAddressBooks()
    mul_address_book_obj.add_address_book(address_book_obj)
    assert address_book_obj != mul_address_book_obj.delete_address_book('Family')