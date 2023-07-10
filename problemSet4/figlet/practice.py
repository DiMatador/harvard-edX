''' using sys and argv to get cmd-line inputs from user'''

# imports
from sys import argv

script, user_name = argv
# reuseable veriable
prompt = '> '

print(F"Hi {user_name}! I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(F"Do you like me {user_name}?")
likes = input(prompt)

print(F"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(F'''
Alright, so you said {likes} about liking me>
You live in {lives}. Not sure where that is
And you have a {computer} computer. Nice!!.
''')
