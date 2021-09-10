import telnetlib


def make_connection():
    ip_merge = '10.159.160.128'
    print(ip_merge)

    tn = telnetlib.Telnet(ip_merge, 23)
    tn.set_debuglevel(10)
    # if tn.read_until('Username:'):
    #     tn.write('admin' + '\n')
    #
    #     password = input('ddd:')
    #     tn.write(bytes(password))
    #     tn.read_until(">")
    #     tn.write("ena" + "\n")
    #     tn.read_until("#")
    #     tn.write('conf' + "\n")
        #self.interactive('boda')

    tn.read_until('Login:')
    tn.write('raisecom')
    tn.read_until('Password:')
    tn.write('raisecom')
    tn.read_until(">")
    tn.write("ena" + "\n")
    tn.read_until('Password:')
    tn.write('raisecom')
    tn.write('raisecom')
    tn.read_until("#")
    tn.read_until()
    tn.write('conf' + "\n")
    tn.write('create vlan 3334 active')
make_connection()