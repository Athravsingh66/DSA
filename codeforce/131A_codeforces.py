# Question
# Codeforces 131A - cAPS lOCK


# Solution
word = input()

if word.isupper() or word[1:].isupper() or len(word)==1:
    print(word.swapcase())
else:
    print(word)
