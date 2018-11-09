def isSafe(v, color, c):
    return False


def graphColorUtil(m, color, v):
    if (v == 5):
        return True

    for c in range(1, m+1):
        if isSafe(v, color, c) == True:
            color[v] = c
            if graphColorUtil(m, color, v+1) == True:
                return True
            print("Here")
        else:
            return False




graphColorUtil(3, [0]*5, 0)
