no_of_s=int(input("Enter the number of students: "))
no_of_q=int(input("Enter the number of questions "))
for i in range(no_of_s):
    marks=[]
    for j in range(no_of_q):
        j=j+1
        m=float(input("Enter marks %d: " % j))
        marks.append(m)
        total=sum(marks)
        print(str(total))