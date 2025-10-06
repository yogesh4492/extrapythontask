""" Printing Name using Lamda Function"""

name=input("Enter Your Name= ")
s1=lambda x: name.upper()
print(f"my name is ".upper(),s1(name))
print("".center(55,'-'))

""" Checking  Condition with lamda function """

#checking positive ,negative,neutral

num=lambda x: 'Positive' if x>0 else "negative" if x<0 else 'zero'
print(num(-5))
print(num(5))
print(num(0))
print(num(7))
print("".center(55,'-'))







