import os
import argparse
import numpy as np

def file_loader():
    parser = argparse.ArgumentParser(description="Loading and printing an array")
    parser.add_argument("--input",
                        "-i",
                        required=True,
                        help="Filepath to CSV for loading and printing")
    args = parser.parse_args()
    return args

def process(filename):
    data = np.loadtxt(filename, delimiter=",")
    print(data)

def main():
    args = file_loader()
    filename = os.path.join("..",
                            "..",
                            "cds-vis-data",
                            "data",
                            "sample-data",
                            args.input)
    process(filename)
    
if __name__=="__main__":
    main()