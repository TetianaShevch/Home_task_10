from collections import UserDict
from record_class import Record

class AddressBook(UserDict):
       
    def add_record(self, record = Record):
        self.data[record.name.value] = record 
        print(f'Contact of {record.name.value} was added')
        