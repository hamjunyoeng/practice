class python_LIST: 
  def __init__(self): 
    self.running = True
    self.addrList = ["www.hufs.ac.kr"] # 초기 사이트 주소 설정
    self.visitList = ["www.hufs.ac.kr"] # go로 방문한 주소 리스트
    self.nowSite = 0 # 현재 방문 주소의 인덱스
    print(self.addrList[self.nowSite]) # 현재 방문 주소를 출력
  
  def go(self,addr):
    if self.nowSite != len(self.addrList)-1: # 현재 방문 사이트 주소가 리스트 중간에 있을 때
      self.nowSite += 1 # 현재 방문 사이트 주소 다음 인덱스에
      for i in range(self.nowSite, len(self.addrList)): #이후에 있는 방문 사이트 주소들은
        del self.addrList[self.nowSite] # 반복문으로 삭제
      self.addrList.append(addr) # addr을 추가하고 출력한다.
      self.visitList.append(addr) # addr을 방문 주소 리스트에 추가
      print(self.addrList[self.nowSite])
    else: # 방문 사이트 주소가 리스트 마지막일 때
      self.addrList.append(addr) # addrList의 현재 방문 사이트 주소 다음에 addr을 추가
      self.visitList.append(addr) # addr을 방문 주소 리스트에 추가
      self.nowSite += 1  # 현재 방문 주소의 인덱스를
      print(self.addrList[self.nowSite]) # addr로 변경하고 출력한다

  def forward(self):
    if self.nowSite == len(self.addrList) - 1: # 다음 주소가 없는 경우
      return None # 출력결과는 없다
    else:
      self.nowSite += 1 # 현재 방문 주소의 인덱스를 다음 방문 주소로 변경
      print(self.addrList[self.nowSite]) # 현재 방문 주소 출력
  
  def backward(self):
    if self.nowSite == 0: #이전 주소가 없는 경우
      return None #출력결과는 없다
    else:
      self.nowSite -= 1 # 현재 방문 주소의 인덱스를 이전 방문 주소로 변경
      print(self.addrList[self.nowSite]) # 현재 방문 주소 출력
  
  def history(self):
    self.historyList=[] # self.addrList 의 중복된 주소를 제거하고 담을 리스트, 순서 때문에 set 사용x
    for i in range(len(self.visitList)-1,-1,-1): # self.visitList의 끝에서 부터
      x=self.visitList[i] # x는 self.visitList[-1]부터 self.visitList[0]까지 거꾸로
      if x not in self.historyList: # 중복을 제거
        self.historyList.append(x) # self.historyList에 방문 주소를 차례대로 append
    for i in self.historyList:
      print(i)
  
  def quit(self):
    self.running=False

item = python_LIST() # 객체 생성
while(item.running): # quit함수 입력 전까지 반복
  a=list(input().split()) # 입력받음
  if a[0]=='go': # go 주소를 입력 받으면 실행
    item.go(a[1]) # go를 제외한 주소 부분만 함수에 입력
  elif a[0]=='backward': # backward 실행
    item.backward()
  elif a[0]=='forward': # forward 실행
    item.forward()
  elif a[0]=='history': # history 실행
    item.history()
  elif a[0]=='quit': # quit 실행
    item.quit()
  else:
    continue
