def num_min (num1,num2,num3,num4,num5):
    li=[num1,num2,num3,num4,num5]
    min=li[0]
    for i in range(5):
        if li[i] < min:
            min=li[i]
    return min
print(num_min(10,13,4,112,-3,))