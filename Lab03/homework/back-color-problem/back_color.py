from random import *
from ex11 import is_inside
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes

texts = [shapes[0]['text'], shapes[1]['text'], shapes[2]['text'],shapes[3]['text']]
colors = [shapes[0]['color'], shapes[1]['color'], shapes[2]['color'],shapes[3]['color']]
rects = [shapes[0]['rect'], shapes[1]['rect'], shapes[2]['rect'],shapes[3]['rect']]

def generate_quiz():
    # texts = [shapes[0]['text'], shapes[1]['text'], shapes[2]['text'],shapes[3]['text']]
    # colors = [shapes[0]['color'], shapes[1]['color'], shapes[2]['color'],shapes[3]['color']]
    # rects = [shapes[0]['rect'], shapes[1]['rect'], shapes[2]['rect'],shapes[3]['rect']]

    return [
                choice(texts),
                choice(colors),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        i = texts.index(text)
        return is_inside([x, y], rects[i])
    else:
        i = colors.index(color)
        return is_inside([x ,y], rects[i])