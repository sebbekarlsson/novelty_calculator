import math
from functools import reduce


distance = lambda x0, y0, x1, y1: math.hypot(x1 - x0, y1 - y0)

novelty = lambda d: 100 / max(1, d)

combined_novelty = lambda x, y, cities: reduce(lambda s, p: s + novelty(distance(x, y, p[0], p[1])), cities, 0)

most_novel_angle = lambda x, y, cities: reduce(
    lambda i, j:\
    j if combined_novelty(x+math.cos(j), y-math.sin(j), cities)\
    >\
    combined_novelty(x+math.cos(i), y-math.sin(i), cities) else i\
    ,
    range(0, 360)
)
