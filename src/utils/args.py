import argparse


def parseArgs():
    """Get command line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d", "--dev", help="enable developer shortcuts", action="store_true"
    )

    return parser.parse_args()
