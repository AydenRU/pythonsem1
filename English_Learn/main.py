import pymorphy2 as py
from translate import Translator

russian_Text = open('Russian_Word.txt', 'r', encoding='utf-8')
text = []
#text = russian_Text.read().lower()
#words = text.split()
#words = [word.strip('.,!;:()[]-—?😍'' ') for word in words]
#print(words)
for i in russian_Text:
    text += i.lower().strip('-,.)?!😍''\n ').split()
print(text)
russian_Text.close()

normal = []
morph = py.MorphAnalyzer()
for i in text:
    normal.append(morph.parse(i)[0].normal_form)
score_word_ru = {}

for i in normal:
    if i in score_word_ru:
        score_word_ru[i] +=1
    else:
        score_word_ru[i] = 1

b = 0
with open('English_Word.txt', 'w',encoding='utf-8') as file:
    for i, j in sorted(score_word_ru.items(), key= lambda par:(par[1]),reverse=True):
        translator = Translator(to_lang="en",from_lang='ru')
        translation = translator.translate(i)
        file.write(f"{i} | {translation} | {j}\n")
        b += 1
        print(b)
        print(len(normal))