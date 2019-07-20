#employee management system using hierarchical inheritance
#bll begins
class Employee:
    list_emp=[]
    def __init__(self):
        self.Id = 0
        self.Name = " "
        self.Type = " "
    '''
    this is the static method to return all the employees in the list after performing all the CRUD operation
    '''
    @staticmethod
    def get_allemployees_inlist():
        return Employee.list_emp

    '''
    this function is use to print the details of the employees returned from the getallemployeesinlist() function 
    i.e. a director or a manager or a trainee
    '''
    @staticmethod
    def showAllEmployees():
        all_emplist = Employee.get_allemployees_inlist()
        for e in all_emplist:
            print(e)

    '''
    This function takes input parameter id of the employee
    This function return the  object of the employee i.e. director or manager or trainee
    '''
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
    This function takes input parameter id of the employee
    This function return the  type of the employee i.e. director or manager or trainee
    '''
    @staticmethod
    def gettype(Id):
        for e in Employee.list_emp:
            if(e.Id==Id):
                return e.Type
        raise Exception("id not found")
    '''
    this function add the employee to the list 
    the employee can be a director ,manager aor the trainee
    '''
    def add(self):
        Employee.list_emp.append(self)
    '''
    this function returns the string for printing the details of the employee
    using print(object)
    '''
    def __str__(self):
        return "Id is: "+str(self.Id)+" "+"name is: "+self.Name+" "+"type is: "+self.Type
    '''
    This function takes input parameter as id of the employee 
    and search in the employee list and returns the name type and id of the employee
    in the self 
    '''
    def get_detailsby_id(self, Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                self.Id = e.Id
                self.Name = e.Name
                self.Type = e.Type
                return
        raise Exception("Id not found")

    '''
    This function modifies the details of the employee using Id as the parameter and store it in the list
    '''
    def modify_detailsby_id(self,Id):
        for e in Employee.list_emp:
            if(e.Id==Id):
                e.Name = self.Name
                e.Type = self.Type
                e.Id = self.Id
                return
        raise Exception("Id not found")
    '''
    this function removes the employee from the list using Id as the argument passed
    '''
    def deletebyId(self,Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                Employee.list_emp.remove(e)
                return
        raise Exception("Id not found")

#director is the derive class and employee is the parent class
class Director(Employee):

    def __init__(self):
        super().__init__()
        self.Dir_special=0
        self.Share=0


    '''
    this function add the director to the list 
    by calling the add function of the super class employee
    '''
    def add(self):
        super().add()

    '''
    this function returns the string for printing the details of the employee
    using print(object)
    '''
    def __str__(self):
        return super().__str__()+" "+"dir_special is: "+str(self.Dir_special)+" "+"share of director is: "+str(self.Share)

    '''
    this function is use to get the details of the director using Id of the employee
    and calling the getdetailsbyId function  of the super class employee 
    This function returns dir_share and share of the director with other details of the director
    '''
    def get_detailsby_id(self, Id):
        for e in Employee.list_emp:
            if(e.Id==Id):
                super().get_detailsby_id(Id)
                self.Dir_special=e.Dir_special
                self.Share=e.Share
                return
        raise Exception("Id not found")


    '''
    This function modifies the details of the director using Id as the parameter and store it in the list
    and also calls the modifydetailsbyId function of the super class employee
    '''

    def modify_detailsby_id(self,Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                super().modify_detailsby_id(Id)
                self.Dir_special = e.Dir_special
                self.Share = e.Share
                return
        raise Exception("Id not found")

    '''
    this function removes the director from the list using Id as the argument passed
    and also calling the delete function of the super class employee
    '''
    def deletebyId(self,Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                super().deletebyId(Id)
                return
        raise Exception("Id not found")

#manager is the derive class and employee is the parent class
class Manager(Employee):

    def __init__(self):
        super().__init__()
        self.Mgr_special=0
        self.Share=0

    '''
    this function add the manager to the list 
    by calling the add function of the super class employee
    '''
    def add(self):
        super().add()

    '''
    this function returns the string for printing the details of the manager
    using print(object)
    '''
    def __str__(self):
        return super().__str__()+" "+"mgr_special is: "+str(self.Mgr_special)+" "+"share of manager is: "+str(self.Share)

    '''
    this function is use to get the details of the manager using Id of the manager
    and calling the getdetailsbyId function  of the super class employee 
    This function returns mgr_share and share of the director with other details of the manager
    '''
    def get_detailsby_id(self, Id):
        for e in Employee.list_emp:
            if(e.Id==Id):
                super().get_detailsby_id(Id)
                self.Mgr_special_=e.Mgr_special
                self.Share=e.Share
                return
        raise Exception("id not found")

    '''
    This function modifies the details of the manager using Id as the parameter and store it in the list
    and also calls the modifydetailsbyId function of the super class employee
    '''

    def modify_detailsby_id(self,Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                super().modify_detailsby_id(Id)
                e.Mgr_special = self.Mgr_special
                e.Share = self.Share
                return
        raise Exception ("Id not found")

    '''
    this function removes the manager from the list using Id as the argument passed
    and also calling the delete function of the super class employee
    '''
    def deletebyId(self,Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                super().deletebyId(Id)
                return
        raise Exception ("Id not found")

#trainee is the derive class and employee is the parent class
class Trainee(Employee):

    def __init__(self):
        super().__init__()
        self.Tr_special=0
        self.Share=0

    '''
    this function add the trainee to the list 
    by calling the add function of the super class employee
    '''
    def add(self):
        super().add()

    '''
    this function returns the string for printing the details of the employee
    using print(object)
    '''

    def __str__(self):
        return super().__str__()+" "+"tr_special is: "+str(self.Tr_special)+" "+"share of trainee is: "+str(self.Share)

    '''
    this function is use to get the details of the trainee using Id of the trainee as the parameter
    and calling the getdetailsbyId function  of the super class employee 
    This function returns tr_share and share of the trainee with other details of the trainee
    '''
    def get_detailsby_id(self, Id):
        for e in Employee.list_emp:
            if(e.Id==Id):
                super().get_detailsby_id(Id)
                self.Share=e.Share
                self.Tr_special=e.Tr_special
                return
        raise Exception("Id not found")

    '''
    This function modifies the details of the trainee using Id as the parameter and store it in the list
    and also calls the modifydetailsbyId function of the super class employee
    '''
    def modify_detailsby_id(self,Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                super().modify_detailsby_id(Id)
                e.Tr_special = self.Tr_special
                e.Share = self.Share
                return
        raise  Exception("Id not found")

    '''
    this function removes the manager from the list using Id as the argument passed
    and also calling the delete function of the super class employee
    '''
    def deletebyId(self,Id):
        for e in Employee.list_emp:
            if (e.Id == Id):
                super().deletebyId(Id)
                return
        raise Exception("Id not found")

#bll ends
