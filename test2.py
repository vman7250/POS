import psycopg2
#connectinng to psycopg2
conn=psycopg2.connect(dbname='shop',user='postgres',port='5432',password='1234')
#need to allow database operation
our_cursor=conn.cursor()

total=0
amt=0

def display(): # displays the vegetable list
    show_query="select * from products"
    our_cursor.execute(show_query)
    to_display= our_cursor.fetchall()
    for i in to_display:
     print(i)

def if_exists(x): # checks if the entered id is valid and exists    
    select_query="select exists(select id from products where id={});".format(x)
    our_cursor.execute(select_query)
    selected_choice=our_cursor.fetchone()
    
    if selected_choice[0]==False: 
       return False
    else:
        return True 
      

    


while True:
    display() #displays the vegetable list
    choice=int(input("Please enter the vegetable id of your choice"))
    
    if choice==0:
        break
    elif (if_exists(choice))==True:
        name_query="select name from products where id={};".format(choice)
        our_cursor.execute(name_query)
        name=our_cursor.fetchone()
        
        quant=int(input("enter the amount of {} : ".format(name[0])))
        
        price_query="select price from products where id={}".format(choice)
        our_cursor.execute(price_query)
        price=our_cursor.fetchone()

        amt=(quant*price[0])/1000
        total+=amt
        print(total)

print("Your total billing amount is {}".format(total))
    


        
    
    
    