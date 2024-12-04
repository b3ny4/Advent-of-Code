if __name__ == "__main__":
    with open("input.txt") as f:
        matrix = [list(line.strip()) for line in f.readlines()]

    num = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] != "A":
                continue

            if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[0])-1:
                continue

            # check diagonal
            if (
                ( 
                    (matrix[i-1][j-1]=="M" and matrix[i+1][j+1] == "S") or
                    (matrix[i-1][j-1]=="S" and matrix[i+1][j+1] == "M")
                ) and 
                ( 
                    (matrix[i-1][j+1]=="M" and matrix[i+1][j-1] == "S") or
                    (matrix[i-1][j+1]=="S" and matrix[i+1][j-1] == "M")
                )
            ):
                num += 1
                continue


            ## check vertical
            #if (
            #    ( 
            #        (matrix[i-1][j]=="M" and matrix[i+1][j] == "S") or
            #        (matrix[i-1][j]=="S" and matrix[i+1][j] == "M")
            #    ) and 
            #    ( 
            #        (matrix[i][j+1]=="M" and matrix[i][j-1] == "S") or
            #        (matrix[i][j+1]=="S" and matrix[i][j-1] == "M")
            #    )
            #):
            #    num += 1

    print(num)

