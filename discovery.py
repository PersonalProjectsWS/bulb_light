import socket

MCAST_GRP = '239.255.255.250'
MCAST_PORT = 1982
MSEARCH_MSG = ('M-SEARCH * HTTP/1.1\r\n' + 
'HOST: 239.255.255.250:1982\r\n' +
'MAN: "ssdp:discover"\r\n' +
'ST: wifi_bulb\r\n');

timeout = 5
isfound = False

socket.setdefaulttimeout(timeout)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.bind(('', MCAST_PORT))
s.sendto(MSEARCH_MSG.encode(),(MCAST_GRP, MCAST_PORT))

while True:
    try:
        data, addr = s.recvfrom(65507)
        data = data.decode("utf-8")

        if data.find("yeelight") != -1:
            isfound = True
            print("Se ha encontrado una bombilla de Yeelight")
            print(data)
            break
    
    except:
        print("No se ha encontrado ninguna bombilla")
        break

print("Proceso terminado")
s.close()
