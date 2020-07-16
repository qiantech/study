# -*- coding: utf-8 -*-
# copyright:   Copyright (c) 2017-2020 qa_tech Co., Ltd. All rights reserved.
# author:      Jia Huang
# create_time: 2020/7/16 11:18
# update_time: 2020/7/16 11:18
# description: function description
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr
from scapy.volatile import RandShort

# tracert 114.114.114.114   windows每次发起3个icmp
ans, u_ans = sr(IP(dst='114.114.114.114', ttl=(1, 20), id=RandShort())/TCP(flags=0x2), timeout=3)
for snd, rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))

# 1 192.168.0.1 False   ttl=1时，到第一个路由时，Time-to-live exceeded返回icmp
# 2 192.168.1.1 False   ttl=2时，到第二个路由时，Time-to-live exceeded返回icmp
# 3 124.90.33.213 False
# 4 123.157.192.1 False
# 5 101.71.244.93 False
# 6 219.158.12.133 False
# 7 60.217.44.158 False
# 8 114.114.114.114 True
# 9 114.114.114.114 True
# 10 114.114.114.114 True

