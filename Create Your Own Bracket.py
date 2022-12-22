import random # Simple project that takes user input to seed a bracket for a desired amount of people

players = input("How many people are participating in your tournament? ")

def make_bracket(list_of_players):
    list_of_seeds = []    
    x = random.randint(0, len(list_of_players)-1)
    for e in range(0,len(list_of_players)):
        x = random.randint(0,len(list_of_players)-1)
        while x in list_of_seeds:
            x = random.randint(0,len(list_of_players)-1)
        list_of_seeds = list_of_seeds + [x]
    print(list_of_seeds)
    seeds_in_order = []
    for e in range(len(list_of_players)):
        for f in range(len(list_of_players)):
            if e == list_of_seeds[f]:
                seeds_in_order = seeds_in_order + [str(list_of_players[f])+": " + str(list_of_seeds[f]+1)]
    for e in (seeds_in_order):
        print(e)

def bracket(players):
    x = 1
    list_of_players = []
    player_count = int(players)
    while player_count >=1:
        playername = input("Name of player " + str(x) + ": " )
        player_count = player_count - 1
        x = x + 1
        list_of_players = list_of_players + [playername]
    print(list_of_players)
    make_bracket(list_of_players)

bracket(players)
