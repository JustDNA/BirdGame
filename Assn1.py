__author__ = 'dhiwakar'

def add(a,b):
    print (a+b)

def sub(a,b):
    print (a-b)

def mul(a,b):
    print (a*b)

def div(a,b):
    print (a/b)

choice = int(input("Enter choice\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Quit\n"))

if(choice < 5):
    running = True
else:
    running = False

while running:
    
    a = float(input("Enter value for a"))
    b = float(input("Enter value for b"))
    
    if(choice == 1):
        add(a,b)
    if(choice == 2):
        sub(a,b)
    if(choice == 3):
        mul(a,b)
    if(choice == 4):
        div(a,b)
    
    choice = int(input("Enter choice\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Quit\n"))
    if(choice >= 4):
        running = False