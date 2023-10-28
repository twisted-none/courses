# Для настольной игры используются карточки с номерами от 1 до n. Одна карточка потерялась.
# Напишите программу, которая выводит номер потерянной карточки.

n = int(input())
full_cards = [i for i in range(1, n + 1)]
our_cards = [int(input()) for _ in range(n - 1)]

for i in range(len(full_cards)):
    if full_cards[i] not in our_cards:
        print(full_cards[i])
        break