# continue - it is used to skip the current iteration and move to the next iteration.
# break - it is used to completely stop the loop.
# pass - it literally does nothing.

# continue
for x in range(1, 11):
    if x == 5:
        continue
    print(x)


# break
for i in range(1, 6):
    if i == 4:
        break
    print(i)


# pass
for i in range(5):
    if i == 3:
        pass
    print(i)

    