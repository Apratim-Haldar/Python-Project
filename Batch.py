import pandas as pd
import ast
import matplotlib.pyplot as plt
lstbd=[]
lstbn=[]
lstdn=[]
lstc=[]
lstst=[]
lst=[]
st=[]
c=[]
s=[]
bdf=pd.DataFrame()
def creation():
    while(1):
        d=input("Enter the new batch id.")
        lstbd.append(d)
        e=input("Enter the batch name.")
        lstbn.append(e)
        f=input("Enter the department name.")
        lstdn.append(f)
        while(1):
            f=input("Enter course name under this batch.")
            lst.append(f)
            x=int(input("Enter 1 to enter more courses into the batch or 0 to exit."))
            if(x==0):
                break
        lstc.append(lst)
        while(1):
            g=input("Enter students enrolled under this batch.")
            s.append(g)
            x=int(input("Enter 1 to enter more students into the batch or 0 to exit."))
            if(x==0):
                break
        st.append(s)
        y=int(input("Enter 1 to create more batches or 0 to exit the Batch Portal."))
        if(y==0):
            print (y)
            break
    bdf=pd.DataFrame({'Batch ID':lstbd,'Batch Name':lstbn,'Department Name':lstdn,'List of Courses':lstc,'List of Students':st})
    bdf.to_csv('Batch.csv', mode='a',header=False,index=False)
def students():
    df=pd.read_csv('Batch.csv')
    df=df.set_index('Batch ID')
    while(1):
        z=input("Enter the batch id.")
        print("List of all students in the batch---\n", df.at[z,'List of Students'])
        x=int(input("Enter 1 to view more batches or 0 to exit."))
        if(x==0):
            break
def courses():
    df=pd.read_csv('Batch.csv')
    df=df.set_index('Batch ID')
    while(1):
        z=input("Enter the batch id.")
        print("List of all students in the batch---\n", df.at[z,'List of Courses'])
        x=int(input("Enter 1 to view more batches or 0 to exit."))
        if(x==0):
            break
def performance():
    a=input("Enter Batch ID.")
    df=pd.read_csv('Batch.csv')
    df=df.set_index('Batch ID')
    listn=[]
    listroll=[]
    s=0
    listp=[]
    df1=pd.read_csv("Student.csv")
    df1=df1.set_index('Student ID')
    df2=pd.read_csv("Course.csv")
    df2=df2.set_index('Course ID')
    lstst=(df.at[a,'List of Students'])
    w=""
    for i in range(0,len(lstst)):
        if(lstst[i].isalnum()):
            w=w+lstst[i]
        if(lstst[i]==","):
            st.append(w)
            w=""
        if(i==(len(lstst)-1)):
            st.append(w)
    listc=(df.at[a,'List of Courses'])
    w=""
    for i in range(0,len(listc)):
        if(listc[i].isalnum()):
            w=w+listc[i]
        if(listc[i]==","):
            c.append(w)
            w=""
        if(i==(len(listc)-1)):
            c.append(w)
    for i in range(0,len(st)):
        listn.append(df1.at[st[i],'Name'])
        listroll.append(df1.at[st[i],'Class Roll Number'])
        p=int(input("Enter percentage considering all subjects."))
        listp.append(p)
    print("Performance Report of Batch ", a)
    df3=pd.DataFrame({'Name':st,'Class Roll':listroll,'Percentage':listp})
    print(df3)
    per=["(90-100)%","(80-90)%"]
    a=0
    b=0
    C=0
    d=0
    e=0
    f=0
    for i in range(0,len(listp)):
        if(listp[i]>=90):
            a=a+1          
        if(listp[i]>=80):
            b=b+1
        if(listp[i]>=70):
            C+=1
        if(listp[i]>=60):
            d+=1
        if(listp[i]>=40):
            e=e+1
        if(listp[i]<40):
            f=f+1
    pi=[a,b]
    plt.figure(figsize=(8,10))
    plt.pie(pi,labels=per,shadow=True)
    plt.legend(title="Performances")
    plt.show()
performance()
