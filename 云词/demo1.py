import jieba

#全模式
text = "我来到北京清华大学"
seg_list = jieba.cut(text, cut_all=True)
print( u"[全模式]: ", "/ ".join(seg_list) )

#精确模式
seg_list = jieba.cut(text, cut_all=False)
print(u"[精确模式]: ", "/ ".join(seg_list) )

#默认是精确模式
seg_list = jieba.cut(text)
print( u"[默认模式]: ", "/ ".join(seg_list)  )

#新词识别 “杭研”并没有在词典中,但是也被Viterbi算法识别出来了
seg_list = jieba.cut("他来到了网易杭研大厦") 
print( u"[新词识别]: ", "/ ".join(seg_list) )

#搜索引擎模式
seg_list = jieba.cut_for_search(text) 
print( u"[搜索引擎模式]: ", "/ ".join(seg_list) )

'''
[全模式]:  我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学
[精确模式]:  我/ 来到/ 北京/ 清华大学
[默认模式]:  我/ 来到/ 北京/ 清华大学
[新词识别]:  他/ 来到/ 了/ 网易/ 杭研/ 大厦
[搜索引擎模式]:  我/ 来到/ 北京/ 清华/ 华大/ 大学/ 清华大学
'''