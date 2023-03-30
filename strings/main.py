# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# PART 1

# 1. Create a variable for every player that scored
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

# 2. Create a variable for each minute of the match that a goal was scored in
goal_0 = 32
goal_1 = 54

# 3. Using the +-operator, create a string that reports on who scored when, according to the format
#    <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)

print(scorers)

# 4. Use f-strings or the +-operator to create a single string with information about who scored when in the format:
#    <scorer_name> scored in the <when_they_scored>nd minute.
#    <scorer_name> scored in the <when_they_scored>th minute.
report = f"{scorer_0} scored in the {goal_0}nd minute" '\n' f"{scorer_1} scored in the {goal_1}th minute"
#! Wincpy geeft een fail als ik het in één regel zet. Daarom heb ik er twee regels van gemaakt. Nu geeft hij wel een pass.

print(report)

# PART 2
# Store the following values in the given variable. You can create temporary variables, like last_name to help you.

# 1.  Choose a player that played in the soccer match and store his name as a string in the variable player.
player = 'Frank Rijkaard'

# 2. first_name: use slicing and the find-method to isolate and store the player's first name.
first_name_len = player.find(' ')
first_name = player[:first_name_len]

# 3. last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_len = len(player) - len(first_name) - 1

# 4. name_short: isolate and store the player's name in this format:
#    G. von Examplestein
last_name = player[(first_name_len + 1):]
name_short = first_name[:1] + '. ' + last_name

# 5. chant: this is what the crowd chants when it looks like your player is going to score a goal --
#    their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name.
#    Because Gut has 3 letters in his name, we repeat his name 3 times.
#    Make sure the last character of this string is not a space! For our example player:
#    Gut! Gut! Gut!
chant_long = (first_name + '! ') * len(first_name)

# 6. good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=).
#    This variable needs to be a boolean, not a string. You can create the value for this variable by comparing
#    the last character of chant with a space character. Try this in your REPL for an example: print(2 != 3).
#    Also try: print(2 != 2).

chant = chant_long[0:-1]

print(chant)

good_chant = chant != ' '

print(good_chant)

# Wincpy Check

# Use wincpy check strings to see if you met all of the requirements for this assignment. Did you pass the test?
