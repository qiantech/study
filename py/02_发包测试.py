# -*- coding: utf-8 -*-
# copyright:   Copyright (c) 2017-2020 qa_tech Co., Ltd. All rights reserved.
# author:      Jia Huang
# create_time: 2020/7/15 15:42
# update_time: 2020/7/15 15:42
# description: function description


"""
scapy发送数据包有常用的如下几种方法：
send(pkt)  发送三层数据包，但不会受到返回的结果。
sr(pkt)  发送三层数据包，返回两个结果，分别是接收到响应的数据包和未收到响应的数据包。
sr1(pkt)  发送三层数据包，仅仅返回接收到响应的数据包。

sendp(pkt)  发送二层数据包。
srp(pkt)  发送二层数据包，并等待响应。
srp1(pkt)  发送第二层数据包，并返回响应的数据包
"""
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr

# sr发送一个数据包，ans为响应的数据包，u_ans为未响应的数据包
pkt = IP(dst='114.114.114.114')/TCP(dport='http')
ans, u_ans = sr(pkt, timeout=1)
print(ans)
print(u_ans)

# 数据包来实现一个简单的SYN端口扫描，flags="S" 表示发送SYN数据包
port_scan = IP(dst='192.168.1.180')/TCP(dport=[22, 3389, 3306, 443, 445], flags='S')
ans, u_ans = sr(port_scan, timeout=1)

ans.summary()


