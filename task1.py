"""
Do zrobienia jest funkcja flatten która będzie wypłaszczać zagnieżdżone listy, czyli przykładowo, dostajemy listę
[1, 2, [3, 4, [5, [6]], 7], 8, 9, 10], a w wyniku powinniśmy dostać [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], oczywiście liczba zagnieżdżeń
może być dowolna i zakładamy, że elementem listy jest albo kolejna lista albo integer
"""

def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened
nested_list = [1, 2, [3, 4, [5, [6]], 7], 8, 9, 10]
flattened_list = flatten_list(nested_list)
print(flattened_list)