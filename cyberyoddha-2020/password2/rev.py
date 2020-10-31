password = "CYCTF{ju$@rcs_3l771l_@_t}bd3cfdr0y_u0t__03_0l3m"
print(password[23:45])
orig = list(password)

for i in range(0,9):
    orig[i] = password[i]
for i in range(45,25,-2):
    orig[i] = password[i]
for i in range(9,24):
    orig[32-i] = password[i]
for i in range(24,47,2):
    orig[70-i] = password[i]

orig = "".join(orig)

print(orig)