import json

import re  # 正则表达式，进行文字匹配
import urllib.request  # 制定url，获取网页数据
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# 主函数
def main():
    getData()


# 获取数据
def getData():
    datalist = []
    k = 1
    for i in range(1,70):
        url = "https://search.51job.com/list/090200,000000,0000,00,9,99,web,2," + str(i) + ".html"
        html = askUrl(url)
        res = re.findall("window.__SEARCH_RESULT__(.*?)</script>", html)
        txt = json.loads(res[0][2:])
        for i in txt['engine_search_result']:
            if len(i['attribute_text']) == 4:
                data = []

                data.append(i['job_name'])
                data.append(i['company_href'])
                data.append(i['company_name'])
                data.append(i['providesalary_text'])
                data.append(i['jobwelf'])
                work_place = i['attribute_text'][0]
                work_request = i['attribute_text'][1]
                work_minimumDegree = i['attribute_text'][2]
                work_recruiternum = i['attribute_text'][3]
                data.append(work_place)
                data.append(work_request)
                data.append(work_minimumDegree)
                data.append(work_recruiternum)
                datalist.append(data)
    return datalist


# 请求访问
def askUrl(url):
    headers = {
        "User-Agent": "Mozilla / 5.0(Macintosh; Intel Mac OS X 10_15_6) AppleWebKit / 605.1 .15(KHTML, like Gecko) Version / 14.0 .3 Safari / 605.1 .15 }"
    }
    html = ''
    try:
        req = urllib.request.Request(url=url, headers=headers, method='GET')
        response = urllib.request.urlopen(req)
        html = response.read().decode('gbk')
    except Exception as e:
        if hasattr(e, "code"):
            print(e)
        if hasattr(e, "reason"):
            print(e)
    return html


# 首先启动主函数
if __name__ == '__main__':
    main()
