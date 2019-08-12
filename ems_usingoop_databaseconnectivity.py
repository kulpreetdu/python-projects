#employee management system using hierarchical inheritance
import pymysql
#bll begins
class Employee:
    con = pymysql.connect(host="localhost", user="****", password="********", database='5thjune2019')
    def __init__(self):
        self.Id = 0
        self.Name = " "
        self.Type = " "
        self.Address = " "
        self.Mobile = " "
    '''
    this is the static method to return all the employees in the list after performing all the CRUD operation
    
    @staticmethod
    def get_allemployees_inlist():
        return Employee.list_emp
    '''
    @staticmethod
    def showAllEmployees():
        myCurSor = Employee.con.cursor()
        strQuery = "select * from customer"
        rowAffected = myCurSor.execute(strQuery)
        if (rowAffected != 0):
            for row in myCurSor.fetchall():
                for cell in row:
                    print(cell, end='\t')
                print()
        else:
            raise Exception("database is empty")
    '''
    This function takes input parameter id of the employee
    This function return the  object of the employee i.e. director or manager or trainee
    
    @staticmethod
    def getempbyid(Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                if(e.Type=="Dir"):
                    return  Director()
                elif(e.Type == "Mgr"):
                    return Manager()
                elif(e.Type == "Tr"):
                    return Trainee()
        raise Exception("Id not found")
    '''
    '''
    This function takes input parameter id of the employee
    This function return the  type of the employee i.e. director or manager or trainee
    '''
    @staticmethod
    def gettype(Id):
        myCurSor = Employee.con.cursor()
        strQuery = "select * from customer where id=%s"
        rowAffected = myCurSor.execute(strQuery,(Id))
        if (rowAffected != 0):
            for row in myCurSor.fetchone():
                return row[2]
                print()
        else:
            raise Exception("Id not found")

    def add(self):
        myCurSor = Employee.con.cursor()
        strQuery = "insert into employee values(%s,%s,%s,%s,%s)"
        myCurSor.execute(strQuery, (self.Id, self.Name, self.Type, self.Address, self.Mobile))
        Employee.con.commit()
    '''
    this function returns the string for printing the details of the employee
    using print(object)
    '''
    def __str__(self):
        return "Id is: "+str(self.Id)+" "+"name is: "+self.Name+" "+"type is: "+self.Type+"address is: "+self.Address+" "+"mobile number is: "+self.Mobile

    def get_detailsby_id(self, Id):
        myCurSor = Employee.con.cursor()
        strQuery = "select * from customer  where id=%s"
        rowAffected = myCurSor.execute(strQuery, (Id))
        if (rowAffected != 0):
            row = myCurSor.fetchone()
            self.Id = row[0]
            self.Name = row[1]
            self.Type = row[2]
            self.Address = row[3]
            self.Mobile = row[4]
            return
        else:
            raise Exception("id not found")

    def modify_detailsby_id(self,Id):
        myCurSor = Employee.con.cursor()
        strQuery = "update employee set id=%s,name=%s,type=%s,address=%s,mobile=%s where id=%s"
        rowAffected = myCurSor.execute(strQuery, (self.Id, self.Name, self.Type, self.Address, self.Mobile, self.Id))
        if (rowAffected != 0):
            Employee.con.commit()
            return
        else:
            raise Exception("id not found")

    def deletebyId(self,Id):
        myCurSor = Employee.con.cursor()
        strQuery = "delete from customer  where id=%s"
        rowAffected = myCurSor.execute(strQuery, (Id))
        if (rowAffected != 0):
            Employee.con.commit()
            return
        else:
            raise Exception("id not found")
#director is the derive class and employee is the parent class
class Director(Employee):

    def __init__(self):
        super().__init__()
        self.Dir_special=0
        self.Share=0

    def add(self):
        super().add()
        myCurSor = Employee.con.cursor()
        strQuery = "insert into employee values(%s,%s)"
        myCurSor.execute(strQuery, (self.Dir_special, self.Share))
        Employee.con.commit()
    '''
    this function returns the string for printing the details of the employee
    using print(object)
    '''
    def __str__(self):
        return super().__str__()+" "+"share of director is: "+str(self.Share)+" "+"dir_special is: "+str(self.Dir_special)

    def get_detailsby_id(self, Id):
        super().get_detailsby_id(Id)
        myCurSor = Employee.con.cursor()
        strQuery = "select * from customer  where id=%s"
        rowAffected = myCurSor.execute(strQuery, (Id))
        if (rowAffected != 0):
            row = myCurSor.fetchone()
            self.Dir_special = row[6]
            self.Share = row[5]
            return
        else:
            raise Exception("Id not found")


    def modify_detailsby_id(self,Id):
        super().modify_detailsby_id(Id)
        myCurSor = Employee.con.cursor()
        strQuery = "update employee set dirspecial=%s,share=%s where id=%s"
        rowAffected = myCurSor.execute(strQuery, (self.Dir_special, self.Share, self.Id))
        if (rowAffected != 0):
            Employee.con.commit()
            return
        else:
            raise Exception("id not found")

    def deletebyId(self,Id):
        super().deletebyId(Id)
        return

#manager is the derive class and employee is the parent class
class Manager(Employee):

    def __init__(self):
        super().__init__()
        self.Mgr_special=0
        self.Share=0

    def add(self):
        super().add()
        myCurSor = Employee.con.cursor()
        strQuery = "insert into employee values(%s,%s)"
        myCurSor.execute(strQuery, (self.Mgr_special, self.Share))
        Employee.con.commit()

    '''
    this function returns the string for printing the details of the manager
    using print(object)
    '''
    def __str__(self):
        return super().__str__()+" "+"share of manager is: "+str(self.Share)+" "+"mgr_special is: "+str(self.Mgr_special)

    def get_detailsby_id(self, Id):
        super().get_detailsby_id(Id)
        myCurSor = Employee.con.cursor()
        strQuery = "select * from customer  where id=%s"
        rowAffected = myCurSor.execute(strQuery, (Id))
        if (rowAffected != 0):
            row = myCurSor.fetchone()
            self.Mgr_special = row[7]
            self.Share = row[5]
            return
        else:
            raise Exception("Id not found")

    def modify_detailsby_id(self,Id):
        super().modify_detailsby_id(Id)
        myCurSor = Employee.con.cursor()
        strQuery = "update employee set mgrspecial=%s,share=%s where id=%s"
        rowAffected = myCurSor.execute(strQuery, (self.Mgr_special, self.Share, self.Id))
        if (rowAffected != 0):
            Employee.con.commit()
            return
        else:
            raise Exception("id not found")

    def deletebyId(self,Id):
        super().deletebyId(Id)
        return

#trainee is the derive class and employee is the parent class
class Trainee(Employee):

    def __init__(self):
        super().__init__()
        self.Tr_special=0
        self.Share=0

    def add(self):
        super().add()
        myCurSor = Employee.con.cursor()
        strQuery = "insert into employee values(%s,%s)"
        myCurSor.execute(strQuery, (self.Tr_special, self.Share))
        Employee.con.commit()

    '''
    this function returns the string for printing the details of the employee
    using print(object)
    '''
    def __str__(self):
        return super().__str__()+" "+"share of trainee is: "+str(self.Share)+" "+"tr_special is: "+str(self.Tr_special)

    def get_detailsby_id(self, Id):
        super().get_detailsby_id(Id)
        myCurSor = Employee.con.cursor()
        strQuery = "select * from customer  where id=%s"
        rowAffected = myCurSor.execute(strQuery, (Id))
        if (rowAffected != 0):
            row = myCurSor.fetchone()
            self.Tr_special = row[8]
            self.Share = row[5]
            return
        else:
            raise Exception("Id not found")

    def modify_detailsby_id(self,Id):
        super().modify_detailsby_id(Id)
        myCurSor = Employee.con.cursor()
        strQuery = "update employee set trspecial=%s,share=%s where id=%s"
        rowAffected = myCurSor.execute(strQuery, (self.Tr_special, self.Share, self.Id))
        if (rowAffected != 0):
            Employee.con.commit()
            return
        else:
            raise Exception("id not found")

    def deletebyId(self,Id):
        super().deletebyId(Id)
        return

#bll ends

#pl begins
while (True):
    user_msg = '''
            1:add employee
            2:search employee
            3:modify employee
            4:delete employee
            5:show all employee
            6:exit
            '''
    print('\n',user_msg,'\n')
    choice=int(input("enter your choice"))
    if(choice==1):
        print("1.Director\n2.Manager\n3.Trainee")
        ch1 = int(input("Enter your choice"))
        if (ch1 == 1):
            # write code to add director
            try:
                obDir = Director()
                obDir.Id = int(input("Enter Id of the director"))
                obDir.Name = input("Enter Name of the director")
                obDir.Type = "Dir"
                obDir.Address = input("Enter Address of the director")
                obDir.Mobile = input("Enter mobile number of the director")
                obDir.Dir_special = int(input("Enter Dir Special"))
                obDir.Share = int(input("Enter Share of the director"))
                obDir.add()
                print("Director Added Sucessfully")
            except Exception as ex:
                print(ex)
        elif (ch1 == 2):
            # write code to add Manager
            try:
                obMgr = Manager()
                obMgr.Id = int(input("Enter Id of the manager"))
                obMgr.Name = input("Enter Name of the manager")
                obMgr.Type = "Mgr"
                obMgr.Address = input("Enter Address of the manager")
                obMgr.Mobile = input("Enter mobile number of the manager")
                obMgr.Mgr_special = int(input("Enter Mgr Special of the manager"))
                obMgr.Share = int(input("Enter share of the manager" ))
                obMgr.add()
                print("Manager Added Sucessfully")
            except Exception as ex:
                print(ex)
        elif (ch1 == 3):
            # write code to add Trainee
            try:
                obTr = Trainee()
                obTr.Id = int(input("Enter Id of the trainee"))
                obTr.Name = input("Enter Name of the trainee")
                obTr.Type = "Tr"
                obTr.Address = input("Enter Address of the trainee")
                obTr.Mobile = input("Enter mobile number of the trainee")
                obTr.Tr_special = int(input("Enter Tr Special of the trainee"))
                obTr.Share = int(input("Enter share of the trainee"))
                obTr.add()
                print("trainee Added Sucessfully")
            except Exception as ex:
                print(ex)
    elif (choice == 2):
        #write the code to search the employee
        try:
            Id = int(input("Enter Id of the employee"))
            '''obj = Employee.getEmpById(id)
            obj.getDetails(id)
            print(obj)
            # write code for getDetails
            '''
            obEmp=Employee()
            type=obEmp.gettype(Id)
            if(type=="Dir"):
                obDir=Director()
                obDir.get_detailsby_id(Id)
                print(obDir)
                print("director is searched successfully")
            elif (type == "Mgr"):
                obMgr = Manager()
                obMgr.get_detailsby_id(Id)
                print(obMgr)
                print("manager is searched successfully")
            elif (type == "Tr"):
                obTr = Trainee()
                obTr.get_detailsby_id(Id)
                print(obTr)
                print("trainee is searched successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 3):
        # write code to modify the employee
        try:
            Id = int(input("Enter Id of the employee"))
            obEmp=Employee()
            type = obEmp.gettype(Id)
            if (type == "Dir"):
                obDir = Director()
                obDir.Id = Id
                obDir.Name = input("Enter New Name of the director")
                obDir.Type = "Dir"
                obDir.Address = input("Enter Address of the director")
                obDir.Mobile = input("Enter mobile number of the director")
                obDir.Share = int(input("Enter new share of the director"))
                obDir.Dr_special = int(input("Enter new dr Special of the director"))
                obDir.modify_detailsby_id(Id)
                print(obDir)
                print("director is modified successfully")
            elif (type == "Mgr"):
                obMgr = Manager()
                obMgr.Id = Id
                obMgr.Name = input("Enter New Name of the manager")
                obMgr.Type = "Mgr"
                obMgr.Address = input("Enter Address of the manager")
                obMgr.Mobile = input("Enter mobile number of the manager")
                obMgr.Share = int(input("Enter new share of the manager"))
                obMgr.Mgr_special = int(input("Enter new mgr Special of the manager"))
                obMgr.modify_detailsby_id(id)
                print(obMgr)
                print("manager is modified successfully")
            elif (type == "Tr"):
                obTr = Trainee()
                obTr.Id=Id
                obTr.Name = input("Enter New Name of the trainee")
                obTr.Type = "Tr"
                obTr.Address = input("Enter Address of the trainee")
                obTr.Mobile = input("Enter mobile number of the trainee")
                obTr.Share = int(input("Enter new share of the trainee"))
                obTr.Tr_special = int(input("Enter new tr Special of the trainee"))
                obTr.modify_detailsby_id(id)
                print(obTr)
                print("trainee is modified successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 4):
        # write code to delete the employee
        try:
            Id = int(input("Enter Id of the employee"))
            obEmp=Employee()
            type = obEmp.gettype(Id)
            if (type == "Dir"):
                obDir = Director()
                obDir.deletebyId(Id)
                print("director is deleted successfully")
            elif (type == "Mgr"):
                obMgr = Manager()
                obMgr.deletebyId(Id)
                print("manager is deleted successfully")
            elif (type == "Tr"):
                obTr = Trainee()
                obTr.deletebyId(Id)
                print("trainee is deleted successfully")
        except Exception as ex:
            print(ex)
    elif(choice == 5):
        #write the code to show all the employees with their details
        try:
            Employee.showAllEmployees()
        except Exception as ex:
            print(ex)
    elif (choice == 6):
        # write code for Exit
        break
#pl ends
