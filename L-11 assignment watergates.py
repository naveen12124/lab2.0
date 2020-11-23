def balance(s):
	stack = []
	balanced = True
	i = 0
	c = 0
	while i<len(s) and balanced:
		char = s[i]
		if char == '(' : stack.append(char)
		else:
			if stack==[]: balanced = False
			else:
				stack.pop()
				c+=1
		i+=1
	if stack==[] and balanced: print(c)
	else: print(-1)

# Taking Input
s = input("Enter the water gates : ")
balance(s)
