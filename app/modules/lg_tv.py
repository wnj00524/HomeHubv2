import wakeonlan

def wakeup(tv_mac_addr):
    wakeonlan.send_magic_packet(tv_mac_addr)