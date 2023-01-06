"""Program calculates monthly salary of employees from a csv file."""
from taxer import taxer

fh_input = open("salaries.csv", "r")  # open input file
fh_output = open("salaries_tax.csv", "w")  # open output file

for line in fh_input:
    line = line.strip()  # remove whitespace(newline character) at end of line
    name, salary = line.split(",")  # split line by comma and store results in variables name and salary.
    tax, net = taxer(float(salary))  # calculate tax and net income and store results in variables tax and net
    fh_output.write(name + "," + salary + ", " + str(tax) + ", " + str(net) + "\n")  # write results to output file

# close files
fh_input.close()
fh_output.close()
