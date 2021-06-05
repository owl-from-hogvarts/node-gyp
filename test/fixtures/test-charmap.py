import sys
import locale
from importlib import reload

try:
    reload(sys)
except NameError:  # Python 3
    pass


def main():
    encoding = locale.getdefaultlocale()[1]
    print(encoding, file=sys.stderr)
    print("Lat\u012Bna", file=sys.stderr)
    if not encoding:
        return False

    try:
        sys.setdefaultencoding(encoding)
    except AttributeError:  # Python 3
        pass

    textmap = {
        "cp936": "\u4e2d\u6587",
        "cp1252": "Lat\u012Bna",
        "cp932": "\u306b\u307b\u3093\u3054",
    }
    if encoding in textmap:
        print(textmap[encoding])
    return True


if __name__ == "__main__":
    print(main())
