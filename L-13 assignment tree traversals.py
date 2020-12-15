class Node:
    def _init_(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def _init_(self,root):
        self.root = Node(root)

    def insert(self,val):
    	node = Node(val)
    	q = [self.root]
    	while len(q)!=0:
    		n = q.pop(0)
    		if n.left == None:
    			n.left = node
    			break
    		else: q.append(n.left)
    		if n.right == None:
    			n.right = node
    			break
    		else: q.append(n.right)

    def preorder(self,start,traversal):
        if start:
            traversal += str(start.value)+"-"
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal 
    
    def inorder(self,sta…
