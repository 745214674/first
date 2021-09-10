import telnetlib
import time

tn = telnetlib.Telnet("1.1.1.1",23)
tn.set_debuglevel(0)

def tn_login(username,password):
    cmd = 'EPON0/5:1'
    mac = input("请输入mac地址：")
    tn.read_until(b"Username:")
    tn.write(username + b"\n" )

    tn.read_until(b"Password:")
    tn.write(password + b"\n" )

    tn.read_until(b">")
    tn.write(b"ena" + b"\n")
    tn.read_until(b"#")
    tn.write(b'conf' + b"\n")
    #tn.write(('show running-config | begin %s' % (cmd + '\n')).encode('gbk'))
    tn.write(('show epon onu-information mac-address %s' %mac + '\n').encode('gbk'))
    time.sleep(0.5)

    result = tn.read_very_eager()
    print(result.decode("gbk"))


# def exec_cmd(cmd):
#     if tn_login()
#     tn.write(('show running-config | begin %s' %(cmd +'\n')).encode('gbk') )
#     time.sleep(2)
#     result = tn.read_very_eager()
#     print(result.decode("gbk"))
tn_login(b'admin',b'admin')

    # tn.write(b"conf"+b"\n")
    # tn.read_until(b"Shi(config)#")
    # tn.write(b"create vlan 253 active\n")
    # tn.read_until(b"BanGongShi#")
    # tn.close()