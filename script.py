netSSID = 'test_SSID' 
iface = 'wlan0'   
dot11 = Dot11(type=0, subtype=8, addr1='d8:80:83:5f:75:ff',
addr2='22:22:22:22:22:22', addr3='33:33:33:33:33:33')
beacon = Dot11Beacon(cap='ESS+privacy')
essid = Dot11Elt(ID='SSID',info=netSSID, len=len(netSSID))
rsn = Dot11Elt(ID='RSNinfo', info=(
'\x01\x00'
'\x00\x0f\xac\x02'
'\x02\x00'
'\x00\x0f\xac\x04'
'\x00\x0f\xac\x02'
'\x01\x00'
'\x00\x0f\xac\x02'
'\x00\x00'))
frame = RadioTap()/dot11/beacon/essid/rsn
sendp(frame, iface=iface, inter=0.001, loop=1)