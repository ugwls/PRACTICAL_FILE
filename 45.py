# Write a program to connect Python with MySQL using database
# connectivity and perform the following operations on data
# in database: Fetch, Update and delete the data

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="dps123",
    charset='utf8')
cur = mydb.cursor()
cur.execute('create database if not exists parctical')
cur.execute('use parctical')
mydb.commit()

table = '''
create table if not exists file_table(
name varchar(50),
address varchar(50),
phone_no varchar(30)
'''
cur.execute(table)
mydb.commit()


def add_Details():
    print('Enter the details :')
    s = 'insert into file_table (name,address,phone_no)' \
        'values(%s,%s,%s) '
    name = input('Enter your name: ')
    address = input('Enter your address: ')
    phone_no = input('Enter your phone number: ')
    value = (name, address, phone_no)
    cur.execute(s, value)
    mydb.commit()
    print("Successfully updated!!!!!!!!")


def delete():
    item_id = input('Enter Name that you want to delete: ')
    s = 'DELETE FROM file_table WHERE name =%s'
    value = (item_id,)
    cur.execute(s, value)
    mydb.commit()
    print('Successfully deleted!!!!!!')
    input('Press ENTER to continue.....')


def update():
    cur.execute('select * from file_table')
    result = cur.fetchall()
    for rec in result:
        print(rec)
    s = "update file_table set address = %s, phone_no = %s where name = %s"
    name = input('Enter name for which you want to update: ')
    address = input('Enter address: ')
    phone_no = input('Enter phone number: ')
    value = (address, phone_no, name)
    cur.execute(s, value)
    mydb.commit()
    print("Successfully updated!!!!!!!!")


def see_details():
    s = 'select * from file_table'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    input('Press ENTER to continue.....')


k = True
while k == True:
    print('''
1.Add Details
2.Update Details
3.Delete Details
4.See Details
5.Exit''')
    option = input('Enter your Options(1/5): ')
    if 0 <= option <= 4:
        if option == 1:
            add_Details()
        elif option == 2:
            update()
        elif option == 3:
            delete()
        elif option == 4:
            see_details()
    elif option == 5:
        k = False
    else:
        print('Invalid Option!')
        continue
