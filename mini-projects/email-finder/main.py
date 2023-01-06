"""script for finding all email addresses in a text file if any"""
from re import search
from re import findall

text_fh = open("text-files/email-text.txt")  # text file to be searched.
text = text_fh.read()

if search("\S+@\S+", text):  # check for presence of email address.
    addresses = findall("\S+@\S+", text)  # generate list of all found email addresses.
    print(f"{len(addresses)} emails found:")

    for address in addresses:  # print all found email addresses.
        print(address)
else:
    print("No emails found.")

text_fh.close()
