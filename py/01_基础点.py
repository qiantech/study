# -*- coding: utf-8 -*-
# copyright:   Copyright (c) 2017-2020 qa_tech Co., Ltd. All rights reserved.
# author:      Jia Huang
# create_time: 2020/7/15 10:23
# update_time: 2020/7/15 10:23
# description: 基础知识
from scapy.config import lsc
from scapy.layers.inet import IP, TCP
from scapy.packet import ls


# pip install scapy
# print('******List  available layers, or infos on a given layer class or name.******')
# print(ls())
from scapy.utils import hexdump

print('******比如ls(IP)来查看IP包的各种默认参数******')
ls(IP())

# print('******比如ls(TCP)来查看TCP包的各种默认参数******')
# print(ls(TCP()))
#
# print('******查看scapy指令集******')
# print(lsc())

pkt = IP(dst='114.114.114.114')
# ls(pkt)

print('使用show()方法来查看数据包信息')
pkt.show()

print('使用summary()方法查看概要信息')
print(pkt.summary())

print('使用hexdump(pkt)开查看数据包的字节信息')
hexdump(pkt)

print('使用 "/" 操作符来给数据包加上一层。例如构造一个TCP数据包，在IP层指明数据包的目的地址。在TCP层可以设定数据包的目的端口等等')
tcp_pkt = IP(dst='114.114.114.114')/TCP()
tcp_pkt.show()

print('数据包的目标端口可以用范围来表示，发送的时候就会发送dport 不同的多个数据包')
tcp_pkt = IP(dst='114.114.114.114')/TCP(dport=(22, 33))
# print(tcp_pkt.summary())
for tcp in tcp_pkt:
    print(tcp.dport)

print('如果设置了多个参数为范围的，最后发送的数据包就是笛卡尔积')
tcp_pkt = IP(dst='114.114.114.114')/TCP(dport=(22, 33), sport=(4567, 4568))
for tcp in tcp_pkt:
    print(tcp.dport, tcp.sport)


