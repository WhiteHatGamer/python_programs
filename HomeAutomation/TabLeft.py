print("############## TebLeft Tablet Calculator ##############")
p=int(input("Enter Day Left: "))
n=int(input("Enter Number of Tablets: "))
Tab=[]
l=[]
t=[]
TabLeft=[["Tablet Name","Tab Required"]]
for i in range(0,int(n)):
    temp=input(f"Enter Tablet Name["{i+1}"]: ")
    Tab.append(temp)
    g=input("Daily Dose: ")
    t.append(int(g))
    temp=int(input("Enter TabLeft: "))
    l.append(temp)

for i in range(0,n):
    temper=[]
    temper.append(Tab[i])
    temp=(t[i]*p)-l[i]
    temper.append(temp)
    TabLeft.append(temper)
for i in TabLeft:
    print(i)