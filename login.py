# -*- coding:utf-8 -*-
# @Time:2020/7/25 10:08
# @Author:zhuqing
# @File:budingcenshu.py
# def printinfo(argl,*vartuple):
#     global l
#     print("输出:%s"%argl)
#     l = vartuple
#     print(l)
# printinfo(70,89,90)
# a=[7,8,9]
# printinfo(a)
# print(type(l))
#登录
import  requests
# host="http://127.0.0.1"
s=requests.session()
class Login():
    def __init__(self,s):#这里的s容易忘填，s 是用来保持登录态
        self.s=s
        self.host="http://127.0.0.1"
    def login(self,username,password):
        url = self.host+"/api/mgr/signin"
        body = {
                "username": username,
                "password": password
            }
        r=self.s.post(url=url,data=body)
        return r
# print(login().text)
# if __name__=="__main__":
#     p=Login(s) #是def __init__(self,s)的s
#     k=p.login("byhy","88888888")
#     print(k.text)


