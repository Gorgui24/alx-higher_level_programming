#!/usr/bin/python3

if __name__ == "__main__":
    """Print the the sum of 1 and 2"""
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
