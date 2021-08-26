print('There is a disease that causes you to infect others.')
print('You must not become infected.')
print('Enter allows you to confirm your answer')
one = input('There is a car you could use to escape an infected person coughing over everybody. Use it? Y to use')
if one == 'Y':
    print('An infected was in the car. You you gained +1 Covid.')
    print('Fail.')
else:
    print('You easily escape the infected without the car')
    two = input('You find a city and you need water. raid a house? Y to raid')
    three = input('Night falls, and you are in the middle of a forest now. Set up camp with some equipment you grabbed while you were in the city? Y to set up a tent')
    if three == 'Y':
        print('It is cold at the night, but you survive due to your shelter')
        four = input('Morning comes, and you walk to a nearby dock with a boat. The captain offers to take you over the sea. Y to come with.')
        if four == 'Y':
            print('You arrive in the arctic, and learn the country you came from has been overrun by this... Infection. You made the right move.')
            five = input('The infection is spreading here, too. There is a nearby military base. M to head to the base, D to stay where the boat docked.')
            if five == 'M':
                six = input('The base has been abandoned. There is an elevator in a cave at the centre of the base. Y to use it.')
                if six == 'Y':
                    print('You enter a lab. There is a strange red object on the floor. Touch it? (Y to touch it)')
                    if six == 'Y':
                        print('it is dynamite...')
                        print('the lab is demolised, and you are buried under piles of rubble.')
                    else:
                        print('You find a cure in the lab. A year later, you are rewarded for saving the world. VICTORY')
            elif five == 'D':
                if two == 'Y':
                    print('You survive in the docks untill the military give their cure to the world. VICTORY')
                else:
                    print('You die from thirst. You should have raided the house')
        else:
            print('The country is overrun by the virus, and you are infected.')    
    else:
        print('You die of cold.')
        