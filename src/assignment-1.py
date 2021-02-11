#!/usr/bin/env python
"""
Load image, find height and width, save output
Parameters:
    path: str <path-to-image-dir>
    outfile: str <filename-to-save-results>
Usage:
    assignment1.py --image <path-to-image>
Example:
    $ python assignment1.py --path data/img --outfile results.csv
## Task
- Save csv showing height and width of every image in a directory
"""

import os
from pathlib import Path
import argparse

# Define main function
def main():
    # Initialise ArgumentParser class
    ap = argparse.ArgumentParser()
    # CLI parameters
    ap.add_argument("-i", "--path", required=True, help="Path to data folder")
    ap.add_argument("-o", "--outfile", required=True, help="Output filename")
    # Parse arguments
    args = vars(ap.parse_args())

    # Output filename
    out_file_name = args["outfile"]
    # Create directory called out, if it doesn't exist
    if not os.path.exists("out"):
        os.mkdir("out")

    # Output filepath
    outfile = os.path.join("out", out_file_name)
    # Create column headers
    column_headers = "filename,height, width"
    # Write column headers to file
    with open(outfile, "a", encoding="utf-8") as headers:
        # add newling after string
        headers.write(column_headers + "\n")

    # Create explicit filepath variable
    filenames = Path(args["path"]).glob("*.jpg")
    # Iterate over images
    for image in filenames:
        # load image
        image = cv2.imread(image)
        (height, width, channels) = image.shape
        # Get novel name
        name = os.path.split(novel)[1]
        # Formatted string
        out_string = f"{name}, {height}, {width}"
        # Append to output file using with open()
        with open(outfile, "a", encoding="utf-8") as results:
            # add newling after string
            results.write(out_string+"\n")
        
# Define behaviour when called from command line
if __name__=="__main__":
    main()