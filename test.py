import psycopg2
conn=psycopg2.connect(dbname='shop',user='postgres',port='5432',password='1234')
our_cursor=conn.cursor() # to perform database operation

total=0

while True:
    choice=input("enter the name of the vegetable: ")

    if choice=='0':
      break   

    read="select * from products where name = '"+ choice +"'"
    our_cursor.execute(read)
    print('')
    result=our_cursor.fetchone()
    quant=int(input("enter the quantity of {} :".format(choice)))
    amt=(quant/1000)* result[4]
    
    total+=amt

    print(total)




