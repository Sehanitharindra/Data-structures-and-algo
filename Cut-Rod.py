#defining simple rod cutting function from the book
def cut_rod(p, n):
    if n == 0:
        return 0
    q = -float('inf') # assigning negative very big value
    for i in range(1, n + 1):# in python the the indexes count from 0 to n-1 therefore the range is set to n+1
        q = max(q, p[i] + cut_rod(p, n - i))# recurssive code for finding maximum revenue gaining way of cutting rod
    return q

# example use of the code
# this example is exactly same example from book
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
rod_length = 4
 
print(f"Maximum revenue at given rod length {rod_length}: {cut_rod(prices, rod_length)}")
