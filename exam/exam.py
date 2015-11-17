# -*- encoding:UTF-8 -*-
'''
这里涉及到考题数据库的调用、显示、答案的存储
采用的技术是python对file的操作
使用Python中数据持久存储与交换标准库
参考：D:\lesson_doc\data_storage_exchange.txt
'''
try:
    import cPickle as pickle
except:
    import pickle