import telnetlib
ip_data = {
    'raisecom':'raisecom',
    'Username':'admin',
}
def make_connection():
    ip_add = '10.159.0.'
    ip_num = input("请输入IP地址：%s" % ip_add).strip()
    print(ip_num)
    ip_split = ip_num.split(".")
    tn = telnetlib.Telnet(ip_add, 23)
    tn.set_debuglevel(10)
    if tn.read_until(b'Username:'):
        tn.write(b'admin' + b'\n')

        if 0 in ip_split:
            tn.read_until(b'Password:' )
            default_password = 'test'
            password = input("请输入密码回车为默认密码：%s" % default_password)
            if len(password) ==0:
                password = default_password
            tn.write(bytes(password))
    else:
        tn.write(b'raisecom' + b'\n')
