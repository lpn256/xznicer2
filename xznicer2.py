#!/usr/bin/python3
import argparse
import lzma
import os
import threading


results = []


def xznicer2(inputfile):
    totalsteps = 0
    nicevalues = list(range(2, 274))
    for idx, nice in enumerate(nicevalues):
        outputfile = f"/tmp/{inputfile}.nice{nice}.xz"  # Improved naming
        t1 = threading.Thread(target=execnicer, args=(inputfile, outputfile, nice))
        t1.start()
        t1.join()
        totalsteps+=1
        print(f"Steps: {totalsteps}/272")

    results.sort(key=lambda x: x[0])
    for row in results:
        print(row)
    print("Best choice:")
    best = results[0]
    print(f"nice={best[1]}, Uses {best[0]} bytes")
    execnicer(inputfile, f"{inputfile}.nice{best[1]}.xz", nice)


def execnicer(inputfile, outputfile, nice):
    with open(inputfile, "rb") as fin:  # read bytes mode
        bytes = fin.read()
    cbytes = lzma.compress(bytes, filters=[{
        "id": lzma.FILTER_LZMA2, "nice_len": nice, "dict_size": 2**20, "lc": 0, "lp": 0, "pb": 0, "mode": lzma.MODE_NORMAL, "preset": 9
    }])
    cbytes += lzma.LZMACompressor().flush()
    with lzma.open(outputfile, "w") as fout:
        fout.write(cbytes)
    size = os.path.getsize(outputfile)
    results.append((size, str(nice)))


def main():
    parser = argparse.ArgumentParser(
        description="Optimize LZMA2 compression using the 'xz' tool"
    )
    parser.add_argument("-i", "--inputfile", required=True, help="Input file to compress")
    args = parser.parse_args()

    if not args.inputfile:
        print("No input file given")
        return

    xznicer2(args.inputfile)  # Pass inputfile directly


if __name__ == "__main__":
    main()
