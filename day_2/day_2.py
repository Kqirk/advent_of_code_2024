


def is_safe(levels):
    # input is guaranteed
    increased = 0
    decreased = 0

    # must be increasing or decreasing
    for i in range(1, len(levels)):
        level = int(levels[i])
        prev_level = int(levels[i-1])
        diff = prev_level - level

    # must differ by at least 1 and at most 3 1 <= x <= 3
        if 1 <= diff <= 3:
            decreased += 1
        elif -3 <= diff <= -1:
            increased += 1
        else:
            return False

    return False if (increased and decreased) else True

def is_safe_tolerate_1(levels):
    print(levels)
    print("-" * 26)
    for i in range(len(levels)):
        removed_1 = levels[:i] + levels[i+1:]
        print(removed_1)
        if is_safe(removed_1):
            return True 
    
    return False

# Part one 
# with open("test_input.txt", "r") as file:
with open("real_input.txt", "r") as file:
    safe_reports = 0

    for report in file:
        levels = report.split(" ")

        if is_safe(levels):
            safe_reports += 1

print(safe_reports)
        
# Part two
tolerated_safe_reports = 0

# with open("test_input.txt", "r") as file:
with open("real_input.txt", "r") as file:

    for report in file:
        levels = report.split(" ")

        if is_safe(levels):
            tolerated_safe_reports += 1
        elif is_safe_tolerate_1(levels):
            tolerated_safe_reports += 1

print(tolerated_safe_reports)