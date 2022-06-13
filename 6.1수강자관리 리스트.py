class Student:
    def __init__(self, st_no=None, name=None):
        self.st_no = st_no # 학번
        self.name = name # 이름

class Course:    # 수업
    def __init__(self):
        self.st_list = [] # 수강자들을 파이썬 리스트로 구현
        self.running = True
        
    def register(self, st_no, name): # 수강 신청
        s = Student()
        s.st_no = st_no 
        s.name = name 
        self.st_list.append(s) # st_list 에 학생(학번,이름) 추가
        
    def withdraw(self, st_no): # 수강 취소
        for i in range(len(self.st_list)): 
            k = self.st_list[i] # 리스트 i번째에 있는 Student 클래스
            if k.st_no == st_no: # k의 학번이 입력한 학번과 같다면
                self.st_list.remove(k) # 리스트에서 k를 삭제
                break
        
    def data(self, st_no): # 정보 출력
        for i in range(len(self.st_list)):
            k = self.st_list[i] # 리스트 i번째에 있는 Student 클래스
            if k.st_no == st_no: # k의 학번이 입력한 학번과 같다면
                print(k.st_no, k.name, end=' ')
                print()
                break
    
    def all_data(self): # 모든 정보 출력
        print(len(self.st_list))
        self.st_list.sort(key = lambda student: student.st_no) # 리스트 객체 중 학번을 오름차순으로 정렬
        for i in range(len(self.st_list)):
            k = self.st_list[i] # 리스트 i번째에 있는 Student 클래스
            print(k.st_no, k.name, end=' ')
            print()
    
    def quit(self): # 끝내기
        self.running = False

c=Course()
while(c.running):
    command = input().split()
    if command[0] == 'N': # 학번 st_no인 학생이 수강 신청
        c.register(command[1],command[2])
    elif command[0] == 'C': # 학번 st_no인 학생이 수강 취소
        c.withdraw(command[1])
    elif command[0] == 'R': # 학번 st_no인 학생의 정보 출력
        c.data(command[1])
    elif command[0] == 'P': # 수강 학생들의 수와 정보를 출력
        c.all_data()
    elif command[0] == 'Q': # 끝내기
        c.quit()
    else:
        continue

