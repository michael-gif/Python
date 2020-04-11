import time
class client(object):
    def __init__(self,name):
        self.name = name
        self.lan = 'None'
    def info(self):
        print('Name: ' + self.name)
        print('LAN connection: ' + self.lan)

client1 = client('michael')
client2 = client('jeff')

class server(object):
    def __init__(self,name,ip,lan,wan):
        self.name = name
        self.ip = ip
        self.lan = lan
        self.wan = wan
        self.clients = [client1,client2]
    def addclient(self,clientname):
        if clientname not in self.clients:
            self.clients.append(clientname)
            self.clients[len(self.clients)-1].lan = 'lan1'
            print('Connected')
        else:
            print('clients already exists')
        logupdate(clientname," Connection Found:")
    def removeclient(self,clientname):
        if clientname in self.clients:
            self.clients[len(self.clients)-1].lan = 'None'
            self.clients.remove(clientname)
            print('Disconnected')
        else:
            print('client does not exist')
        logupdate(clientname," Connection Lost:")
    def info(self,clientvariablename):
        if clientvariablename in self.clients:
            print('Name: ' + self.name)
            print('IP: ' , self.ip)
            print('Hosting:' + self.lan)
            print('WAN connection: ' + self.wan)
        else:
            print('No LAN connection')
    def logs(self,clientname):
        if clientname in self.clients:
            logupdate(clientname," Log Request:")
            f = open('serverlogs.txt','r')
            print(f.read())
            f.close()
        else:
            print('No LAN connection')

def logupdate(clientname,logtype):
    f = open("serverlogs.txt","a")
    f.write(time.asctime(time.localtime(time.time())) + logtype + clientname.name + "\n")
    f.close()

server1 = server('LAN1-server',0,'lan1','None')
client3 = client(input('Enter a username'))
run = True
while run == True:
    command = input("")
    if command == 'lan connect':
        server1.addclient(client3)
    elif command == 'lan disconnect':
        server1.removeclient(client3)
    elif command == 'self info':
        client3.info()
    elif command == 'server info':
        server1.info(client3)
    elif command == 'logs':
        server1.logs(client3)
    elif command == 'end':
        if client3.lan != 'None':
            server1.removeclient(client3)
        run = False
    else:
        print('unknown command')
