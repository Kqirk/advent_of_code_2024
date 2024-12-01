list_1 = []
list_2 = []

# with open("test_input.txt", "r") as file:
with open("puzzle_input.txt", "r") as file:
    for lines in file:
        inputs = lines.strip().split("   ")
        list_1.append(int(inputs[0]))
        list_2.append(int(inputs[1]))

list_1.sort()
list_2.sort()

total = 0

for i in range(len(list_1)):
    total += abs(list_1[i] - list_2[i])

print(total)

# Similarity score, part two
similarity_score = 0

for num in list_1:
    similarity_score += num * list_2.count(num)

print(similarity_score)
