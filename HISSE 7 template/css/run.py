students=list()

def getDataFromUser():
    inputAd=input('Adinizi daxil edin : ')
    inputSoyad=input('Soyadiniz daxil edin :')
    return [inputAd,inputSoyad]

# Student classi yaratmaq

class Student():
    # name,surname property
    def __init__(self,ad,soyad):
        self.Name=ad
        self.Surname=soyad
    # showStudentData behaviour
    def showStudentData(self):
        # print(self.Name + ' | ' +self.Surname)
        return f'{self.Name} | {self.Surname}'
    
def createStudentAndAddToList():
    inputData=getDataFromUser()
    # students.append(Student(inputData[0],inputData[1]))

    stud=Student(inputData[0],inputData[1])
    students.append(stud)

for i in range(1,4):
    print(f'{i} -inci telebe melumatlarini daxil edin')
    createStudentAndAddToList() 
  
for student in students:
    print(student.showStudentData())