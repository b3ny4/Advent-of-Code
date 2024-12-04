if __name__ == "__main__":
    with open("input.txt") as f:
        matrix = [list(line.strip()) for line in f.readlines()]

    num = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'X':
                # search down
                if (len(matrix) >= i+len("XMAS")
                    and matrix[i+1][j] == "M"
                    and matrix[i+2][j] == "A"
                    and matrix[i+3][j] == "S"):
                    num += 1
                # search up
                if (i >= len("XMAS")-1
                    and matrix[i-1][j] == "M"
                    and matrix[i-2][j] == "A"
                    and matrix[i-3][j] == "S"):
                    num += 1
                # search left
                if (j >= len("XMAS")-1
                    and matrix[i][j-1] == "M"
                    and matrix[i][j-2] == "A"
                    and matrix[i][j-3] == "S"):
                    num += 1
                # search right
                if  (len(matrix[0]) >= j+len("XMAS")
                    and matrix[i][j+1] == "M"
                    and matrix[i][j+2] == "A"
                    and matrix[i][j+3] == "S"):
                    num += 1


                # search NW
                if  (i >= len("XMAS")-1
                    and j >= len("XMAS")-1
                    and matrix[i-1][j-1] == "M"
                    and matrix[i-2][j-2] == "A"
                    and matrix[i-3][j-3] == "S"):
                    num += 1
                # search NE
                if  (i >= len("XMAS")-1
                    and len(matrix[0]) >= j+len("XMAS")
                    and matrix[i-1][j+1] == "M"
                    and matrix[i-2][j+2] == "A"
                    and matrix[i-3][j+3] == "S"):
                    num += 1
                # search SW
                if  (len(matrix) >= i+len("XMAS")
                    and j >= len("XMAS")-1
                    and matrix[i+1][j-1] == "M"
                    and matrix[i+2][j-2] == "A"
                    and matrix[i+3][j-3] == "S"):
                    num += 1
                # search SE
                if  (len(matrix) >= i+len("XMAS")
                    and len(matrix[0]) >= j+len("XMAS")
                    and matrix[i+1][j+1] == "M"
                    and matrix[i+2][j+2] == "A"
                    and matrix[i+3][j+3] == "S"):
                    num += 1

    print(num)
