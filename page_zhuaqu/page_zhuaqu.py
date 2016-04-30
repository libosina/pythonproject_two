#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib

'''
抓取指定的页面并copy到本地
'''

def callbackfunc(blocknum, blocksize, totalsize):
	'''回调函数
	@blocknum: 已经下载的数据块
	@blocksize: 数据块的大小
	@totalsize: 远程文件的大小
	'''
	percent = 100.0 * blocknum * blocksize / totalsize
	if percent > 100:
		percent = 100
	print "%.2f%%"% percent

#html页面
# url = 'http://www.sina.com.cn'
# local = r'E:\python2.7\www\python\page_zhuaqu\html\com.cn.html'
# urllib.urlretrieve(url, local, callbackfunc)

#图片
# url = 'http://n.sinaimg.cn/sports/20160412/JDct-fxrckae7827812.jpg'
# local = r'E:\python2.7\www\python\page_zhuaqu\html\JDct-fxrckae7827812.jpg'
# urllib.urlretrieve(url, local, callbackfunc)

#视频
#http://v6.pstatp.com/origin/10638/4427174058?Signature=KJcyxR8l3tGf0EAk%2BXedm%2BQsoMw%3D&Expires=1460452601&KSSAccessKeyId=qh0h9TdcEMrm1VlR2ad/
url = 'http://v6.pstatp.com/origin/12538/6996033668?Signature=qv9%2FvAwpuFLfySiydAmJH761SI4%3D&amp;Expires=1461241184&amp;KSSAccessKeyId=qh0h9TdcEMrm1VlR2ad/'
local = r'D:\MP3\mp4\2016_04_21.mp4'
urllib.urlretrieve(url, local, callbackfunc)