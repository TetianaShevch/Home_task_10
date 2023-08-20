from address_book_class import AddressBook
from record_class import Record
from name_class import Name
from phone_class import Phone

if __name__ == "__main__":
    
    name = Name('Bill')

    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok')

    # new_phone = Phone('5778890')
    # rec.add_phone(new_phone)
    # mistaken_phone = Phone('789000')
    # rec.del_phone(mistaken_phone)
    # rec.del_phone(new_phone)
    # rec.add_phone(mistaken_phone)
    # rec.change_phone(mistaken_phone,new_phone)
