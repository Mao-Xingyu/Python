#Ask user for an input (for their name)
name = input("What's your name? \n")

# Remove whitespace from str using functions : strip()
# Capitalize user's name based on each word : title()
name = name.strip().title()


#say hello to user
print(f'Hello, {name}')