a = input()
b = []

for x in a:
    if x == " ":
        pass
    else:
        b.append(int(x))


# abc
# ab+c
# ac+b
# ba+c
# bc+a
# ca+b
# cb+a

# a = b[0], b = b[1], c = b[2]

b0_str = str(b[0])
b1_str = str(b[1])
b2_str = str(b[2])

# ab+c
b01_str = b0_str + b1_str
ab_c = int(b01_str) + b[2]

# ac+b
b02_str = b0_str + b2_str
ac_b = int(b02_str) + b[1]

# ba+c
b10_str = b1_str + b0_str
ba_c = int(b10_str) + b[2]

# bc+a
b12_str = b1_str + b2_str
bc_a = int(b12_str) + b[0]

# ca+b
b20_str = b2_str + b0_str
ca_b = int(b20_str) + b[1]

# cb+a
b21_str = b2_str + b1_str
cb_a = int(b21_str) + b[0]

max_ans = 0
if max_ans < ab_c:
    max_ans = ab_c
if max_ans < ac_b:
    max_ans = ac_b
if max_ans < ba_c:
    max_ans = ba_c
if max_ans < bc_a:
    max_ans = bc_a
if max_ans < ca_b:
    max_ans = ca_b
if max_ans < cb_a:
    max_ans = cb_a

print(max_ans)
