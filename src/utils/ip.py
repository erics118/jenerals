import socket


# CITE: code modified from https://stackoverflow.com/a/28950776
def getLocalIp():
    """Get the IP address of the current machine."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # doesn't have to be reachable
        sock.connect(("203.0.113.0", 1))
        ip = sock.getsockname()[0]
    except socket.error:
        ip = "0.0.0.0"
    finally:
        sock.close()

    # should work when on the same local network
    return ip
    # if with tailscale
    # return "100.64.81.124"


def encodeIp(ip):
    """Encode an IP address into a nice, human-readable format."""

    parts = ip.split(".")
    encodedParts = []
    for part in parts:
        part = int(part)
        tensPlace = part // 26
        onesPlace = part % 26
        encodedPart = chr(tensPlace + 97) + chr(onesPlace + 97)
        encodedParts.append(encodedPart)
    return "".join(encodedParts)


def decodeIp(encodedIp):
    """Decode an IP address from a nice, human-readable format."""

    parts = [encodedIp[i : i + 2] for i in range(0, len(encodedIp), 2)]
    decodedParts = []
    for part in parts:
        tensPlace = ord(part[0]) - 97
        onesPlace = ord(part[1]) - 97
        decodedPart = tensPlace * 26 + onesPlace
        decodedParts.append(str(decodedPart))
    return ".".join(decodedParts)
