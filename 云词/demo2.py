'''
把一段用jieba文本分词。
用wordcloud生成云图，并保存为图片。
用matplotlib来显示图片
'''
import jieba
from wordcloud import WordCloud
from matplotlib import pylab as plt

text="\ufeff《盗墓笔记》中，一段与二月红有关的故事。\n《老九门》壹：二月红①\n丝帐许久没有换过了。\n\u3000\u3000她半夜入不了眠，睁开眼睛，便看到床边垂下的帐面，在月光下看着有一死暗淡。原来可是丝丝的带着光亮，好像最白的银拉出来的丝一般。\n\u3000\u3000果然再好的东西，也总是由好往坏了去。\n\u3000\u3000以往一过立秋。"
# 替换不需要的
text = text.replace('\ufeff','')
text = text.replace('\n','')
text = text.replace('\u3000','')
#强调特殊名词
jieba.suggest_freq(('二月红'), True)
segs=jieba.cut(text)

mytext_list = []
for seg in segs:
    mytext_list.append(seg.replace(" ",""))
cloud_text = ",".join(mytext_list)

wc = WordCloud(
    background_color="white",   #背景颜色
    max_words=200,              #显示最大词数
    font_path='小巧体.ttf',     #使用字体
    min_font_size=15,
    max_font_size=50,
    width=400                   #图幅宽度
)
wc.generate(cloud_text)
wc.to_file('pic.png') #保存图片

#下面这段是用matplotlib来显示图片
plt.imshow(wc)#用plt显示图片
plt.axis('off')#不显示坐标轴
plt.show()#显示图片
