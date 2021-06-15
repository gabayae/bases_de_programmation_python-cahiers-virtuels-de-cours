import time

print("hello world")

time.sleep(1)

print("Are you looking for me?")

time.sleep(2)

f = open("richie.txt")
for line in f:
  print (line.rstrip())
  time.sleep(0.2)

f.close()

