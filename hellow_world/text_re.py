import re
f1 = open(a1.txt)
#pattern = re.compile()
#lines = f1.readlines()

for line in f1:
    #email - "\w+@\w+[.com|.co.in|org]"
    #mobileNumber - [6-9]\d{9}
    match = re.findall("condition",line) #condition to be email/mobilenumber
    for j in match:
        print("Mobile #" + j)

print("End of program")

f1.close()