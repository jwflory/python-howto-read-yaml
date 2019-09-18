#!/usr/bin/env python3
"""
A brief introduction to Python data objects. Refer to official Python docs or
other online resources for more detailed explanations.

list:
  - one
  - two
  - three

list[0]   -> return str
list[1]   -> return str

dict:
  - "one": "first number"
  - "two": "second number"
  - "three": "third number"
  - "four": "obj1,obj2,obj3,obj4"

dict[0].key()    -> returns str
dict[3].value()  -> returns List
"""

import random
import yaml

# Load config file
with open("test.yml") as f:
    config = yaml.safe_load(f)

# What does this actually look like under the hood?
print("An internal representation of test.yml with a list inside of a dict:\n"
      + str(config) + "\n")

# Ask the user if they like a random food from our list
print("Do you like {}?".format(random.choice(config["favorite_foods"])))

# Potatos?
print("What about {}?".format(config["favorite_foods"][0]))

# How about a couple foods?
print("Or, there is always {} and {}.".format(
    config["favorite_foods"][1],
    config["favorite_foods"][2])
)

# I brought you a surprise...
print("I knew you liked {0}, so I brought you ten boxes of {0}.".format(
    config["favorite_foods"][3])
)
