import os
def clear():
  os.system('clear')
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
n=True
print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
d={'+':add,"-":sub,"/":divide,"*":multiply} 
n1=float(input("enter the first number "))
n2=float(input("enter the second number "))
for i in d:
  print(i)
op=input("enter the operation ")
function=d[op]
calc=function(n1,n2)
print( f"{n1} {op} {n2} = {calc}")

c=input("enter y or n ")
while(c=="y"):
  new_op=input("enter next operation ")
  function=d[new_op]
  n3=float(input("enter the number "))
  print(f"{calc} {new_op} {n3}={function(calc,n3)}")
  c=input("enter y to calculate further else n ")
#if(c=="n"):
  #you could use calculator function here and through recursion the calculator will run forever