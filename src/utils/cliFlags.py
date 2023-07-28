# originally written by me, in C++
# ported over to python by manually rewriting it


class ArgsConfig:
    def __init__(self, **kwargs):
        self.short = kwargs["short"]
        self.long = kwargs["long"]


# super simple flags parser, inspired by: https://www.npmjs.com/package/simple-args-parser
# - allows multiple short options put together (`-abc` = `-a -b -c`)
# - silently ignores incorrect usage and unknown args
# - doesn't support using equal signs (only `-a value`, not `-a=value`)
# - ending with a `:` means that it takes in a value
def parse(args, config):
    res = dict()
    for i in range(len(args)):
        a = args[i]
        # long arg (two dashes)
        if a.startswith("--"):
            a = a[2:]
            # if it's a valid long arg
            if a in config.long:
                res[a] = True
            elif i + 1 != len(args) and ((a + ":") in config.longArgs):
                i += 1
                res[a] = args[i]
        # short arg (one dash)
        elif a.startswith("-"):
            a = a[1:]
            # in the case of -abc, loop over each char individually
            for ch in a:
                if ch in config.short:
                    res[ch] = True
            # check if the last short arg requires a value
            if (i + 1 != len(args)) and ((a[-1] + ":") in config.short):
                i += 1
                res[a] = args[i]

    return res


if __name__ == "__main__":
    config = ArgsConfig(
        short=["c:"],
        long=["hhh"],
    )
    args = ["-c", "f", "--hhh"]

    res = parse(args, config)
