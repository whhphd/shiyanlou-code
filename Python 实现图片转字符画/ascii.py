import itertools

from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output', default='output.txt')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

args = parser.parse_args()

IMG = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    gray_num = 0.2126 * r + 0.7152 * g + 0.0722 * b
    seq = int((gray_num / 255) * (len(ascii_char) - 1))

    return ascii_char[seq]


if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    with open(OUTPUT, 'w') as f:
        f.write(txt)

