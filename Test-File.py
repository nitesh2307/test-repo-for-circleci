f = open("day3.txt", "r")
d = {}
sum = 0
with open("day3lookup.txt") as g:
    for line in g:
        (key, val) = line.split()
        d[key] = int(val)
#print (d)

for x in f:
    y = x.strip()
  #  print(len(y)) 
    first_half = y[:len(y)//2]
    second_half = y[len(y)//2:]
    #print(y + " ----- " + first_half + "  +  " + second_half)
    for i in first_half:
        if second_half.find(i) != -1:
            sum = sum + int(d[i])
            break
        else:
            continue
print("Answer is below Kushagr")
print(sum)



