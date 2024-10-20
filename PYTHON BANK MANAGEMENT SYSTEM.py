#Testing new codes/trying new things
import pandas as pd
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd='0319',database='bnksystm')
mycursor=mycon.cursor()
if mycon.is_connected():
    print('MySQL Connected')
else:
    print('MySQL Connection Problem')
print("************************************************************")
print("============== WELCOME TO GOLDEN HORIZON BANK ==============")
print("************************************************************")
print("==========     (1). Open New  Account            ===========")
print("==========     (2). Withdraw a Money             ===========")
print("==========     (3). Deposit a Money              ===========")
print("==========     (4). Check Balance in Account     ===========")
print("==========     (5). Update Personal Detail       ===========")
print("************************************************************")
chc=int(input('enter your requirement:'))
if chc==1:       
    l=[]
    Account_No=int(input("enter the account no:"))
    l.append(Account_No)
    Pin=int(input('enter the pin:'))
    l.append(Pin)
    Name=input("enter the name:")
    l.append(Name)
    Balance=int(input("enter deposited amount:"))
    l.append(Balance)
    Account_Type =input("enter account type(s/c):")
    l.append(Account_Type)
    Contact_No=input("enter the contact no:")
    l.append(Contact_No)
    City=input('enter the city:')
    l.append(City)
    custinf=(l)
    qry="insert into custinf values({},{},{},{},{},{},{});".format(Account_No, Pin,Name,Balance,Account_Type, Contact_No,City)
    mycursor.execute(qry)
    mycon.commit()
    print('New Account Added')
    df1=pd.read_sql('select*from custinf',mycon)
    print(df1)
   
elif chc==2:        
    ac=int(input("enter the account no:"))
    dps=int(input("enter the  amount to withdraw:"))
    qry="UPDATE custinf set Balance=Balance-{} WHERE Account_No ={};".format(dps,ac)
    mycursor.execute(qry)
    mycon.commit()
    print('Account Modified')
    df1=pd.read_sql('select*from custinf',mycon)
    print(df1)
    
elif chc==3:        
     ac=int(input("enter the account no:"))
     dps=int(input("enter the  amount to deposit:"))
     qry="UPDATE custinf set Balance=Balance+{} WHERE Account_No ={};".format(dps,ac)
     mycursor.execute(qry)
     mycon.commit()
     print('Account Modified')
     df1=pd.read_sql('select*from custinf',mycon)
     print(df1)
    
elif chc==4:  
     ac=int(input("enter the account no:"))
     qry='Select Balance from custinf where Account_no=%s'%(ac,)
     df1=pd.read_sql(qry,mycon)
     print(df1)
elif chc==5:
    print('1.Update Name')    
    print('2.Update Contact no.')
    print('3.Update City')
    print('4.Update Pin')
    chd=int(input('enter your choice:'))
    if chd==1:      #put name in inverted commas
        Account_No=int(input('enter the account number:'))
        Nm=input('enter new name:')
        qry="UPDATE custinf set Name={} WHERE Account_No ={};".format(Nm,Account_No)
        mycursor.execute(qry)
        mycon.commit()
        print('Account Modified')
        df1=pd.read_sql('select*from custinf',mycon)
        print(df1)
    elif chd==2:
        Account_No=int(input('enter the account number:'))
        cnt=int(input('enter the new contact number:'))
        qry="UPDATE custinf set Contact_No={} WHERE Account_No ={};".format(cnt,Account_No)
        mycursor.execute(qry)
        mycon.commit()
        print('Account Modified')
        df1=pd.read_sql('select*from custinf',mycon)
        print(df1)
    elif chd==3:    #put city in inverted commas
        Account_No=int(input('enter the account number:'))
        cty=input('enter new city:')
        qry="UPDATE custinf set City={} WHERE Account_No ={};".format(cty,Account_No)
        mycursor.execute(qry)
        mycon.commit()
        print('Account Modified')
        df1=pd.read_sql('select*from custinf',mycon)
        print(df1)
    elif chd==4:
        Account_No=int(input('enter the account number:'))
        Pin=int(input('enter the new pin:'))
        qry="UPDATE custinf set Pin={} WHERE Account_No ={};".format(Pin,Account_No)
        mycursor.execute(qry)
        mycon.commit()
        print('Account Modified')
        df1=pd.read_sql('select*from custinf',mycon)
        print(df1)
else:
    print('enter a valid choice')
    
    