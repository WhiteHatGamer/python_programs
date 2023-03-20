def smartdiv(f):
        #whats this argument?????
        #     print("L#1 Inside Decor Function")
        #     print("Address of f : ", id(f))
        #     def inner(i,j):
        #         print("L#4 Inside Inner of Decor")
        #         if not j:
        #    #number can be used condition >0 True 0 - False
        #             print("L#5 j is zero - Zero Divide error so returning zero default")
        #             #b=1
        #             #f(a,b)
        #             return 0
        #         else:
        #  #(a and b is normal...normal execution...
        #             #return i/j -             #print(id(f))            #return i/j            #avoid duplicate....            #res=div(i,j)            res=f(i,j)   #actual div function# f is the function ref to refer old div func            return res            #return f(i,j)    print("L#2 Address of Inner : ", id(inner))    return inner# Monkey Patching  vs Decorator  #Dynamic functionality User can change#function aliasing   div=smartdiv(div)@smartdiv # remove this and use decorfunc = smartdiv(div) to have botdef div(a,b):  #15lnes of code....5,0   5/0    print("L#5 Inside original Divide method",id(div))    return a/b  #10/0 --- DivisionByZero#######################################################################a=input("Enter 2 numbers").split() #"10" "20"a=[int(x) for x in input("Enter 2 numbers").split()]   #list comprehensionprint("L#3 1st line of my main program")print("inner ID using div ",id(div))   #id----inner.......#f(10,20) , div(10,20).....div(10,0)#f=smartdiv(div)   #function aliasing...#result=f(a[0],a[1])  #normal div invoked indirectly#print("L#6 Divide of {} and {} is {}".format(a[0],a[1],result))oldresult=div(int(a[0]),int(a[1]))  #normal div invoked indirectlyprint("L#6 OLD Divide of {} and {} is {}".format(int(a[0]),int(a[1]),oldresult))#oldresult=f(int(a[0]),int(a[1])) #print("L#6 OLD Divide of {} and {} is {}".format(int(a[0]),int(a[1]),oldresult))"""inref=smartdiv(div)  #normal div invoked indirectlynewresult=inref(a[0],0) #decorated inner functionprint("L#6 NEW Divide of {} and {} is {}".format(a[0],0,newresult))print("In Between Decord method and Invoking")#decorfunc = smartdiv(div) print("L#7 Address of DecorFunc: ", id(decorfunc))result=decorfunc(a[0],a[1]) #point3#result=div(10,2) #inner(10,0) #point #1#result=div(10,2)print("Divide of {} and {} is {}".format(a[0],a[1],result))   """
