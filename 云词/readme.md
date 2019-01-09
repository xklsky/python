## 模块解释
- wordcloud -- 词云展示
- jieba -- 分词库
- matplotlib -- 2D绘图库     
- scipy -- 利用numpy做更高级的数学，信号处理，优化，统计等等
- NumPy -- 支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库

## 结巴中文分词支持的三种分词模式包括：
1. 精确模式：试图将句子最精确地切开，适合文本分析；
2. 全模式：把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义问题；
3. 搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。  

同时结巴分词支持繁体分词和自定义字典方法。  
案例: demo1.py

## WordCloud参数说明
- font_path : string
    - 字体路径，需要展现什么字体就把该字体路径+后缀名写上，如：font_path = '黑体.ttf'
- width : int (default=400) 
    - 输出的画布宽度，默认为400像素
- height : int (default=200)
    - 输出的画布高度，默认为200像素
- mask : nd-array or None (default=None)
    - 图片背景参考形状，如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将被忽略，遮罩形状被 mask 取代。
- scale : float (default=1)
    - 图幅放大、缩小系数  
- min_font_size : int (default=4)
    - 最小的字符
- min_font_size : int (default=4)
    - 最大的字符
- font_step : int (default=1) 
    - 字体步长，如果步长大于1，会加快运算但是可能导致结果出现较大的误差。
- max_words : number (default=200)
    - 最多显示的词数
- stopwords : set of strings or None
    - 不需要显示的词
- background_color : color value (default="black")
    - 背景颜色
- mode : string (default=”RGB”) 
    - 当参数为“RGBA”并且background_color=None，背景为透明。
- prefer_horizontal : float (default=0.90) 
    - 词语水平方向排版出现的频率，默认 0.9 （所以词语垂直方向排版出现频率为 0.1 ）

- relative_scaling : float (default=.5) 
    - 词频和字体大小的关联性
- color_func : callable, default=None 
    - 生成新颜色的函数，如果为空，则使用 self.color_func
- regexp : string or None (optional) 
    - 使用正则表达式分隔输入的文本
- collocations : bool, default=True 
    - 是否包括两个词的搭配
- colormap : string or matplotlib colormap, default=”viridis” 
    - 给每个单词随机分配颜色，若指定color_func，则忽略该方法。
- fit_words(frequencies) 
    - 根据词频生成词云【frequencies，为字典类型】
- generate(text) 
    - 根据文本生成词云
- generate_from_frequencies(frequencies[, ...]) 
    - 根据词频生成词云
- generate_from_text(text) 
    - 根据文本生成词云
- process_text(text) 
    - 将长文本分词并去除屏蔽词（此处指英语，中文分词还是需要自己用别的库先行实现，使用上面的 fit_words(frequencies) ）
- recolor([random_state, color_func, colormap]) 
    - 对现有输出重新着色。重新上色会比重新生成整个词云快很多。
- to_array() 
    - 转化为 numpy array
- to_file(filename)
    - 输出到文件