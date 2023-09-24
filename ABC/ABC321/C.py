k = int(input())
numbers = list(range(1, 10))
index = 0

while len(numbers) < k:
    num = numbers[index]
    for i in range(10):
        new_num = num * 10 + i
        num_str = str(new_num)
        valid = True
        for j in range(len(num_str) - 1):
            if num_str[j] <= num_str[j + 1]:
                valid = False
                break
        if valid:
            numbers.append(new_num)
    index += 1

result = numbers[k - 1]
print(result)
