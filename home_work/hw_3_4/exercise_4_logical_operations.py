i = 4
j = 9
print(i and j > 0)
print(i and j == 3)
print(i == 4 and j > i)
print(i == j and i < j)

print(i > 0 or j > 0)
print(i == 0 or j == 3)
print(i == 4 or j > i)
print(i == j or i > j)

text_a = 'Mikalai'
text_b = 'Adzintsou'

val_a_b = text_a > text_b or text_a == text_b
print('string: ', val_a_b)

val_a_b = text_a > text_b and text_a == 'Mikalai'
print('string: ', val_a_b)
