with open("test.txt", "w") as f:
  for i in range(3,31):
    for j in range(2, i):
      f.write("%s/%s," % (j,i))
    f.write("\n")

