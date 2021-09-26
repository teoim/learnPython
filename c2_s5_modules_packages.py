# C2 S5 modules and packages
# 1. Create and import modules - details
# 2. Documentation ( used by the help(module) function )
# 3. Packages / Python directories


# -- 1. Create and import modules - details -- #

import myfunctions_doc
import myfunctions
# when we import a module, python automatically runs it and creates the __pycache__ directory
# we don't want to see results that the imported module may display
# Solution:
# print(__name__)
# We are going to make use of the __name__ variable:
# __name__ will be "__main__" when we run this file directly;
# __name__ will be "myfunctions" when we run this code after import in a different module
#
# So when we have code that we don't want to be ran from modules that import our module,
# we can put it under: if __name__ == '__main__': ...

l = [10, 20, 30, 40, 50, 60, 70, 80]
key = 70
print("result1:", myfunctions.binsearch(l, key), "- Expected: True")
key = 5
print("result2:", myfunctions.binsearch(l, key), "- Expected: False")
key = 100
print("result3:", myfunctions.binsearch(l, key), "- Expected: False")


# -- 2. Documentation ( used by the help(module) function ) -- #

# PYTHON help() DOCUMENTATION
#help(myfunctions)  # Will print some random stuff from myfunctions.py
# Created myfunctions_doc.py as a copy of myfunctions.py
# Added documentation to myfunctions_doc, to show difference from myfunctions

help(myfunctions_doc)


# -- 3. Packages / Python directories -- #

# Packages are just python directories
# All you have to do is to create an empty "__init__.py" file, in the same folder structure
# Once you create this file, that folder will be considered a python directory
