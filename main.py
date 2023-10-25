import random

def gamewin(comps, you):
    if comps == you:
        return None
    elif comps == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comps == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comps == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp turn: Snake(s) Water(w) or Gun(g) ?")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    comps = 's'
elif randNo == 2:
    comps = 'w'
elif randNo == 3:
    comps = 'g'
    
you = input("Your turn: Snake(s) Water(w) or Gun(g) ?")
result = gamewin(comps, you)

if result is None:
    print("The game is a tie")
elif result:
    print("You win")
else:
    print("You lose")
