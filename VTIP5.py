def function1():
    with open('plan.txt', 'r') as f:
        full_txt = sorted(f.read().split())
        print(full_txt)
    with open('sort_plan.txt', 'w') as s:
        print(full_txt, file=s)
function1()

def function2():
    import re
    import urllib.request

    pat = re.compile(r'[\w.-]+@[\w.-]+(?=\.[\w]+)+')
    emails = []
    url = "http://dfedorov.spb.ru/python/files/mbox-short.txt"
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            urls = pat.findall(line)
            if urls:
                emails += urls

    with open("mail.txt", 'w') as text1:
        print(emails, file=text1)
function2()

def function3():
    import re
    import urllib.request

    pat = re.compile('<.*?>')
    url = "http://dfedorov.spb.ru/python/files/p.html"
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            urls = pat.sub('', line)
            print(urls)
function3()

def function4():
    import urllib.request
    slovar = {}
    count = 0
    url = "http://dfedorov.spb.ru/python3/src/romeo.txt"
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            abc = line.split()
            for i in abc:
                for j in abc:
                    if i == j:
                        count = count + 1
                        slovar[i] = (count)

                count = 0

            print("подсчет повторений каждого слова в абзаце")
            print(slovar)
function4()

def function5():
    name=input("Введите название текстового файла")
    word=input("Введите слово которое хотите найти")
    c=0
    with open(name) as f:
        a=f.read()
        a=a.split()
        for i in a:
            if i==word:
                c+=1
        print("Данное слово встречается ",c ,"раз" )
function5()

def function6():
    name=input("Введите название файла")
    line=input("Введите подстроку, которую хотите найти")
    with open(name) as f:
        a=f.readlines()
        for i in a:
            if line in i:
                print(i)
        print(line)
function6()

import re
def function7():
    url=input("Введите название  HTML файла")
    with open(url) as f:
        for lines in f:
            res = re.findall('href="(\S*)"', lines)
            print(res)
function7()
