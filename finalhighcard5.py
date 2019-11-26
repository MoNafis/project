rank_list = ['x','A','2','3','4','5','6','7','8','9','10','J','Q','K']

playerlist1 = ['QS', 'JD', 'KH', '10C', '2S']
playerlist2 = ['AD', '7S', '9C', '2C', 'KS']
relist = []

for i in playerlist1:
    b = i[0]

    if b == '1':
        c = i
        relist += [c]
        # print(relist, "LETS SEE C yay 10 got added")
    else:
        for j in rank_list:

            if b == j:

                index = rank_list.index(b)
                index = str(index)

                string = ""
                string += i

                newstring = string.replace(b, index)
                # print(newstring)
                relist += [newstring]

print(playerlist1, "original list")
print(relist, "upgraded list")

high = 0
for i in relist:
    # print(i[0], i[1], "AND ME",i[0][0],"mME ")#how is i[0]the same as i[0][0]

    # print(i[0], "HERE", i)

    if len(i) > 2:

        if int(i[0] + i[1]) > high:

            high = int(i[0] + i[1])
            print(high)

    elif len(i) == 2:

        if int(i[0]) > high:

            high = int(i[0])
            print(high)
    else:
        print("invalid card , as it cannot have a length of less than 2")

print(high, "this is the highest card")
