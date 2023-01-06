studentList = []

class Info:
    def __init__(self, name, mid_score, final_score):
        self.name = name
        self.mid_score = mid_score
        self.final_score = final_score
        self.grade = 'none'
    
##############  menu 1
def Menu1(name,mid,final):
    #사전에 학생 정보 저장하는 코딩
    instance = Info(name, mid, final)
    studentList.append(instance)

##############  menu 2
def Menu2():
    #학점 부여 하는 코딩
    for i in range(len(studentList)):
        average = (studentList[i].mid_score + studentList[i].final_score) / 2
        if average >= 90:
            studentList[i].grade = 'A'
        elif average >= 80:
            studentList[i].grade = 'B'
        elif average >= 70:
            studentList[i].grade = 'C'
        else:
            studentList[i].grade = 'D'

##############  menu 3
def Menu3():
    #출력 코딩
    print()
    print("-----------------------------")
    print("name\tmid\tfinal\tgrade")
    print("-----------------------------")
    for i in range(len(studentList)):
        print("{}\t{}\t{}\t{}".format(studentList[i].name,studentList[i].mid_score,studentList[i].final_score,studentList[i].grade))

##############  menu 4
def Menu4(names):
    for i in range(len(studentList)):
        if(names == studentList[i].name):
            del studentList[i]
            break
#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        print("Enter name mid-score final-score: ")

        try:
            n, ms, fs = input().split()
        except ValueError: # input 개수 안맞을때 
            print("Num of data is not 3!")
            continue

        try:
            for i in range(len(studentList)):
                if(studentList[i].name == n): #이름 중복 
                    raise Exception
        except Exception:
            print("Already exits name!") 
            continue

        try:
            msFloat = float(ms)
            fsFloat = float(fs)
            msInt = int(msFloat)
            fsInt = int(fsFloat)
            if( float(msInt) < msFloat or float(fsInt) < fsFloat or ms < '0' or fs < '0' ): #음의 정수이거나 정수형 아닐때 
                raise Exception
        except Exception:
            print("Score is not positive integer!")
            continue
        else: 
            ms = int(ms)
            fs = int(fs)
            Menu1(n, ms, fs)


    elif choice == "2" :
        try:
            if (not studentList): #학생 정보 없으면 예외
                raise Exception
        except Exception:
            print("No Student Data!")
            continue
        else:
            Menu2()
            print("Grading to all students.")

    elif choice == "3" :
        try:
            if(not studentList): #학생 정보 없으면 예외
                raise Exception
        except Exception:
            print("No Student Data!")
            continue

        try:
            for i in range(len(studentList)): 
                if(studentList[i].grade == 'none'): #학생 grade가 'none'으로 저장되어있으면 예외 
                    raise Exception
        except Exception:
            print("There is a student who didn't get grade.")
            continue
        else:
            Menu3()

    elif choice == "4" :
        try:
            if(not studentList): #학생 정보 없으면 예외
                raise Exception
        except Exception:
            print("No Student Data!")
            continue
        
        nameToDelete = input("Enter the name to delete: ")
        count = 0
        for i in range(len(studentList)):
            if(nameToDelete == studentList[i].name):
                Menu4(nameToDelete)
                print("{} student information is deleted.".format(nameToDelete))
                break
            count = count + 1
            if count == len(studentList):
                print("Not exist name!")
                break
        continue

        
    elif choice == "5" :
        print("Exit the program!")
        break

    else:
        print("Wrong number. Choose again.")
        continue
