# Open the file
with open("Day 1\\trebuchet.txt", "r") as input_file:
    lines = input_file.readlines()
    codes = []

    # Process each line
    for line in lines:
        line = line.strip()
        code = ""

        # Extract first digit
        for char in line:
            if char.isdigit():
                code += char
                break

        # Extract last digit
        for char in line[::-1]:
            if char.isdigit():
                code += char
                break

        # Add code to list
        codes.append(int(code))

    # Output
    print(sum(codes))
