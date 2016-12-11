

# Python Exercise 1

def one():
    print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

# Exercise 2

def two():
    import sys
    print (sys.version)

# Exercise 3 Current Date and time

def three():
    import datetime

    now = datetime.datetime.now()
    print ("Current date and time : ")  
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Exercise 4 radius of a circle 

def four():
    import math

    radius = input("Enter the Radius of the circle:")
    Area = float(radius) * float(math.pi)
    print ("The Area of the Radius",radius, "is",Area)

# Exercise 5

def five():
    firstname = input("What is your First Name? ")
    lastname = input("What is your Last Name? ")
    print ("Whats up? " + lastname + " " + firstname)

# Exercise 6

def six():
    values = input("Input some comma seprated numbers : ")
    list = values.split(",")
    tuple = tuple(list)
    print('List : ',list)
    print('Tuple : ',tuple)

# Exercise 7

def seven():
    filename = input("Input the Filename: ")
    f_extns = filename.split(".")
    print ("The  extension of the file is : " + repr(f_extns[-1]))

# Exercise 8

def eight():
    color_list = ["Red", "Green","White","Black"]
    print(color_list[0],color_list[3])

# Exercise 9

def nine():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : %d/%d/%d"%exam_st_date)
    
# Exercise 10

def ten(): # Have no idea whats going on here Google 
    n = int(input("Input an integer : "))
    n1 = int( "%s" % n )
    n2 = int( "%s%s" % (n,n) )
    n3 = int( "%s%s%s" % (n,n,n) )
    print (n1+n2+n3)

# Exercise 11 # What?

def eleven():
    func_help = input("Enter a valid Python function name: ")
    display = help(func_help)
    print(display)

# Exercise 12 # what?

def twelve():
    import calendar
    y = int(input("Input the year : "))
    m = int(input("Input the month as an integer: "))
    print(calendar.month(y, m))

# Exercise 13

def thirteen():
    print ("""a string that you "don't" have to escape \nThis \nis a ......multi line \nheredoc string""")

# Exercise 14

def fourteen():
    from datetime import date
    start_date = date(2014, 7, 2)
    end_date = date(2014, 7, 11)
    delta = end_date - start_date
    print(delta.days)
                
# Exercise 15

def fifteen():
    #V = 4/3(3.14)(r)^3
    pi = 3.14159
    r = 6
    V=4/3* pi* r**3
    print("The Volume of the Sphere is: ", V)

# Exercise 16

def sixteen():
    # Enter a integer subtract 17
    # if the number is greater than 17 multiple it by the absolute difference

    x = int(input ("Input an integer"))
    
    if (x > 17):
       return  (x - 17)*2
    else:
        return x - 17

 
# Exercise 17

def seventeen():

    x = int(input("Enter an integer"))

    if x <= 100:
        print ("The number is less than 100")
    elif 100 < x<= 1000:
        print ("The number is less than 1000")
    elif x > 1000 and x <= 2000:
        print ("The number is less than 2000")
    
# Exercise 18

        
def eighteen():
    
    n1=int(input("enter first number"))
    n2=int(input("enter second number"))                 
    n3=int(input("enter third number"))
    x = n1+n2+n3                         
    if (n1 == n2 == n3):
        print ("Thrice sum:", int(x * 3))
    else:
        print("sum:",int(x))

# Exercise 19

def nineteen():

    x = str(input("Enter a sentence"))
    if x.startswith('is'):
        return x
    else:
        return 'is ' + x
# Exercise 20

def twenty():

    strng=input("Give any string:")
    copies=int(input("Enter how many copies:"))
    Copied_String=copies*strng

    print(strng *copies )
    
# Exercise 21
# whether a given number (accept from the user) is even or odd

def twentyone():
    x = int(input("Enter a number now!"))

    z = x % 2

    if z > 0:
        print ("Odd Todd")
        
    else:
        print("Even Steven")
# Exercise 22

'''def twentytwo():
    
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

        print(list_count_4([1, 4, 6, 7, 4]))
        print(list_count_4([1, 4, 6, 4, 7, 4]))'''

#Exercise 23

def twentythree():

    str=input("Enter any string:")
    copies=int(input("Enter how many copies you want to print:"))
    if(len(str)<2):
        print(copies*('\n'+str))
    else:
        a=str[:2]
        print(copies*('\n'+a))

#Exercise 24      not working 

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
    print(is_vowel('c'))
    print(is_vowel('e'))

#Exercise 25   not working
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
    print(is_group_member([1, 5, 8, 3], 3))
    print(is_group_member([5, 8, 3], -1))


def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])

if __name__== "__main__":
    one()
    print("")
    two()
    print("")
    three()
    print("")
    four()
    print("")
    five()
    print("")
    six()
    print("")
    seven()
    print("")
    eight()
    print("")
    nine()
    print("")
    ten()
    print("")
    eleven()
    print("")
    twelve()
    print("")
    thirteen()
    print("")
    fourteen()
    print("")
    fifteen()
    print("")
    sixteen()
    print("")
    seventeen()
    print("")
    eighteen()
    print("")
    nineteen()
    print("")
    twenty()
