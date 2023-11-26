print("20,19,18,17,16,15,14,12,11,10,9,8,7,6,5,4,3,2,1")

for i in range(20,0,-1):
  if i == 13:
    continue
  print(i)
  
i = 20
while (i > 0):
  if i ==13:
    i -= 1
    continue
  print(i)
  i -= 1   