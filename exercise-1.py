# Istifadəçinin girdiyi mətnlərdəki hərfləri əlifba sırsanıda
# özünən sonra gələn hərflə dəyişdirən program yazın. 
# Örnək: input: Men Python 3 oyrenirem
# output: Nfo Qzuipo 3 pzsfojsfn

your_sentences = input("Write sentence\n")

result = []

word = ""
for sentence in your_sentences:
    if ord(sentence) !=32:
        order = chr(ord(sentence)+1)
        word += order
    else:
        result.append(word)
        word = ""
        
else:
    result.append(word)
print(*result)
    
# İstifadəçinin girdiyi mətn daxilindəki hərflərin ingilis əlifbasındakı
# sırasına qarşılıq gələn ədədlərlə dəyişdirilmiş şəkildə göstərin. 
# Örnək: input: Men Javascript oyrenirem
# output: 13,5,14, 10,1,22,1,19,3,18,9,16,20, 15,25,18,5,14,9,18,5,13,

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


your_sentences = input("Enter sentence:\n").lower()


sentence = ""
for letter in your_sentences:
    if ord(letter) !=32:
        new_letter = letters.index(letter)+1
        sentence +=str(new_letter) + ","
print(sentence)


# Atadan 2 oğula bir ferma miras qalıb. Ata vəsiyyətində deyir ki, 
# fermanı ortadan 2-yə bölün, birinci yarısı böyük oğula, 
# ikinci yarısı isə kiçik oğula verilsin. Ədalətsizliyi aradan qaldırmaq üçün qardaşlar razılaşır ki, 
# gəl hərəmizə düşən fermadakı heyvanların qiymətlərini hesablayaq, 
# əgər kimin ferması daha çox pul edirsə,
# o aradakı fərqi bağlamaq üçün cibindən çıxarıb, digərinə nəğd pul versin. 
# Misal üçün əgər böyük qardaşın ferması 20000 manat,
# kiçik qardaşınkı 15000 manatdırsa, böyük qardaş öz cibindən çıxarıb kiçiyə 2500 manat versin,
# beləliklə hər birinin sərvəti eyni olsun.

farm = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
prices = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

big_brother = []
little_brother = []
big_brother_money = 0
little_brother_money = 0

for i in range(len(farm)):
    
    if i < len(farm) // 2:
        big_brother.append(farm[i])
        big_brother_money += prices[farm[i]]
    else:    
        little_brother.append(farm[i]) 
        little_brother_money += prices[farm[i]]

print(f'Big brother\'s money: {big_brother_money}')
print(f'Big brother\'s money: {little_brother_money}')

if big_brother_money > little_brother_money:
    result =(big_brother_money - little_brother_money) // 2
    print(f"The elder brother has to give {result} manat to the younger brother.")
else:
    result =(little_brother_money - big_brother_money) // 2
    print(f"The younger brother has to pay {result} manat to the older brother.")
















