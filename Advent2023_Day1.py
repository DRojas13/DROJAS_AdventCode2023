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
    global calibration_values
    numbers_only = list()

    # Cycle through the full string and identify all numbers in the order they appear
    for character in line_of_text:
        if character.isdigit() == True:
            numbers_only.append(character)
            
    combined_value = numbers_only[0] + numbers_only[-1]
        
    # Add the two digit number to the global list
    calibration_values.append(int(combined_value))
    
            
def total_of_calibration_values(values_list, part):
    """
    Function used to generate the sum of values for the extracted calibrations
    """
    sum_total = 0
    
    for value in values_list:
        sum_total += value
    
    print(f"The calibration values sum for part {part} is - {sum_total}")



def main():
    """
    Main function to runn all of the different sets of code
    """
    global calibration_values
    
    # Part 1 is addressed here
    for content in data:
        calibration_extractor(content)
    
    total_of_calibration_values(calibration_values, 'ONE')
    
    # Part 2 is addressed here

    total_of_calibration_values(calibration_values, 'ONE')

    



if __name__ == "__main__":
    main()
    data_day_1.close() # Close out the document