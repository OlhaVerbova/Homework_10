from classes import AddressBook
from classes import Record
from classes import Phone

global command_word
addressBook = AddressBook()



#decorator
def input_error(function):
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Invalid name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return "Invalid input format. Give me phone please."
        except TypeError:
            return 'Invalid command'
    return inner

# main functions
def hello():
    return "How can I help you?"

def show_all():
    result_list = addressBook.return_all_records()
    format_list = "|{:^30s}|{:^40s}".format("name", "phone(s)") 
    format_list += "\n"
    format_list += "-"*72
    format_list += "\n"
    text_no_phone = "Contact does`t phone"
    for dictionary in result_list:
        for name, phone in dictionary.items():
            if phone != None:
                format_list += "|{:<30s}|{:^40s}".format(name, phone)
                format_list += "\n"
            else:
                format_list += "|{:<30s}|{:^40s}".format(name, text_no_phone)
                format_list += "\n"
    return format_list


def say_good_bye():
    return "Good bye!"

@input_error
def add_new_telephone_contact(text):    
    text_list = text.split()
    already_enter_contacts = addressBook.get_keys_from_all_records() 
    
    if text_list[1] in already_enter_contacts:
        return f"{text_list[1]} is already in our book"
    else:
        if len(text_list) == 3:
            name =text_list[1].title()           
            phone = Phone(text_list[2])
            record = Record(name, phone)
            addressBook.add_record(record)          
    
        if len(text_list) == 2:
            name =text_list[1].title()              
            record = Record(name)  
            addressBook.add_record(record)            

def add_new_phone_to_contact(text):
    text_list = text.split()
    name_to_find = text_list[2].title()  
    if name_to_find in addressBook.data.keys(): 
        existing_record = addressBook.data[name_to_find]
        existing_record.add_phone(Phone(text_list[3]))
    else:
        return f"We dont have {text_list[2]} in our addressBook, please, try again"  

def delete_phone(text):
    text_list = text.split()
    name_to_find = text_list[2].title()
    if name_to_find in addressBook.data:
        existing_record = addressBook.data[name_to_find]
        existing_record.remove_phone(Phone(text_list[3]))        
    else:
        return f"We dont have {text_list[2]} in our addressBook, please, try again"    

    
@input_error
def change_phone_number(text):
    text_list = text.split()
    name_to_find = text_list[1].title()
    if name_to_find in addressBook.data.keys():
        existing_record = addressBook.data[name_to_find]
        existing_record.change_phone(Phone(text_list[2]),Phone(text_list[3]))


@input_error
def show_name_contact(text):
    text_list = text.split()
    all_records = addressBook.return_all_records()
    for dictionary in all_records:
        for key, value in dictionary.items():
            if text_list[1].title() in value:
                return key

def show_contact_info(text):
    text_list = text.split()
    all_records = addressBook.return_all_records()
    for dictionary in all_records:
        for key, value in dictionary.items():
            if text_list[2].title() in key:
                return f"Contact {key} has phone(s): {value}"
            
def text_helper():
    help_text = "Help on how to enter commands correctly\n"
    help_text += "show all    --> show you all records\n"
    help_text += "add (name)    --> record contact\n"
    help_text += "add (name phone)    --> record name + phone\n"
    help_text += "change (name old_phone new_phone)    --> changes changes the old phone number to a new one for a contact\n"
    help_text += "delete phone (name phone)    --> delete phone for a contact\n"
    help_text += "phone (phone)    --> show you contact`s owner\n"
    help_text += "show contact (name )    --> show you contact`s phone(s)\n"
    help_text += "close/good bye/exit    -->  will end the session\n"
    return help_text
   
def bot_operation(text):
    match text:
        case "hello":
            result = hello()   
                     
        case "close":
            result = say_good_bye()  

        case "good bye":
            result = say_good_bye()  

        case "exit":
            result = say_good_bye()   

        case "show all":
            result = show_all()           
            
        case "change":
            result = change_phone_number(command_word)
            
        case "phone":
            result = show_name_contact(command_word)

        case "add phone": 
            result = add_new_phone_to_contact(command_word)

        case "add":
            result = add_new_telephone_contact(command_word)

        case "delete phone":
            result = delete_phone(command_word)

        case "show contact":
            result = show_contact_info(command_word)
        
        case "help":
            result = text_helper()
            
    return result