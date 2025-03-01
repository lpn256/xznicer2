#!/usr/bin/python3
import argparse
import lzma

def xznicer(inputfile, nice):
    output_filename = f"{inputfile}.nice{nice}.xz"  # Improved naming
    with open(inputfile, "rb") as fin:  # read bytes mode
        bytes = fin.read()
    cbytes = lzma.compress(bytes, filters=[{
    "id": lzma.FILTER_LZMA2, "nice_len": nice, "dict_size": 2**20, "lc": 3, "lp": 0, "pb": 2, "mode": lzma.MODE_FAST
    }])
    cbytes += lzma.LZMACompressor().flush()
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

    xznicer(args.inputfile, 100)  # Pass inputfile directly

if __name__ == "__main__":
    main()
