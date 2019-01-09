'''
绘制指定形状的云词图
保存，并用 matplotlib 显示出来
'''

import jieba
from PIL import Image
import numpy as np
from wordcloud import WordCloud,ImageColorGenerator
from matplotlib import pyplot as plt


text = '''赵心安现年38岁，中等个头，面相憨憨的，教高三（八）班的语文。八班是本届高三唯一的一个重点班，此次模拟，原本圈定的冲击清华北大的尖子生，语文成绩大多都没有达到125分的保底线，赵心安心里很着急。

“这怎么行？背诵默写还在丢分，背诵默写，竟然还在丢分！这怎么行呢？！”周一早读，他拿着戒尺，黑着脸，立在教室门口，亲自检查学生的背诵默写。为这事他昨晚几乎思谋了一夜。“这帮学生，不来点厉害的，就不知道马王爷三只眼！”就在这时候，他忽然感觉到了腹部一阵一阵的疼痛。“坏了，昨天晚上的麻辣烫吃坏了。”他想。

头一天下午，他耐着性子加班阅完学生的周考卷，刚出办公室准备回家，就遇到那个爱说爱笑的燕玲了，她蹦蹦跳跳的，脑后扎起的那缕发髻油亮顺滑。

“这不是巧了嘛！刚想遇到一个人，你就出现了。”燕玲说备课坐了大半天，椎间盘都快“突出”了，正想找人去打一阵儿乒乓球，就遇到了赵心安。蔫蔫的赵心安毫不犹豫地改变了原来回家的主意，马上给老婆打了电话，说晚上忙得很，要加班改卷，就果决地与燕玲一起打球去了。

据他说，他们玩到晚上7点多，还一起到街上的麻辣烫小店里吃了个饭——燕玲就爱吃这个。

于是，这天早读上，赵心安本想严肃地查一查学生的背诵情况，“台词”是前一天晚上就想好的：“今天，我亲自来查，都是考过的内容，谁还背不上来，就给我个合理的解释！”原本叽叽喳喳的学生全被镇住了，惊慌地翻着试卷，深埋着头，生怕赵老师站在自己面前。

然而，就在这个时候，肚子却“适时”地疼了起来，他无奈地连续上了两趟厕所。半个小时的语文早读就这样在学生莫名的惊喜中过去了，酝酿了一个晚上的严肃也被尴尬地消解掉了。

“山重水复疑无路，柳暗花明又一村”，伴着早自习的下课铃声，学生们长出了一口气。'''

#强调特殊名词
jieba.suggest_freq(('昨天'), True)
segs = jieba.cut(text)

mytext_list = []
for seg in segs:
    mytext_list.append(seg.replace(" ",""))
cloud_text = ",".join(mytext_list)

#加载背景图片
cloud_mask = np.array(Image.open('src/heart.png'))

# 忽略显示的词
st = set(["中等","肚子"])

#生成wordcloud对象
wc = WordCloud(
    background_color='white',      #背景颜色(mode="RGBA",background_color=None,背景为透明)
    mask=cloud_mask,            #图片背景参考形状
    max_words=200,              #显示最大词数
    font_path="src/msyh.ttf",   #使用字体
    min_font_size=20,
    max_font_size=100, 
    width=400,                  #图幅宽度
    stopwords=st,               #不需要显示的词
    #mode="RGBA"
)

wc.generate(cloud_text)
wc.to_file('pic.png')#保存图片

#下面这段是用matplotlib来显示图片
plt.imshow(wc)#用plt显示图片
plt.axis('off')#不显示坐标轴
plt.show()#显示图片