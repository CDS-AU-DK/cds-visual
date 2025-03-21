from argparse import ArgumentParser

def arg_parser():
    parser = ArgumentParser(description="Gets name variables")
    parser.add_argument("--name",
                        required=True,
                        help="Please enter a valid name!")
    args = parser.parse_args()

    return args

def hello(name):
    print(f"Hello, {name}!")

def main():
    """
    The main logic of our code
    """
    args = arg_parser()
    hello(args.name)

if __name__=="__main__":
    # "if this code is called from the command line, do the following"
    main()
