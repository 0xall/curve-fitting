import argparse

import numpy as np

import matplotlib.pyplot as plt


args = argparse.ArgumentParser()

args.add_argument('points', type=float, nargs='+', help='2D Points for fitting curves')
args.add_argument('-s', '--sample', type=int, help='The number of samples for fitting curves.')
args.add_argument('-v', '--visualize', action='store_true', help='Visualize the fitting curves and points.')


def visualize(a, b, c, points):
    min_x, max_x = float('inf'), -float('inf')
    min_y, max_y = float('inf'), -float('inf')

    for point in points:
        plt.plot(point[0], point[1], 'rx')

        min_x, max_x = min(min_x, point[0]), max(max_x, point[0])
        min_y, max_y = min(min_y, point[1]), max(max_y, point[1])

    x = np.linspace(min_x - 1.0, max_x + 1.0, 100)
    y = a * (x ** 2) + b * x + c

    plt.plot(x, y)
    plt.xlim(min_x - 1.0, max_x + 1.0)


if __name__ == '__main__':
    args = args.parse_args()

    # Converts 1xN matrix to (N/2)x2 matrix.
    try:
        points = np.array(args.points).reshape((-1, 2))
    except ValueError:
        print('The number of points should be even.')

    # if the number of samples are defined, randomly permutates the
    # matrix and choose N samples.
    if args.sample:
        points = np.random.permutation(points)[:args.sample]

        print(f'{args.sample} Samples selected..')
        print(points)
        print()

    # Curve fittings using least squares.
    # X` = pinv(X) * Y
    X = np.concatenate([points[:,[0]] ** 2, points[:,[0]], np.ones((len(points), 1))], axis=1)
    Y = points[:, [1]]

    X_ls = np.matmul(np.linalg.pinv(X), Y)

    # gets a, b, c with least square error.
    a, b, c = X_ls[0][0], X_ls[1][0], X_ls[2][0]

    print(f'f(x) = {a}x^2 + {b}x + {c}')

    if args.visualize:
        visualize(a, b, c, points)
        plt.show()
