# Question
# Codeforces 785A - Anton and Polyhedrons



# Solution
faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

n = int(input())
total_faces = 0

for i in range(n):
    shape = input().strip()
    total_faces += faces[shape]

print(total_faces)


# Another Apporach to slove this same problem with same Time and Space Complexity 

n = int(input())
count = 0

for i in range(n):
    shape = input().strip().lower()
    if shape == "tetrahedron":
        count += 4
    elif shape == "cube":
        count += 6
    elif shape == "octahedron":
        count += 8
    elif shape == "dodecahedron":
        count += 12
    elif shape == "icosahedron":
        count += 20

print(count)