x = ["d", "d", "d", "c", "c", "c", "b", "a", "b", "a", "c", "c", "d", "d", "a", "d", "c", "d", "d", "b", "c", "a", "a", "d", "b", "c", "c", "a", "b", "d", "c", "d", "b", "d", "d", "d", "a", "c", "b", "c", "c", "c", "a", "b", "c", "a", "b", "d", "b", "b", "b", "d", "d", "b", "b", "b", "b", "d", "d", "a", "d", "c", "c", "a", "c", "b", "b", "a", "a", "a", "a", "c", "d", "d", "a", "a", "c", "d", "a", "d", "d", "a", "d", "d", "c", "b", "c", "a", "c", "d", "d", "b", "d", "b", "c", "b", "b", "a", "c", "c" ]

def getListOfAnswers():
    global x
    #Replace the path to the location of ComputerBasicsTestController.cs with the correct path on your machine
    file = open("D:\K\LMS_MVC\LMS_MVC\Controllers/ComputerBasicsTestController.cs", 'r')
    for line in file:
        if 'public List<string> correctAnswers' in line:
            line = line.split('{')[1].replace('}','').replace(';','').replace('\n','').replace('"','').replace(' ','')
            answers = line.split(',')
            answers.remove('')
            x = answers

def changeAns():
    ans = int(input("What question do you want to change (1-100)? "))
    if ans < 1 or ans >100:
        print("Not a valid question number!")
        changeAns()
    print("Number " + str(ans) + " is " + x[ans-1])
    change = input("Enter the correct answer (a,b,c,d): ")
    if change in ['a','b','c','d']:
        x[ans-1] = change
    else:
        print("Not a valid answer!")
        changeAns()

def getCSharpList():
    List = 'public List<string> correctAnswers = new List<string> ' + str(x).replace('[','{').replace(']','}').replace('\'','"') + ';'
    print("Copy and paste this list into your C# code\n")
    print(List)

def main():
    print("Current correct answer list is ")
    print(str(x))
    more = True
    while more == True:
        changeAns()
        check = input("Change another answer? (y/n): ").lower()
        if check != 'y':
            more = False
    getCSharpList()
try:
    getListOfAnswers()
except:
    print("Couldn't get list from C# Controller")
main()
