"""Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y."""

sum = int(input("Input sum number:\n"))
product = int(input("Input product number:\n"))
x = 0
y = sum
while x <= sum / 2:
    if x * y == product:
        break
    x += 1
    y -= 1
    if x > sum / 2:
        print("Solution not found")
        quit()
print(x, y)
