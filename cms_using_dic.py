# write a program to create a customer management system using list and its functions

#bll starts
#here id is the key and values i.e. name ,address and mobile no. are stored in the form of list
#such as list=[str_name,str_address,str_mobile]
dict_Cust={}
def add_customer(int_id,str_name,str_address,str_mobile):
    list=[]
    list.append(str_name)
    list.append(str_address)
    list.append(str_mobile)
    dict_Cust[id]=list
    return dict_Cust

def search_customer(int_id):
    print("Id of the customer is : ", id,'\n'
    "Name of the customer is:", dict_Cust[id][0],'\n'
    "Address of the customer is: ", dict_Cust[id][1],'\n'
    "Mobile number of the customer is:", dict_Cust[id][2])


def modify_customer(int_id,str_name,str_address,str_mobile):
    dict_Cust[id][0]=str_name
    dict_Cust[id][1]=str_address
    dict_Cust[id][2]=str_mobile
    return dict_Cust

def delete_customer(int_id):
    dict_Cust.pop(int_id)


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
        dict_Cust=add_customer(id,name,address,mobile)
        print("details of the the customer",dict_Cust)
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
        dict_Cust=modify_customer(id,name,address,mobile)
        print("details after modification:",dict_Cust)
        print("customer is modified successfully")
    elif(choice==4):
        # write the code to delete the details of the customer
        id = int(input("ENTER THE ID OF THE CUSTOMER"))
        delete_customer(id)

        print("customer is deleted successfully")
    else:
        break                  # out of loop
#pl ends