# 导入socket库:
import socket,time,threading
import gzip
import time
 

# 创建一个socket:
# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('192.168.123.30', 9000))
s.listen(5)
print('Waiting for connection...')
#处理函数
def receivemsg(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # sock.send(b'Welcome!')
    while True:
        localtime = time.strftime("%Y-%m-%d %X",time.localtime())
        localdate = time.strftime("%Y-%m-%d",time.localtime())
        data = sock.recv(1024)
        data = data.decode('utf-8','ignore').replace('#END#','').strip()
        time.sleep(1)
        if data:
            print(localtime,data)
            f = open(localdate +'.txt',"a",encoding='UTF-8')
            f.write(localtime + data + '\n')
        if not data:
            break
        # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
while True:
# 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=receivemsg,args=(sock, addr))
    t.start()