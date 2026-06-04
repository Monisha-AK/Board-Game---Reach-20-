import random
import time

print('''------------------------------------
Welcome to the Reach-20 Board Game!
------------------------------------------''')
name=input('Enter your name: ')
print('Welcome',name,'!')
def homepg():
    print('''
    1. Enter game
    2. Exit game
    ''')
    x=int(input('Enter your choice: '))
    if x==1:
          game()
    elif x==2:
          print('Thank You!')

def game():
    position = 0
    iteration=0
    obstacles = random.sample(range(1, 20), 3)
    obstacles.sort()
    print('Obstacles placed at:', obstacles)
    print('---')
    while position < 20:
        time.sleep(0.5)
        input('Press Enter to roll the die...')
        die = random.randint(1, 6)
        iteration+=1
        print('Rolling........')
        time.sleep(1)
        print('You rolled:', die)
        time.sleep(1)


        if position + die > 20:
            print('Invalid roll! You need',(20-position),'to win')
            print('Roll again')
            print()
            print('---')
            continue


        position += die
        print('Moved to position:', position)


        if position in obstacles:
            position -= 5
            if position < 0:
                position = 0
            print('Hit an obstacle! Move back 5 steps')
            print('New position:', position)
        print('---')
    print('You reached 20!')
    x=input('Want to see your score?(y/n): ')
    if x=='y':
        score=10000-(iteration*10)
        print(name,', your final score:',score,'!')

    end()
def end():
    print('''
    1. Play again
    2. Exit game
    ''')
    x=int(input('Enter your choice: '))
    if x==1:
          game()
    elif x==2:
          print('Thank You!')

    
homepg()




