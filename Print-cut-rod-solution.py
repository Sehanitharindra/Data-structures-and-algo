#defining function for extended_bottom_up_cut_rod
def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1) #initializing two r and s arrays 
    s = [0] * (n + 1)

    for j in range(1, n + 1):#for increassing the rod length j
        q = float('-inf')
        for i in range(1, j + 1):#i is the position of the first cut
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i #best cut location so far for length j
        r[j] = q #remember the solution value for length j

    return r, s

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])  # cut location for length n
        n -= s[n] # length of the remainder of the rod

# example use of the functions
        #exact emaple from the book
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
rod_length = 4

print(f"Maximum revenue at rod length {rod_length}: {extended_bottom_up_cut_rod(prices, rod_length)[0][-1]}") # last element of the array at 0 th position of 'r'array gives maximum revenue
print("Cut locations:") # printing cut locations
print_cut_rod_solution(prices, rod_length)
