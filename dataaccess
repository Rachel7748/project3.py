import sqlite3
from customer import Customer


class DataAccess():

    def __init__(self, db_path):
        conn = sqlite3.connect(db_path)
        self.db_path = db_path
        self.cur = conn.cursor()

    def print_all_customers(self):
        self.cur.execute('SELECT * FROM Customer')
        for row in self.cur:
            print(Customer(row[0],row[1],row[2],row[3],row[4]))


    def insert_customer(self,Customer):
        self.cur.execute(f'INSERT INTO customer VALUES("{Customer.id}","{Customer.fname}", "{Customer.lname}", "{Customer.address}", {Customer.mobile_number})')
        return f'Customer{Customer.fname} {Customer.lname}'


    def delete_customer(self, id):
        self.cur.execute(f'DELETE FROM CUSTOMER WHERE id = {id}')
        self.db_path.commit()




    def get_all_customers(self):
        self.cur.execute('SELECT * FROM CUSTOMER')
        _lst = []
        for row in self.cur:
            _lst.append(row)
            return [f'{row[1]}{row[2]}'for row in self.cur]

    def get_customer_by_id(self,id):
        self.cur.execute(f'SELECT * FROM CUSTOMER WHERE id = {id}')
        return [f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}' for row in self.cur]

    def update_customer(self,id,Customer):
        self.cur.execute (f'UPDATE CUSTOMER SET id ={Customer.id} ')
        self.cur.execute(f'UPDATE CUSTOMER SET id ={Customer.fname}')
        self.cur.execute(f'UPDATE CUSTOMER SET id ={Customer.lname}')
        self.cur.execute(f'UPDATE CUSTOMER SET id ={Customer.address}')
        self.cur.execute(f'UPDATE CUSTOMER SET id ={Customer.mobile_number}')
        self.db_path.commit()


    def __repr__(self):
        return f'DataAccess({self.db_path})'

    def __str__(self):
        return f'DataAccess: db_path: {self.db_path}'



