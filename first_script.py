import math

string1="Hello"
string2="world"
twoonthree=2/3
string3="more"
a=[1,2,3,4,5,6,7,8,15,6,2,98,7,9]

print("This is my first script.")
print(string1 + " " + string2 + "!"*3)
print("\n"*2)
print("2 divided by 3 is about {}".format(twoonthree))
print("Or with fewer decimal points: {: f}".format(twoonthree))
print("You can print {0} than one variable, here\'s Pi:{1}. that makes {2} variables!" .format(string3,math.pi,3))
print("\n"*2)
for num in range(2,10,2):
    print(num)
print("\n")
for element in a:
    if element ==  max(a):
        print(element*"=")
        print("Here, we reached the largest.")
    else:
        print(element*"=")
