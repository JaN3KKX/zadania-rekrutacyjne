# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu
import json

with open('dane/kategorie.json',mode="r",encoding="UTF-8") as c:
    categories = json.load(c)
with open('dane/zbiór_wejściowy.json',mode="r",encoding="UTF-8") as d:
    data = json.load(d)

def convert_mass(m: str) -> float: 
    m=m.replace(',','.')
    if 'ct' in m:
        return float(m[:-2])*0.2/28.35
    elif 'g' in m:
        return float(m[:-1])/28.35

def value_per_unit(item: dict, category: list) -> float: 
    for i in category:
        if item['Typ'] == i['Typ'] and item['Czystość'] == i['Czystość']:
            return i['Wartość za uncję (USD)'] * convert_mass(item['Masa'])
    return 0.0


items_with_value = []

for item in data:
    value = value_per_unit(item, categories)
    items_with_value.append((item, value))

top_5_items = sorted(items_with_value, key=lambda x: x[1], reverse=True)[:5] 

print("5 najbardziej wartościowych obiektów:")
i=1

for item, value in top_5_items:
    print(f"Typ: {item['Typ']}, Masa: {item['Masa']}, Czystość: {item['Czystość']}, Wartość: {value:.2f} USD, Właściciel: {item['Właściciel']}, Pochodzenie: {item['Pochodzenie']}")
    i+=1