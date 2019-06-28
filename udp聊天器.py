# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:14:52 2019

【udp聊天器】

@author: 张伟英
"""
import socket

def send_info(udp_socket):
    
    recv_ip = input('请输入对方ip：')
    
    recv_port = int(input('请输入对方的port：'))
    
    send_msg = input('请输入要发送的内容：')
    
    send_msg = udp_socket.sendto(send_msg.encode('utf-8'),(recv_ip, recv_port))
    
def recv_info(udp_socket):
    
    recv_msg = udp_socket.recvfrom(1024)
    
    print('%s:%s' % (str(recv_msg[1]), recv_msg[0].decode('utf-8')))

def main():
    
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(('', 6653))  # 绑定本机的ip和端口号
    
    while True:
        
        print('***简易聊天器***')
        
        print('1.发送消息','2.接受消息','0.退出')
        
        num = input('请输入所需功能前面的数字：')
        
        if num == '1':
            
            # 2.发送消息
            send_info(udp_socket)
            
        elif num == '2':
    
            # 2.2 接收数据 
            recv_info(udp_socket)
            
        elif num == '0':
            
            break
        
        else:
            
            print('输入有误，请重新输入')
            
    
    # 3.关闭套接字
    udp_socket.close()
    
if __name__ == '__main__':
    
    main()
