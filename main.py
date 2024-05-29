def ritual():
  door = []
  for i in range(1, 65):
    door.append(-1*i)
    for j in range(1,65):
      if i % j == 0:
        door[i-1] = door[i-1] * -1
    if door[i-1] > 0:
      print('#'+ str(door[i-1]), end="")
ritual()