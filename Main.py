import pandas as pd
print("******************WELCOME TO STUDENT EXAMINATION PORTAL******************")
while(1):
    q=int(input("\nList of Operations.\n0.Exit Examination Portal Software\n1.View Student Database\n    5.Create new Student Detail\n    6.Update Student Database\n    7.Remove a student from the Database\n    8.Generate Student Report Card\n2.View Course Database\n    9.Create new Course\n    10.View student's performance in any Course\n    11.View Course Statistics\n3.View Batch Database\n    12.Update Batch Details\n    13.View list of all students in a batch.\n    14.View list of all courses.\n    15.View Student Performance in a Batch\n4.View Department Database.\n    16.Create new Department.\n    17.View all batches in a department\n18. Register a new examunation and view statistics of the same."))
    if(q==1):
        print(pd.read_csv('Student.csv'))
    if(q==2):
        print(pd.read_csv('Course.csv'))
    if(q==3):
        print(pd.read_csv('Batch.csv'))
    if(q==4):
        print(pd.read_csv('Department.csv'))
    if(q==5):
        from student import creation
    if(q==6):
        from student import updation
    if(q==7):
        from student import removal
    if(q==8):
        from student import report
    if(q==9):
        from Course import creation
    if(q==10):
        from Course import perf
    if(q==11):
        from Course import stat
    if(q==12):
        from Batch import creation
    if(q==13):
        from Batch import students
    if(q==14):
        from Batch import courses
    if(q==15):
        from Batch import performance
    if(q==16):
        from Department import creation
    if(q==17):
        from Department import batches
    if(q==18):
        import Examination
   