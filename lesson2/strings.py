name = "Michael"

# print(type(name))
# print(name[1])

# String slicing uses list notation to select items from a string based on their index
# Eg: string[start_index: end_index]
word = "pineapple"
#print(word[-5:])

# reorder word in reverse order
reverse_word = word[::-1]

# upper and lower case letters
upper_word = word.upper() # Upper case letters
lower_word = word.lower() # Lower case letters
initial_caps = word.capitalize() # Make the first letter capital

capitalise_last = word[:-1] + word[-1].capitalize()

# split words and make changes and join them again
word_split = list(word)
capitalise_last_word = ("").join(word_split[:-1]) + word_split[-1].capitalize()

# Print each letter in word separated by space
spaced_word = ",".join(word)

user_detail = "Michael,Okolo,30,Gaming" # CSV (Comma separated Values)
spit_user_detail = user_detail.split(",")

# print(" ".join(spit_user_detail))

# String Operations - Interpolation
name = "Michael"

print("Hello! " + name + " Welcome to Programming")
print("Hello! {} Welcome to Programming".format(name))
print(f"Hello! {name} Welcome to Programming")