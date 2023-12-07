# An attempt to perform daily practice on a new skill.
# A focus on how I can use Python to solve problems
# through the use of coding concepts that may be new to me.

# Day 2 - Cube Conundrum

# PUZZLE PART 1 #

# Puzzle understanding - The games need to be identified where the outcomes
# are not possible based on the bags containing only 12 red cubes, 13 green cubes
# and 14 blue cubes. The IDs of the games where they are possible will need to
# be added up and provide the answer for the first part of the puzzle.


# PUZZLE PART 2 #

# Puzzle understanding - The idea is to identify the minimum number of cubes
# needed to make each game possible. Once the minimum number of cubes are ID'd,
# the 'power' is calculated by multiplying the minimum of each color against one
# another. All of the game powers are then summed together to provide the answer
# to part 2 of the puzzle.


# Variable Listing
game_ids = list()
game_powers = list()



data_day_2 = open("Data_Files\Day2.txt", "r") # Opens the data file
with data_day_2 as f:
    data = f.read().splitlines() # Presents the data in a list format (can be verified with print(type(data)))
    

def game_sets(data_input):
    """
    Used to build a dictionary of sets for each submitted game
    """
    set_counter = 1
    collected_sets = dict()
    starting_index = data_input.find(':')
    for identified_sets in data_input[starting_index + 1:].split(';'):
        working_set = dict()
        for cube_sets in identified_sets.split(','):
            color_list = list()
            for color_set in cube_sets.split():
                color_list.append(color_set)
            working_set[color_list[1]] = int(color_list[0])
            color_list = list()
        collected_sets[set_counter] = working_set
        set_counter += 1
    return collected_sets
    

def possible_games(game_num, game_sets):
    """
    Used to go through the different sets in a game
    and identify if the game as a whole is possible
    Will provide the data to solve part 1.
    """
    
    global game_ids
    successful_game = True
    
    
    def flagged_possible(number):
        if number in game_ids:
            pass
        else:
            game_ids.append(number)

    for x in game_sets.values():
        if ('blue' in x) == True:
            if x['blue'] > 14:
                successful_game = False
        if ('red' in x) == True:
            if x['red'] > 12:
                successful_game = False
        if ('green' in x) == True:
            if x['green'] > 13:
                successful_game = False
    
    if successful_game == True:
        flagged_possible(game_num)


def power_of_game(game_set_data):
    """
    Used to calculate the minimum number of each color needed
    for each game to be possible. Then multiply the max of each
    color to get the power. The power will be added for all games.
    Will provide data to solve part 2.
    """
    color_set = {'blue':0, 'red':0, 'green':0}
        
    
    for x in game_set_data.values():
        for color, amount in color_set.items():
            if (color in x) == True:
                if amount < x[color]:
                    color_set[color] = x[color]

    
    game_power = color_set['blue'] * color_set['red'] * color_set['green']
    game_powers.append(game_power)
                    
    


def main(content):
    # Identify the index of the colon
    colon_location = content.find(':')
    # Get the game ID number only
    game_id = int(content[5:colon_location])
    # Build out the dictionary of game sets
    game_content = game_sets(content)
    # Check which games are possible
    possible_games(game_id, game_content)
    # Calculate all game powers
    power_of_game(game_content)



if __name__ == "__main__":
    for game in data:
        main(game)
        
    # Add up the ID's of all the possible games
    sum_game_ids = sum(game_ids)
    # Add up the total of all game powers identified
    sum_game_powers = sum(game_powers)
    # Print solutions
    print(f"Solution to part 1: {sum_game_ids}")
    print(f"Solution to part 2: {sum_game_powers}")

    data_day_2.close()