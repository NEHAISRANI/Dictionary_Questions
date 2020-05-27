def studentRecords():
    user=input("how many records you want to entered")
    studentData=[]
    studentsRollNoList=[]
    studentClassList=[]
    studentNames=[]
    i=0
    while i<user:
        studentName=raw_input("enter the student name")
        studentNames.append(studentName)
        studentRollNo=input("enter the student roll no")
        studentClass=input("enter the student class")
        if  studentClass not in studentClassList:
            studentClassList.append(studentClass)
        if studentRollNo not in studentsRollNoList:
            studentsRollNoList.append(studentRollNo)
        i=i+1 
    
    for i in range(0,len(studentClassList)):
        for j in range(i+1,len(studentClassList)):
            if studentClassList[i]>studentClassList[j]:
                new=studentClassList[j] 
                studentClassList[j]=studentClassList[i]
                studentClassList[i]=new

    for i in range(0,len(studentsRollNoList)):
        for j in range(i+1,len(studentsRollNoList)):
            if studentsRollNoList[i]>studentsRollNoList[j]:
                new=studentsRollNoList[j]
                studentsRollNoList[j]=studentsRollNoList[i]
                studentsRollNoList[i]=new

    print(user)
    dataOfStudent=[]

    for i in range(0,user):
        dic={}
        dic["name"]=studentNames[i]
        dic["rollNo"]=studentsRollNoList[i]
        dic["class"]=studentClassList[i]
        dataOfStudent.append(dic)
    return(dataOfStudent)
studentData=(studentRecords())
print(studentData)

