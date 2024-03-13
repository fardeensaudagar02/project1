import random

def gamewin(comp, you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
    elif you =='g':
        return True
    
    elif comp=='w':
        if you=='g':
            return False
    elif you =='s':
        return True
    
    elif comp=='g':
        if you=='s':
            return False
    elif you =='w':
        return True
    
print("Welcome to the snake water and gun game")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
you=input("your turn: enter s for snake, w for water, g for gun: ")
a=gamewin(comp, you)
print(f'computer chose {comp}')
print(f'you chose {you}')
if a==None:
    print('The game is tied')
elif a:
    print('You win')
else:
    print('you loose')
