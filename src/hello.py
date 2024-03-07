def hello(name:"World"):
    """
    A simple function to print a greeting to the screen
    """
    print("Hello, " + name)

def main():
    """
    The main logic of our program
    """
    hello()

if __name__=="__main__":
    # "if this code is called from the command line, do the following"
    main()