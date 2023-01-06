import re

fh = open("table-of-contents.txt")

for line in fh:
    if re.search("^Chapter", line):
        print(re.findall("^Chapter ([0-9]+ .+) [0-9]+", line)[0])

fh.close()
