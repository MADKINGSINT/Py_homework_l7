def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
           
            
            phone_number = int(phone_number)
            valid = True
        except:
            print('Номер телефона должен состоять из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info