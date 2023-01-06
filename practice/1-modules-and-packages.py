"""
 Script that imports two modules from a newly-created package located in one of the directories specified by sys.path
 package: my_package
 modules: hello, goodbye
     Each module contains a fruitless function greet.
"""

# importing entire package
import my_package


# importing hello and goodbye module from package (dot syntax)
import my_package.hello
import my_package.goodbye


# importing hello and goodbye module from package (without dot syntax)
from my_package import hello
from my_package import goodbye


# importing functions from modules in package
from my_package.hello import greet
from my_package.goodbye import greet

greet()  # selects greet() from last import statement.


# importing with aliases
import my_package as pkg
from my_package import hello as h
from my_package.hello import greet as g

# all statements access greet function with aliases
pkg.hello.greet()
h.greet()
g()

import sys
print(sys.path)  # Print all directories where Python looks for modules
