def bubble_sort(list):
    temp =[]
    for i in range(len(list)-1, 0, -1):
        for idx in range(i):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list=[4,1,6,2,9,7]
bubble_sort(list)
print(list)