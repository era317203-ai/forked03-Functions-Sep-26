
# text = "Кот, кот. Собака, собака! Кот."

def most_common_word(text):
    text = text.lower()
    for symbol in ",.!?;:-":
        text = text.replace(symbol, "")
    words = text.split()
    counts ={}
    for el in range (len(words)):
       word = words [el]
       if word not in counts:
        counts [word] =1
       else:
        counts [word] +=1
    most_common = None 
    max_count = 0
    for word in counts:
        if counts[word] > max_count:
            max_count = counts[word]
            most_common = word

    return most_common                                  
# print (most_common_word(text))                                                                                                     # most_common = max(counts, key=counts.get)
    

assert most_common_word("кот кот собака") == "кот", "Самое частое слово — кот"
assert most_common_word("Кот кот КОТ собака") == "кот", "Регистр должен игнорироваться"
assert most_common_word("молоко, молоко! молоко? хлеб.") == "молоко", "Знаки препинания должны игнорироваться"
assert most_common_word("слово") == "слово", "Ожидалось единственное слово"
res = most_common_word("а б а б")
assert res in ("а", "б"), "Ожидалось одно из слов с максимальной частотой"
