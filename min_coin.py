# Authors: Dilton D'souza & Nigel Fernandes

# A Dynamic Programming based Python program to
# find minimum of coins to make a given change V

import sys

# m is size of coins array (number of distinct coins)
def minCoins(coins, m, V):
	
	# table[i] will be storing the minimum
	# number of coins required for i value.
	# table[V] will have result
	table = [0 for i in range(V + 1)]

	# Base case (If given value V is 0)
	table[0] = 0

	# Initialize all table values as Infinite
	for i in range(1, V + 1):
		table[i] = sys.maxsize

	# Compute minimum coins required
	# for all values from 1 to V
	for i in range(1, V + 1):
		
		# Go through all coins smaller than i
		for j in range(m):
			if (coins[j] <= i):
				sub_res = table[i - coins[j]]
				if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
					table[i] = sub_res + 1
	
	if table[V] == sys.maxsize:
		return -1
	
	return table[V]

coins = [9, 5, 2, 1]
m = len(coins)
V = int(input(">> Minimum Coin change Program\n\n>> Enter value: "))
print(" Minimum coins required: ", minCoins(coins, m, V))
