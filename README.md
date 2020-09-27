# Curve fitting

This program finds 2nd order curve fitting using least squares.

## Usage

```
python .\least_square.py -2.9 35.4 -2.1 19.7 -0.9 5.7 1.1 2.1 0.1 1.2 1.9 8.7 3.1 25.7 4.0 41.5 -s 6 -v
```
Gets a, b, and c in ax^2 + bx + c, which has least square with randomly selecting 6 points (`-s 6`) in
(-2.9, 35.4), (-2.1, 19.7), (-0.9, 5.7), (1.1, 2,1), (0.1, 1.2), (1.9, 8.7),
(3.1, 25.7) and (4.0, 41.5) and visualize (`-v` option) the result.