import sqlite3
def create_users():
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users('
        'Firstname text, '  
        'id integer primary key autoincrement, '  
        'Surname text,'
        'Gender text,'
        # 'Email text,'
        'Phone text,'
        'Birthday text'
        # 'Country text,'
        # 'City text,'
        # 'Hobbies text,'
        # 'Preferences text,'
        # 'Passport text,'
        # 'Address text,'
        # 'Education text,'
        # 'Job text,'
        # 'Family status text,'
        # 'Kids text,'
        # 'Spouse text,'
        # 'Uploaded text'
        ');'
    )
    connect.commit()


create_users()


def create_smth_smart(table: str, data: dict):
    keys = list(data.keys())
    values = list(data.values())
    req = f'CREATE TABLE IF NOT EXISTS {table}('

    for i in range(len(keys)):
        req += f'{keys[i]} {values[i]}, '
    req = req[:-2] + ')'
    print(req)

    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    cursor.execute(req)
    connect.commit()


create_smth_smart(table='Country',
                  data={
                      'id': 'integer primary key autoincrement',
                      'name': 'text unique',
                  })

create_smth_smart(table='country_user',
                  data={
                      'id': 'integer primary key autoincrement',
                      'user_id': 'integer',
                      'country_id': 'integer',
                      'foreign key (user_id)': 'references users (id) ON DELETE CASCADE',
                      'foreign key (country_id)': 'references Country (id) ON DELETE CASCADE'
                  })


def get_users(name):
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    get = f'SELECT name, phone FROM users WHERE name="{name}"'
    cursor.execute(get)
    result = cursor.fetchall()
    print(result)


def add_smth_to_sometable(table: str, data: dict):
    connect = sqlite3.connect('some_data_base.db')
    cursor = connect.cursor()
    columns = ''
    values = ''
    for i in range(len(data.keys())):
        columns += f'{list(data.keys())[i]}, '
        values += f'"{list(data.values())[i]}", '
    columns = columns[:-2]
    values = values[:-2]

    request_in_smth = f'INSERT INTO {table}' \
                      f' ({columns}) ' \
                      f'VALUES ' \
                      f'({values});'
    print(request_in_smth)
    cursor.execute(request_in_smth)
    connect.commit()


def fill_country_db():
    list = ['USA', 'GERMANY', 'JAPAN']
    for idx in range(len(list)):
        add_smth_to_sometable('Country', data={
            'name': list[idx]})


fill_country_db()


def countryChoise():
    list = ['USA', 'GERMANY', 'JAPAN']
    for idx in range(len(list)):
        print(idx + 1, ".", list[idx])
    num = int(input('Enter Country number'))

    return num


def addUser():
    firstName = input('Enter firstname: ')
    lastName = input('Enter lastname: ')
    birthday = input('Enter birth: ')
    phone = input('Enter phone: ')
    add_smth_to_sometable(table='users',
                          data={
                              'Firstname': firstName,
                              'Surname': lastName,
                              'Phone': phone,
                              'Birthday': birthday
                          })

def addUsersCountry():
    userID = input('Enter userID: ')
    countryID = countryChoise()

    add_smth_to_sometable(table='country_user',
                          data={
                              'user_id': userID,
                              'country_id': countryID
                          })

while True:
    num = int(input("Хотите ли ві добавить пользователя ? 1- ДА , 2 - NO"))
    if (num == 2): break
    addUser()

addUsersCountry()
#
# add_smth_to_sometable(table='country_user',
#                       data={
#                           'user_id': '1',
#                           'country_id': '3'
#                       })
# add_smth_to_sometable(table='country_user',
#                       data={
#                           'user_id': '2',
#                           'country_id': '3'
#                       })
