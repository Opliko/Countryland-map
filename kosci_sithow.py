
import re
from robobrowser import RoboBrowser
import requests
from random import randint
from bs4 import BeautifulSoup
import schedule
import time
cookie={}
urls = ["https://grupy.jeja.pl/topic,numer_tematu,rzuty-koscmi,nowe.html"] 
#zastąp "numer_tematu"... numerem tematu. Możesz też zmienić nazwę (tu "rzuty-koscmi", swoją zobacz w url)

def login():
    global cookie
    browser = RoboBrowser(user_agent="bot autorstwa opliko95", parser="html.parser")
    browser.open("https://www.jeja.pl/logowanie.html")
    login_form = browser.get_form(class_="standard-form log-form")
    login_form["login"].value = "login" #zastąp loginem
    login_form["passw0rd"].value = "hasło" #zastąp hasłem
    login_form["remember"].value = "1"
    browser.submit_form(login_form)
    cookie = {"Remember":browser.session.cookies["Remember"]}

def bot():
    global urls
    for url in urls:
        try:
            s = requests.Session()
            strona = s.get(url, cookies=cookie)
            zupa = BeautifulSoup(strona.text, "html.parser")
            n = zupa.find_all("a", {"class":'pagination-number'})
            if len(n)>0:
                if "https://www.grupy.jeja.pl/{}".format(str(n[-1].get("href"))) != url:
                    urls[url.index(url)] = "https://www.grupy.jeja.pl/{}".format(str(n[-1].get("href")))
                    s = requests.Session()
                    strona = s.get(url, cookies=cookie)
                    zupa = BeautifulSoup(strona.text, "html.parser")
            z = zupa.find_all("div", {"class":"komentarz kom-mar"})
            nick = z[-1].find("div", {"class":"nick"})
            nr = 1
            nick = nick.find("a", href=True).contents[0]
            print(nick)
            while "kosci_sithow" not in nick:
                no_post=0
                try:
                    postid = str(z[-1*nr].get("id")[4:])
                    #avatar = z[-1*nr].find("img", {"class":"komentarz-foto"}).get("src")
                    post = z[-1*nr].find("div", {"class":"text"})
                    t = '[quote=[url=https://www.jeja.pl/user,{0}]{0}[/url]]'.format(nick.replace(" ", ""))
                    for i in post.contents:
                         t+=str(i)
                    
                    replacable = ['<a class="fancybox" data-fancybox="grupy" data-fancybox-group="fancybox" href="',
                                  '">', '<img alt="" src="', '" style="max-width:510px"/>', '</a>', '<a class="withUl" href="',
                                  '" rel="nofollow', '" target="_blank', '<strong>', '</strong>', '<em>', '</em>', '<u>', '</u>',
                                  '<iframe allowfullscreen="" frameborder="0" height="285" src="https://www.youtube.com/embed/',
                                  '" width="510]</iframe>', '<br/>']
                    replaces = ['[url=', ']', '[img]', '[/img]', '[/url]', '[url=', '', '', '[b]', '[/b]', '[i]', '[/i]',
                                '[u]', '[/u]', '[youtube]', '[/youtube]', '']
                    for i in range(len(replacable)):
                        t = t.replace(replacable[i], replaces[i])
                    dice = t.lower().find("[dice]")
                    if dice==-1:
                        no_post=1
                    while dice!=-1:
                        wiad = ''
                        dice_end=t.lower().find("[/dice]")
                        kosc = t[dice+6:dice_end]
                        oc = kosc.find("k")
                        if oc == -1:
                            oc = kosc.find("d")
                        if oc!=-1:
                            il = kosc[:oc]
                            ocz = kosc[oc+1:]
                            wyniki = []
        
                            if il.isdigit() and ocz.isdigit():
                                for i in range(int(il)):
                                    wyniki.append(randint(1, int(ocz)))
            
                                if ocz in ("4", "6", "8", "10", "12", "20"):
                                    for wyn in wyniki:
                                        wiad+="[img]https://countryland.tk/kosci/D{}/{}.png[/img]\n".format(ocz, wyn)
                                else:
                                    for wyn in wyniki:
                                        wiad+="[b]{}[/b]\n".format(wyn)
                                t = t[:dice]+wiad[:-1]+t[dice_end+7:]
                        dice = t.lower().find("[dice]")
                    if no_post==0:
                        t+="[/quote]"
                        s.post(url[:-10]+",odpowiedz.html#odp", data={"post":str(t), "action":"Odpowiedz"}, cookies=cookie)
                        s.post("https://grupy.jeja.pl/post,usun,{}.html".format(postid), data={"action":"Usuń"}, cookies=cookie)
                        
                except Exception as e:
                    print(str(e))
                nr+=1
                nick = z[-nr].find("div", {"class":"nick"})
                nick = nick.find("a", href=True).contents[0]
                time.sleep(10.5)
        except Exception as e:
            print(str(e))
login()
bot()
schedule.every(2).minutes.do(bot)
schedule.every(3).weeks.do(login)



while True:
    schedule.run_pending()
    time.sleep(60)
