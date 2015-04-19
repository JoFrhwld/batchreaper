import os
import glob
import subprocess
import argparse

class DirectoryException(Exception):
    '''Problem with output directory'''
    pass

def check_outdir(outdir):
    '''Checks to see if there is an output directory'''
    if not os.path.exists(outdir):
        raise DirectoryException("No such directory %s"%outdir)
    elif not os.path.isdir(outdir):
        raise DirectoryException("%s is not a directory"%outdir)

def setup_parser():
    '''set up argument parser'''
    parser = argparse.ArgumentParser(description = ("batch processes audio "
                                                    "files with reaper"),
                                     fromfile_prefix_chars="+")
    parser.add_argument("input")
    parser.add_argument("output")

    return parser


def batchreaper(input, output):
    check_outdir(output)

    audios = glob.glob(os.path.join(input, "*.wav"))
    basenames = [os.path.splitext(os.path.basename(x))[0] for x in audios]
    outf0 = [os.path.join(output, x) for x in [x+".f0" for x in basenames]]
    outpoints = [os.path.join(output, x) for x in [x+".points" for x in basenames]]

    triplet = zip(audios, outf0, outpoints)

    for infile, f0, points in triplet:
        subprocess.call(["reaper", "-i", infile, "-f", f0, 
                        "-p", points, "-m", "20",
                        "-a"])
    
if __name__ == '__main__':
    parser = setup_parser()
    opts = parser.parse_args()

    batchreaper(opts.input, opts.output)