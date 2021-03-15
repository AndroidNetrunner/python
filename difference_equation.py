i = 2
n_minus_one = 50
n_minus_two = 100
n = 0.5 * n_minus_one + 0.01 * n_minus_two
print("time: 0 h, population: 100.00")
print("time: 1 h, population: 50.00")
while n > 5:
	print("time: {} h, population: {:.2f}".format(i,n))
	n_minus_two = n_minus_one
	n_minus_one = n
	n = 0.5 * n_minus_one + 0.01 * n_minus_two
	i += 1
print("time: {} h, population: {:.2f}".format(i,n))
print("The target population is reached after {} hours".format(i))
