import json
from tools.pi_info import PI
from tools.redis_connection import r
import time


def main():
    pi = PI()
    pi_info = pi.all_info()
    ram_state = pi_info.get('ram_state')
    disk_state = pi_info.get('disk_state')
    pi_info['ram_state'] = json.dumps(ram_state)
    pi_info['disk_state'] = json.dumps(disk_state)
    r.hmset('pi_info', pi_info)


if __name__ == '__main__':
    main()
