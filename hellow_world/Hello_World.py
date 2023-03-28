snake_case = "this_is_a_snake_case_format_in_coding"
camelCase = "thisIsCamelCaseInCoding. perfectFor C#?"
PascalCase = "AndThisIsPascalCase"
CONSTANT = "This is constant variable like Pi"
PI = 3.14159
NAME = "<Your Full Name Here>"
RADIANS_TO_DEGREE = 180 / PI

"""
print("Complex The sum of values of " ,a, "," , b,
      ", and", c , "is  :", a+b+c)
 
print(f"FString The sum of values of {a},{b}, and {c} is {a+b+c}")
 
print("BPsum of values {}, {} and {} is {}".format(a,b,c,a+b+c))
print("NPsum of values {0}, {2} and {1} is {3}".format(a,b,c,a+b+c))
print("VPsum of values {a1}, {b1} and {c1} is {ee}".format(c1=c,ee=a+b+c,a1=a,b1=b))

print("PThe sum of values of %i , %d and  %f is  : %s" %(a,b,c,a+b+c))
print("P The sum of values of %i , %s and  %8.3f is  : %s" %(a,b,c,a+b+c))
print("P The sum of values of %f , %d and  %i is  : %d" %(a,b,c,a+b+c))
"""
num1 = input("Ente the First Number: ")
num2 = input('Enter the Second Number: ')
summation = num1+num2
print(type(num1))
print("The Sum Is", summation)
name = "jose"
avg = 123.56176
#result = "The REsult is" + avg #gonna give Error Cause avg is not str
#so we like string formatting ONLY IN python3.6+
result = f"The Result is {avg}"

#we could also make templates
greeting = "Hellow , {}"
#also multiple
day_greeting = "Good {day}, {name}"

#using string as an object it has a function like format
greeting_str = greeting.format(NAME)
#this would result in "Hellow , <Your Full Name Here>"
day_greeting_str = day_greeting.format(day = "Evening",name=NAME)

#commentatory

#and (TT=T, TF=F,FT=F,FF=F)
#or (TT=T, TF=T,FT=T,FF=F)
#not True 
Bosd = True
BossA = False
truthy = Bosd or BossA #return tru bcz bosd is true
falsy = BossA and Bosd #return false cause bossa is false
eg_name = "" #user no input (free exception handling coming)
eg_surname = "eg_surname"
eg_full_name = eg_name or eg_surname #still gonna cause error if surname empty but we could generalize
s2nd_truthy = not falsy

#comments--single line or mutiple lines which developer doesn't want to run
'''
Python - Dynamically typed prg Lang..
java - Strictly/Strongly typed prog lang...
int num1; #declaring variable....
other lang...Datatype for variable also.....
Datatype is actually exist for value/Literals..
'''
'''
THIS IS
DOUBLE LINED
COMMANDS
'''
"""
1Or like These????
"""
my_gawd_its_also_a_string = """
Heloo Python #&$
"""

num1=eval(input('Enter the first number'))
#num1=int(input('Enter the first number'))
#num1=10  //integer value.....
print(type(num1))
num2=eval(input("Enter the second number"))
num3=eval(input("Enter the third number"))
 
summation=num1+num2   #sum of 2 variables...
mult=num1*4
print("sum result is ", summation)
print("multiply result is ", mult)
 
#num1 > num2,  >, <, >=, <=, ==, !=
if (num1 > num2 and num1 > num3):
    print("Num1 is greatest")
elif (num2 > num1 and num2>num3):
    print("Num2 is greatest")
else:
    print("Num3 is greatest")
    

diff=num1-num2
div= num1/num2
fldiv=num1//num2 #floor division. rounds the value to minimum
rem= num1%num2
print("sum result is ", summation)
print("difference result is ", diff)
print("divide result is ", div)
print("floor division result is ", fldiv)
print("remainder result is ", rem)
 
#this program will calculate.....
"""
n="Athaulla"  #String
c=90.25  #float data
num1=100.23   #num1 float variable...
print(type(num1)) #prints float
num2="Athaulla"  #num2 string
num1=False  #True  #true false
print(type(num1))
"""

list_of_numbers = [1,3,4]
list_of_numbers.remove(4)
list_of_numbers.remove(3)
list_of_numbers.append(2)
list_of_numbers.append(3)
list_of_numbers.remove(list_of_numbers[2])
#try to maintain homogenius list (same type of elements:like friends,furniture etc)
Frind = [
    ['Jose',3],
    ['haha',5],
    ['Hello',2],
    ['Hi',1],
    ['Heyyyy',4]
]#we can do list of list

tuple1 = (1,2,3,'f')
set = {3,36,73,True,'sfa',342} #when compiling duplicate values deleted automaticlaly
list1 = ['saf','af','f']
dictionary = {'key':'value',1:'a',2:'b'}


confirmation = ['YES', 'Yes', 'yes', 'yEs']
for i in confirmation:
    if i.lower()=='yes': #used .lower to generalise every string so everythings 'yes' in smaller case
        print("Confirmed")


set = {3,36,73,True,'sfa',342} #when compiling duplicate values deleted automaticlaly
artFriends = {"rolf","anne"}
scienceFriendS = {"jen", "charlie"}
artFriends.add("jen") #add in set without order and cant add twice
artFriends.remove("rolf") #remove element from set
#easy for set operations
artButNotScience = artFriends.difference(scienceFriendS) #artFrineds-scienceFriends
notInBoth = artFriends.symmetric_difference(scienceFriendS) 
artAndScience = artFriends.intersection(scienceFriendS)
allStudents = artFriends.union(scienceFriendS)

#dictionaries
friendAges = {"mary":23 ,"Charlie":22, "Anas": 23}
print(friendAges["Anas"])
friendAges["Athaulla"] = 22
#as we used in project
friends = ['mary','Karim','Ronaldo','Messi','John Cena']
family = ['Father','Mother','Brother']
Frineds = (
    {"name":"Athaulla","age" : 23},
    {"name":"Karim Benzema","age": 24}
)
fiends = [("Chainsaw",20),("Blood",30)]
fiends_dict = dict(fiends)

grades = [12,45,4,65,54,54654,645,21,546,213,213,21,123]
total = sum(grades)
length = len(grades)
average_grade = total/length

#List is total flexible ....Tuple is not mutable

#so we have agrades list but printing it would look like [232,23,321]etc, so simplify
#But wont work with integers i think
comma_seperated = ','.join(friends)

#If Statements:
user_name = input("Enter Your Name: ")
if user_name in friends:
    print(f"Hello {user_name}, How Are you Friend")
elif user_name in family:
    print(f"Hello {user_name}, How are You Cousin")
else:
    print(f"Hello {user_name}")

#while_loops
is_learning = True
while is_learning:
    print("Im Learning")
    user_input = input("Are you still Learning?:")
    is_learning = user_input.lower() == "yes"

#for_loops:
for index in range(10,0,-1):
    print(f"Countdown: {index}")
for friend in Frineds:
    print(f"Name of friend is {friend['name']}")

#destructuring:
mask = 'yes', '88%'
is_mask, percentage = mask
for fiend,age in fiends:
    print(f"{fiend} is {age} years old")

#iteraring over dictionaries:
for name in friendAges:
    print(f"{name} is {friendAges[name]} Years Old")
for Age in friendAges.values():
    print(f"Age is {Age}")
for name, age in friendAges.items():
    print(f"{name} is {age} years old")

#break and coninue
for i in list1:
    if (i.lower() == 'F'):
        print("WHat F")
        break
    elif(i.lower() == 'af'):
        continue
    print(f"{i}")
else:#for excecuting only if no Break/no F in List
    print("Everything Fine")
    '''
        but if you want to print index you should go for continue with flag and value
        because else wont work with continue
    '''

def function(a,b):
    pass #For initialising so we need to write anyhting in function/class

fruits=['Apple',"Orange","Guava","Strawberry",'Chikku']
for fruit in fruits:
    if fruit.lower()=='guava':
        pass
        #continue   #it will break or exit the loop
    print(fruit)
else:
    print("Else Part") #else part excecute only when Loop fails first time itself

print("Out side the loop - Normal Statment")

from math import sqrt,floor
def prime_n(number):
    #doing sqrt method
    for n in range(2,number):
        for x in range(2,floor(sqrt(n))):
            if(n%x == 0):
                """
                    here n is not a prime
                """
                break
        else:
            print(f"{n} is a prime")
#List Slicing
l3 = list_of_numbers[3:]
l3 = list_of_numbers[:5]
l3 = list_of_numbers[-3:]
l3 = list_of_numbers[0:-2]
l3 = list_of_numbers[-3:-1]

#List Comprehension
l1 = [15,456,564,104,616,5,21,165,4,51,654,654,4,13,1,54,654,54,31,4,6]
for i in l1:
    if not i%2:
        print (i)
print([i for i in l1]) #list comprehension GOOOOOD
print(tuple(i for i in l1)) #tuple comprehension theres also set,lst,tuple comprehensions
print([f"hello {i}" for i in l1]) #its a statement before comprehension

name_input = input("Enter Friends Name: ")
friends_lower = [name.lower() for name in friends]
if name_input.lower() in friends_lower:
    print(f"{name_input.title()} is one of your friends.")

#list COmprehension with conditionals
print([f"{odd}" for odd in range(15) if odd % 2 == 1]) #WhHHAAAAAA with condition

guests = ['Ronaldo','Messi']

#list comprehension can be split into lines
present_friends = [
    name.title()
    for name in guests
    if name.lower() in friends_lower
]
print(present_friends)

#let the list be days since i seen those friends
friend_time = [i for i in range(len(friends))]
#finding friends with more than 3 days not seeing
long_timers = {
    friends[i]:friend_time[i]
    for i in range(len(friends))
    if friend_time[i] > 3
}

#zip
long_timers = dict(zip(friends,friend_time))
long_timers = list(zip(range(len(friends)),friends,friend_time))

#functions in python
def greeter():
    name = input("Enter your Name: ")
    print(f"Hey {name}! Greetings")
greeter()

cars = [
    {"make": "Chevrolet","name": "Camaro","mileage": 12000,"fuel_consumed": 400},
    {"make": "Chevrolet","name": "Cruze","mileage": 18000,"fuel_consumed": 400},
    {"make": "Chevrolet","name": "Trailblazer","mileage": 15000,"fuel_consumed": 400},
    {"make": "Chevrolet","name": "Beat","mileage": 22000,"fuel_consumed": 400},
    {"make": "Chevrolet","name": "Corvette","mileage": 13000,"fuel_consumed": 400}
]
#arguments and parameters
def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    return mpg


def car_name(car_to_calculate):
    name = f"{car_to_calculate['make']} {car_to_calculate['name']}"
    return name


def print_car_info(car_to_calculate):
    mpg = calculate_mpg(car_to_calculate)
    name = car_name(car_to_calculate)
    print(f"{name} does {mpg} mils per gallon")
    return None


for car in cars:
    print_car_info(car)

def divide(x,y):
    if (y==0):
        return("You Tried to divide by zero")
    else:
        return x/y

print(divide(6,3))

#Default Parameter Values
def add(x,y=5):
    print(x+y)

add(6)
add(6,3)
add(x=4)
print(1,2,3,4,5,6,7, sep=' - ') #prints = 1 - 2 - 3 - 4 - 5 - 6 - 7

#lambda
divide = lambda x, y: x / y
print(divide(3,78))
tuple1 = tuple(i for i in l1)
average = lambda sequence: sum(sequence) / len(sequence)
print(average(tuple1))

def before_and_after(function):
    print("Before...")
    function()
    print("After...")

operations = {
    "average" : lambda sequence: sum(sequence) / len(sequence),
    "total" : sum,
    "max" : max
}
operation = input("Enter Operation 'average' 'total' 'max' :")
result = operations[operation](tuple1)
print (result)



or_l3 = any(l3) #Similiar to OR Gate.. Return true if any elements in an iterable is True
and_l1 = all(l1) #only returns true if every Element in an iterable is True
#mutability 
#once a variable is assigned i cant be changed
#all strings  are immuatable
#int 0-256

#parameters for creating a function
#Default: Default def variables, gets equal to etc

def square(n):
    return (n*n)


#same as
square_lambda = lambda n: n*n

n= int(input("Enter the number: "))
squareValue = square(n)
print(f"The Square is {squareValue}")

l1=[6,45,51,21,51,546,15,54,64,46,464,64,46,46,464,64,646,4]

from functools import reduce

sumSlist = reduce(lambda a,b: a+b, l1)

#
def account(name, amount, accoundholder = list()): #list only initialize the first time
    accoundholder.append({name:amount})
    return accoundholder

def account1(name, amount, accountholder = None): #creates a list always
    if not accountholder:
        accountholder = []
    accountholder.append({name:amount})
    return accountholder

print(account("Mary",20000)) #positional: by order of calling
print(account1("Rani",15000)) 
print(account1("Sharookh",10000)) #adds with Rani
#key

#unpacking example
def greatest(a,b,c): 
    gtest = a if a>b and a>c else b if b>a else c  #like ternary operator in C (a>b && a>c)? a : (b>a? b : c)
    return gtest
l1 = [12,87,54] #type(t1) = tuple
gtest = greatest(l1[0],l1[1],l1[2])
gtest = greatest(*l1) #same as first Unpacking

def run(object,*dimension,speed = 1):
    for i in range(len(object)):
        object[i] += dimension[i]*speed


run([1,2,3],12,23,34)
run([2,3,4],34,45,56,speed=10) #i did this to show how different calling methods work.. BUT This CALLED POLYMORPHISM

#classes
class Employee: #pascal case
    def __init__(self,new_eid,new_name,new_department,new_salary,new_email): #special/magic/dendor method
        self.employeeid = new_eid
        self.name = new_name
        self.department = new_department
        self.salary = new_salary
        self.email = new_email
        print(f"An Object Employee is created{self.name}")

    def display(this):
        print(f"Emplyee Id : {this.employeeid}")
        print(f"Name : {this.name}")
        print(f"Department : {this.department}")
        print(f"Salary : {this.salary}")
        print(f"Email : {this.email}")


professor = Employee(1012,"name2","cs",11200000,"abc2@example.com")
print(professor.__class__) #prints the class name of worker ,like here = <class Employee>
professor.display()
Employee.display(professor) #we can also call like this if we need to include two object

#like if user need to create n employee.. can we create a for loop with
employee_list = []
n = int(input("How many New Employees:"))
for i in range(n):
    new_eid = input("Employee Id: ")
    new_name = input("Enter Name: ")
    new_department = input("Department: ")
    new_salary = input("Salary: ")
    new_email = input("Email: ")
    obj = Employee(new_eid,new_name,new_department,new_salary,new_email)
    employee_list.append(obj)

for i in employee_list:
    i.display()

#incorrect annswers 
#1. list is consistent - every copy is edited
#2. Dunder Method is Built-in Functions or class
#3. Tuples - consists of a number of values separated by comma and enclosed within parentheses.
#4. set cant append

#instance variables - Specific data to the object
#class variable - This variable not specific to object(like college of students)
#multiple level inheritance - Staff(Employee(Human))
#multiple Inheritance - child(parent1,parent2)
#heirarchy inheritance - child1(parent),child2(parent)
#Hybrid Inheritance - child1(parent1(Grandparnet),parent2)
#MRO Method resolution Order
#C3 Algorithm Order
#F(D(A(O),B(O)),E(B(O),C(O)),C(O))
#python supports most inheritance

#polymorphism of two types
#Overloading OR compile time polymorphism OR Early Binding
    #Operator Overloading
        # + overloaded with some bydefault
        #we can include __add__ dunder method to make our own operation
'''
        __add__         +
        __mul__         *
        __div__         /
        __sub__         -
        __floordiv__    //
        __pow__         ^
        __iadd__        +=
        __isub__        -=
        __imul__        *=
        __idiv__        /=
        __isub__        -=
        __ifloordiv__   /=
        __gt__          >
        __lt__          <
        __ge__          >=
        __le__          <=
        __eq__          ==
        __ne__          !=
'''
    #Instance MEthod Overloading #Costructor Overloading #Python dont need support for this Overloading
#oververriding OR Run-Time Polymorphism OR Late Binding

#how to return with placeholders(%d) . you did with --str--


class Test:
    def __init__(self) -> None:
        self.list = []
        pass

    def __len(self):
        return len(self.list)

    def __getitem__(self,i):
        return self.list[i]

    def __repr__(self):
        return f"<Test {self.list}>"

    def __str__(self):
        return f"Test with {len(self)} Objects"
    

print(Test.greetings)
object1 = Test()
object1.list.append(1)

#using __len__:
print(len(object1)) #returns size of list
#using __getitem__:
print(object1[0]) #returns the element from rhe list with index {i=0}
#using __str__:
print(object1) #returns the string, For user
#using__repr:
    #Coming tut #!imp for debugging
    #every class to create should have repr

#Inheritance
class Staff(Employee): #staff inherited from Employee
    CLASS_VARIABLE = "Works at {this} Company"

    def __init__(self,new_eid,new_name,new_department,new_salary,new_email,new_month_left):
        super().__init__(new_eid,new_name,new_department,new_salary,new_email)
        self.month_left = new_month_left
    
    @property #property decorator
    def days_left(self):
        return self.month_left * 30
    
    @classmethod #Mandatory for class method/class variable Need to be used together method (Decorator)
    def company(cls): #Any variable can be used... and cannot instance variable using classmethod
        print(f"Called by {cls.__name__}")
        print(cls.CLASS_VARIABLE)
        pass

    @staticmethod #optional but used to define static methods for the methods in class #utility Method
    def daysinmonth(): #interpreter can understand without @staticmethod because no parameters
        pass

    @staticmethod #but if using parameters it should have static method decorator
    def compare_employee(employee_a,employee_b):
        print(f"Salary Difference of the Employees is{employee_a.salary - employee_b.salary}")

    def display(this): #ovverriding
        super().display()
        print(f"Month Left : {this.month_left}")
        pass

    def calc_salary(this):
        #perhour = 2000
        pass


worker = Staff(1010,"name1","cs",12000,"abc1example.com",12) #constructor - intialise yor variable
worker.display() #normal class Method
print(worker.days_left) #we dont need () of methods.. Using @property decorator
professor = Staff(1012,"name2","cs",11200000,"abc2@example.com",36)
Staff.compare_employee(worker,professor) #giving two objects as attributes using @staticmethod decorator

class Money():
    def __init__(self, value1):
        self.amount = value1

    @classmethod
    def Sum_from(cls, value1, value2):
        return cls(value1 + value2)
    
    def __repr__(self):
        return f'<Money {self.amount:.2f}>'
    
class Dollar(Money):
    def __init__(self, value1):
        super().__init__(value1)
        self.symbol = '$'
        pass

    def __repr__(self):
        return f'<Dollar {self.symbol}{self.amount:.2f}>'
    
number = Money.Sum_from(12.3254,32.45235)
dolla_number = Dollar.Sum_from(423.36,357.4327)
print(number)       #prints <Money 43.43>       ps: random amount
print(dolla_number) #prints <Dollar $352.65>    ps: random amount

#Function Aliasing
def hellow(name):
    print(f"Hello {name}")
greet = hellow
greet("name is this") #same as hellow,we give alias


#EXCEPTION HANDLING
"""
    ValueError
    ZeroDivisionError
    NameError
"""
#the interpreter Raising The errors when some exception errors

#try-n(except)-else-finally block #always follow this order
try:
    n1 = 12
    n2 = input("ENter the number: ")
    if n2==0:
        raise ZeroDivisionError("You are trying to divide by zero")
    print(n1/n2)
    class User:
        def __init__(self,name,password):
            self.username = name
            self.password = password
        
        def Login(self):
            raise NotImplementedError("This feature is not implemented yet") #for developers to usr messages
        
except ZeroDivisionError as zde:
    print(f"{zde}Please enter non-zero number")
    pass
except (ValueError,NameError) as vne:
    print(f"Some name errors as {vne}")
    pass
except Exception as Ex:
    print("This is General Exception AS : ", Ex)
else: # only works when no exception #Use before finally
    print("No Errors Occured")
    pass
finally: #works always
    print("Every Exception is handled")
    pass
print("After Try and except")
#after error program exited. can we make program to try again until no error...
#I DONT THINK WE CAN

class Garage():
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car,Car):
            raise TypeError(f"Tried to add {car.__class__.__name__} to Garage, But you can only add Car Object")
        self.append(car) #we dont need else because if raised exception the code exited without running this

    def car_details(self,car):
        raise NotImplementedError("Haven't yet implemented this Feature")


class Car():
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}"
    

Home_shed = Garage()
camaro = Car('Chevrolet', 'Camaro')
Home_shed.add_car(camaro)
print(len(Home_shed))
print(camaro)


#offtopic, i always see you open so many windows. may i know how much RAM you have if you dont mind

























#Advanced Built-in functions in python
evenlambda = lambda a:not a%2
#for making every even item in list as a list: 2 ways
#1 Normal way
evenList = []
for i in l1:
    if evenlambda(i):
        evenList.append(i)

#2 using filter
evenList = list(filter(evenlambda, l1))
'''
filter takes a condition, or a lambda with iterable
for i in l1:
    evenList.append(filter(i%2))
'''

l2 = [1,2,3,4,5,6,7,8,9]
sumlist = list(map(lambda n: n+5,l2))













#decorators
def smartdiv(c): #the reference of old function gets stored in c
    print("Inside smartdiv function: ", id(smartdiv))
    def inner(d,e):
        if e:
            #some exception handling
            pass
        else:
            result = c(d,e)
            return result
            #excecuting same logic when no errors
        pass
    pass


#monkey patching - interview question
#why some functions deprecating without using decorators?
#theres deprecation warning when using old buggy library methods

@smartdiv
def div(a,b):
    print("Inside div function: ",id(div))
    return a/b

#if we called 
div(10,0) #this calls smartdiv automatically

#if no decorator we can call this as
inner_reference = smartdiv(div)
inner_reference(10,0) #same as calling div with decorator


#iterator - since we cant import large dataset to memory it will affect ram.. so iterator gets only the first
            #elemnt and called using next()

l1_iter = iter(l1)
example_list = (i for i in range(100))
print(next(example_list))
print(l1_iter.__next__())

#when you were taking list comprehension.. and called for without square bracket, a generator object was created
#it happened when im doing project also
#generator function
#yield instead of return

#we've learnt so much and that's all because of your amazing teaching. Thank you Mr. Athaulla

#multitasking
#concurrency parellelism
#syncronous and asyncronous
#main thread - application
#fcfs theory like
#Add - 2sec, Sub - 2sec, Mul - 3sec
#Total with one thread 7 second
#if multitasked completed with 3 sec
#Asyncronous - the process that does'nt depend on the user it keeps running until its completed
from threading import Thread

def functioncall():
    pass


filenames = [
    'test1.txt',
    'test2.txt',
    'test3.txt'
]

from time import perf_counter

time_counter = perf_counter()
threads = [Thread(target=functioncall, args=(filename,'id','ids')) for filename in filenames]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

lock = Thread.lock

#somefunction call
time_counter -= perf_counter()
print(f"Took {time_counter} time to complete process")