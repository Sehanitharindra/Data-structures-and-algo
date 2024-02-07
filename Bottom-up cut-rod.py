#defining bottom up cut rod function
def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)  # initializing a array of size n to store solution values
    for j in range(1, n + 1):
        q = -float('inf') # initialize q at negtive ifinity
        for i in range(1, j + 1): # i is the function of first cut
            q = max(q, p[i] + r[j - i])
        r[j] = q #remember the solution value for length j
    return r[n]

#example use of function
#the same example from the book
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
rod_length = 4
result = bottom_up_cut_rod(prices, rod_length)
print(f"Maximum revenue at rod length {rod_length}: {result}")
