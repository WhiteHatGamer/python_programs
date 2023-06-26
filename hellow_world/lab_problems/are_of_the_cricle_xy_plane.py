def distance(x1,y1,x2,y2):
    """
    Find distance between two points on a x,y plane
    """
    a=((x1-x2)**2)+((y2-y1)**2)
    d=a**.5
    return d


print ("Co Ordinates of the circle")
x1=int(input("Enter The X1 Coordinate:"))
y1=int(input("Enter The Y1 Coordinate:"))
x2=int(input("Enter The X2 Coordinate:"))
y2=int(input("Enter The Y2 Coordinate:"))
a=3.14*(distance(x1,y1,x2,y2)**2)
print ("Area Of the Circle=",a)
