# Chocolate Fest , HackerRank Algorithm Challenge.
n = int(input("enter the amount of money\n"))
c = int(input("enter the price of 1 chocolate\n"))
m = int(input("the number of wrappers he can turn in for a free bar\n"))

def choco_fest(n,c,m):
	total_choco = 0
	# c_initial is the inital no of chocolate bought from the money he/she has
	c_initial = n // c 
	# perks variable keep the number of free chocolate bought from the left over wrappers
	perks = c_initial // m
	total_choco += perks
	# rem is the remaining wrappers after exchanging for free chocos
	rem = c_initial % m
	#Note: left variable is assigned with an arbitary value to set the loop in motion
	left = 1

			
	while left != 0:
		left = (perks + rem) // m
		total_choco += left
		rem = (perks + rem) % m
		perks = left
	total_choco += c_initial
	return total_choco
print(choco_fest(n,c,m))
