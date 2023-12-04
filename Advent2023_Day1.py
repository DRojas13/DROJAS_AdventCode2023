# An attempt to perform daily practice on a new skill.
# A focus on how I can use Python to solve problems
# through the use of coding concepts that may be new to me.

# Day 1 - Trebuchet?!

# PUZZLE PART 1 #

# Puzzle understanding - There is a series of lines of alphanumeric text
# the application needs to combine the first digit and the last digit
# to create a two digit value. Once all of the two digit numbers have been
# identified, then all of the values will need to be summed.
# The sum value is the desired input for the puzzle.

# Variable collective
calibration_values = list() # Target list for all of my extracted values


data_day_1 = open("Data_Files\Day1.txt", "r") # Opens the data file
with data_day_1 as f:
    data = f.read().splitlines() # Presents the data in a list format (can be verified with print(type(data)))


def calibration_extractor(line_of_text):
    """
    Function receives a line of text and goes through each value in the line from first first
    then will go from the back until a numeric value is identified.
    """
    first_value = 0
    second_value = 0
    counter = -1
    
    first_value_found = False
    second_value_found = False
    
    while first_value_found == False:
        for character in line_of_text:
            if character.isdigit() == True:
                first_value_found = int(charcter)
                first_value_found = True

    while second_value_found == False:
        if character[counter].isdigit() == True:
            second_value = int(character[counter])
            second_value_found = True
        else:
            counter -= 1



def main():
    """
    Main function to runn all of the different sets of code
    """
    pass



if __name__ == "__main__":
    main()
    data_day_1.close() # Close out the document