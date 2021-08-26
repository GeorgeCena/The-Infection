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
    if two == 'Y':
        print('You grabbed a bottle of water')
        print('Good. You have enough supplies to continue your journey.')
        three = input('Night falls, and you are in the middle of a forest now. Set up camp with some equipment you grabbed while you were in the city? Y to set up a tent')
        if three == 'Y':
            print('It is cold at the night, but you survive due to your shelter')
            four = input('Morning comes, and you walk to a nearby dock with a boat. The captain offers to take you over the sea. Y to come with.')
            if four == 'Y':
                print('You arrive in the arctic, and learn the country you came from has been overrun by this... Infection. You made the right move.')
            else:
                print('The country is overrun by the virus, and you are infected. FAIL.')
        else:
            print('You die of cold in the night. Your water changes nothing.')
    else: 
        print('You did not enter the city')
        print('You might need water though.')
        print('Night falls and you have no water.')
        print('You die of thirst in the forest.')

    