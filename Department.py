import pandas as pd
dn=[]
lstbh=[]
id=[]
l=[]
ddf=pd.DataFrame()
def creation():
    while(1>0):
        i=input("Enter Department ID.")
        n=input("Enter Department name.")
        while(1):
            b=input("Enter batches under this department and press 0 to exit.")
            id.append(i)
            dn.append(n)
            l.append(b)
        lstbh.append(l)
        z=int(input("Enter 1 to add more departments, 2 to show updated dataframe or press 0 to exit."))
        if(z==0):
            break
        elif(z==2):
            print(pd.read_csv('Department.csv'))
        else:
            continue
    ddf=pd.DataFrame({'Department ID':id,'Department Name':dn,'List of Batches':lstbh})
    ddf.to_csv('Department.csv', mode='a',header=False)  
def batches():
    df=pd.read_csv('Department.py')
    df=df.set_index('List of Batches')
    while(1):
        z=input("Enter the department id.")
        print("List of all Batches in the department---\n", df.at[z,'List of Batches'])
        x=int(input("Enter 1 to view more batches or 0 to exit."))
        if(x==0):
            break
def courses():
    df=pd.read_csv('Batch.py')
    df=df.set_index('Batch ID')
    while(1):
        z=input("Enter the batch id.")
        print("List of all students in the batch---\n", df.at[z,'List of Courses'])
        x=int(input("Enter 1 to view more batches or 0 to exit."))
        if(x==0):
            break