a=[]
b=[]
m=int(input("Enter No. Of Rows for Matrix"))
n=int(input("Enter No. Of Columns for Matrix"))
for i in range (m):
    c=[]
    for j in range (n):
        print ("Enter The Value at [",i,",",j,"] of the First Matrix",)
        x=int(input())
        c.append(x)
    a.append(c)
print (a)
for i in range (m):
    c=[]
    for j in range (n):
        print ("Enter The Value at [",i,",",j,"] Of the Second Matrix:",)
        x=int(input())
        c.append(x)
    b.append(c)
print (b)
bt=[]
for i in range (n):
    r=[]
    for j in range (m):
        k=b[j][i]
        r.append(k)
    bt.append(r)
s=[]
for i in range (m):
    c=[]
    for j in range(n):
        x=a[i][j]+bt[i][j]
        c.append(x)
    s.append(c)
print ()
print (a,"+",bt,"=",s)
