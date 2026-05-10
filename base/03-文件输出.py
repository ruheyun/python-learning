# f = open('./text.txt', 'w', encoding='utf-8')
# print('人生苦短，我用Python', file=f)
# f.close()

with open('./base/text.txt', 'w', encoding='utf-8') as f:
    print('人生苦短，我用Python', file=f)
    