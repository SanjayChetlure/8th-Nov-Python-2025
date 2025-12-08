
# def functionName():
#     function body

print("-------Function Without/Zero parameter---------")

# Ex1: Function Without/zero parameter
def f1():                   #function declaration
    print("--function started--")
    print("HI")            # line 7-9 function body
    print("hello")
    print("gn")
    print("--function ended--")

def add():
    num1=10
    num2=20
    print(num1+num2)

f1()                   #function Call ->functionName()
f1()
add()
add()

print("-------Function With parameter---------")

# Ex2: Function With parameter
def add(num1,num2):     #num1=5, num2=6
    print(num1+num2)      #30+40 = 70

add(10,20)      #30
add(30,40)      #70
add(5,6)        #11


def printStudentName(name):     #name=mahesh
    print(name)

printStudentName("Amol")
printStudentName("Ganesh")
printStudentName("mahesh")


def findSquareOfNum(num):
    print(num*num)

findSquareOfNum(4)
findSquareOfNum(6)


def studentInfo(name,rollNum,per,grade):
    print("Student Name:",name)
    print("Student RollNum:", rollNum)
    print("Student Percentage:", per,"%")
    print("Student Grade:", grade)

studentInfo("Pallavi",101,65.1,"A+")
studentInfo("Uma",102,59.5,"A")








