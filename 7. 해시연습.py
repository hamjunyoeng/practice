#학생의 학번은 key, 이름은 value로 해싱
class Course:
    def __init__(self):
        self.M = 13 # 테이블 크기
        self.keyList = [None] * 13 # 학번 저장 리스트
        self.valueList = [None] * 13 # 이름 저장 리스트
        self.N = 0 # 저장된 항목 수
        self.running = True
        

    def R(self): # M 보다 작은 소수 R
        x=1
        for i in range(1,self.M):
            a = 0
            for j in range(1,i):
                if i % j == 0:
                    a += 1
            if a == 1: # i가 소수면
                x = i
        return x # slef.M 보다 작은 소수 return 

    def hashFunc1(self,key): # 키를 해시테이블의 인덱스로 변환
        return key % self.M
    
    def hashFunc2(self,key): # 충돌 발생시 점프크기 정하는 함수
        ##############################################################
        return self.R() - (key % self.R()) # 충돌발생시 무한루프 도는 error
        
    
    def register(self,key,value): # 수강 신청
        initialPos = self.hashFunc1(key)
        i = initialPos
        j=0
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            if self.keyList[i] == key:
                self.valueList[i] = value
                return 
            j += 1
            i = (initialPos + j*self.hashFunc2(key)) % self.M # self.hashFunc2에 j를 곰하지 않으면 무한루프
            if self.N > self.M: # 해시테이블이 꽉 차면
                break
    
    def data(self,key): # 학생의 정보 출력
        initialPos = self.hashFunc1(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                print(self.keyList[i], self.valueList[i])
            j += 1
            i = (initialPos + j*self.hashFunc2(key)) % self.M # self.hashFunc2에 j를 곰하지 않으면 무한루프
        return None # key가 해시테이블에 없을 때
    
    def withdraw(self,key): #수강 취소
        initialPos = self.hashFunc1(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                self.keyList[i] = None
                self.valueList[i] = None
            j += 1
            i = (initialPos + j*self.hashFunc2(key)) % self.M # self.hashFunc2에 j를 곰하지 않으면 무한루프
        return None
    
    def all_data(self): # 수강 학생들의 수와 학생들의 정보를 오름차순으로 출력
        deleteNoneList = filter(None,self.keyList) # keyList에서 None을 제거
        sortedList = sorted(deleteNoneList) # None을 제거한 리스트를 오름차순 정렬 
        print(len(sortedList))
        for i in range(len(sortedList)): # 정렬된 keyList를 data 함수로 출력
            self.data(sortedList[i])
    
    def quit(self):
        self.running = False
        
c=Course()
while(c.running):
    command = input().split()
    if command[0] == 'N': # 학번 st_no인 학생이 수강 신청
        c.register(int(command[1]),command[2])
    elif command[0] == 'C': # 학번 st_no인 학생이 수강 취소
        c.withdraw(int(command[1]))
    elif command[0] == 'R': # 학번 st_no인 학생의 정보 출력
        c.data(int(command[1]))
    elif command[0] == 'P': # 수강 학생들의 수와 정보를 출력
        c.all_data()
    elif command[0] == 'Q': # 끝내기
        c.quit()
    else:
        continue

