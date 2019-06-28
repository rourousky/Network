# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:37:44 2019
【服务端】
@author: 张伟英
"""
import socket



#############TCP服务端
def main():
    
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2.绑定端口
    tcp_socket.bind('', 6905)
    
    # 3.listen监听套接字
    tcp_socket.listen(128)
    
    while True:
        
        # 4.accept等待链接
        new_socket, client_addr = tcp_socket.accept()
        
        while True:
            
            #5.接收客户端发来的信息
            client_msg = new_socket.recv(1024)
            
            if client_msg :
                
                # 6.反馈给客户端
                new_socket.send('hahah'.encode('utf-8'))
                
            else:
                
                break
        
        # 7.关闭套接字
        new_socket.close() # 关闭客户端的套接字
        
    tcp_socket.close() # 关闭服务器端的套接字，停止服务
    

if __name__ == '__main__':
    
    main()

##################TCP客户端
import socket

def mgr():
    
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2.创建链接
    tcp_socket.connet('192.168.6.236', 6675)
    
    while True:
        
        # 3.收发数据
        tcp_socket.send('nihaoma'.encode('utf-8'))
        
        recv_msg = tcp_socket.recv()
        print(recv_msg.decode('utf-8'))
    
    # 4.关闭套接字
    tcp_socket.close()
    
    
if __name__ == '__main__':
    
    mgr()














