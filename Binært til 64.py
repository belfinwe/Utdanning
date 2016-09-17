# Skriv tallene 0 - 64 med det binære tallsystemet.

# Programstart /E

# Skriv inn tallene 0 - 64 /P

# Skriv ut tallene 0 - 64 /P

# Programslutt /E


# binært   => desimalt
# 00000000 => 0
# 00000001 => 1 (1 * (2**0))
# 00000010 => 2 (1 * (2**1))
# 00000011 => 3 (1 * (2**1) + 1 (2**0))
# 00000100 => 4 (1 * (2**2))
# 00000101 => 5
# 00000110 => 6
# 00000111 => 7
# 00001000 => 8
# 00001001 => 9
# 00001010 => 10
# 00001011 => 11
# 00001100 => 12
# 00001101 => 13
# 00001110 => 14
# 00001111 => 15
# 00010000 => 16
# 00010001 => 17
# 00010010 => 18
# 00010011 => 19
# 00010100 =>



eksponent = 0
x = 1
print(0)
while True:
    x = 2 ** eksponent
    eksponent += 1
    print(x)
    if x == 64:
        break
