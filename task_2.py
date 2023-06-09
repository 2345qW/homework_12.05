def para (a,b):
    list_1 =[]
    for i in range(a,b):
        if i % 2 ==0 :
            list_1.append(i)
    return list_1
print(para(8,50))
