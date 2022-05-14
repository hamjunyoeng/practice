class dList:
  class Node: # 이중연결리스트 노드
    def __init__(self,data,back=None,next=None):
        self.data = data
        self.next = next
        self.back = back

  def __init__(self): # 이중연결리스트 초기화
    self.head = self.Node(None)
    self.tail = self.Node(None, self.head)
    self.head.next = self.tail
    self.size = 0

  def size(self): # 리스트의 사이즈
    return self.size
  
  def is_Empty(self): # 리스트가 비어있는가
    return self.size == 0
  
  def getNode(self,pos): # pos번째 노드 반환
    if pos<0: return None
    node=self.head.next # node는 head 앞 노드부터 시작
    while pos>0 and node != self.tail: # pos가 0이상, node가 끝에 도달하기 전까지 반복
      node = node.next
      pos -= 1
      return node
  
  def getData(self,pos): # pos번째 노드의 데이터 반환
    node= self.getNode(pos)
    if node == None : return None
    else: return node.data
  
  def insert_after(self,location,data): # location 뒤에 새 노드 삽입
    oldNode = location.next # location이 가리키고 있던 노드
    newNode = self.Node(data,location,oldNode) # 삽입할 새로운 노드
    location.next = newNode # location의 앞에 새로운 노드
    oldNode.back = newNode # locatino이 가리키고 있던 노드 뒤에 새로운 노드
    self.size += 1
    
  def insert_before(self,location,data): # location 앞에 새 노드 삽입
    oldNode = location.back # location이 가리키고 있던 노드
    newNode = self.Node(data,oldNode,location) # 삽입할 새로운 노드
    location.back = newNode # location의 뒤에 새로운 노드
    oldNode.next = newNode # locatino이 가리키고 있던 노드 앞에 새로운 노드
    self.size += 1
  
  def insert(self,pos,data): # pos번째 위치에 새 노드 삽입
    if pos < 0 or pos > self.size()+1:
      return None
    before = self.getNode(pos-1) # before 노드 찾음
    after = before.next # before 이 가리키고 있던 노드
    newNode = self.Node(data,before,after) # 삽입할 새로운 노드
    before.next = newNode # location의 앞에 새로운 노드
    after.back = newNode # locatino이 가리키고 있던 노드 뒤에 새로운 노드
    self.size += 1

  def delete(self, node):
    oldBackNode = node.back
    oldNextNode = node.next
    oldBackNode.next = oldNextNode
    oldNextNode.back = oldBackNode
    self.size -= 1
  
  def print_list(self):
    if self.is_Empty():
      print('리스트가 비어있음')
    else:
      p = self.head.next
      while p != self.tail:
        print(p.data)
        p = p.next


class List:
  def __init__(self):
    self.running = True # True면 동작
    self.addrList = dList()  # 초기 사이트 주소 설정
    self.visitList = dList() # go로 방문한 주소 리스트
    self.addrList.insert_after(self.addrList.head,'www.hufs.ac.kr')
    self.visitList.insert_after(self.addrList.head,'www.hufs.ac.kr')
    self.nowSite = 1 # 현재 방문 주소의 인덱스
    
  def go(self, addr):
    if self.nowSite != self.addrList.size:
      self.nowSite += 1 # 현재 방문 사이트 주소 다음 인덱스
      self.addrList.insert(self.nowSite,addr) # 중간에 삽입
      self.visitList.insert_before(self.visitList.tail,addr) # 방문 기록은 뒤에 삽입
      n = self.addrList.getNode(self.nowSite) # 삽입한 노드
      while n.next != self.addrList.tail: # 삽입한 노드 다음 노드가 tail일 때 까지 반복
        self.addrList.delete(n.next) # 삽입한 노드와 tail 사이의 노드 삭제
      print(self.addrList.getData(self.nowSite)) # 현재 방문 주소 출력
    else: # 방문 사이트 주소가 리스트 마지막 일 때
      self.addrList.insert_before(self.addrList.tail,addr) # addrList의 현재 방문 사이트 주소 다음에 addr을 추가
      self.visitList.insert_before(self.visitList.tail,addr) # addr을 방문 주소 리스트에 추가
      self.nowSite += 1 # 현재 방문 주소의 인덱스를 addr로 변경
      print(self.addrList.getData(self.nowSite)) # 현재 방문 주소 출력
    
  def forward(self):
    if self.nowSite == self.addrList.size:
      return None
    else:
      self.nowSite += 1 # 현재 방문 주소의 인덱스를 다음 방문 주소로 변경
      print(self.addrList.getData(self.nowSite)) # 현재 방문 주소 출력
    
  def backward(self):
    if self.nowSite == 1: # 이전 주소가 없는 경우 (www.hufs.ac.kr이 최초의 주소)
      return None
    else:
      self.nowSite -= 1 # 현재 방문 주소의 인덱스를 이전 방문 주소로 변경
      print(self.addrList.getData(self.nowSite)) # 현재 방문 주소 출력
    
  def history(self):
    self.historyList=[] # self.addrList 의 중복된 주소를 제거하고 담을 리스트, 순서 때문에 set 사용x
    for i in range(self.visitList.size()-1,-1,-1): # self.visitList의 끝에서 부터
      x = self.visitList.getData(i) # x는 self.visitList 끝 노드부터 self.visitList 첫 노드까지 거꾸로
      if x not in self.historyList: # 중복을 제거
        self.historyList.append(x) # # self.historyList에 방문 주소를 차례대로 append
    for i in self.historyList:
      print(i)
    
  def quit(self):
    self.running = False

item = List() # 객체 생성
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
