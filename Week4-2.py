s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
list1=[s1[0],s2[0],s3[0]]
sum=0
studentName=str(input("Enter student's name"))
if (studentName in list1):
    if (studentName in s1):
        for i in range(1,len(s1)):
            sum=sum+s1[i]
        print(sum)
    elif studentName in s2:
        for i in range(1,len(s2)):
            sum=sum+s2[i]
        print(sum)
    elif studentName in s3:
        for i in range(1,len(s3)):
            sum=sum+s3[i]
        print(sum)
else:
    print("Student is not recorded 0 ")
