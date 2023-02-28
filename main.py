from All_Programs import All_Basic_Programs


# if __name__ == "__main__":
    
    # replace = All_Basic_Programs()
    # replace.replcing_names()

    # Diffence = All_Basic_Programs()
    # Diffence.Finding_Diffence()

    # tolisttuple = All_Basic_Programs()
    # tolisttuple.intolist_tuple()

    # fandlfromlist=All_Basic_Programs()
    # fandlfromlist.firstlast()


    # showcalender=All_Basic_Programs()
    # showcalender.disCalender()

    # showrdays = All_Basic_Programs()
    # showrdays.remaindays()


    # containnum = All_Basic_Programs()
    # containnum.Cointaing()


    # Concatinate=All_Basic_Programs()
    # Concatinate.Conct()



obj = All_Basic_Programs()


while True:

    print("\nSelect your Option\n1 : replacing the String Program\n2 : Finding The Differce Program\n3 : Coverting Into The List And Tuple Program\n4 : Printing First and Last From The List Program\n5 : To Display the month calender Program\n6 : To Display the remaining Days Program\n7 : Program to find the cointaning specific value ")

    select_option = int(input())


    if select_option == 1:
            obj.replcing_names()
    elif select_option == 2:
            obj.Finding_Diffence()    
    elif select_option == 3:
            obj.intolist_tuple()
    elif select_option == 4:
            obj.firstlast()    
    elif select_option == 5:
            obj.disCalender()
    elif select_option == 6:
            obj.remaindays()
    elif select_option == 7:
            obj.Cointaing()        
    else:
            print("Enter the Valid Option")    

