from time import sleep
n=int(input("Enter The Limit:"))
j=0
k=1
print(j+"")
print(k)
while True:
    temp=k
    k=k+j
    j=temp
    sleep(1)
    if k>n:
        break
    print(k)
print("Iteration Completed:")
