#pl begins
import emsusinginheritance as em
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
            # write code for add director
            try:
                obDir = em.Director()
                obDir.Type = "Dir"
                obDir.Id = int(input("Enter Id of the director"))
                obDir.Name = input("Enter Name of the director")
                obDir.Dir_special = int(input("Enter Dir Special"))
                obDir.Share = int(input("Enter Share of the director"))
                obDir.add()
                print("Director Added Sucessfully")
            except Exception as ex:
                print(ex)
        elif (ch1 == 2):
            # write code for add Manager
            try:
                obMgr = em.Manager()
                obMgr.Type = "Mgr"
                obMgr.Id = int(input("Enter Id of the manager"))
                obMgr.Name = input("Enter Name of the manager")
                obMgr.Mgr_special = int(input("Enter Mgr Special of the manager"))
                obMgr.Share = int(input("Enter share of the manager" ))
                obMgr.add()
                print("Manager Added Sucessfully")
            except Exception as ex:
                print(ex)
        elif (ch1 == 3):
            # write code for add Trainee
            try:
                obTr = em.Trainee()
                obTr.Type = "Tr"
                obTr.Id = int(input("Enter Id of the trainee"))
                obTr.Name = input("Enter Name of the trainee")
                obTr.Tr_special = int(input("Enter Tr Special of the trainee"))
                obTr.Share = int(input("Enter share of the trainee"))
                obTr.add()
                print("trainee Added Sucessfully")
            except Exception as ex:
                print(ex)
    elif (choice == 2):
        #write the code to search the employee
        try:
            id = int(input("Enter Id of the employee"))
            '''obj = Employee.getEmpById(id)
            obj.getDetails(id)
            print(obj)
            # write code for getDetails
            '''
            obEmp=em.Employee()
            type=obEmp.gettype(id)
            if(type=="Dir"):
                obDir=em.Director()
                obDir.get_detailsby_id(id)
                print(obDir)
                print("director is searched successfully")
            elif (type == "Mgr"):
                obMgr = em.Manager()
                obMgr.get_detailsby_id(id)
                print(obMgr)
                print("manager is searched successfully")
            elif (type == "Tr"):
                obTr = em.Trainee()
                obTr.get_detailsby_id(id)
                print(obTr)
                print("trainee is searched successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 3):
        # write code to modify the employee
        try:
            id = int(input("Enter Id of the employee"))
            obEmp=em.Employee()
            type = obEmp.gettype(id)
            if (type == "Dir"):
                obDir = em.Director()
                obDir.Name = input("Enter New Name of the director")
                obDir.Dr_special = int(input("Enter new dr Special of the director"))
                obDir.Share = int(input("Enter new share of the director"))
                obDir.Type="Dir"
                obDir.Id=id
                obDir.modify_detailsby_id(id)
                print(obDir)
                print("director is modified successfully")
            elif (type == "Mgr"):
                obMgr = em.Manager()
                obMgr.Name = input("Enter New Name of the manager")
                obMgr.Mgr_special = int(input("Enter new mgr Special of the manager"))
                obMgr.Share = int(input("Enter new share of the manager"))
                obMgr.Type = "Mgr"
                obMgr.Id=id
                obMgr.modify_detailsby_id(id)
                print(obMgr)
                print("manager is modified successfully")
            elif (type == "Tr"):
                obTr = em.Trainee()
                obTr.Name = input("Enter New Name of the trainee")
                obTr.Tr_special = int(input("Enter new tr Special of the trainee"))
                obTr.Share = int(input("Enter new share of the trainee"))
                obTr.Type = "Tr"
                obTr.Id=id
                obTr.modify_detailsby_id(id)
                print(obTr)
                print("trainee is modified successfully")
        except Exception as ex:
            print(ex)
    elif (choice == 4):
        # write code to delete the employee
        try:
            id = int(input("Enter Id of the employee"))
            obEmp=em.Employee()
            type = obEmp.gettype(id)
            if (type == "Dir"):
                obDir = em.Director()
                obDir.deletebyId(id)
                print("director is deleted successfully")
            elif (type == "Mgr"):
                obMgr = em.Manager()
                obMgr.deletebyId(id)
                print("manager is deleted successfully")
            elif (type == "Tr"):
                obTr = em.Trainee()
                obTr.deletebyId(id)
                print("trainee is deleted successfully")
        except Exception as ex:
            print(ex)
    elif(choice == 5):
        #write the code to show all the employees with their details
        try:
            em.Employee.showAllEmployees()
        except Exception as ex:
            print(ex)
    elif (choice == 6):
        # write code for Exit
        break
#pl ends
