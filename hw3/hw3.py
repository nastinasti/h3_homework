from datetime import date
# d = date(1969, 6, 26) - конструктор даты
# d.year < 2020 - проверка даты

# database - список словарей, эмулирующий базу данных со строками и полями
database = list()


def _validate_input(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей, валидирует каждый из словарей на наличие
    всех необходимых полей и тип их данных. Возвращает bool в зависимости от результатов проверки.
    Правила валидации:
    first_name - string, не пустой, короче 48 символов
    last_name - string, не пустой, короче 64 символов
    birth - date, не пустой, не в будущем, не старше 100 лет
    email - string, формат строка, затем @, затем опять строка, точка,
    строка от 2 до 3 символов
    Допустимые символы в email: буквы, цифры
    """
    first_name_len = 48
    last_name_len = 64
    max_age = 100
    for row in data:
        if not _validate_name(row['first_name'], first_name_len):
            return False
        if not _validate_name(row['last_name'], last_name_len):
            return False
        if not _validate_birth(row['birth'], max_age):
            return False
        if not _validate_email(row['email']):
            return False

    return True


def _validate_name(name, max_len):
    if not type(name) is str:
        return False
    if not 0 < len(name) < max_len:
        return False
    return True


def _validate_birth(birth, max_age):
    if not type(birth) is date:
        return False
    if birth > date.today():
        return False
    if date.today().year - birth.year > max_age:
        return False
    return True


def _validate_email(email):
    if not type(email) is str:
        return False
    email_parts = email.split('@')
    if len(email_parts) != 2:
        return False
    if not email_parts[0].isalnum():
        return False
    domain_parts = email_parts[1].split('.')
    if len(domain_parts) == 1:
        return False
    if not 2 <= len(domain_parts[-1]) <= 3:
        return False
    return True


def insert_to_db(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей с данными, валидирует каждую запись с
    помощью вспомогательной функции validate_input, и если данные валидны,
    добавляет их в database.
    Возвращает bool по результатам успешного/неуспешного выполнения.
    """
    if _validate_input(data):
        database.extend(list(data))
        return True
    else: 
        print("Error inserting data to database. Please check!")
        exit()


def _format_output(data) -> str:
    """
    Принимает тапл диктов с данными из БД.
    Форматирует данные в таблицу вида:
    ---------------------------------------
    | название колонки | название колонки |
    ---------------------------------------
    | значение строки  | значение колонки |
    Возвращает таблицу строкой.
    """
    print("\t\t\t\t------TABLE OF THE DATABASE------")
    max_table_len = 105
    borders = max_table_len*'-'
    print(max_table_len*'-')    
    print('| {0:20} |    {1:25}   | \
{2:10}  |             {3:20}|'.format('First Name', 'Last Name', 'Birth Date', 'Email'))
    print(max_table_len*'-') 
    count = len(data)
    while count > 0:
        for item in data:
            table = f"| {item['first_name']:20} | {item['last_name']:30} |  {item['birth']} | \
{item['email']:31} |\n" + borders            
            print(table)
            count = count - 1
    return table


def select_from_db(field, value):
    """
    Функция возвращает таблицу (строка) с релевантными результатами, где переданное значение встречается в переданном ключе.
    Форматирование результатов выполняет вспомогательная функция _format_output
    """
    try:
        required_dict = list()
        required_dict.append(next(item for item in database if item[field] == value))
        _format_output(list(required_dict))
    except KeyError:
        print(f"\nError. The FIELD - {field} is wrong! Please check and start the programm again!\n")
        choose = input("do you want to start again? Y/N\n")
        if choose == "Y" or choose == "y":
            main()
    except StopIteration:
        print(f"\nError. The VALUE - {value} is wrong! Please check and start the programm again!\n")
        choose = input("do you want to start again? Y/N\n")
        if choose == "Y" or choose == "y":
            main()

def main():
    in_data = ({"first_name": "Guido", "last_name": "Van Rossum",
            "birth": date(1969, 6, 27), "email": "iamguido@python.org"},
            {"first_name": "Not Guido", "last_name": "But Van Rossum",
            "birth": date(1969, 6, 28), "email": "iamanotherguido@python.org"},
            {"first_name": "Abra Cadabra", "last_name": "Fig Znayet Chto",
            "birth": date(1939, 9, 1), "email": "abrafigznayet@python.org"})
    result = insert_to_db(in_data)
    print(result)
    _format_output(in_data)
    field = input("Please inpute the field: ")
    value = input("Please inpute the value: ")
    select_from_db(field, value)

if __name__ == '__main__':
    main()