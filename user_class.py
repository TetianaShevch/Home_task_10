from address_book_class import AddressBook

class User():
    def __init__(self, user_name:str, User_AddressBook:AddressBook):
        self.name = user_name
        self.User_AddressBook = User_AddressBook