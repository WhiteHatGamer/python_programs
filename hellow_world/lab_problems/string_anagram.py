def ispermute(a,b):
    if len(a)==len(b):
        c=0
        for i in a:
            if i in b:
                c=c+1
                continue
            else:
                print ("Not Permutable")
                break
        if c>0:
            print ("Permutable")
    else:
        print ("Not Permutable")
