class Queue:
    def  __init__(self,n):
      self.items = [None]*n #queue의 크기는 n
      self.front = -1
      self.rear =-1
      self.size = 0

    def isEmpty(self):
      return self.size == 0

    def enqueue(self, e):
      if self.size == len(self.items):
        print("Queue is full")
        self.resize(2*len(self.items))
      else:
        self.rear = (self.rear+1)%(len(self.items))    
        self.items[self.rear] = e
        self.size += 1
    
    def dequeue(self):
      if self.isEmpty():
        print("Queue is empty")
      else:        
        self.front = (self.front+1)%(len(self.items))
        e = self.items[self.front]
        self.size -= 1
        return e
      
    def resize(self, cap):
      olditems = self.items
      self.items = [None]*cap
      walk = self.front
      for k in range(self.size):
        self.items[k] = olditems[walk]
        walk = (walk + 1)% len(olditems)
      self.front = -1
      self.rear = self.size - 1

n=int(input()) #입력받을 사람 수 = queue의 크기
sum_time=0 #총 대기시간
store_time=0 #저장된 대기시간      

A=Queue(n) #도착시간
B=Queue(n) #심사시간

for i in range(n): #q에 도착시간과 심사시간을 n번 입력한다
  a,b=map(int,input().split())
  A.enqueue(a)
  B.enqueue(b)

Atime=A.dequeue() #1번째 사람은 기다리지 않는다.

for i in range(1,n):
  Atime=int(A.dequeue()) # 2,3,4,5,...n  의 도착시간
  Btime=int(B.dequeue()) # 1,2,3,4,...n-1의 심사시간 , n번째 사람의 심사시간은 기다리는 평균시간에 포함하지 않는다
  
  if (store_time+Btime-Atime)>=0:
    sum_time+=store_time+Btime-Atime
    store_time=store_time+Btime-Atime
  else:
    store_time=0

result=sum_time/n
print(format(result,".2f"))


