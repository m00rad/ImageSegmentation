Gaussian = [[1 / 16, 2 / 16, 1 / 16],
            [2 / 16, 4 / 16, 2 / 16],
            [1 / 16, 2 / 16, 1 / 16]]
GaussianSize = len(Gaussian[0])

Box = [[1 / 9, 1 / 9, 1 / 9],
       [1 / 9, 1 / 9, 1 / 9],
       [1 / 9, 1 / 9, 1 / 9]]
BoxSize = len(Box[0])

laplacian = [[0, 1, 0],
             [1, -4, 1],
             [0, 1, 0]]
laplacianSize = len(laplacian[0])

bilateral = [[16 / 273, 26 / 273, 16 / 273],
             [26 / 273, 41 / 273, 26 / 273],
             [16 / 273, 26 / 273, 16 / 273]]
bilateralSize = len(bilateral[0])