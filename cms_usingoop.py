#customer management system using OOP's

#BLL BEGINS
class customer:
    list_cust = []          # creating a list to store the customer
    def __init__(self):     # constructor
        self.Id = 0         # storing the id of the customer
        self.Name = " "       # storing the name of the customer
        self.Address = " "    # storing the address of the customer
        self.Mobile = " "     # storing the mobile number of the customer
    '''
    this is the static method use to return the details of the customer in list_cust
    this method does not take any parameter 
    '''
    @staticmethod
    def getAllCustomerInList():
        return customer.list_cust
    '''
    this function is use to overwrite the str method of object class to return the details of the customer
    when directly object of the customer class in called in the print function
    eg - cust=customer() 
         print(cust)
    '''
    def __str__(self):
        return "id is: "+str(self.Id)+" "+"name is: "+self.Name+" "+"Address is: "+ self.Address + " "+"mobile no. is:" + self.Mobile
    '''
    this function is defined to append the customer in the list_cust
    this function takes self as the parameter 
    '''
    def add_customer(self):
        customer.list_cust.append(self)
    '''
    this function is defined to search the customer stored in the list_cust
    this function takes id of the customer as the parameter and search in the list_cust
    and after searching returns the details of the customer 
    and if id is not found then throw the exception
    '''
    def search_customer(self,Id):
        for i in customer.list_cust:
            if(i.Id==Id):
                self.Name=i.Name
                self.Address = i.Address
                self.Mobile = i.Mobile
                self.Id = i.Id
                return
        raise Exception("id not found")
    '''
    this function is defined to modify the customer stored in the list_cust
    this function takes id of the customer as the parameter 
    and after modification returns the customer to the list
    and if id is not found then throw the exception
    '''
    def modify_customer(self,Id):
        for i in customer.list_cust:
            if(i.Id==Id):
                i.Name = self.Name
                i.Address = self.Address
                i.Mobile  = self.Mobile
                return
        raise Exception("id not found")
    '''
    this function is defined to delete the customer stored in the list_cust
    this function takes id of the customer as the parameter
    and if id is not found then throw the exception
    '''
    def delete_customer(self,Id):
        for i in customer.list_cust:
            if(i.Id==Id):
                customer.list_cust.remove(i)
                return
        raise Exception("id not found")

    '''@staticmethod
    def showAllCustomer():
        for e in customer.list_cust:
          print(e)
    '''

#BLL ENDS

#PL BEGINS
'''
this method is use to show the details of all the customers 
received in the list(all_custlist) from the getAllCustomerInList() method 
'''
def showAllCustomer():
        all_custlist=customer.getAllCustomerInList()
        for e in all_custlist:
            print(e)
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
            cust = customer()
            cust.Id=int(input("ENTER THE ID OF THE CUSTOMER"))
            cust.Name = (input("ENTER THE NAME OF THE CUSTOMER"))
            cust.Address = (input("ENTER THE ADDRESS OF THE CUSTOMER"))
            cust.Mobile = (input("ENTER THE MOBILE OF THE CUSTOMER"))
            cust.add_customer()
            print("customer is added successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 2):
        # write the code to search the customer
        try:
            cust = customer()
            Id = int(input("ENTER THE ID OF THE CUSTOMER"))
            cust.search_customer(Id)
            print(cust)
            print("customer is searched successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 3):
        # write the code to modify the customer
        try:
            cust = customer()
            Id = int(input("ENTER THE ID OF THE CUSTOMER"))
            cust.Name = (input("ENTER THE NEW NAME OF THE CUSTOMER"))
            cust.Address = (input("ENTER THE NEW ADDRESS OF THE CUSTOMER"))
            cust.Mobile = (input("ENTER THE NEW MOBILE OF THE CUSTOMER"))
            cust.Id=Id
            cust.modify_customer(Id)
            print(cust)
            print("customer is modified successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 4):
        # write the code to delete the customer
        try:
            cust = customer()
            Id = int(input("ENTER THE ID OF THE CUSTOMER"))
            cust.delete_customer(Id)
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