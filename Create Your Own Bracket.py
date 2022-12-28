import random # Simple project that takes user input to seed a bracket for a desired amount of people

players = input("How many people are participating in your tournament? ")

def seed_bracket(list_of_players):
    list_of_seeds = []    
    x = random.randint(0, len(list_of_players)-1)
    for e in range(0,len(list_of_players)):
        x = random.randint(0,len(list_of_players)-1)
        while x in list_of_seeds:
            x = random.randint(0,len(list_of_players)-1)
        list_of_seeds = list_of_seeds + [x]
    seed_in_order = {}
    updated_seeds = {} # this stores the inputs into a dictionary in case I wanted to take this project further by linking it to the front end
    for e in range(0,len(list_of_players)): 
        for f in range(0,len(list_of_players)):
            if e == list_of_seeds[f]:
                updated_seeds.update({str(list_of_seeds[f]+1):str(list_of_players[f])})
    seeds_in_order = [] # this part prints them in a list
    for e in range(0,len(list_of_players)):
        for f in range(0,len(list_of_players)):
            if e == list_of_seeds[f]:
                seeds_in_order = seeds_in_order + [str(list_of_seeds[f]+1)+": " + str(list_of_players[f])]
    for e in (seeds_in_order):
        print(e)
    makethisbracket(list_of_players,updated_seeds,seeds_in_order)

def bracket(players):
    x = 1
    list_of_players = []
    player_count = int(players)
    while player_count >=1:
        playername = input("Name of player " + str(x) + ": " )
        player_count = player_count - 1
        x = x + 1
        list_of_players = list_of_players + [playername]
    seed_bracket(list_of_players)

bracket(players)
