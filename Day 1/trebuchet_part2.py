# Open the file
with open("Day 1\\trebuchet.txt", "r") as input_file:
    lines = input_file.readlines()
    codes = []
    valid_digits = [str(x) for x in range(10)] + \
                   ["zero", "one", "two", "three", "four", 
                    "five", "six", "seven", "eight", "nine"]
    
    # Loop through the lines
    for line in lines:
        line = line.strip()

        # Find first occurence of every digit
        first_occur = {}
        for digit in valid_digits:
            if digit in line:
                first_occur[line.index(digit)] = digit

        # Find last occurence of every digit
        last_occur = {}
        for digit in valid_digits:
            if digit in line:
                last_occur[line[::-1].index(digit[::-1])] = digit

        # Get earliest and latest digits
        first_digit = first_occur[min(first_occur.keys())]
        second_digit = last_occur[min(last_occur.keys())]

        # Translate to numbers
        actual_first_digit = str(valid_digits.index(first_digit) % 10)
        actual_second_digit = str(valid_digits.index(second_digit) % 10)

        # Add the code
        codes.append(int(actual_first_digit + actual_second_digit))

    # Output
    print(sum(codes))
