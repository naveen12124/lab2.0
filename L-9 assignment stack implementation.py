class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,data,n):
        if data not in self.stack and len(self.stack)<n:
            self.stack.append(data)
            return
        print("OverFlow")
        return
    def pop(self):
        if len(self.stack)>0:
            l=self.stack[-1]
            self.stack.pop()
            return l
        print("Underflow")
        return
    def peek(self):
        if len(self.stack)>0:
            return self.stack[-1]
        return
    def popelement(self,data):
        if data in self.stack:
            self.stack.remove(data)
            return
        print("Element not found")
        return
    def printStack(self):
        for i in self.stack:
            print(i,end=" ")
        return
n=int(input("Enter size of stack "))
s=Stack()
for i in range(n+1):
    s.push(int(input()),n)
print("pop",s.pop())
print("pop",s.pop())
print("pop",s.pop())
print("peek",s.peek())
k=int(input("enter element you want to delete "))
s.popelement(k)
s.printStack()
