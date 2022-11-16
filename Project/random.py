import random
z = 0
val_1 = 0
val_2 = 0
val_3 = 0
val_4 = 0
val_5 = 0
val_6 = 0
val_7 = 0
val_8 = 0
val_9 = 0
val_10 = 0

while z < 1:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    d = random.randint(1, 9)
    e = random.randint(1, 9)
    f = random.randint(1, 9)
    g = random.randint(1, 9)
    h = random.randint(1, 9)
    i = random.randint(1, 9)
    j = random.randint(1, 9)
    if 0 <= a + b + c + d + e + f + g + h + i + j <= 90:
        if a < 10:
            val_1 = a
        if b < 10:
            val_2 = b
        if c < 10:
            val_3 = c
        if d < 10:
            val_4 = d
        if e < 10:
            val_5 = e
        if f < 10:
            val_6 = f
        if g < 10:
            val_7 = g
        if h < 10:
            val_8 = h
        if i < 10:
            val_9 = i
        if j < 10:
            val_10 = j
        z += 1


print('Test lottery:')
print(str(val_1) + ' - ' + str(val_2) + ' - ' + str(val_3) + ' - ' + str(val_4) + ' - ' + str(val_5) + ' - ' + str(val_6) +
      ' - ' + str(val_7) + ' - ' + str(val_8) + ' - ' + str(val_9) + ' - ' + str(val_10))
