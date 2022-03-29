import os
import socket


class PI:
    def __init__(self):
        self.pi_info = {}

    def get_host_ip(self):
        """
        查询本机ip地址
        :return: ip
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    # Return CPU temperature as a character string
    def getCPUtemperature(self):
        res = os.popen('vcgencmd measure_temp').readline()
        return (res.replace("temp=", "").replace("'C\n", ""))

    # Return RAM information (unit=kb) in a list
    # Index 0: total RAM
    # Index 1: used RAM
    # Index 2: free RAM
    def getRAMinfo(self):
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i == 2:
                return (line.split()[1:4])

    # Return % of CPU used by user as a character string
    def getCPUuse(self):
        return (str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

    # Return information about disk space as a list (unit included)
    # Index 0: total disk space
    # Index 1: used disk space
    # Index 2: remaining disk space
    # Index 3: percentage of disk used
    def getDiskSpace(self):
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i == 2:
                return (line.split()[1:5])

    def all_info(self):
        # CPU informatiom
        CPU_temp = self.getCPUtemperature()
        CPU_used = self.getCPUuse()
        # RAM information
        # Output is in kb, here I convert it in Mb for readability
        RAM_stats = self.getRAMinfo()
        RAM_total = round(int(RAM_stats[0]) / 1000, 1)
        RAM_used = round(int(RAM_stats[1]) / 1000, 1)
        RAM_free = round(int(RAM_stats[2]) / 1000, 1)
        # Disk information
        DISK_stats = self.getDiskSpace()
        DISK_total = DISK_stats[0]
        DISK_used = DISK_stats[1]
        DISK_perc = DISK_stats[3]
        self.pi_info['cpu_temp'] = CPU_temp
        self.pi_info['cpu_used'] = CPU_used
        self.pi_info['ram_state'] = {'ram_total': RAM_total, 'ram_used': RAM_used, 'ram_free': RAM_free}
        self.pi_info['disk_state'] = {'disk_total': DISK_total, 'disk_used': DISK_used, 'disk_percent': DISK_perc}
        self.pi_info['ip'] = self.get_host_ip()
        return self.pi_info


if __name__ == '__main__':
    obj = PI()
    info = obj.all_info()
    print(info)
    # print('------------')
    # print('CPU Temperature = ' + CPU_temp)
    # print('CPU Use = ' + CPU_usage)
    # print('------------')
    # print('RAM Total = ' + str(RAM_total) + ' MB')
    # print('RAM Used = ' + str(RAM_used) + ' MB')
    # print('RAM Free = ' + str(RAM_free) + ' MB')
    # print('------------')
    # print('DISK Total Space = ' + str(DISK_total) + 'B')
    # print('DISK Used Space = ' + str(DISK_used) + 'B')
    # print('DISK Used Percentage = ' + str(DISK_perc))
    # print(get_host_ip())
