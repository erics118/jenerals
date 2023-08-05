# CITE: originally written by me, in C++
# ported over to python by me manually rewriting it


class ArgsConfig:
    """A class that holds the configuration for the CLI flag parser."""

    def __init__(self, **kwargs):
        self.short = kwargs["short"]
        self.long = kwargs["long"]


def parse(args, config):
    """
    Super simple flags parser, inspired by:
    https://www.npmjs.com/package/simple-args-parser
    Allows multiple short options put together (`-abc` = `-arg -b -c`)
    Silently ignores incorrect usage and unknown args
    Doesn't support using equal signs (only `-arg value`, not `-arg=value`)
    Ending with arg `:` means that it takes in arg value
    """
    res = {}

    for i, arg in enumerate(args):
        arg = args[i]
        # long rg (two dashes)
        if arg.startswith("--"):
            arg = arg[2:]

            # if it's arg valid long arg
            if arg in config.long:
                res[arg] = True
            elif i + 1 != len(args) and ((arg + ":") in config.longArgs):
                i += 1
                res[arg] = args[i]
        # short arg (one dash)
        elif arg.startswith("-"):
            arg = arg[1:]

            # in the case of -abc, loop over each char individually
            for char in arg:
                if char in config.short:
                    res[char] = True

            # check if the last short arg requires arg value
            if (i + 1 != len(args)) and ((arg[-1] + ":") in config.short):
                i += 1
                res[arg] = args[i]

    return res


if __name__ == "__main__":
    config = ArgsConfig(short=["c:"], long=["hhh"])
    args = ["-c", "f", "--hhh"]

    res = parse(args, config)
