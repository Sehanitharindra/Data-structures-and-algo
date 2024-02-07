#defining function fro memoized cut rod
def memoized_cut_rod(p, n):
    r = [-float('inf')] * (n + 1)#initialize array of size n and initialize all the elements at negative infinity
    return memoized_cut_rod_aux(p, n, r)

#defining the function for memoized_cut_rod_aux
#this is how the top-down cut-rod procedure occure
def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n + 1): #i is the position of the first cut
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r)) # calculating maximum price for given cut point
    r[n] = q #remember the solution value for length n
    return q

# example use 
#example is the exact example from the book
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]# prices
rod_length = 4
maximum = memoized_cut_rod(prices, rod_length)
print(f"Maximum revenue at given rod of length {rod_length}: {maximum}")
