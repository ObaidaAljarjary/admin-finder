#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError
R = "\033[0;31m"
print(R)
def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1
import os
os.system("clear")
os.system("figlet admin-finder")

def findAdmin():
        f = open("link.txt","r");
        link = raw_input("Enter Website :  ")
        print "\n\nAvilable links : \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break                                                                           req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "OK => ",req_link


findAdmin()
