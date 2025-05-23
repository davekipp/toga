from System.Drawing import Color
from travertino.colors import TRANSPARENT, rgba

CACHE = {TRANSPARENT: Color.Transparent}


def native_color(c):
    try:
        color = CACHE[c]
    except KeyError:
        color = Color.FromArgb(
            int(c.rgba.a * 255),
            int(c.rgba.r),
            int(c.rgba.g),
            int(c.rgba.b),
        )
        CACHE[c] = color

    return color


def toga_color(c):
    return rgba(c.R, c.G, c.B, c.A / 255)
