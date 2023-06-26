d={}
n=int(input("Enter the Number of key Items: "))
for i in range(n):
    k=input("Enter key name: ")
    v=eval(input("Enter value: "))
    d[k]=v
print (d)