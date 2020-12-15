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

    # Itearative Function
    def solve(self, root):
        if root is None: return True
        q = deque()
        q.append(root)
        c = 1
        while c>0:
            ld = 0
            rd = 0
            node = q.popleft()
            c-=1
            if node.left:
                q.append(node.left)
                c+=1
                ld = self.height(node.left)
            if node.right:
                q.append(node.right)
                c+=1
                rd = self.height(node.right)
            if abs(ld-rd)>0: return False
        return True

    # Recursive Function
    def height(self,root):
        if not root: return 0
        return 1 + max(self.height(root.right),self.height(root.left))


tree = BinaryTree(1)
n = int(input("Enter the number of extra nodes of the tree: "))
for i in range(n):
    n = int(input("Enter the value of the node you want to add : "))
    tree.insert(n)
print(tree.solve(tree.root))
