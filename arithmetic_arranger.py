def arithmetic_arranger(problems):
    # Initialize empty strings for each line in the arranged problems
    line1 = line2 = line3 = line4 = ""

    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Iterate through each problem in the list
    for problem in problems:
        # Split the problem into its components (number1, operator, number2)
        num_1, op, num_2 = problem.split()

        try:
            # Convert numbers to integers
            num_1 = int(num_1)
            num_2 = int(num_2)

            # Check if numbers are within the specified range
            if num_1 <= 9999 and num_2 <= 9999:

                # Perform the operation based on the operator
                if op == "+":
                    solution = str(int(num_1) + int(num_2))
                elif op == "-":
                    solution = str(int(num_1) - int(num_2))
                else:
                    return "Error: Operator must be '+' or '-'."

            else:
                return "Error: Numbers cannot be more than four digits."

        except ValueError:
            return "Error: Numbers must only contain digits."

        # Calculate the width needed for formatting
        width = max(len(str(num_1)), len(str(num_2))) + 2

        # Build each line of the arranged problem
        line1 += str(num_1).rjust(width) + "    "
        line2 += op + " " + str(num_2).rjust(width - 2) + "    "
        line3 += "-" * width + "    "

        # Include the solution line if it's calculated
        if 'solution' in locals():
            line4 += str(solution).rjust(width) + "    "

    # Combine all lines to form the arranged problems
    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    if line4:
        arranged_problems += "\n" + line4.rstrip()

    return arranged_problems
