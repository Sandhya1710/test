def sum(n):
	if n==1:
		return 1
	else:
		return n+sum(n-1)

n=int(input("Enter the number: "))
print(f"the sum of first {n} numbers is {sum(n)}")
