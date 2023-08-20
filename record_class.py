from name_class import Name
from phone_class import Phone

class Record():
    
    def __init__(self, name: Name, phone: Phone = None): # телефон не обовязковий агрумент, тому може бути і None
        self.name = name
        self.phones = [] # по замовчюванню стовримо пустий список
        if phone:
            self.phones.append(phone)  # якщо телефон задано, то додамо його в список
    
    def add_phone(self, phone: Phone):
        for i in self.phones:
            if i == phone:
                print('Phone is already in Address Book') # якщо телефон вже є в списку
                return
        self.phones.append(phone)  # якщо телефона в списку немає, додамо його в список
        print('Phone was added')
        
    def del_phone(self, phone: Phone):
        for i in self.phones:
            if i == phone:
                self.phones.remove(i) # якщо телефон в списку, видаляємо його
                print(f'Phone was removed')
                return
        print('Phone is not in Address Book') # якщо телефона немає в списку

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for i in self.phones:
            if i == old_phone:
                i = new_phone  #  якщо телефон в списку, змінюємо його
                print(f'Phone was changed')
                return
        print('Phone is not in Address Book') # якщо телефона немає в списку
    


    
    