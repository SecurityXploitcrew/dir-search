#-*- coding: utf-8 -*-
import requests

logo = """
╔╦╗┬┬─┐  ╔═╗┌─┐┌─┐┬─┐┌─┐┬ ┬
 ║║│├┬┘  ╚═╗├┤ ├─┤├┬┘│  ├─┤
═╩╝┴┴└─  ╚═╝└─┘┴ ┴┴└─└─┘┴ ┴
Author : Katyusha_sxc
Team   : SecurityXploitCrew
"""
print logo
target = raw_input('target ~>  ')
wordlist = open('word.txt','r').read()
bawah = wordlist.split("\n")
total = 0
print ""
for i in bawah:
     url = target+"/"+i
     code = requests.get(str(url)).status_code
     if code == 200:
             total += 1
             print "[+] OK : "+url
else :
             print "[-] ER : "+url
print ""
print "Total :",str(total)
