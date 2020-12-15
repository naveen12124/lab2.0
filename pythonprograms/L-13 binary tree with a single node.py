class TreeNode:

	def _init_(self,data):
		self.data = data
		self.left = None
		self.right = None

	def printhead(self):
		print(self.data)

treenode = TreeNode(35)
treenode.printhead()
