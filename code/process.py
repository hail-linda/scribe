#coding=utf-8
import codecs , chardet

f=codecs.open("./strokes/strokes.txt")

a=f.readlines()
b=[]
for i in range(len(a)):
	try:
		a[i]=a[i].decode("gb2312")
		a[i]=a[i].replace(u"横折折折钩/横撇弯钩","1")
		a[i]=a[i].replace(u"横折弯钩/横斜钩","2")
		a[i]=a[i].replace(u"横撇/横钩","3")
		a[i]=a[i].replace(u"竖折/竖弯","4")
		a[i]=a[i].replace(u"横折折撇","5")
		a[i]=a[i].replace(u"竖折折钩","6")
		a[i]=a[i].replace(u"竖弯钩","7")
		a[i]=a[i].replace(u"横折钩","8")
		a[i]=a[i].replace(u"横折","9")
		a[i]=a[i].replace(u"竖钩","10")
		a[i]=a[i].replace(u"竖提","11")
		a[i]=a[i].replace(u"斜钩","12")
		a[i]=a[i].replace(u"弯钩","13")
		a[i]=a[i].replace(u"撇点","14")
		a[i]=a[i].replace(u"撇折","15")
		a[i]=a[i].replace(u"竖","16")
		a[i]=a[i].replace(u"横","17")
		a[i]=a[i].replace(u"点","18")
		a[i]=a[i].replace(u"撇","19")
		a[i]=a[i].replace(u"捺","20")
		a[i]=a[i].replace(u"提","21")
		a[i]=a[i].replace(u"、"," ")
		b.append(a[i][:-3])
		print(a[i])
	except:
		pass
for i in b:
	print(i)


