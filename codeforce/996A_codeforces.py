# Question
# Codeforces 996A - Hit the Lottery


# Solution
m = int(input())
count = 0

# For 100 dollars
r = m//100
m = m - r*100
count+=r

# For 20 dollars
r1 = m//20
m = m - r1*20
count+=r1

# For 10 dollars
r2 = m//10
m = m - r2*10
count+=r2

# For 5 dollars
r3 = m//5
m = m -r3*5
count+=r3

# For 1 dollars
r4 = m//1
m = m - r4*1
count+=r4

# Final Nunber of notes
print(count)


    
    