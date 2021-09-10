import telnetlib


class OLT(object):
    def __init__(self):
        pass

    def judgement_type(self):
        pass

    def make_connection(self):
        ip_add = '10.159.0.'
        ip_num = input("请输入IP地址：%s" % ip_add).strip()
        ip_merge = ip_add + ip_num
        print(ip_merge)
        ip_split = ip_num.split(".")
        tn = telnetlib.Telnet(ip_merge, 23)
        tn.set_debuglevel(10)
        if tn.read_until(b'Username:'):
            tn.write(b'admin' + b'\n')

            if 0 in ip_split:
                tn.read_until(b'Password:')
                default_password = 'test'
                password = input("请输入密码回车为默认密码：%s" % default_password)
                if len(password) == 0:
                    password = default_password
                tn.write(bytes(password))
                tn.read_until(b">")
                tn.write(b"ena" + b"\n")
                tn.read_until(b"#")
                tn.write(b'conf' + b"\n")
                self.interactive('boda')

        else:
            tn.write(b'raisecom' + b'\n')
            tn.read_until(b'Password:')
            default_password = "test"
            password = input("请输入密码回车为默认密码：%s" % default_password)
            if len(password) == 0:
                password = default_password
                tn.write(bytes(password))
                tn.read_until(b">")
                tn.write(b"ena" + b"\n")
                tn.read_until(b"#")
                tn.write(b'conf' + b"\n")
                self.interactive('raisecom')

    def interactive(self, device):

        menu = '''---当前设备为 %s---
        1.查询ONU上线情况
        2.查询ONU口子vlan
        3.查询ONU光功率
        4.查询PON口配置

        5.修改ONU口子vlan
        6.
        ''' % device

        menu_dic = {
            '1': self.query_online,
            '2': self.query_vlan,
            '3': self.query_transceiver,
            '4': self.query_PONconfig,
            '5': self.modify_config,

        }
        exit_flag = False
        while not exit_flag:
            print(menu)
            user_option = input("输入序号继续下文:").strip()
            if user_option in menu_dic:
                menu_dic[user_option]()
            else:
                print("\033[1m;31Option does not exist!\033[0m")


    def query_online(self):
        pass

    def query_vlan(self):
        pass

    def query_PONconfig(self):
        pass


    def query_transceiver(self):
        pass

    def modify_config(self):
        pass
