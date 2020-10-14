# -*- coding: utf-8 -*-

import sacn
import time

output_univ = 3

cf_position = 1
cf_position_rev = 1
cf_univ = 1
cf_addr = 1
a_univ = 5
b_univ = 2
a_data = [1,1]
b_data = [2,2]
a_raw = []
b_raw = []
out_data = []

sender = sacn.sACNsender()
sender.bind_port = 14372
sender.start()
sender.activate_output(output_univ)
sender[output_univ].multicast = True

receiver = sacn.sACNreceiver()
receiver.start()

print("開始しました")
@receiver.listen_on('universe', universe=a_univ)
def a_callback(packet):
	global cf_position
	global a_data
	global b_data
	global out_data
	global a_raw
	global sender

	a_raw = packet.dmxData
	a_data = [int(i * cf_position) for i in packet.dmxData]
	time.sleep(0.0000012)

	out_data = tuple([a if a > b else b for a, b in zip(a_data, b_data)])
	sender[output_univ].dmx_data = out_data

@receiver.listen_on('universe', universe=b_univ)
def b_callback(packet):
	global cf_position_rev
	global a_data
	global b_data
	global out_data
	global b_raw
	global sender

	b_raw = packet.dmxData
	b_data = [int(i * cf_position_rev) for i in packet.dmxData]
	time.sleep(0.0000015)

	out_data = tuple([a if a > b else b for a, b in zip(a_data, b_data)])
	sender[output_univ].dmx_data = out_data

@receiver.listen_on('universe', universe=cf_univ)
def callback(packet):
	global cf_position
	global cf_position_rev
	global a_data
	global b_data
	global a_raw
	global b_raw
	global out_data
	global sender

	cf_position = packet.dmxData[cf_addr - 1] / 255.0
	cf_position_rev = 1.0 - (packet.dmxData[cf_addr - 1] / 255.0)
	a_data = [int(i * cf_position) for i in a_raw]
	b_data = [int(i * cf_position_rev) for i in b_raw]

	out_data = tuple([a if a > b else b for a, b in zip(a_data, b_data)])
	print(out_data)
	sender[output_univ].dmx_data = out_data

receiver.join_multicast(a_univ)
receiver.join_multicast(b_univ)
receiver.join_multicast(cf_univ)

time.sleep(600)  #10分間動かす
sender.stop()
receiver.stop()