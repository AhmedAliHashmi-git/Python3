def twoSum(list , target):
    p = 0
    q = 1

    list2 = {}
    check = True
    for i in range(0 , len(list)):
        if(list[p] + list[q] == target):
            list2[0] = list[i]
            list2[1] = list[i]
            check = False
    if(not check):
        for i in range(len(list2)):
            print(i)
    else:
        print("List is Empty")
            




list = [0,2,1,4,5]
twoSum(list , 3)
