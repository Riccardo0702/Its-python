class ContactManager:
    def __init__(self, contacts:dict[str,list[str]]):
        self.contacts = contacts

    def create_contact(self, contact_name:str, phone_number:list[str]):
        new_dict = {}
        if contact_name not in self.contacts:
            self.contacts[contact_name] = [phone_number]
            new_dict[contact_name] = [phone_number]
        else:
            return "Errore: il contatto esiste già"

    def add_phone_number(self, contact_name:str, phone_number:str):
        new_dict = {}
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                return "Errore: il numero di telefono esiste già"
            else:
                self.contacts[contact_name] = phone_number
                new_dict[contact_name] = [phone_number]
                return new_dict
        else:
            return "Errore: il contatto non esiste"
    
    def remove_phone_number(self, contact_name:str, phone_number:str):
        new_dict = {}
        if contact_name in self.contacts:
            if phone_number in contact_name:
                self.contacts[contact_name].remove(phone_number)
                new_dict[contact_name] = [phone_number]
            else:
                return "Errore: il numero di telefono non è presente"
        else:
            return "Errore: il contatto non esiste"
        
    def update_phone_number(self, contact_name:str, old_phone_number:str, new_phone_number:str):
        new_dict = {}
        if contact_name in self.contacts:
            if old_phone_number in contact_name:
                self.contacts[contact_name].remove[old_phone_number]
                new_dict[contact_name] = [new_phone_number]
            else:
                return "Errore: il numero non è presente"
        else:
            return "Errore: il contatto non esiste"
    
    def list_contacts(self):
        list = []
        for key in self.contacts:
            list.append(key)
        return list
    
    def list_phone_numbers(self, contact_name:str):
        list = []
        if contact_name in self.contacts:
            list.append(self.contacts[contact_name])
            return list
        else:
            return "Errore: il contatto non esiste"
    
    def search_contact_by_phone_number(self, phone_number:str):
        
        


