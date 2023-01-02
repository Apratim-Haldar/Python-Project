import pandas as pd
lstn=[]
lstrno=[]
lstbch=[]
lstid=[]
lst=[]
lstm=[]
grades=[]
pf=[]
def creation():
    while(1>0):
        i=input("Enter student id.")
        n=input("Enter Student name.")
        r=int(input("Enter student roll number."))
        b=input("Enter student batch name.")
        lstid.append(i)
        lstn.append(n)
        lstrno.append(r)
        lstbch.append(b)
        z=int(input("Enter 1 to add more students, 2 to show updated dataframe or press 0 to exit."))
        if(z==0):
            break
        elif(z==2):
            print(df)
        else:
            continue
    df=pd.DataFrame({'Student ID':lstid,'Name':lstn,'Roll Number':lstrno,'Batch ID':lstbch})
    df.to_csv('Student.csv', mode='a',header=False)
def updation():
    while(1):
        b=int(input("Choose an option\n 1. Update Student ID \n 2. Update Student name.\n 3. Update Class Roll Number.\n 4. Update Batch ID."))
        if(b==1):
            a=input("Enter the Student ID to be updated.")
            x=input("Enter the new student id.")
            df=pd.read_csv('Student.csv')
            df.loc[df['Student ID']==a, 'Student ID']=x
            df.to_csv('Student.csv')
        elif(b==2):
            v=input("Enter the name to be updated.")
            y=input("Enter the new student name.")
            df=pd.read_csv('Student.csv')
            df.loc[df['Name']==v,'Name']=y
            df.to_csv('Student.csv')
        elif(b==3):
            u=input("Enter the roll number to be updated.")
            z=input("Enter the new roll number.")
            df=pd.read_csv('Student.csv')
            df.loc[df['Class Roll Number']==u,'Class Roll Number']=z
            df.to_csv('Student.csv')
        elif(b==4):
            s=input("Enter the Batch ID to be updated.")
            w=input("Enter the new Batch ID.")
            df=pd.read_csv('Student.csv')
            df.loc[df['Batch ID']==s,'Batch ID']=w
            df.to_csv('Student.csv')
        else:
            print("Invalid input. Try again.")
            continue
        c=(int)(input("Enter 1 to update more values, 2 to show the updated dataframe and 0 to exit."))
        if(c==0):
            break
        elif(c==2):
            print(df)
        else:
            continue
def removal():
    i=0
    while(1):
        d=input("Enter the Student ID to be removed.")
        df=pd.read_csv('Student.csv')
        if((d in df.values)== True):
            while(2):
                if(df.loc[i,'Student ID']==d):
                    df.drop([i],axis=0,inplace=True)
                    break
                else:
                    i+=1
        else:
            print("Invalid input.Try again")
            continue
        v=(int)(input("Enter 1 to update more values, 2 to show the updated dataframe and 0 to exit."))
        if(v==0):
            break
        elif(v==2):
            print(df)
        else:
            continue
    df.set_index('Student ID')
    df.to_csv('Student.csv',index=False)
def report():
    a=input("Enter the Student ID.")
    b=int(input("Enter the number of subjects."))
    for i in range(0,b):
        c=input("Enter subject")
        lst.append(c)
        d=int(input("Enter the marks scored out of 100"))
        lstm.append(d)
        if d>=90:
            grades.append("A")
        elif d>=80:
            grades.append("B")
        elif d>=70:
            grades.append("C")
        elif d>=60:
            grades.append("D")
        elif d>=50:
            grades.append("E")
        else:
            grades.append("F")
        if d<40:
            pf.append("FAILED")
        else:
            pf.append("PASSED")
    S=pd.read_csv("Student.csv")
    S=S.set_index('Student ID')
    print("PERFORMACE REPORT OF ",S.at[a,'Name'])
    rep=pd.DataFrame({"Subjects":lst,"Marks":lstm,"Grades":grades,"Pass/Fail Status":pf})
    rep=rep.reset_index()
    print(rep)
report()
