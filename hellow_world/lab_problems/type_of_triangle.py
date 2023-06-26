a=input("Enter The Length of 1st Side:")
b=input("Enter The Length of 2nd Side:")
c=input("Enter The Length of 3rd Side:")
if(a==b):
    if(b==c):
        print("Equilateral Triangle")
    else:
        print("Isoscelous Triangle")
elif(b==c):
    print("Isoscelous Triangle")
elif(a==c):
    print("Isoscelous Triangle")
else:
    print("Scalene Triangle")
