class Student:
    def __init__(self, st_no = None, name = None, dept = None, grade = None, score = None):
        self.st_no = st_no # 학번(문자열)
        self.name = name # 이름(문자열)
        self.dept = dept # 학과(문자열)
        self.grade = grade # 학년(양의 정수)
        self.score = score # 성적
        

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class Course:
    def __init__(self):
        self.root = None
        self.running = True
    def register(self, st_no, name, dept, grade): # 수강신청
        s = Student()
        s.st_no = st_no 
        s.name = name
        s.dept = dept
        s.grade = grade
        self.insert(st_no, s) # key가 학번이고 value가 Student의 객체인 노드를 이진 탐색트리에 삽입
    
    def fix_grade(self, st_no, grade): # 학생의 성적 수정
        s = self.search(st_no)
        s.grade = grade
    
    def withdraw(self, st_no): # 수강취소
        self.delete(st_no)
        
    def data(self, st_no): # 조회
        s = self.search(st_no)
        print(s.st_no, s.name, s.dept, s.grade)
        
    def dept_data(self, dept): # 학과 학생들 정보 출력
        self.dept_count = 0
        self.subtreeInorder_dept_count(self.root,dept)
        print(self.dept_count)
        self.subtreeInorder_dept(self.root,dept)
    
    def all_data(self): # 모든 정보 출력
        print(self.size())
        self.subtreeInorder(self.root)
    
    def subtreeInorder(self,p): # key를 오름차순으로 방문하며 출력
        if p is not None:
            self.subtreeInorder(p.left)
            s = p.value
            if s.score == None:
                print(s.st_no, s.name, s.dept, s.grade)
            else:
                print(s.st_no, s.name, s.dept, s.grade, s.score)
            self.subtreeInorder(p.right)
    
    def subtreeInorder_dept(self,p,dept): # key를 오름차순으로 방문하며 학과 학생들 정보출력
        if p is not None:
            self.subtreeInorder_dept(p.left,dept)
            s = p.value
            if s.dept == dept:
                if s.score == None:
                    print(s.st_no, s.name, s.dept, s.grade)
                else:
                    print(s.st_no, s.name, s.dept, s.grade, s.score)
            self.subtreeInorder_dept(p.right,dept)
            
    def subtreeInorder_dept_count(self,p,dept): # 학과 학생들 숫자 출력
        if p is not None:
            self.subtreeInorder_dept_count(p.left,dept)
            s = p.value
            if s.dept == dept:
                self.dept_count += 1
            self.subtreeInorder_dept_count(p.right,dept)
    
    def minNode(self,node): # 가장 작은 key를 갖는 노드
        if node.left == None:
            return node
        else:
            return self.minNode(node.left)
        
    def insert(self, key, value): # 이진탐색트리 삽입 연산
        self.root = self.insertSubtree(self.root, key, value)
    
    def insertSubtree(self, node, key, value):
        if node == None:
            return Node(key, value)
        elif key < node.key:
            node.left = self.insertSubtree(node.left, key, value)
        elif key > node.key:
            node.right = self.insertSubtree(node.right, key, value)
        else:
            pass
        return node
    
    def search(self, key): # 이진탐색트리 탐색 연산
        return self.searchSubtree(self.root, key)

    def searchSubtree(self, node, key):
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self.searchSubtree(node.left, key)
        else:
            return self.searchSubtree(node.right, key)
    
    def delete(self, key): # 이진트리 삭제 연산
        self.root = self._deleteNode(self.root, key)

    def _deleteNode(self,node,key):
        if node == None:
            return None
        if key < node.key:    # 삭제할 키의 노드가 node의 왼쪽 부트리인 경우
            node.left = self._deleteNode(node.left, key)
            return node
        elif key > node.key:  # 삭제할 키의 노드가 node의 오른쪽 부트리인 경우
            node.right = self._deleteNode(node.right, key)
            return node
        else:                     # node가 삭제할 키의 노드인 경우
            if node.right == None:  # node의 오른쪽 자식노드가 없을 경우
                return node.left
            if node.left == None:    # node의 왼쪽 자식노드가 없을 경우
                return node.right
            
            rightMinNode = self.minNode(node.right)  # node의 오른쪽 부트리에서 최소키의 노드를 찾음
            node.key = rightMinNode.key                   # node의 오른쪽 부트리에서 최소키의 노드를 복사 node에 복사
            node.value = rightMinNode.value
            node.right = self._deleteNode(node.right, rightMinNode.key)   # node의 오른쪽 부트리에서 최소키의 노드를 삭제        
            return node

    def size(self): # 노드의 개수
        return self.subtreeSize(self.root)
    
    def subtreeSize(self, p):
        if p is None:
            return 0
        else:
            return 1 + self.subtreeSize(p.left) + self.subtreeSize(p.right)

    def quit(self): # 끝내기
        self.running = False

c=Course()
while(c.running):
    command = input().split()
    if command[0] == 'N': # 학번 st_no인 학생이 수강 신청
        c.register(command[1],command[2],command[3],command[4])
    elif command[0] == 'G': # 학번 st_no인 학생의 성적을 수정
        c.fix_grade(command[1],command[2])
    elif command[0] == 'C': # 학번 st_no인 학생이 수강 취소
        c.withdraw(command[1])
    elif command[0] == 'R': # 학번 st_no인 학생의 정보 출력
        c.data(command[1])
    elif command[0] == 'D': # 학과의 학생들의 정보를 출력
        c.dept_data(command[1])
    elif command[0] == 'P': # 수강 학생들의 수와 정보를 출력
        c.all_data()
    elif command[0] == 'Q': # 끝내기
        c.quit()
    else:
        continue