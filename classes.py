from collections import UserDict

class AddressBook(UserDict):     

    def add_record(self, record):
        self.data[record.name.value] = record      
    
    def return_all_records(self):
        all_records = []
        for name, record in self.data.items():
            temp = {}
            phones = ', '.join(phone.value for phone in record.phones) 
            temp.update({name: phones})     
            all_records.append(temp)
        return all_records
    
    def get_keys_from_all_records(self):
        all_records = self.return_all_records()  
        keys = [list(i.keys())[0] for i in all_records]
        return keys


class Field:
    def __init__(self, value):
        self.value = value            


class Name(Field):    
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)


class Record:
    def __init__(self, name, phone=None):
         self.name = Name(value=name)
         self.phones = []
         
         if phone:
            self.phone = Phone(value=phone)
            self.phones.append(phone) 

    def add_phone(self, new_phone):
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        for index, values in enumerate(self.phones):
            if values.value == phone.value:
                self.phones.pop(index)

    def change_phone(self, phone, new_phone):       
        for index, values in enumerate(self.phones):
            if values.value == phone.value:
                self.phones[index] = new_phone
                print(f"Phone '{phone.value}' changed to '{new_phone.value}'.")
                return
        print(f"Phone '{phone.value}' not found.")    
    
 
