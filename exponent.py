def exponent(num, power=2):
	"""exponent(num, power) raises num to specified power. Power defaults to 2."""
	return num ** power

print(exponent(2,3)) #8
print(exponent(3)) #9
print(exponent(7)) #49

print(exponent(power=3, num=4))
print(exponent(num=4, power=3))