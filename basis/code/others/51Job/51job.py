import time
import random
import csv
import requests
from lxml import etree

headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
			'Host': 'search.51job.com'
		}

# 51job小爬虫
def Spider(keyword, num_page=2):
	data = {}
	error_time = 0
	for i in range(1, num_page+1):
		print('[INFO]: Start to get the MNIST_data in page-%d' % i)
		url = 'http://search.51job.com/list/190200,000000,0000,00,9,99,%s,2,%d.html' % (keyword, i)
		try:
			res = requests.get(url, headers=headers)
			res.encoding = 'gbk'
			# 将源码转化为能被XPath匹配的格式
			html = etree.HTML(res.text)
			'''
			四种标签的使用方法 
			1) // 双斜杠 定位根节点，会对全文进行扫描，在文档中选取所有符合条件的内容，以列表的形式返回。 
			2) / 单斜杠 寻找当前标签路径的下一层路径标签或者对当前路标签内容进行操作 
			3) /text() 获取当前路径下的文本内容 
			4) /@xxxx 提取当前路径下标签的属性值 
			5) | 可选符 使用|可选取若干个路径 如//p | //div 即在当前路径下选取所有符合条件的p标签和div标签。 
			6) . 点 用来选取当前节点 
			7) .. 双点 选取当前节点的父节点 
			'''
			page_data_list = html.xpath("//div[@class='dw_table']")
			for pdl in page_data_list:
				# 职位
				position = pdl.xpath("./div/p/span/a/@title")
				# 公司名称
				company = pdl.xpath("./div/span[@class='t2']/a/text()")
				# 工作地区
				area = pdl.xpath("./div[@class='el']/span[@class='t3']")
				# 工资
				wage = pdl.xpath("./div[@class='el']/span[@class='t4']")
				# 发布时间
				publishtime = pdl.xpath("./div[@class='el']/span[@class='t5']")
				# 详情页链接
				link = pdl.xpath("./div/p/span/a/@href")
				# 数据保存
				for j in range(len(position)):
					data[company[j]] = [position[j], area[j].text, wage[j].text, publishtime[j].text, link[j]]

			time.sleep(1 + random.random())
		except:
			error_time += 1
			time.sleep(60)
			if error_time > 3:
				break


		with open("demo.csv", "w", newline="") as datacsv:  # newline="" 如果不加这个参数，新的一行会隔一行写入。
			# dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
			csvwriter = csv.writer(datacsv, dialect=("excel"))
			csvwriter.writerow(["公司名称", "岗位", "地点", "薪资", "发布日期"])
			for item in data:
				# csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
				csvwriter.writerow([item,data[item][0], data[item][1], data[item][2],data[item][3]])

	# with open('MNIST_data.txt', 'wb') as f:
		# pickle.dump(MNIST_data, f)
		# f.write(MNIST_data)

if __name__ == '__main__':
	Spider('python')