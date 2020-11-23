def balance(s):
	stack = []
	opens = "{[("
	close = "}])"
	balanced = True
	i = 0
	while i<len(s) and balanced:
		char = s[i]
		if char in opens: stack.append(char)
		else:
			if stack==[]: balanced = False
			else:
				check = stack.pop()
				if opens.index(check)!=close.index(char): balanced = False
		i+=1
	if stack==[] and balanced: print("They are balanced")
	else: print("They are not balanced")

# Taking Input
s = input("Enter a string of paranthesis : ")
balance(s)
