import re

sum = 0

def sum_of_mul(line):
    cur_sum = 0
    print(line)
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)

    for match in matches:
        print(match)
        first_no = int(re.search("\d{1,3},", match).group()[:-1])
        second_no = int(re.search(",\d{1,3}", match).group()[1:])
        cur_sum += first_no * second_no

    return cur_sum 

with open("input.txt", "r") as file:
# with open("test_input.txt", "r") as file:
    for line in file:
        sum += sum_of_mul(line)

print(sum)

# Part two
new_sum = 0
enabled = True
with open("input.txt", "r") as file:
# with open("test_input.txt", "r") as file:
    for line in file:
        while line:
            print(f"enabled: {enabled}")
            next_dont = re.search("don't\(\)", line)

            # enabled muls
            if enabled:
                end_idx = next_dont.span()[1] if next_dont else len(line)
                matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line[:end_idx])
                for match in matches:
                    first_no = int(re.search("\d{1,3},", match).group()[:-1])
                    second_no = int(re.search(",\d{1,3}", match).group()[1:])
                    new_sum += first_no * second_no
            
                line = line[end_idx:]
                if not next_dont:
                    enabled = True
                else:
                    enabled = False
            else:
                next_do = re.search("do\(\)", line)
                start_idx = next_do.span()[1] if next_do else len(line)

                if next_do:
                    start_idx = next_do.span()[1]
                    enabled = True
                else:
                    start_idx = len(line)

                line = line[start_idx:]

print(new_sum)