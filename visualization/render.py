"""Draw the worked winning selection from a rotating 3D camera."""

from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 800, 480
INK, MUTED = "#f3f7ff", "#b9cae4"
BG, PANEL = "#101b2e", "#182942"
CYAN, ORANGE = "#80e8cf", "#ffc185"
BLUE = "#7799c8"
PATH = [(-2.1, .23), (-1.10, -.30), (0, .14), (1.10, -.25), (2.1, .23)]
TOPS = ["y", "z", "p", "x", "x"]
CHOICES = [(1, "A · L"), (3, "B · R"), (1, "C · L")]


def font(name, size):
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default(size=size)


def project(x, y, z, angle):
    u = x*cos(angle) - y*sin(angle)
    depth = x*sin(angle) + y*cos(angle)
    up = z*cos(.31) - depth*sin(.31)
    zoom = 9/(9-depth*cos(.31)-z*sin(.31))
    return 457+u*104*zoom, 256-up*89*zoom, depth


def render(angle, fonts):
    title, label, small, strong = fonts
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.text((28, 22), "Three paths, one winning choice", font=title, fill=INK)
    draw.rounded_rectangle((26, 91, 774, 408), 14, fill=PANEL)
    for row, (leader, name) in enumerate(CHOICES):
        z = (1-row)*1.10
        points = [project(x,y,z,angle) for x,y in PATH]
        picked = set(range(leader-1, leader+2))
        draw.text((44, 141+94*row), name, font=label, fill=INK)
        for i in range(4):
            fill = CYAN if i in picked and i+1 in picked else BLUE
            draw.line([points[i][:2], points[i+1][:2]], fill=fill, width=5)
        for i in sorted(range(5), key=lambda j: points[j][2]):
            x,y,_ = points[i]
            fill = ORANGE if i == leader else CYAN if i in picked else BLUE
            draw.ellipse((x-16,y-16,x+16,y+16), fill=fill, outline=PANEL,width=2)
            draw.text((x,y-1), TOPS[i], fill=BG, font=small, anchor="mm")
    draw.text((30, 423), "p = g = 9", font=strong, fill=CYAN)
    draw.text((264, 432), "A and C supply the matching.", font=label, fill=INK)
    return image


def main():
    fonts = (font("Arial Bold.ttf", 43),font("Arial.ttf",30),
             font("Arial Bold.ttf",22),font("Arial Bold.ttf",42))
    frames = [render(-.49+.72*sin(tau*i/72),fonts) for i in range(72)]
    frames[0].save(Path(__file__).with_name("five-voter-paths.gif"), save_all=True,
                   append_images=frames[1:], duration=84, loop=0, optimize=False)


if __name__ == "__main__":
    main()
