import firebase.firebase
import requests                 #將<div>, <li>, <a>, <h1>, <h2>, <h3>, <span>內的文字print出來的爬蟲
from firebase import firebase

text = requests.get('https://zh.wikipedia.org/zh-tw/%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2') #爬的網址，可任意更改，這裡用的是：維基百科網路爬蟲頁面
output = text.text.rsplit(">")

pops = []
for i in range(len(output)):    #若有</div>, </p>, <p>, </b>, <b>, </button>, <button>, </li>, </a>, </h1>, </h2>, </h3>, </font>, </span>, <span>, <br>則保留，其餘的刪除
    if output[i].find("</div") == -1 and output[i].find("</p") == -1 and output[i].find("<sup") == -1 and output[i].find("<p") == -1 and output[i].find("</b") == -1 and output[i].find("<b") == -1 and output[i].find("</button") == -1 and output[i].find("<button") == -1 and output[i].find("</li") == -1 and output[i].find("</a") == -1 and output[i].find("<a") == -1 and output[i].find("</h1") == -1 and output[i].find("</h2") and output[i].find("</h3") == -1 and output[i].find("</h4") == -1 and output[i].find("</font") == -1 and output[i].find("</span") == -1 and output[i].find("<span") == -1 and output[i].find("<br") == -1:
        pops.append(i)

def dopop():
    global pops
    pops.reverse()
    for i in range(len(pops)):
        output.pop(pops[i])
    pops = []
dopop()


for i in range(len(output)):    #刪除<span>和<br>、<b>、<p>、<a>、<sup>、<button>的屬性內容和特殊符號
    if output[i].find("<span") != -1:
        temp = output[i].rsplit("<span")
        output[i] = temp[0]
    if output[i].find("<sup") != -1:
        temp = output[i].rsplit("<sup")
        output[i] = temp[0]
    if output[i].find("<a") != -1:
        temp = output[i].rsplit("<a")
        output[i] = temp[0]
    if output[i].find("<br") != -1:
        temp = output[i].rsplit("<br")
        output[i] = temp[0]
    if output[i].find("<button") != -1:
        temp = output[i].rsplit("<button")
        output[i] = temp[0]
    if output[i].find("<b") != -1:
        temp = output[i].rsplit("<b")
        output[i] = temp[0]
    if output[i].find("<p") != -1:
        temp = output[i].rsplit("<p")
        output[i] = temp[0]
    if output[i].find("{\\") != -1:
        pops.append(i)

dopop()

for i in range(len(output)):    #刪除剩餘的</部分和空格、換行、特殊符號
    output[i] = output[i].replace("</div","")
    output[i] = output[i].replace("</p","")
    output[i] = output[i].replace("</button","")
    output[i] = output[i].replace("</b","")
    output[i] = output[i].replace("</h1","")
    output[i] = output[i].replace("</h2","")
    output[i] = output[i].replace("</h3","")
    output[i] = output[i].replace("</h4","")
    output[i] = output[i].replace("</span","")
    output[i] = output[i].replace("</a","")
    output[i] = output[i].replace("</li","")
    output[i] = output[i].replace("</font","")
    output[i] = output[i].replace("    "," ")
    output[i] = output[i].replace("   "," ")
    output[i] = output[i].replace("  "," ")
    output[i] = output[i].replace("&gt;","")
    output[i] = output[i].replace("&nbsp;","")
    output[i] = output[i].replace("&times;","")
    output[i] = output[i].replace("\t","")
    output[i] = output[i].replace("\n\n\n","\n")
    output[i] = output[i].replace("\n\n","\n")
    #output[i] = output[i].replace("\n","")    #換行
    output[i] = output[i].replace("\r","")
    output[i] = output[i].strip(" ")

for i in range(len(output)):    #刪除陣列內的無意義內容
    if output[i] == ' ' or output[i] == '' or output[i] == '.' or output[i].find("&#") != -1:
        pops.append(i)

dopop()

sum = "".join(output)          #將陣列結合成單個字串
#print(sum)

print(output)
i = input("Press Enter to continue:")