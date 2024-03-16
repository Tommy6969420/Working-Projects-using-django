class_name=input("Enter class name: ")
subj=input("Enter subj name: ")
no_of_s=int(input("Enter the number of students: "))
no_of_q=int(input("Enter the number of questions "))
marks=[]
with open(class_name+"_"+subj+".csv","w") as file:
    file.write("Students Name, Obtained Marks,\n")
    file.close()
for i in range(no_of_s):
    name=input("Enter students Name: ")
    for i in range(no_of_q):
        m=int(input("Enter marks "))
        marks.append(m)
        total=sum(marks)
        print(name+" "+str(total))
    with open(class_name+"_"+subj+".csv","a") as file:
        file.write("%s,%d,\n" % (name,total))
        file.close()
    marks=[]