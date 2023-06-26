def countdown(x):
    if x==0:
        return
    else:
        print x
        countdown(x-1)
n=input("Enter The Starting")
countdown(n)
