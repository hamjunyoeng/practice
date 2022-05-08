class Node:
  def __init__(self,element):
    self.data=element
    self.link=None

class LinkedStack: #연결 구조를 이용해 스택을 구현
  def __init__(self):
    self.top=None
  
  def isEmpty(self):
    return self.top == None
  
  def push(self,e):
    newNode = Node(e)
    newNode.link=self.top
    self.top=newNode
  
  def pop(self):
    if (self.isEmpty()):
      return False #스택이 비어있으면 False 출력
    e=self.top.data
    self.top=self.top.link
    return e
  
  def peek(self):
    e=self.top.data
    return e

def evalPostfix(expr): #postfix 계산 함수
  s=LinkedStack() #스택 객체 생성
  for token in expr: #모든 linked data에 대해
    if token in "+-*/%//": #항목이 연산자이면
      val2=s.pop() #피연산자2
      val1=s.pop() #피연산자1
      if val1==False or val2==False: #후위 표기 수식의 오류 검사
        return False #피연산자가 비어있을 시 false 출력
      if(token=='+'): s.push(val1+val2) #각 연산을 수행하고
      elif(token=='-'): s.push(val1-val2) #결과는 스택에 다시저장
      elif(token=='*'): s.push(val1*val2)
      elif(token=='/'): s.push(val1/val2)
      elif(token=='%'): s.push(val1%val2)
      elif(token=='//'): s.push(val1//val2)
    elif token == ';':
      return s.pop() #;가 나오면 결과를 반환한다
    else: #data가 피연산자이면
      s.push(float(token)) #실수로 변경해서 스택에 저장
  if s.isEmpty() == False:
    return False

postfix=input().split()
result=evalPostfix(postfix)
if result: #후위 표기 수식에 오류가 없을 때
  print(int(result))
else:#후위 표기 수식에 오류가 있을 때
  print('error')