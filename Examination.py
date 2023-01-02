import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
listN=[]
listr=[]
listM=[]
crs=[]
listB=[]
stu=[]
col=(np.random.random(), np.random.random(),np.random.random())
while(1):
    e=input("Enter the Course name.")
    crs.append(e)
    n=int(input("Enter the number of students who have taken this examination."))
    df1=pd.read_csv("Student.csv")
    df1=df1.set_index('Student ID')
    for j in range(0,n):
        a=input("Enter Student ID.")
        stu.append(a)
        listN.append(df1.at[a,'Name'])
        listr.append(df1.at[a,'Class Roll Number'])
        listB.append(df1.at[a,'Batch ID'])
        b=input("Enter marks scored.")
        listM.append(b)
    df3=pd.DataFrame({'Name':listN,'Class Roll':listr,'Marks':listM})
    df3.to_csv('Examination.csv',index=False)
    print("PERFORMANCE REPORT")
    print(pd.read_csv('Examination.csv'))
    plt.scatter(listM,listN,color=col)
    plt.show()
    z=int(input("Enter 1 to view more course performances or 0 to exit."))
    if(z==0):
        break
