import requests                 #將<div>, <li>, <a>, <h1>, <h2>, <h3>, <span>內的文字print出來的爬蟲
from firebase import firebase
import os

address = input("input a address:")         #輸入爬的網址，直到網址正確或錯誤10次
max_try = 10
try_count = 0
for _ in range(max_try):
    try:
        text = requests.get(address)
        break 
    except:
        try_count+=1
        if try_count < max_try:
            address = input("wrong address!\ninput a address:")
        else:
            _ = input("out of max try! program shot down!")
            os._exit()

def dopop():                    #刪除所有output裡的指定物件
    global pops
    pops.reverse()
    for i in range(len(pops)):
        output.pop(pops[i])
    pops = []

output = text.text.rsplit(">")
pops = []
for i in range(len(output)):    #若有</div>, </p>, <p>, </b>, <b>, </button>, <button>, </li>, </a>, </h1>, </h2>, </h3>, </font>, </span>, <span>, <br>則保留，其餘的刪除
    if (output[i].find("</div") == -1 and output[i].find("</p") == -1 and output[i].find("<sup") == -1 and output[i].find("<p") == -1 and output[i].find("</b") == -1 and output[i].find("<b") == -1 and 
    output[i].find("</button") == -1 and output[i].find("<button") == -1 and output[i].find("</li") == -1 and output[i].find("</a") == -1 and output[i].find("<a") == -1 and output[i].find("</h1") == -1 and 
    output[i].find("</h2") and output[i].find("</h3") == -1 and output[i].find("</h4") == -1 and output[i].find("</font") == -1 and output[i].find("</span") == -1 and output[i].find("<span") == -1 and 
    output[i].find("<br") == -1):
        pops.append(i)
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
    output[i] = output[i].replace("\r","")
    output[i] = output[i].strip(" ")

for i in range(len(output)):    #刪除陣列內的無意義內容
    if output[i] == ' ' or output[i] == '' or output[i].find("&#") != -1:
        pops.append(i)

dopop()

sum = " ".join(output)          #將陣列結合成單個字串


sum  = sum.replace("  "," ")    #刪除多餘換行和空格
sum  = sum.replace("\n ","\n")
sum  = sum.replace(" \n","\n")
sum  = sum.replace("\n\n\n","\n") 
sum  = sum.replace("\n\n","\n")
sum  = sum.replace("\n\n","\n")
sum  = sum.replace("\n\n","\n")

if sum.startswith("\n"):
    sum = sum.replace("\n","",1)

print(sum)                          #輸出預覽

'''
fdb = firebase.FirebaseApplication('https://...', None) 
fdb.post('/',sum)
'''

path = os.path.dirname(os.path.abspath(__file__))

if not(os.path.exists(path + "\\output")):  #若不存在文件夾建立文件夾
    os.mkdir(path + "\\output")

path = path + "\\output"

file_count = 0                              #確認已輸出txt存在幾個
while True:
    if file_count == 0:
        if os.path.exists(path + "\\output.txt"):
            file_count+=1
        else:
            break
    if(os.path.exists(path + "\\output" + str(file_count+1) + ".txt")):
        file_count+=1
    else:
        break

if file_count == 0:                         #輸出到txt
    f = open(path + "\\output.txt", "w", encoding="utf-8")
else:
    f = open(path + "\\output" + str(file_count+1) + ".txt", "w", encoding="utf-8") 
f.write(sum)                                
f.close()

#print(output)
i = input("Press Enter to continue:")       #等待用戶確認才結束程式