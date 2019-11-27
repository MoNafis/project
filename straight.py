import sys

"""this is the straight function."""

rank_list = ['x', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

playerlist1 = ['QS', 'JD', '8H', '10C', '9S']
playerlist2 = ['AS', '5D', '6C', '8H', '7S']
print(playerlist1, "this is the players hand")
# PART 1
index_list = []
for i in playerlist1:

    b = i[0]

    if b == '1':
        index = 10

    else:
        index = rank_list.index(b)
    index_list += [index]
    # print(index)
print(index_list, "this is the index list")


# PART 2 Sorting the list
A = index_list
for i in range(len(A)):

	min_index = i

	for j in range(i + 1, len(A)):
		if A[min_index] > A[j]:

			min_index = j
	A[i], A[min_index] = A[min_index], A[i]

print(A, "this is the sorted index list")

if A[-1] - A[0] == 4:
    print(playerlist1, "this is a straight hand")
else:
    print(playerlist1, "this is not a straight hand")
    # print("as the difference is not 4,", "its: ", A[-1] - A[0])

'''
IGNORE THIS FOR NOW 
# PART 3 Finding the difference
diff_list = [A[i + 1] - A[i] for i in range(len(A) - 1)]
print(diff_list, "this is the difference list")

B = diff_list
print(B[0], B[1], B[2], B[3])
if B[0] and B[1] and B[2] and B[3] == 1 or B[-1] - B[0] == 1:
	print(playerlist1, "this is a straight hand")  # (and return True)
else:
	print(playerlist1, "is not a straight hand")
'''