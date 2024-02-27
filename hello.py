def main():
    hello()
    name = input("Whats your name? \n")
    hello(name)

def hello(uname="world"):
    

    # Remove whitespace from str using functions : strip()
    # Capitalize user's name based on each word : title()
    uname = uname.strip().title()


    #say hello to user
    print(f'Hello,', uname)




main()
