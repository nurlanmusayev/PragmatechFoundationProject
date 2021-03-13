a=input("Ededi daxil edin :")

for i in range(len(a)):
    if a[i]=='.':
        dot_index=i
        break

x=int(a[: dot_index])
y=x+1
print(x*y)