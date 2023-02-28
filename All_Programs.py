import calendar  


class All_Basic_Programs():

    
    def replcing_names(self):
        name=input("enter the first name: ")
        name1=input("enter the second name: ")
        print(str(name,)[::-1],str(name1,)[::-1])


    def Finding_Diffence(self):
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])

        print("\nDifferenct of color_list_1 and color_list_2:")
        print(color_list_1.difference(color_list_2))


    def intolist_tuple(self):
        values = input("enter the numbers : ")
        list1 = values.split(",")
        tuple1 = tuple(list1)
        print('List : ',list1)
        print('Tuple : ',tuple1)

    def firstlast(self):
        color_list = ["Red","Green","White" ,"Black"]
        print( "%s %s"%(color_list[0],color_list[-1]))


    def disCalender(slef):
       
        year = int(input ("enter the Year: ")) 
        month = int(input ("enter the month: "))   
        
        print("\nThe Calendar of: \n\n", calendar.month(year, month)) 


    def remaindays(self):
            from datetime import date
            first_date = date(2023, 2, 27)
            last_date = date(2023, 5, 18)
            result = last_date - first_date
            print(result.days)


    def Cointaing(self):
        number=[ 5, 8, 3, 5, 34, 0 ]

        i=5

        if i in number:
            print("True")
        else:
            print("false")        


    def Conct(self):
        l = [ 'hello', 'Mohammad', 'Aqeeb','ankalagi']

        result = ' '
        for i in l:

            result = result+ ' '+ i

        print(result)        















