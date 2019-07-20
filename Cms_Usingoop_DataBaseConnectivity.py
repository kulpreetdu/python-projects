#customer management system using OOP's
import pymysql
#BLL BEGINS
class Customer:
    con = pymysql.connect(host="localhost", user="root", password="******", database='5thjune2019')
    def __init__(self):     # constructor
        self.id = 0         # storing the id of the customer
        self.name = " "       # storing the name of the customer
        self.address = " "    # storing the address of the customer
        self.mobile = " "     # storing the mobile number of the customer
    '''
    this function is use to overwrite the str method of object class to return the details of the customer
    when directly object of the customer class in called in the print function
    eg - cust=customer() 
         print(cust)
    '''
    def __str__(self):
        return "id is: "+str(self.id)+" "+"name is: "+self.name+" "+"address is: "+ self.address + " "+"mobile no. is:" + self.mobile
    def add_customer(self):
        myCurSor = Customer.con.cursor()
        strQuery = "insert into customer values(%s,%s,%s,%s)"
        myCurSor.execute(strQuery, (self.id, self.name, self.address, self.mobile))
        Customer.con.commit()
    def search_customer(self,id):
        myCurSor = Customer.con.cursor()
        strQuery = "select * from customer  where id=%s"
        rowAffected = myCurSor.execute(strQuery, (id))
        if (rowAffected != 0):
            row = myCurSor.fetchone()
            self.id = row[0]
            self.name = row[1]
            self.address = row[2]
            self.mobile = row[3]
            return
        else:
            raise Exception("id not found")
    def modify_customer(self,id):
        myCurSor = Customer.con.cursor()
        strQuery = "update customer set id=%s,name=%s,address=%s,mobile=%s where id=%s"
        rowAffected = myCurSor.execute(strQuery, (self.id,self.name,self.address,self.mobile,self.id))
        if (rowAffected != 0):
            Customer.con.commit()
            return
        else:
            raise Exception("id not found")
    def delete_customer(self,id):
        myCurSor = Customer.con.cursor()
        strQuery = "delete from customer  where id=%s"
        rowAffected = myCurSor.execute(strQuery, (id))
        if (rowAffected != 0):
            Customer.con.commit()
            return
        else:
            raise Exception("id not found")
#BLL ENDS

#PL BEGINS
def showAllCustomer():
    myCurSor = Customer.con.cursor()
    strQuery = "select * from customer"
    rowAffected = myCurSor.execute(strQuery)
    if (rowAffected != 0):
        for row in myCurSor.fetchall():
            for cell in row:
                print(cell,end='\t')
            print()
    else:
        raise Exception("database is empty")

while (True):
    user_msg='''
            1:add customer
            2:search customer
            3:modify customer
            4:delete customer
            5:show all customer
            6:exit
            '''
    print('\n',user_msg,'\n')
    choice=int(input("enter your choice"))

    if(choice==1):
        #write the code to add the customer
        try:
            cust = Customer()
            cust.id=int(input("ENTER THE id OF THE CUSTOMER"))
            cust.name = (input("ENTER THE name OF THE CUSTOMER"))
            cust.address = (input("ENTER THE address OF THE CUSTOMER"))
            cust.mobile = (input("ENTER THE mobile OF THE CUSTOMER"))
            cust.add_customer()
            print("customer is added successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 2):
        # write the code to search the customer
        try:
            cust = Customer()
            id = int(input("ENTER THE id OF THE CUSTOMER"))
            cust.search_customer(id)
            print(cust)
            print("customer is searched successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 3):
        # write the code to modify the customer
        try:
            cust = Customer()
            id = int(input("ENTER THE id OF THE CUSTOMER"))
            cust.name = (input("ENTER THE NEW name OF THE CUSTOMER"))
            cust.address = (input("ENTER THE NEW address OF THE CUSTOMER"))
            cust.mobile = (input("ENTER THE NEW mobile OF THE CUSTOMER"))
            cust.id=id
            cust.modify_customer(id)
            print(cust)
            print("customer is modified successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 4):
        # write the code to delete the customer
        try:
            cust = Customer()
            id = int(input("ENTER THE id OF THE CUSTOMER"))
            cust.delete_customer(id)
            print("customer is deleted successfully")
        except Exception as ex:
            print(ex)
    elif(choice==5):
        # write the code to show all the customers
        try:
            showAllCustomer()
        except Exception as ex:
            print(ex)
    else:
        #out of loop
        exit()
#PL ENDS

