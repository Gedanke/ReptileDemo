'''
Function:
	分析51jb招聘数据
作者:
	Python编程学习圈
公众号:
	Python编程学习圈
'''
import os
import pickle
from pyecharts import Bar
from pyecharts import Pie
from pyecharts import Map


# 柱状图(2维)
def DrawBar(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	bar = Bar(title)
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	bar.add('', attrs, values, mark_point=["min", "max"], is_convert=True)
	bar.render(os.path.join(savepath, '%s.html' % title))


# 饼图
def DrawPie(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	pie = Pie(title, title_pos='center')
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	pie.add('', attrs, values, is_label_show=True, radius=[30, 50], rosetype="radius", legend_pos="left", legend_orient="vertical")
	pie.render(os.path.join(savepath, '%s.html' % title))


# 地图
def DrawMap(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	map_ = Map(title, width=1200, height=600)
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	map_.add('', attrs, values, maptype='china', is_visualmap=True, visual_text_color='#000')
	map_.render(os.path.join(savepath, '%s.html' % title))



if __name__ == '__main__':
	with open('MNIST_data.pkl', 'rb') as f:
		data = pickle.load(f)

	wageDict = {}
	for key, value in data.items():
		area = value[1].split('-')[0]
		wage = value[2]
		if wage:
			if wage[-1] == '年':
				continue
			try:
				wage_1, wage_2 = wage.split('-')
				if wage_2[-3] == '万':
					wage_2 = wage_2[:-3]
					wage = (float(wage_1) * 1e4 + float(wage_2) * 1e4) / 2
				elif wage_2[-3] == '千':
					wage_2 = wage_2[:-3]
					wage = (float(wage_1) * 1e3 + float(wage_2) * 1e3) / 2
				else:
					continue
			except:
				if wage[-3] == '万':
					wage = wage[:-3]
					wage = float(wage) * 1e4
				elif wage[-3] == '千':
					wage = wage[:-3]
					wage = float(wage) * 1e3
				else:
					continue
			if area not in wageDict:
				wageDict[area] = [wage, 1]
			else:
				temp = wageDict[area]
				wageDict[area] = [temp[0]+wage, temp[1]+1]
	wageDict_avg = {}
	for key, value in wageDict.items():
		if value[0] / value[1] < 11000:
			continue
		wageDict_avg[key] = value[0] / value[1]
	DrawBar(title='部分城市Python相关岗位平均薪资柱状图', data=wageDict_avg, savepath='./results')
	'''
	'''
	statistics_area = {}
	for key, value in data.items():
		area = value[1].split('-')[0]
		if area in ['合肥']:
			area = '安徽'
		elif area in ['杭州', '宁波', '金华', '温州', '舟山']:
			area = '浙江'
		elif area in ['广州', '佛山', '深圳']:
			area = '广东'
		elif area in ['南京', '常州', '苏州']:
			area = '江苏'
		elif area in ['济南']:
			area = '山东'
		elif area in ['武汉']:
			area = '湖北'
		elif area in ['成都', '德阳']:
			area = '四川'
		elif area in ['呼和浩特']:
			area = '内蒙古'
		elif area in ['长沙']:
			area = '湖南'
		elif area in ['郑州']:
			area = '河南'
		elif area in ['沈阳']:
			area = '辽宁'
		elif area in ['西安']:
			area = '陕西'
		elif area in ['福州']:
			area = '福建'
		elif area in ['南昌']:
			area = '江西'
		elif area in ['贵阳']:
			area = '贵州'
		elif area in ['南宁']:
			area = '广西'
		elif area in ['昆明']:
			area = '云南'
		elif area in ['石家庄']:
			area = '河北'
		if area not in statistics_area:
			statistics_area[area] = 1
		else:
			statistics_area[area] += 1
	DrawMap(title='部分地区Python相关岗位招聘需求量', data=statistics_area, savepath='./results')

	positionDict = {}
	for key, value in data.items():
		position = value[0]
		if position in positionDict:
			positionDict[position] += 1
		else:
			positionDict[position] = 1
	positionDict_new = {}
	for key, value in positionDict.items():
		if value < 100:
			continue
		positionDict_new[key] = value
	DrawPie(title='Python相关岗位有哪些', data=positionDict_new, savepath='./results')