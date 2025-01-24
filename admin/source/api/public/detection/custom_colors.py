from dataclasses import dataclass
from typing import TypedDict
from reportlab.lib.colors import Color


@dataclass
class CustomColor:
    name: str
    rgb: Color


colors: list[CustomColor] = [
    CustomColor("Dark Red", Color(139 / 255, 0 / 255, 0 / 255, 1)),
    CustomColor("Dark Green", Color(0 / 255, 100 / 255, 0 / 255, 1)),
    CustomColor("Dark Blue", Color(0 / 255, 0 / 255, 139 / 255, 1)),
    CustomColor("Dark Yellow", Color(204 / 255, 204 / 255, 0 / 255, 1)),
    CustomColor("Dark Cyan", Color(0 / 255, 139 / 255, 139 / 255, 1)),
    CustomColor("Dark Magenta", Color(139 / 255, 0 / 255, 139 / 255, 1)),
    CustomColor("Navy", Color(0 / 255, 0 / 255, 128 / 255, 1)),
    CustomColor("Charcoal", Color(54 / 255, 69 / 255, 79 / 255, 1)),
    CustomColor("Midnight Blue", Color(25 / 255, 25 / 255, 112 / 255, 1)),
    CustomColor("Olive", Color(128 / 255, 128 / 255, 0 / 255, 1)),
    CustomColor("Maroon", Color(128 / 255, 0 / 255, 0 / 255, 1)),
    CustomColor("Forest Green", Color(34 / 255, 139 / 255, 34 / 255, 1)),
    CustomColor("Saddle Brown", Color(139 / 255, 69 / 255, 19 / 255, 1)),
    CustomColor("Dark Slate Gray", Color(47 / 255, 79 / 255, 79 / 255, 1)),
    CustomColor("Dark Orchid", Color(153 / 255, 50 / 255, 204 / 255, 1)),
    CustomColor("Dark Goldenrod", Color(184 / 255, 134 / 255, 11 / 255, 1)),
    CustomColor("Dark Turquoise", Color(0 / 255, 206 / 255, 209 / 255, 1)),
    CustomColor("Dark Violet", Color(148 / 255, 0 / 255, 211 / 255, 1)),
    CustomColor("Dark Khaki", Color(189 / 255, 183 / 255, 107 / 255, 1)),
    CustomColor("Chocolate", Color(210 / 255, 105 / 255, 30 / 255, 1)),
    CustomColor("Dark Sea Green", Color(143 / 255, 188 / 255, 143 / 255, 1)),
    CustomColor("Dim Gray", Color(105 / 255, 105 / 255, 105 / 255, 1)),
    CustomColor("Steel Blue", Color(70 / 255, 130 / 255, 180 / 255, 1)),
    CustomColor("Slate Blue", Color(106 / 255, 90 / 255, 205 / 255, 1)),
    CustomColor("Indigo", Color(75 / 255, 0 / 255, 130 / 255, 1)),
    CustomColor("Purple", Color(128 / 255, 0 / 255, 128 / 255, 1)),
    CustomColor("Royal Blue", Color(65 / 255, 105 / 255, 225 / 255, 1)),
    CustomColor("Dark Slate Blue", Color(72 / 255, 61 / 255, 139 / 255, 1)),
    CustomColor("Black", Color(0 / 255, 0 / 255, 0 / 255, 1)),
    CustomColor("Brown", Color(165 / 255, 42 / 255, 42 / 255, 1)),
    CustomColor("Crimson", Color(220 / 255, 20 / 255, 60 / 255, 1)),
    CustomColor("Teal", Color(0 / 255, 128 / 255, 128 / 255, 1)),
    CustomColor("Antique White", Color(250 / 255, 235 / 255, 215 / 255, 1)),
    CustomColor("Beetroot", Color(142 / 255, 33 / 255, 27 / 255, 1)),
    CustomColor("Forest", Color(34 / 255, 77 / 255, 56 / 255, 1)),
    CustomColor("Gunmetal", Color(42 / 255, 52 / 255, 57 / 255, 1)),
    CustomColor("Onyx", Color(53 / 255, 56 / 255, 57 / 255, 1)),
    CustomColor("Coal", Color(51 / 255, 50 / 255, 49 / 255, 1)),
    CustomColor("Ebony", Color(85 / 255, 93 / 255, 80 / 255, 1)),
    CustomColor("Sapphire", Color(15 / 255, 82 / 255, 186 / 255, 1)),
    CustomColor("Emerald", Color(80 / 255, 200 / 255, 120 / 255, 1)),
    CustomColor("Auburn", Color(165 / 255, 42 / 255, 42 / 255, 1)),
    CustomColor("Burgundy", Color(128 / 255, 0 / 255, 32 / 255, 1)),
    CustomColor("Tamarind", Color(144 / 255, 93 / 255, 49 / 255, 1)),
    CustomColor("Claret", Color(127 / 255, 23 / 255, 52 / 255, 1)),
    CustomColor("Grape", Color(111 / 255, 45 / 255, 168 / 255, 1)),
    CustomColor("Plum", Color(142 / 255, 69 / 255, 133 / 255, 1)),
    CustomColor("Zinnia", Color(173 / 255, 55 / 255, 48 / 255, 1)),
    CustomColor("Cedar", Color(115 / 255, 76 / 255, 52 / 255, 1)),
    CustomColor("Pine", Color(4 / 255, 43 / 255, 17 / 255, 1)),
    CustomColor("Seashell", Color(255 / 255, 245 / 255, 238 / 255, 1)),
]
