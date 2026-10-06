# Question
# Codeforces 208A - Dubstep



# Solution
word = input()
new_word = word.split("WUB")

for w in range(len(new_word)):
    if new_word[w] != "":
        print(new_word[w] ,end=" ")
        

# Another way to Solve this with boolean concept
        
word = input()
new_word = word.split("WUB")

for w in new_word:
    if w:  # In Python, non-empty strings evaluate to True
        print(w, end=" ")