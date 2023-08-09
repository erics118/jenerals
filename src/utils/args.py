import argparse


def parseArgs():
    """Get command line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--dev", action="store_true")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--primary", action="store_true")
    group.add_argument("--secondary", action="store_true")

    parser.add_argument("--code", type=str, required=False)

    args = parser.parse_args()

    return args
