#!/usr/bin/python3
import argparse
import lzma

def xznicer(inputfile):
    nicevalue = 200
    output_filename = f"{inputfile}.nice{nicevalue}.xz"  # Improved naming
    with open(inputfile, "rb") as f_in:
        data = f_in.read()
    with lzma.open(output_filename, "w") as f_out:
        f_out.write(data)

def main():
    parser = argparse.ArgumentParser(
        description="Optimize LZMA2 compression using the 'xz' tool"
    )
    parser.add_argument("-i", "--inputfile", required=True, help="Input file to compress")
    args = parser.parse_args()

    if not args.inputfile:
        print("No input file given")
        return

    xznicer(args.inputfile)  # Pass inputfile directly

if __name__ == "__main__":
    main()
