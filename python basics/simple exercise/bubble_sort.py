num1=0
temp=0
arrnum = [7, 4, 1, 3, 8, 6]
for num1 in range(6):
    for num1 in range(5):
        if arrnum[num1]>arrnum[num1+1]:
            temp=arrnum[num1]
            arrnum[num1]=arrnum[num1+1]
            arrnum[num1+1]=temp
            
for num1 in range(6):
    print(arrnum[num1])
