import telnetlib

def tn_login()



def initalization(username,password):

    mac = input("请输入mac地址：")
    tn.read_until(b"Username:")
    tn.write(username + b"\n" )

    tn.read_until(b"Password:")
    tn.write(password + b"\n" )

    tn.read_until(b">")
    tn.write(b"ena" + b"\n")
    tn.read_until(b"#")
    tn.write(b'conf' + b"\n")