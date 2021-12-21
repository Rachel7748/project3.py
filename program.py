import sqlite3
from customer import Customer
from dataaccess import DataAccess

conn = sqlite3.connect('C:/racheli/proj3/proj3.db')
cur = conn.execute('SELECT * FROM customer')
cust1 = DataAccess('C:/racheli/proj3/proj3.db')

def menu():
    return f'1. Get all customers \n2. Get customer by id \n3. Insert customer \n4. Delete customer \n5. Update customer \n6. Exit \n please enter your choose'

def print_all_customers(self):
    self.cur.execute('SELECT * FROM CUSTOMER')
    for row in self.cur:
            print (Customer(row[0],row[1],row[2],row[3],row[4]))

def get_customer_by_id():
    id = int(input('enter id:'))
    Customer = cust1.get_customer_by_id(id)
    print(Customer)

def insert_customer(Customer):
    id = int(input('enter id:'))
    fname = str(input('enter first name:'))
    lname = str(input('enter last name:'))
    address = str(input('enter address:'))
    mobile_number = str(input('enter phone number:'))
    Customer = Customer(id, fname, lname, address, mobile_number)
    cust1.insert_customer(Customer)
    print('records updated')

def delete_customer(id):
    id = int(input('enter id:'))
    cust1.delete_customer({id})
    print('records updated')


def update_customer():
    id = int(input('enter current id:'))

    _id = int(input('enter new id:'))
    _fname = str(input('enter first name:'))
    _lname = str(input('enter last name:'))
    _address = str(input('enter address:'))
    _mobile_number = str(input('enter phone number:'))
    _customer = Customer = (_id, _fname, _lname, _address, _mobile_number)
    cust1.update_customer(id,_customer)
    print('records updated')


def select(choose_num):
    if choose_num == 1:
         print_all_customers(cust1)
    elif choose_num == 2:
        return get_customer_by_id()
    elif choose_num == 3:
        return insert_customer(Customer)
    elif choose_num == 4:
        return delete_customer(id(''))
    elif choose_num == 5:
        return update_customer()

def main():
    choose_num = int(input(f'\n{menu()}'))
    select(choose_num)
    return f'chosen number: {choose_num}'


main()






