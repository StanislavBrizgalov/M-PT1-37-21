import datetime

l1 = {0: "первого", 1: "второго", 2: "третьего", 3: "четвертого", 4: "пятого", 5: "шестого", 6: "седьмого",
      7: "восьмого", 8: "девятого", 9: "десятого", 10: "одинадцатого", 11: "двенадцатого", 12: "первого",
      13: "второго", 14: "третьего", 15: "четвертого", 16: "пятого", 17: "шестого", 18: "седьмого",
      19: "восьмого", 20: "девятого", 21: "десятого", 22: "одинадцатого", 23: "двенадцатого", 24: "первого"}

l2 = {00: "", 1: "одна минута", 2: "две минуты", 3: "три минуты", 4: "четыре минуты", 5: "пять минут", 6: "шесть минут",
      7: "семь минут", 8: "восемь минут", 9: "девять минут", 10: "десять минут", 11: "одинадцать минут",
      12: "двенадцать минут", 13: "тринадцать минут", 14: "четырнадцать минут", 15: "пятнадцать минут",
      16: "шестнадцать минут", 17: "семнадцать минут", 18: "восемнадцать минут", 19: "девятнадцать минут",
      20: "двадцать минут", 21: "двадцать одна минута", 22: "двадцать две минуты", 23: "двадцать три минуты",
      24: "двадцать четыре минуты", 25: "двадцать пять минут", 26: "двадцать шесть минут", 27: "двадцать семь минут",
      28: "двадцать восемь минут", 29: "двадцать девять минут", 30: "половина", 31: "тридцать одна минута",
      32: "тридцать две минуты", 33: "тридцать три минуты", 34: "тридцать четыре минуты", 35: "тридцать пять минут",
      36: "тридцать шесть минут", 37: "тридцать семь минут", 38: "тридцать восемь минут", 39: "тридцать девять минут"}

l3 = {00: "час", 1: "два", 2: "три", 3: "четыре", 4: "пять", 5: "шесть", 6: "семь",
      7: "восемь", 8: "девять", 9: "десять", 10: "одинадцать", 11: "двенадцать", 12: "час", 13: "два", 14: "три",
      15: "четыре", 16: "пять", 17: "шесть", 18: "семь", 19: "восемь", 20: "девять", 21: "десять", 22: "одинадцать",
      23: "двенадцать", 24: "час"}

l4 = {40: "без двадцати минут", 41: "без девятнадцати минут", 42: "без восемнадцати минут", 43: "без семнадцати минут",
      44: "без шестнадцати минут", 45: "без пятнадцати минут", 46: "без четырнадцати минут", 47: "без тринадцати минут",
      48: "без двенадцати минут", 49: "без одиннадцати минут", 50: "без десяти минут", 51: "без девяти минут",
      52: "без восьми минут", 53: "без семи минут", 54: "без шести минут", 55: "без пяти минут",
      56: "без четырех минут",
      57: "без трех минут", 58: "без двух минут", 59: "без одной минуты"}

l5 = {1: "час ровно", 2: "ровно два часа", 3: "ровно три часа", 4: "ровно четыре часа", 5: "ровно пять часов",
      6: "ровно шесть часов", 7: "ровно семь часов", 8: "ровно восемь часов", 9: "ровно девять часов",
      10: "ровно десять часов",
      11: "ровно одинадцать часов", 12: "ровно двенадцать часов", 13: "ровно час дня", 14: "ровно два часа дня",
      15: "ровно три часа дня", 16: "ровно четыре часа дня", 17: "ровно пять часов вечера",
      18: "ровно шесть часов вечера",
      19: "ровно семь часов вечера", 20: "ровно восемь часов вечера", 21: "ровно девять часов",
      22: "ровно десять часов",
      23: "ровно одинадцать часов", 00: "ровно двенадцать часов", 24: "ровно двенадцать часов"}

t = datetime.datetime.today()
print(t.strftime("%H.%M"))

# Реализовать текстовый вывод времени
if 1 <= t.minute <= 39:
    x1 = l1[t.hour]
    x2 = l2[t.minute]
    print(x2, x1)
elif t.minute >= 40:
    x1 = l3[t.hour]
    x2 = l4[t.minute]
    print(x2, x1)
elif t.minute == 0:
    x = l5[t.hour]
    print(x)
else:
    print("ошибка")

a, b = map(int, input("Введите время: ").split(" "))

# текстовый вывод времени, введённого с консоли

if 1 <= b <= 39:
    x1 = l1[a]
    x2 = l2[b]
    print(x2, x1)
elif b >= 40:
    x1 = l3[a]
    x2 = l4[b]
    print(x2, x1)
elif b == 00:
    x = l5[a]
    print(x)
else:
    print("ошибка")
