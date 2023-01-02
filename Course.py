import pandas as pd
import ast
import matplotlib.pyplot as plt
lstcid=[]
lstcn=[]
dictm={}
lstm=[]
lst=[]
i=1
lstv=[]
lst=[]
cdf=pd.DataFrame()
def creation():
    while(1):
        d=input("Enter the new course id.")
        lstcid.append(d)
        e=input("Enter the course name.")
        lstcn.append(e)
        while(1):
            f=input("Enter the student id.")
            g=int(input("Enter the marks obtained for this student."))
            dictm[f]=g
            x=int(input("Enter 1 to enter more students into the course or 0 to exit."))
            if(x==0):
                break
        lstm.append(dictm)
        y=int(input("Enter 1 to enter more courses or 0 to exit the Course Portal."))
        if(y==0):
            break
        else:
            continue
    cdf=pd.DataFrame({'Course ID':lstcid,'Course Name':lstcn,'Marks obtained':lstm})
    cdf.to_csv('Course.csv', mode='a',header=False,index=False)
def perf():
    df=pd.read_csv('Course.csv')
    df=df.set_index("Course ID")
    x=input("Enter the course ID for which you wish to see the students' performance.")
    d=ast.literal_eval(df.at[x,'Marks obtained'])
    lstk=list(d.keys())
    lstv=list(d.values())
    ndf=pd.DataFrame({'Student ID':lstk,'Marks Obtained':lstv})
    print(ndf)
    x=[]
    for i in range(0,len(lstv)):
        if(lstv[i]>=90):
            x.append('A')            
        if(lstv[i]>=80):
            x.append('B')
        if(lstv[i]>=70):
            x.append('C')
        if(lstv[i]>=60):
            x.append('D')
        if(lstv[i]>=50):
            x.append('E')
        if(lstv[i]>=40):
            x.append('F') 
    plt.hist(x)
    plt.xlabel("Grades")
    plt.ylabel("Number of Students.")
    plt.title("Course Statistics.")
    plt.show()
perf()
