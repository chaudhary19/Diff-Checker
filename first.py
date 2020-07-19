def find(i, j, path, A, B):

    if i == 0 and j == 0 :
        return ""

    if path[i][j] == 1 :
        return find(i-1, j, path, A, B) + B[i-1] + "// added " + "\n"

    if path[i][j] == 2:
        return find(i, j-1, path, A, B) + A[i-1] + "// deleted" + "\n"
    return find(i-1, j-1, path, A, B) + A[j-1]

def match(A, B):

    if len(A) > len(B) or len(A) < len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False

    return True

def main():

    fptr1 = open('file1.txt', 'r')
    fptr2 = open('file2.txt', 'r')

    A = []
    B = []

    while True:
        line = fptr1.readline()
        if not line:
            break
        A.append(line)
    fptr1.close()

    while True:
        line = fptr2.readline()
        if not line:
            break
        B.append(line)
    fptr2.close()

    dp = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
    path = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]

    for i in range(len(A)+1):
        path[0][i] = 2

    for i in range(1, len(B)+1):
        path[i][0] = 1

    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if dp[i][j-1] >= dp[i-1][j]:
                dp[i][j] = dp[i][j-1]
                path[i][j] = 2
            else:
                dp[i][j] = dp[i-1][j]
                path[i][j] = 1
            if(match(A[j-1], B[i-1])):
                if(dp[i-1][j-1] + 1 > dp[i][j-1] and dp[i-1][j-1] + 1 > dp[i-1][j]):
                    dp[i][j] = dp[i-1][j-1] + 1
                    path[i][j] = 3

    print(find(len(B), len(A), path, A, B));
 
 if __name__ == "__main__":
     main()
