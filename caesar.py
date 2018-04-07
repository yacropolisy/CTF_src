import sys

def rot_n(c, n):
    if 'a' <= c and c <= 'z':
        return chr((ord(c) - ord('a') + int(n)) % 26 + ord('a'))

    if 'A' <= c and c <= 'Z':
        return chr((ord(c) - ord('A') + int(n)) % 26 + ord('A'))

    return c

def rot(s, n):
    c = (rot_n(c, n) for c in s)
    print(''.join(c))

if __name__ == '__main__':
    param = sys.argv
    s = param[1]
    r = param[2]
    rot(s, r)
