string = input('Введите строку, содержащую информацию о количестве ягод на каждом кусте через пробел: ') #2 5 6 7 9 5 6
a = string.split()
for i in range(len(a)):
    a[i] = int(a[i])
res = 0
max_res=res
for i in range(len(a)-2):
    res = a[i]+a[i+1]+a[i+2]
    if res>=max_res:
        max_res = res
print(max_res) #22