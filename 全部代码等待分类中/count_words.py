import jieba

txt=open("不顾一切.txt", "r", encoding='utf-8').read()
words=jieba.lcut(txt)
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # key=lambda x: x[1]：按x的第二维数据排序，x[0]则是第一维

for i in range(10):
   word, count = items[i]
   print(f"{word} with times: {count}")