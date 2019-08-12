#bll begins

import pickle
class Customer:
    listCus=[]
    def __str__(self):
        return "Id: "+str(self.id)+" "+ "Name: "+self.name+" "+"Address: "+self.address+" "+"Mobile No: "+self.mob

    @staticmethod
    def saveDatainFile():
        fs=open("cusMgtPickle.txt",'wb')
        pickle.dump(Customer.listCus,fs)

    @staticmethod
    def loadDatafromFile():
        fs = open("cusMgtPickle.txt", 'rb')
        Customer.listCus=pickle.load( fs)
        return Customer.listCus

    @staticmethod
    def getAllCustomerInLIst():
        return Customer.listCus
    def __int__(self):
        self.id = 0
        self.name = " "
        self.address = " "
        self.mob = " "
    def addCustomer(self):
        Customer.listCus.append(self)
    def searchCustomer(self,id):
        for e in Customer.listCus:
            if(e.id==id):
                self.name=e.name
                self.mob=e.mob
                self.address=e.address
                self.id=e.id
                return
        raise Exception("id not found")

    def modify_customer(self, id):
        for e in customer.list_cust:
            if (e.id == id):
                e.name = self.name
                e.address = self.address
                e.mobile = self.mobile
                return
        raise Exception("id not found")

    def deleteCustomer(self, id):
        for e in Customer.listCus:
            if (e.id == id):
                Customer.listCus.remove(e)
                return
        raise Exception("id not found")

#bll ends
#PL Code begins
if __name__=="__main__" :
    def showAllCustomer():
        allCus=Customer.getAllCustomerInLIst()
        for e in allCus:
            print(e)

    while(True):
        print("1.Add\n2.Search\n3.Delete\n4.Modify\n5.Show All Customer\n6.Save Data in File\n7.Load Data from File\n0.Exit")
        ch=int(input("Enter your choice"))
        if(ch == 1):
        #write the code to add the customer
            try:
                cus=Customer()
                cus.id=int(input("Enter Id"))
                cus.name=input("Enter Name")
                cus.address=input("Enter Address")
                cus.mob=input("Enter Mobile No")
                cus.addCustomer()
                print("Customer Added Sucessfully")
            except Exception as ex:
                print(ex)

        elif(ch == 2):
        #write the code to search the customer
            try:
                cus=Customer()
                id=int(input("Enter ID"))
                cus.searchCustomer(id)
                print(cus)
                # print("ID:",cus.id,"Name:",cus.name,"Address:",cus.address,"Mobile No",cus.mob)
            except Exception as ex:
                print(ex)

        elif (ch == 3):
        #write the code to delete the customer
            try:
                cus = Customer()
                id = int(input("Enter ID"))
                cus.deleteCustomer(id)
                print("Customer Deleted Sucessfully")
            except Exception as ex:
                print(ex)

        elif (ch == 4):
        # write the code to modify the customer
            try:
                cus = Customer()
                id = int(input("ENTER THE id OF THE CUSTOMER"))
                cus.name = (input("ENTER THE NEW name OF THE CUSTOMER"))
                cus.address = (input("ENTER THE NEW address OF THE CUSTOMER"))
                cus.mobile = (input("ENTER THE NEW mobile OF THE CUSTOMER"))
                cus.id=id
                cus.modify_customer(id)
                print(cus)
                print("customer is modified successfully")
            except Exception as ex:
                print(ex)

        elif(ch == 5):
        #write the code to show all the customer
            try:
                showAllCustomer()
            except Exception as ex:
                print(ex)

        elif (ch == 6):
        #write the code to save all the customers in the file
            try:
                Customer.saveDatainFile()
            except Exception as ex:
                print(ex)

        elif (ch == 7):
        #write the code to load all the customers from the file
            try:
                Customer.loadDatafromFile()
                showAllCustomer()
            except Exception as ex:
                print(ex)

        else:
        #out of loop
            break
#PL Code ends