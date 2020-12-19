import wakeonlan
from pylgtv import WebOsClient

def wakeup(tv_mac_addr):
    wakeonlan.send_magic_packet(tv_mac_addr)

def run_app(tv_ip, app):
    try:
        webos_client = WebOsClient(tv_ip)
        webos_client.launch_app(app)
        return 0

    except:
        return -1

def first_run(tv_ip):
    try:
        pass

    except:
        pass