# This is the solution of the HackerRank's Algorithm section challenge "HackerLand Radio Transmitters. The question is  " Hackerland is a one-dimensional city with houses aligned at integral locations along a road. The Mayor wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a fixed range meaning it can transmit a signal to all houses within that number of units distance away. Given a map of Hackerland and the transmission range, determine the minimum number of transmitters so that every house is within range of at least one transmitter. Each transmitter must be installed on top of an existing "


def min_transmitter(a, b):
	min_transmitter = 0
	a.sort()
	c = len(a)
	lastH = a[c - 1] #the number of the last house .
	range = 2 * b + 1 #the total number of houses covered by the antenna.
	
	div = lastH // range
	if lastH % range > 0:
		min_transmitter = div + 1
	else:
		min_transmitter = div
	return min_transmitter

a = [7, 2, 4, 6, 5, 9, 2, 11] #house numbers of the Hackerland city that needed to be covered my antenna.

b = 2         #range of an single antenna

print(min_transmitter(a, b)) #feel free to input your own parameters and play around.
