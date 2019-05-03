#余弦相似度计算句子相似度
import jieba
import numpy

#创建停用词list
def stopwordslist(filepath):
    stopwords=[line.strip() for line in open(filepath,'r',encoding='utf-8').readlines()]
    return stopwords

#将语料库句子集合表示成‘词-句子’矩阵
fin=open("News_result2.txt","r",encoding='utf-8')
stopwords=stopwordslist('stopword.txt')#加载停用词路径
lines=fin.readlines()
word=[]
sent=[]
for line in lines:
    sent.append(line)
    sent_cut=jieba.cut(line)
    for wd in sent_cut:
        if wd not in stopwords:
            if wd not in word:
                word.append(wd)
wordLen=len(word)
sentLen=len(sent)
word_sent=numpy.zeros((wordLen+1,sentLen+1))
for j in range(sentLen):
    for i in range(wordLen):
        if word[i] in sent[j]:
            word_sent[i][j]=word_sent[i][j]+1
T,S,D=numpy.linalg.svd(word_sent)
#用户输入句子
'''IN=input()
#sent.append(IN)
in_cut=jieba.cut(IN)
for outstr in in_cut:
    for i in range(wordLen):
        if word[i]==outstr:
            word_sent[i][sentLen]=word_sent[i][sentLen]+1
for j in range(sentLen):
    num = float(numpy.sum(word_sent[:,j]*word_sent[:,sentLen]))
    denom = numpy.linalg.norm(word_sent[:,j]) * numpy.linalg.norm(word_sent[:,sentLen])
    cos = num / denom
    word_sent[wordLen,j] = 0.5 + 0.5 * cos
fifth=[0 for i in range(5)]
for i in range(5):
    Max=0
    for j in range(sentLen):
        if(word_sent[wordLen,j]>Max):
            Max=word_sent[wordLen,j]
            temp=j
    fifth[i]=temp
    word_sent[wordLen,temp]=0
    temp=0
#for i in fifth:
#    print(sent[i])'''
