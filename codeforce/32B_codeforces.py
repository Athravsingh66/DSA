# Question 
# Codeforces 32B - Borze


# Solution
borze_code = input()

decode = ""
i = 0
while i < len(borze_code):
    if borze_code[i] == ".":
        decode += "0"
        i += 1
    elif borze_code[i:i+2] == "-.":
        decode += "1"
        i += 2
    elif borze_code[i:i+2] == "--":
        decode += "2"
        i += 2
            
print(decode)
            

# Another way to slove this problem but order matter,
# always greater number first replace in this "--" by 2 and then "-." by 1 then at last "." by 0

borze_code = input()

decode = borze_code.replace("--","2").replace("-.","1").replace(".","0")

print(decode)
