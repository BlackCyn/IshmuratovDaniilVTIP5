import re
import urllib.request

#Отсортированное по алфавиту содержимое файла plan.txt поместите в файл sort_plan.txt
def fun1():
    with open('plan.txt', 'r') as file:
        full_txt = sorted(file.read().split())
        print(full_txt)
    with open('sort_plan.txt', 'w') as sorted_file:
        print(full_txt, file=sorted_file)
fun1()

#Найдите в файле (файл находится в сети интернет) строки, содержащие почтовые адреса.
#Запишите найденные строки в файл с именем mail.txt
def fun2():

    pat = re.compile(r'[\w.-]+@[\w.-]+(?=\.[\w]+)+')
    email = []
    url = "http://dfedorov.spb.ru/python/files/mbox-short.txt"
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            urls = pat.findall(line)
            if urls:
                email += urls

    with open("mail.txt", 'w') as textt:
        print(email, file=textt)
fun2()

#Очистите файл от HTML-тегов. Выведите на экран чистый текст
def fun3():

    pattern = re.compile('<.*?>')
    url = "http://dfedorov.spb.ru/python/files/p.html"
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            urls = pattern.sub('', line)
            print(urls)
fun3()

#Определите частоту встречаемости всех слов для текста, находящегося в сети Интернет
def fun4():
    voc = {}
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
                        voc[i] = (count)

                count = 0

            print("Счетчик повторений каждого слова в абзаце")
            print(voc)
fun4()

#Напишите функцию stringCount, которая принимает два входных аргумента - имя файла и строку,
#а возвращает число повторений указанной строки в указанном файле
def fun5():
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
fun5()

#Реализуйте функцию myGrep, которая принимает два входных аргумента -имя файла и строку
#А выводит на экран все строки указанного файла, содержащие заданную строку в качестве подстроки
def fun6():
    name=input("Введите название файла")
    line=input("Введите подстроку, которую хотите найти")
    with open(name) as f:
        a=f.readlines()
        for i in a:
            if line in i:
                print(i)
        print(line)
fun6()

#Реализуйте функцию links, которая принимает на вход имя HTML-файла
# и возвращает количество гиперссылок в этом файле(тег </a>)
def fun7():
    url=input("Введите название файла с разрешением HTML")
    with open(url) as f:
        for lines in f:
            res = re.findall('href="(\S*)"', lines)
            print(res)
fun7()







