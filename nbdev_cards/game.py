# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_game.ipynb.

# %% auto 0
__all__ = ['COMBAT_OPTIONS', 'init_player', 'combat', 'game_loop']

# %% ../nbs/01_game.ipynb 4
def init_player():
    print(f"Hi there, your speciality ? {Ability.ability_types}")
    while True:
        ability_type = input()
        if ability_type in Ability.ability_types:
            break
        else:
            print(f"Invalid ability choice, what is your speciality ? {Ability.ability_types}")
    name = input("What is your name, mage ?")
    return Mage(name, 100, Ability(10, ability_type))

# %% ../nbs/01_game.ipynb 6
COMBAT_OPTIONS = ["attack"]

def combat(player, boss):
    print("Combat has begun!")
    while True:
        print(player)
        print(boss)
        print(f"What do you want to do ? {COMBAT_OPTIONS}")
        player_move = input()
        if player_move not in COMBAT_OPTIONS:
            print("Not an option, you lose a move!")
        else:
            if player_move == "attack":
                player.attack(boss)
                if boss.current_health <= 0:
                    return player
        
        boss.attack(player)
        if player.current_health <= 0:
            return boss


# %% ../nbs/01_game.ipynb 8
def game_loop(player, n=5): # n is number of rounds
    for i in range(1, n + 1):
        boss = Demon("Ravana", 50 * i)
        print(f"A demon named {boss.name} appeared! They seem to have chip on thir shoulder and want to fight you.")
        winner = combat(player, boss)

        if winner == player:
            print(f"Well done, you beat {boss.name} and leveled up to {i + 1} !")
            player.level_up()
        else:
            print(f"You have fallen to {boss.name} Game Over!")
            break
    if i == n:
        print(f"Congratulations, you've defeated all the bosses and won the game. {player.name}'s name shall go down in istory!")

