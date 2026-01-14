# day 11 level 2 exercise 1

def evensAndOdds(num):
    evens = 0
    odds = 0
    if num % 2 == 0:
        odds = (num // 2)
        evens = odds + 1
    else:
        evens = num // 2 + 1
        odds = evens
    print(f'Number of evens: {evens} \nNumber of odds: {odds}')

evensAndOdds(100)
        