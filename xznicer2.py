#!/usr/bin/python3
import argparse
import lzma

def xznicer(inputfile, nice):
    output_filename = f"{inputfile}.nice{nice}.xz"  # Improved naming
    with open(inputfile, 'rb') as fin:  # read bytes mode
        bytes = fin.read()
    lzc = lzma.LZMACompressor()
    cbytes = lzc.compress(bytes)
    cbytes += lzc.flush()
    with lzma.open(output_filename, "w") as fout:
        fout.write(cbytes)

def main():
    parser = argparse.ArgumentParser(
        description="Optimize LZMA2 compression using the 'xz' tool"
    )
    parser.add_argument("-i", "--inputfile", required=True, help="Input file to compress")
    args = parser.parse_args()

    if not args.inputfile:
        print("No input file given")
        return

    xznicer(args.inputfile, 200)  # Pass inputfile directly

if __name__ == "__main__":
    main()
