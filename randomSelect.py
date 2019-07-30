import os, random
import argparse
from shutil import copyfile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--input', help='Path of input folor.',required=True)
    parser.add_argument(
            '--output', help='Path of output folder.',required=True)
    parser.add_argument(
            '--number', help='number of selecting files.')
    args = parser.parse_args()

    if not args.number:
        SelectNumber = 100
    else:
        SelectNumber = args.number


    for x in range(int(SelectNumber)):
        files = os.listdir(args.input)
        index = random.randrange(0,len(files))
        src = args.input + files[index]
        dst = args.output + files[index]
        copyfile(src,dst)

if __name__ == '__main__':
    main()

