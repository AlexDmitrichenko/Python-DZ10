import Model

pb = Model.PhoneBook('Phone.txt')

while True:
    print(pb.mainMenu())
    choice = input('Выберите пункт меню: ')
    if choice.isdigit() and 0 <int(choice)<= 7:
        choice = int(choice)
    else:
        print(f'Не верно введено значение, введите число от 1 до 7')
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите Фамилию и Имя: ')
            phone = input('Введите номер телефона: ')
            comment = input('Введите комментарий: ')
            pb.addNewContact(name, phone, comment)
            pb.showMessage(f'Контакт успешно добавлен!')
        case 3:
            search = input('Введите поисковый запрос: ')
            if pb.findContact(search) != '':
                print(pb.findContact(search))
            else:
                pb.showMessage(f'Искомый контакт не найден!')
        case 4:
            print(pb)
            index = int(input('Введите индекс изменяемого контакта: '))
            name = input('Введите Фамилию и Имя или оставьте пустое поле, для выхода без изменений: ')
            phone = input('Введите номер телефона или оставьте пустое поле, для выхода без изменений: ')
            comment = input('Введите комментарий или оставьте пустое поле, для выхода без изменений: ')
            pb.changeContact(index-1, name, phone, comment)
            pb.showMessage('Контакт успешно изменен!')
        case 5:
            print(pb)
            index = int(input('Введите индекс удаляемого контакта: '))
            pb.deleteContact(index-1)
            pb.showMessage('Контакт успешно удален!')
        case 6:
            pb.save()
            pb.showMessage('Внесенные изменения успешно сохранены!')
        case 7:
            break

 