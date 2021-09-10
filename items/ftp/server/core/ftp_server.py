import socketserver,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import configparser
from conf import settings
import os,subprocess
import hashlib
import re

STATUS_CODE  = {
    200 : "Task finished",
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",
    259 : "path doesn't exist on server",
    260 : "path changed",
}

import json
class FTPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            if not self.data:
                print("client closed...")
                break
            data  = json.loads(self.data.decode())
            if data.get('action') is not None:
                #print("---->",hasattr(self,"_auth"))
                if hasattr(self,"_%s"%data.get('action')):
                    func = getattr(self,"_%s"% data.get('action'))
                    func(data)
                else:
                    print("invalid cmd")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)

    def send_response(self,status_code,data=None):
        '''向客户端返回数据'''
        response = {'status_code':status_code,
                    'status_msg':STATUS_CODE[status_code],
                    }
        #print("data",data)
        if data:
            #print("goes here....")
            response.update( { 'data': data  })
        #print("-->data to client",response)
        self.request.send(json.dumps(response).encode())

    def _auth(self,*args,**kwargs):
        data = args[0]
        if data.get("username") is None or data.get("password") is None:
            self.send_response(252)

        user =self.authenticate(data.get("username"),data.get("password"))
        if user is None:
            self.send_response(253)
        else:
            print("passed authentication",user)
            self.user = user
            self.user['username'] =  data.get("username")

            self.home_dir = "%s/home/%s" %(settings.BASE_DIR,data.get("username"))
            self.current_dir = self.home_dir
            self.send_response(254)


    def authenticate(self,username,password):
        '''验证用户合法性，合法就返回用户数据'''

        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print("pass auth..",username)
                config[username]["Username"] = username
                return config[username]
