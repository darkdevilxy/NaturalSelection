def getFixedInput(a, b, money):
	traits = ['speed', 'sense', 'wisdom', 'size']
	mi = a
	mx = b
	mn = money
	perks = []
	
	for i in traits:
		mx = max(min(mx, money//2+1), mi)
		a = input(f"Enter a number between {mi} and {mx} for {i}:\n")
		while not(int(a)>=mi and int(a)<=mx):
			print('Invalid input')
			a = input(f"Enter a number between {mi} and {mx} for {traits[0]}:\n")
		perks.append(int(a))
		money -= int(a)
	return perks
	

