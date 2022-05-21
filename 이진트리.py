class TNode: 
  def __init__(self, data, left=None, right = None):
    self.data = data
    self.left = left
    self.right = right

class BinaryTree:
  def __init__(self):
    self.root = None
  
  def inorder(self):
    self._inorderSubtree(self.root)
    
  def _inorderSubtree(self, node):
    if node is not None:
      self._inorderSubtree(node.left)
      print(node.data, end = ' ')
      self._inorderSubtree(node.right)
  
  def preorder(self):
    self._preorderSubtree(self.root)
  
  def _preorderSubtree(self, node):
    if node is not None:
      print(node.data, end = ' ')
      self._preorderSubtree(node.left)
      self._preorderSubtree(node.right)
  
  def _postorderSubtree(self, node):
    if node is not None:
      self._postorderSubtree(node.left)
      self._postorderSubtree(node.right)
      print(node.data, end = ' ')
   
     
