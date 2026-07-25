import random
class Trail:
    def __init__(self,hp,food,ammo,milesleft,days):
        global tm
        tm=milesleft
        self.hp=hp
        self.food=food
        self.ammo=ammo
        self.milesleft=milesleft
        self.days=days

    def Rules(self):
        print("Some points to remember ----")
        print('''
        1. In zombie raid (Hide) you may be caught and takes health damage
        2. In zombie raid (Run) you had health loss and double food loss ''')

    def ZombieRaid(self):

        print("    It is Zombie raid today ")
        print('''You have three options ---
        1.Attack on Zombies (Press A).
        2.Run from there (Press R).
        3.Hide for right time (Press H).''')
        choice=(input("Enter your choice:")).upper()
        if choice=='A':
            self.days+=1
            self.food-=5
            bullets=random.randint(5,8)
            if self.ammo>=bullets:
                print("You defeated the Zombie ,Nice go forward")
                self.ammo-=bullets
                self.milesleft-=random.randint(10,20)
            else:
                print("You don't have enough ammo to kill Zombie")
                self.hp-=5
                self.milesleft-=random.randint(5,10)
            

        elif choice=='R':
            self.days+=1
            self.hp-=10
            self.food-=5
            self.milesleft-=20
            print("You are escaping but you had a loss of health")



        elif choice=='H':
            pr=random.randint(1,2)
            if pr ==1:
                print("Nothing happens you are safe ,Zombie is unable to find you")
                self.milesleft-=random.randint(10,20)
            else:
                print("oops !, A Zombie finds you and damages you")
                self.milesleft-=10
                self.hp-=20  
            self.food-=5
            self.days+=1

        else:
            print("Invalid input read options carefully,in next day")
            print("You wasted your day and food")
            self.food-=5
            self.days+=1
    
    def title(self):
        print("\n" +"="*50)
        print("\n           SURVIVE TILL END    ")
        print("\n"+"="*50)

    def info(self):
        if self.food<0:
            self.food=0
        print()
        print(f"{self.hp} units is  your Health.")
        print(f"{self.food} Units of food is left.")
        print(f"{self.ammo} ammos are left in your hand.")
        print(f"{self.milesleft} miles are left to win the survival game.")
        print(f"{self.days} days you survived.")

    def Scavenge(self):
        
        print(" \n   Amazing you get a chance to increase your ammo resources!")
        
        print('''
        You need assets so (press S) or (press N) to skip
        NOTE:::IF YOU PRESS S YOU HAVE TO SPEND TWO DAYS ''')
        choice2=input("Enter your choice:").upper()
        self.food-=5
        
        if choice2=='S':
            a1=random.randint(5,10)
            f1=random.randint(3,10)
            self.ammo+=a1
            self.food+=f1
            self.days+=2
            print(f"Today is your day you got {a1} ammos and {f1} units of food.")

        elif choice2=='N':
            self.days+=1
            self.milesleft-=20
        
        else:
            print("Invalid input read options carefully")
            self.days+=1
    
    def safe(self):
        print("\nToday's day is safe for you ,Move forward and get win as soon as possible")
        print("No fight or other event today")
        c=input("press enter to continue:")

        self.milesleft-=20
        self.days+=1
        self.food-=5

p1=Trail(50,50,20,random.randint(150,250),0)
p1.title()
p1.info()
p1.Rules()
while p1.milesleft>0 and p1.hp>0:
    
    event=random.randint(1,10)
    if event in (1,2,3,4):
        p1.ZombieRaid()
    elif event in (5,6,7):
        p1.Scavenge()
    else:
        p1.safe()
    if p1.food<=0:
        p1.hp-=10
    print()
    print("Next day begins...")
    p1.info()
if p1.hp<=0:
    print("you are dead ,GAME OVER")
elif p1.milesleft<=0:
    print("CONGRATULATIONS!You won the game and survived the Zombie apocalypse.")
    print(f"You survived for {p1.days} days and your health is {p1.hp} and you have {p1.food} units of food left and {p1.ammo} ammos left in your hand and you travels {tm} Miles.")
    print("Thanks for playing the game,But days you took to survive are too much ,Try to survive in less days next time.")