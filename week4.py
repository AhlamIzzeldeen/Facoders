grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
grades ={'grade_one':grade_one, 'grade_two' :grade_two, 'grade_three': grade_three}

def  students_names( classname):
  if classname in grades :
    for i in grades[classname]:
      print (i)
  else: print("theres no class called -",classname)

def student_score( studentname,  classname):
  if classname in grades :
    for i in grades[classname]:
      if i == studentname :
        print(sum(grades[classname][i]))
  else: print("theres no class called -",classname)


def  student_count(  classname):
    if classname in grades :
      print(len(grades[classname].keys()))
    else: print("theres no class called -",classname)




teacher_opinion ='more'

while(teacher_opinion == 'more'):
  input1=input("Choose one: 1- students_names, 2- student_score, 3- students_count")
  if (input1 == ("students_names")):
    input2=input("enter class name ")
    students_names(input2)
  elif (input1 == ("student_score")):
     input2=input("enter class name ")
     input3=input("enter student name ")
     student_score(input3,input2)
  elif (input1 == ("students_count")):
     input2=input("enter class name ")
     student_count(input2)
  teacher_opinion=input("if done please insert done if you want to do more function insert 'more'")

print('thank you ')
