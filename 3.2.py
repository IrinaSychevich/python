def personal_information():
    def my_sum(name, surname, year_of_birth, city, email, phone_number):
        l = name + ' ' + surname + ' ' + year_of_birth + ' ' + city + ' ' + email + ' ' + phone_number
        return l
    n = input('Введите имя: ')
    s = input('Введите фамилию: ')
    y = input('Введите год рождения: ')
    c = input('Введите город проживания: ')
    e = input('Введите адрес электронной почты: ')
    p = input('Введите номер телеона: ')
    return my_sum(name=n, surname=s, year_of_birth=y, city=c, email=e, phone_number=p)
print(personal_information())









