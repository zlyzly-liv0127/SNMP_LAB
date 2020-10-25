import re
import os,sys
import time
import platform


def getRam(host):
    result = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + '.1.3.6.1.2.1.25.2.2.0').read()
    # 截取后面需要读的部分
    index = result.rfind(":") + 2
    result = result[index:]
    result = result.strip('\n')
    print(result)
    return result

def getRamrate(host):
    result = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + '.1.3.6.1.2.1.25.2.3.1.6').read()
    # 截取后面需要读的部分
    index = result.rfind(":") + 2
    result = result[index:]
    result = result.strip('\n')
    #result += '%'
    result2 = getRam(host)
    result2 = result2[:-7]
    rate = int(result)/int(result2)
    print(rate)
    return result

def getDisk(host):
    result = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + '.1.3.6.1.4.1.2021.9.1.6').read()
    # 截取后面需要读的部分
    index = result.rfind(":") + 2
    result = result[index:]
    result = result.strip('\n')
    result += 'kB'
    print(result)
    return result

def getCPU(host):
    result = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + '.1.3.6.1.4.1.2021.11.9.0').read()
    # 截取后面需要读的部分
    index = result.rfind(":") + 2
    result = result[index:]
    result = result.strip('\n')
    result += '%'
    print(result)
    return result

def getFlow(host):
    result = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + '.1.3.6.1.2.1.2.2.1.11').read()
    # 截取后面需要读的部分
    index = result.rfind(":") + 2
    result = result[index:]
    result = result.strip('\n')
    result += '个数据报'
    print(result)
    return result

def main():
    print("系统信息")
    result = getRamrate('192.168.112.130')
    #print(result)

if __name__ == '__main__':
    main()