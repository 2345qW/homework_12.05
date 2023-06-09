
def nun_num(num1,num2):
    if num1 > num2:num1,num2 = num2,num1
    fin_nam=1
    for i in range(num1,num2+1):
        fin_nam=fin_nam * i
    return fin_nam
print(nun_num(5,2))