print('Complement Operator or Tilde Operator')
print(~12)      # Here concept of 2's complement (1's complement+1) is used if we do
                # 1's complement +1 of 13 we will get complement of 12

print(' Bitwise and operator')
print(12 & 13)  # 12 = 00001100
                # 13 = 00001101 if we do AND operation we will get 12
print(11 & 222)

print('Bitwise OR Operator')
print(12 | 13)  # 12 = 00001100
                # 13 = 00001101 if we do OR operation we will get 13
print(11 | 222) 

print('Bitwise XOR Operator')
print(12^13)    # 12 = 00001100
                # 13 = 00001101  in XOR if we have two same bits ex: 11 we wil get 0
print(11^222)

print('Left shift')
print(bin(12))  # 1100.00000
print(12<<2)    # shifting 2 places so 2 more zeros will be added last
print(bin(48))  # 110000.000

print('Right shift')
print(bin(12))  # 1100.00000
print(12>>2)    # shifting 2 places so 2 more zeros will be added last
print(bin(3))   # 11.0000000



