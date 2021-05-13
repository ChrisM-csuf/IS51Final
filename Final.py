"""
--- STRUCTURED ENGLISH ---


this program will take a set of grades (integers) from file "final.txt"
using this data, we will first return the number of lines found in the file
using that we will calculate the average grade
given the average grade, we will calculate the percent of grades that are higher than the average
"""

"""
--- PSEUDO-CODE ---
def main():
    open Final.txt as infile
    assign the lines of the list to list
    close input file
    calculate_percent_above_average(lines)


def calculate_percent_above_average():
    num_of_lines = len(lines)
    sum = sum(lines)
    average = sum/ num_of_lines

    iterate through lines:
        if the current line is greater than average:
            above_average += 1

    percent_above_average = above_average / num_of_lines
    print(percent_above_average)
"""

def main():
    with open('Final.txt') as infile:
        lines = infile.readlines()
        infile.close()
    calculate_percent_above_average(lines)


def calculate_percent_above_average(input):
    for i in range(len(input)):
        input[i] = int(input[i])

    num_of_lines = len(input)
    Sum = sum(input)
    average = Sum / num_of_lines
    
    above_average = 0
    for i in range(len(input)):
        if input[i] > average:
            above_average += 1

    percent_above_average = (above_average / num_of_lines) * 100
    percent_above_average = round(percent_above_average, 2)

    print(f"{num_of_lines} Provided")
    print(f"The Average Grade was a {average}%")
    print(f"{percent_above_average}% grades were higher than the average")

main()