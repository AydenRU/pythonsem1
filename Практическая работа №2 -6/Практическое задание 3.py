def read_file(f):
    with open(f, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words = text.split()
        words = [word.strip('.,!;:()[]-—? ') for word in words]
    slova=[]
    for i in words:
        if i not in slova:
            slova.append(i)
    slova.sort()
    return slova
def save_file():
    with open('count.txt','w',encoding='utf-8') as d:
        d.write('Всего уникальных слов : ')
        d.write(str(len(word)))
        d.write('\n==================================\n')
        for i in range(len(word)):
            d.write(word[i])
            d.write('\n')
f = 'text_work.txt'
word = read_file(f)
save_file()


