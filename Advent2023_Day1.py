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
part2_calibration_values = list() # Target list for extracted values for part 2


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


def part2_calibration_extractor(line_of_text):
    """
    Function used to re-evaluate the data file text for part 2 of the puzzle.
    The new parameters include words for numbers amongst the number values.
    """
    text_number_list = ['one','two','three','four','five','six','seven','eight','nine']
    identified_numbers = dict()
    index_start = -1
    

    for index, value in enumerate(line_of_text):
        if value.isdigit() == True:
            identified_numbers[index] = value

    # Checking the word versions of the numbers in the strings
    for number in text_number_list:
        testing = number in line_of_text
        if testing == True:
            # check for each instance of the found word and its index
            while True:
                index_start = line_of_text.find(number, index_start + 1)
                if index_start == -1:
                    break
                else:
                    identified_numbers[index_start] = str(text_number_list.index(number) + 1)
    
    # Take the newly created dictionary and sort based on the key        
    sortedList = dict(sorted(identified_numbers.items()))
    # Create a list of the values from the sorted dictionary
    values_only = list(sortedList.values())
    # Create the combined value based on the sorted list
    combined_value = values_only[0] + values_only[-1]
    # Add the two digit number to the global list
    part2_calibration_values.append(int(combined_value))
    # input()
    
            
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
    for part_2_content in data:
        part2_calibration_extractor(part_2_content)

    
    total_of_calibration_values(part2_calibration_values, 'TWO')

    



if __name__ == "__main__":
    main()
    data_day_1.close() # Close out the document