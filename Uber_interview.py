a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 26]
from iteration_utilities import accumulate
from itertools import repeat
import operator
tuple(accumulate(a, operator.add))[1:]
(6, 12, 20, 30, 42, 56, 72, 90, 110, 134, 160)
tuple(accumulate(a, operator.mul))[1:]
(8,
 48,
 384,
 3840,
 46080,
 645120,
 10321920,
 185794560,
 3715891200,
 89181388800,
 2318716108800)