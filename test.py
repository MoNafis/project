"""docstring."""

suit_list = ['x', 'c', 'd', 'h', 's']
rank_list = ['x', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q'
             '\n', 'K']
'''

list1 = ['8C', '9C', '2D', '7C', '3S']  # in this case use k as 12
high = 0
for i in list1:

    print(i, i[0])

    if int(i[0]) > high:
        high  = int(i[0])
        print(high)
'''

ranklist = ['A', 'J', 'Q', 'K']

list2 = ['10S', '8H', '2D']
high = 0
for i in list2:
    # print(i[0], i[1], "AND ME",i[0][0],"mME ")#how is i[0]the same as i[0][0]

    print(i[0], "HERE", i)

    if len(i) > 2:

        if int(i[0] + i[1]) > high:

            high = int(i[0] + i[1])
            print(high)

    elif len(i) == 2:

        if int(i[0]) > high:

            high = int(i[0])
            print(high, "this is the final high")
    else:
        print("invalid card , as it cannot have a length of less than 2")

    '''
    if i[0] > high:
        high = int(i[0])
print(high)
'''
# for j in i
# print(j)
