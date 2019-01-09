## 模块解释
- wordcloud -- 词云展示
- jieba -- 分词库
- matplotlib -- 2D绘图库     
- scipy -- 利用numpy做更高级的数学，信号处理，优化，统计等等

## 结巴中文分词支持的三种分词模式包括：
1. 精确模式：试图将句子最精确地切开，适合文本分析；
2. 全模式：把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义问题；
3. 搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。  

同时结巴分词支持繁体分词和自定义字典方法。  
案例: demo1.py

## WordCloud参数说明
- font_path : string
    - 使用的字体库
- width : int (default=400)
    - 图片宽度
- height : int (default=200)
    - 图片高度
- mask : nd-array or None (default=None)
    - 图片背景参考形状  
- scale : float (default=1)
    - 图幅放大、缩小系数  
- min_font_size : int (default=4)
    - 最小的字符
- min_font_size : int (default=4)
    - 最大的字符
- max_words : number (default=200)
    - 最多显示的词数
- stopwords : set of strings or None
    - 不需要显示的词
- background_color : color value (default="black")
    - 背景颜色
- ......