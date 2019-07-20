# write a program to create a customer management system using list and its functions

#bll starts
listId=[] #list created to enter the id of the customer
listName=[] #list created to enter the name of the customer
listAddress=[] #list created to enter the address of the customer
listMobile=[] #list created to enter the mobile nmmber of the customer
def add_customer(int_id,str_name,str_address,str_mobile):
    listId.append(int_id)
    listName.append(str_name)
    listAddress.append(str_address)
    listMobile.append(str_mobile)
    return listId,listName,listAddress,listMobile

def search_customer(int_id):
    if(listId.__contains__(id)):
        i=listId.index(id)
        print("Id of the customer is : ", listId[i],'\n'
        "Name of the customer is:", listName[i],'\n'
        "Address of the customer is: ", listAddress[i],'\n'
        "Mobile number of the customer is:", listMobile[i])
    else:
        print("you have entered invalid Id of the customer to be searched")
def modify_customer(int_id,str_name,str_address,str_mobile):
    if (listId.__contains__(id)):
        i = listId.index(id)
        listId[i]=id
        listName[i]=name
        listAddress[i]=address
        listMobile[i]=mobile
    else:
        print("you have entered invalid Id of the customer to be modified")
    return listId,listName,listAddress,listMobile

def delete_customer(int_id):
    if (listId.__contains__(id)):
        i = listId.index(id)
        listId.pop(i)
        listName.pop(i)
        listAddress.pop(i)
        listMobile.pop(i)
    else:
        print("you have entered invalid Id of the customer to be deleted")


#bll ends
#pl starts
while(True):
    user_msg="""
            1-add customer
            2-search customer
            3-modify customer
            4-delete customer
            5-exit"""
    print(user_msg)
    choice=int(input("enter your choice"))
    if(choice==1):
        # write the code to add the customer
        id=int(input("ENTER THE ID OF THE CUSTOMER"))
        name =(input("ENTER THE NAME OF THE CUSTOMER"))
        address = (input("ENTER THE ADDRESS OF THE CUSTOMER"))
        mobile = (input("ENTER THE MOBILE NUMBER OF THE CUSTOMER"))
        listId,listName,listAddress,listMobile=add_customer(id,name,address,mobile)
        print("list of id:",listId)
        print("list of name:",listName)
        print("list of address:",listAddress)
        print("list of mobile number:",listMobile)
        print("customer is added successfully")
    elif(choice==2):
        # write the code to search the customer
        id=int(input("ENTER THE ID OF THE CUSTOMER"))
        search_customer(id)
        print("customer is searched successfully")
    elif(choice==3):
        #write the code to modify the details of the customer
        id = int(input("ENTER THE ID OF THE CUSTOMER"))
        name = (input("ENTER THE NEW NAME OF THE CUSTOMER"))
        address = (input("ENTER THE NEW ADDRESS OF THE CUSTOMER"))
        mobile = (input("ENTER THE NEW MOBILE NUMBER OF THE CUSTOMER"))
        listId,listName,listAddress,listMobile=modify_customer(id,name,address,mobile)
        print("list of id:",listId)
        print("list of name:",listName)
        print("list of address:",listAddress)
        print("list of mobile number:",listMobile)
        print("customer is modified successfully")
    elif(choice==4):
        # write the code to delete the details of the customer
        id = int(input("ENTER THE ID OF THE CUSTOMER"))
        delete_customer(id)
        print("customer is deleted successfully")
    else:
        break                  # out of loop
#pl ends