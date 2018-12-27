import threading
import optparse 
import socket
def scan(host,port):
    try:
      socc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      b = bytes("hello",encoding='utf-8')
      socc.connect((host,port))
      socc.send(b)
      socketdata=socc.recv(1024)
      print(u'端口:%s开放了-----------\n%s' %(port,socketdata) )
      socc.close
    except :
        print (u'端口:%s没有开放\n' %port )
        socc.close
   
def main():
    args = [8080,8081,8082,443,8088,8087,8086,9876,80]
    host = "127.0.0.1"
    for i in args:
        t = threading.Thread(target=scan, args=(host, i))
        t.start()
if __name__ == '__main__':
  main()