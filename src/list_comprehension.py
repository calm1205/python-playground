# 自乗のリスト
double_sequence = [x**2 for x in range(10)]
print(double_sequence)

double_sequence_even = [x**2 for x in range(10) if x % 2 == 0]
print(double_sequence_even)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(list(zip(*matrix)))

translate_matrix = [[row[i] for row in matrix] for i in range(4)]
print(translate_matrix)
