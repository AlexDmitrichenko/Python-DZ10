class Contact:

    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def toString(self):
        return f'{self.name};{self.phone};{self.comment}'
    
    def __str__(self):
        return f'{self.name:<20} | {self.phone:<20} | {self.comment:<20}'
    
class PhoneBook:

    def __init__(self, path: str):
        self.path = path
        self.phoneList = []
        self.openFile()
 
    def openFile(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            newContact = contact.strip().split(';')
            self.phoneList.append(Contact(*newContact))

    def save(self):
        data = '\n'.join([contact.toString() for contact in self.phoneList])
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def mainMenu(self):
        return '''Главное меню:
        1. Показать все контакты
        2. Добавить контакт
        3. Найти контакт
        4. Изменить контакт 
        5. Удалить контакт
        6. Сохранить 
        7. Выйти'''

    def addNewContact(self, name: str, phone: str | int, comment: str):
        self.phoneList.append(Contact(name, phone, comment))

    def findContact(self, search: str):
        result = []
        for contact in self.phoneList:
            if search in contact.toString():
                result.append(f'{contact}')
        return '\n'.join(result)

    def changeContact(self, index: int, name: str, phone: str, comment: str):
        name = name if name != '' else self.phoneList[index].name
        phone = phone if phone != '' else self.phoneList[index].phone
        comment = comment if comment != '' else self.phoneList[index].comment
        self.phoneList[index] = Contact(name, phone, comment)

    def deleteContact(self, index: int):
        self.phoneList.pop(index)

    def __str__(self):
        result = ''
        i = 0
        for contact in self.phoneList:
            i += 1
            result += f'{i}. {contact}\n'
        return result[:-2]

    def showMessage(self, message: str):
        print('-'*len(message))
        print(message)
        print('-'*len(message))

    