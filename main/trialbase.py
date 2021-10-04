arr = [["null"] * 8 for _ in range(8)]
count = 0
for x in range(8):
    for y in range(8):
        count = count + 1
        arr[x][y] = " [ "+str(x)+" : "+str(y)+"] "
        print(arr[x][y], end=" ")
    print(end="\n")
mid = int(input("i : "))
mid2 = int(input("j : "))
print("left upper quadrant")
x = mid - 1
y = mid2 - 1

while True:
    print(arr[x][y])
    y -= 1
    x -= 1
    if x < 0 or y < 0:
        break

print("right lower quadrant")
x = mid + 1
y = mid2 + 1

while True:
    print(arr[x][y])
    y += 1
    x += 1
    if x > 7 or y > 7:
        break

print("right upper quadrant")
x = mid - 1
y = mid2 + 1

while True:
    print(arr[x][y])
    y += 1
    x -= 1
    if x < 0 or y > 7:
        break

print("left lower quadrant")
x = mid + 1
y = mid2 - 1

while True:
    print(arr[x][y])
    y -= 1
    x += 1
    if x > 7 or y < 0:
        break
