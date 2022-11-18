# total = 0

# def increment():
# 	total += 1
# 	return total

# increment() # Error!

total = 0

def increment():
	global total
	total += 1
	return total

print(increment())
