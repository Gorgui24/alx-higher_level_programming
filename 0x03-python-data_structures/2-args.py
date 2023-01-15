#!/usr/bin/python3

if __name__ == "__main__":
    """Print the the sum of 1 and 2"""
    import sys
    compteur = len(sys.argv) - 1

    if compteur == 0:
        print("0 arguments.")
    elif compteur == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(compteur))
    for i in range(compteur):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
