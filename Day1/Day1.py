
lines = []
with open('input/input.txt') as f:
    lines = f.readlines()

elfs_total_calories = []

elfs_calories = 0
for x in lines:
  if x == "\n":
    elfs_total_calories.append(elfs_calories)
    elfs_calories = 0
  else:
    elfs_calories += int(x)

print("Solution 1: " + str(max(elfs_total_calories)))

elfs_total_calories.sort(reverse=True)

sum_max3 = int(elfs_total_calories[0]) + int(elfs_total_calories[1]) + int(elfs_total_calories[2])
print("Solution 2: " + str(sum_max3))