import random
building = "A guy jumps off a building. What do you do?"
villain = "You encounter a villain. What do you do?"
cat = "A cat is stuck in a tree. What do you do?"
kid = "A kid asks you for ice cream. What do you do?"
car = "A car is about to hit an old lady. What do you do?"
robbery = "A robber has escaped from the bank. What do you do?"
earthquake = "An earthquake is occuring and you see a boy stuck under some rubble. What do you do?"
train = "A train is getting derailed. What do you do?"
boat = "There has been a boating accident and people are stranded in the sea. What do you do?"
mugging = "An old lady's purse has been stolen by a stranger! What do you do?"
bomb = "There is a bomb attached to a building. What do you do?"
dog = "You see a woman kicking her dog. What do you do?"
homeless = "You see a homeless man. What do you do?"
fight_options = "\n Fight \n Watch \n Run \n I want to: "
save_options = "\n Save \n Watch \n Run \n I want to: "
situations = {
    building: save_options,
    cat: save_options,
    kid: save_options,
    car: save_options,
    earthquake: save_options,
    train: save_options,
    boat: save_options,
    bomb: save_options,
    dog: save_options,
    homeless: save_options,
    villain: fight_options,
    robbery: fight_options,
    mugging: fight_options
}
save = ["save", "watch", "run"]
fight = ["fight", "watch", "run"]
random_situations = ""
rank = 7854
current_power = 0
situation_input = ""
easy = 0
medium = 0
hard = 0
difficulty = {
    building: "hard",
    cat: "easy",
    kid: "easy",
    car: "medium",
    earthquake: "medium",
    train: "hard",
    boat: "medium",
    bomb: "hard",
    dog: "medium",
    homeless: "easy",
    villain: "hard",
    robbery: "medium",
    mugging: "easy"
}

diamond_tier = (rank <= 500)
gold_tier = (rank <= 2000)
silver_tier = (rank <= 4500)
bronze_tier = (rank <= 6000)
def rank_calculator(rank, option, difficulty, power):
    if option == "save" or option == "fight":
        if difficulty <= power:
            print("Success! Your rank improves.")
            if diamond_tier:
                rank -= random.randint(1, 100)
            elif gold_tier:
                rank -= random.randint(1, 500)
            elif silver_tier:
                rank -= random.randint(1, 1000)
            else:
                rank -= random.randint(1, 1500)
        else:
            print("Failure! Your rank decreases.")
            if diamond_tier:
                rank = rank + random.randint(1, 100)
            elif gold_tier:
                rank = rank + random.randint(1, 500)
            elif silver_tier:
                rank += random.randint(1, 1000)
            else:
                rank += random.randint(1, 1500)
    elif option == "watch":
        print("You watched. Rank remains unchanged.")
        pass
    elif option == "run":
        if difficulty >= power:
            print("You ran from a difficult situation. Rank increases.")
            rank -= random.randint(1, 500)
        else:
            print("You ran from an easy situation! Your rank decreases slightly for cowardice.")
            if diamond_tier:
                rank += random.randint(1, 50) 
            elif gold_tier:
                rank += random.randint(1, 100)
            elif silver_tier:
                rank += random.randint(1, 200)
            else: 
                rank += random.randint(1, 300)
    if rank > 10000:
        rank = 10000
    elif rank < 1:
        rank = 1
    return rank
d = 0
while rank != 1:
    current_power = 10000 - int(rank)
    random_situation = random.choice(list(situations))
    easy = random.randint(0, 3000)
    medium = random.randint(3000, 6000)
    hard = random.randint(6000, 10000)
    situation_input = input(random_situation + situations[random_situation])
    situation_input = situation_input.lower()
    if situations[random_situation] == save_options:
        while situation_input not in save:
            situation_input = input(random_situation + situations[random_situation])
    else:
        while situation_input not in fight:
            situation_input = input(random_situation + situations[random_situation])
    if difficulty[random_situation] == "easy":
        d = easy
    elif difficulty[random_situation] == "medium":
        d = medium
    else:
        d = hard
    rank = rank_calculator(rank, situation_input, d, current_power)
    print(f"Current rank: {rank}")
