import requests
from urllib import request
import json
import time
import urllib.request


for i in range(1,23):
    iurl = 'http://test.mingrisoft.com/uploads/ebook/548/22.jpg'
    r = requests.get(iurl)
    with open('./results/{}.jpg'.format(i),'wb') as f:
        f.write(r.content)

url = 'https://www.mingrisoft.com/EBookAjax/getCatalogInfo.html'

# 快速添加引号
# (.*?):(.*)
# '$1':'$2',

headers = {
    # 指定浏览器可以支持的web服务器返回内容压缩编码类型
    "Accept-Encoding":"gzip, deflate, br",
    # 浏览器可接受的语言
    "Accept-Language":"zh-CN,zh;q=0.9",
    # 表示是否需要持久连接。（HTTP 1.1默认进行持久连接）
    # 短连接的操作步骤是：
    # 建立连接——数据传输——关闭连接...建立连接——数据传输——关闭连接
    # 长连接的操作步骤是：
    # 建立连接——数据传输...（保持连接）...数据传输——关闭连接
    "Connection":"keep-alive",
    # 请求的内容长度
    "Content-Length":"16",
    # 请求的与实体对应的MIME信息
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"PHPSESSID=4tpmgtvcu68majoq10kgpdrsr2; Hm_lvt_1eb058d15d1f06c8d5a885184451caaa=1571827057,1572013725,1572067967,1572499489; Hm_lpvt_1eb058d15d1f06c8d5a885184451caaa=1572499552",
    # "Host":"www.mingrisoft.com",
    # 'Origin': 'https://www.mingrisoft.com',
    # 先前网页的地址，当前请求网页紧随其后,即来路
    'Referer': 'https://www.mingrisoft.com/ebook/548.html',
    # "Sec-Fetch-Mode":"cors",
    # "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
    }
data = {
    'p': 23,
    'ebook_id': 44
}
content = []
num = []
for i in range(45,47):
    data['p'] = i
    r = requests.post(url,data=data,headers=headers)
    time.sleep(1)
    r.encoding = 'utf-8'
    result = json.loads(r.text)
    # print(result)
    content.append(result)
    num.append(i)
    time.sleep(1.5)

# print(content)
# print(num)

for i,info in enumerate(content):
    print(info)
    path_code = info['path_code']
    chapter = info['chapter']
    img_url = 'http://test.mingrisoft.com//uploads/ebook/536/' + str(chapter) + '/' + str(num[i]) + path_code + '.jpg'
    # http://test.mingrisoft.com//uploads/ebook/536/1/05ab9bcb9c4205.jpg
    print(img_url)
    file_path = r'D:\Python上课代码\demo\results'
    filename = file_path + '\\' + str(i) + '.jpg'
  
    print(filename)
    urllib.request.urlretrieve(img_url, filename=filename)


for info,num1 in zip(content,num):
    path_code = info['path_code']
    chapter = info['chapter']
    # http://test.mingrisoft.com//uploads/ebook/548/3/855cb98d4ef00bc.jpg
    img_url = 'http://test.mingrisoft.com//uploads/ebook/536/'+str(chapter)+'/'+str(num1)+path_code+'.jpg'
    print(img_url)
    file_path=r'D:\Python上课代码\demo\results'
    filename = file_path + '\\' + str(num1) + '.jpg'
    # file_name ='%d'%num1
    # file_suffix = os.path.splitext(img_url)[1]
    # filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
    print(filename)
    urllib.request.urlretrieve(img_url,filename=filename)

	

# 为什么这么多人喜欢自学
# 害怕失败

# 保持方向感,人生规划离不开时代大环境
# 不要低头盲目的去学习任何一门语言,抬头看看这个时代,看看这个社会的进步

# 人工智能大发展,各种语言争奇斗艳
# 很多传统的工作岗位,会被替代,越来越多的人力工作 会被取代 高速公路上的收费员 被干掉了 原先这可是金饭碗
# 1.01的365次方是非常大的值   而0.99的365次方是一个非常小的值
# 之前我有一位同学，在阿里年薪是50-100之间,他是怎么学习的？
# 花钱去学习各种各样的知识   如何高效学习  时间管理等等
# 如果你长了一个省钱的脑袋  那么赚钱就很难做到

# 技术会更新,速度会变快
# 复合岗位
# 行业将洗牌,越来越专业
# 人才储备越来越充裕,毕业生数量和质量逐年提高
# 如何你还想以比较粗范的学习方式来学习的话,那一定不会有一个好的结果
# 互联网行业野蛮生长期进入尾声
# 面试Java程序员,录取让去学Python

# 也会在我们课程里面加上操作系统和计算机组成原理	
	
	
