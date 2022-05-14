#cumle daxilinde en cox tekrarlanan karakteri tap

your_sentence = input("Enter your Sentence\n")

letter_dictionary = {}

for letter in your_sentence:
    if letter in letter_dictionary:
        letter_dictionary[letter] +=1
    else:
        letter_dictionary[letter] = 1
        

new_dict = sorted(letter_dictionary.items(),key =lambda x:x[1],reverse=True)
    
print(new_dict[0])

#Verilen ededin sade bolenlerinin tapilmasi

reqem = int(input("Write number\n"))

sade_bolenler = []
bolen = 2
qismet = reqem//bolen

while True:
    if reqem % bolen == 0:
        sade_bolenler.append(bolen)
        reqem = reqem/bolen
    else:
        bolen +=1
        
    if reqem / bolen == 1:
        sade_bolenler.append(bolen)
        break
        
        
print(sade_bolenler)