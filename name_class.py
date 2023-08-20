from field_class import Field

class Name(Field):
    def __init__(self, name, obligatory = True):
        self.value = name
