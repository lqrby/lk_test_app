import re,os,yaml,time,sys
file_path = os.path.join(os.path.abspath('.'))
file_path = file_path.replace('\\', '/')
sys.path.append(file_path)
from Common.log import get_logger
from Common.splicing import caps
log = get_logger(logger_name="移动设备硬件资源监控日志")


class DevicePerformanceMonitoring():

    def __init__(self):
        self.package_name = ""
        self.get_applist()
    # 读取进程名称（包名）
    def get_applist(self):
        with open(os.path.join(caps, "desired_caps.yaml"), encoding="utf-8") as file:
            desired_capsArr = yaml.load(file, Loader=yaml.FullLoader)
            desired_caps = desired_capsArr[0]
            self.package_name = desired_caps["appPackage"]
        


    #获取app使用内存
    def get_memoryUse(self):
        lines = os.popen("adb shell dumpsys meminfo {}".format(self.package_name)).readlines() #逐行读取
        returnList= ""
        total = "TOTAL"
        for line in lines:
            if re.findall(total, line): # 找到TOTAL 这一行
                lis = line.split(" ")  #将这一行，按空格分割成一个list
                while '' in lis:       # 将list中的空元素删除
                    lis.remove('')
                returnList = lis[1] #返回总共内存使用
        return returnList        


    #获取cpu使用率
    def getCpuUsage(self):
        li = os.popen("adb shell top -m 10 -n 1 -s 9").readlines()
        name = "com.ourydc"
        cpuUsage = 0
        memoryUsage = 0
        for line in li:
            if re.findall(name,line):
                cuplist = line.split(" ")
                while '' in cuplist: # 将list中的空元素删除
                    cuplist.remove('')
                try:
                    cpuUsage = float(cuplist[8].strip('%')) #去掉百分号，返回一个float
                    memoryUsage = float(cuplist[9].strip('%')) #去掉百分号，返回一个float
                except:
                    log.info("出现异常: {}".format(cuplist[8]))
                break       
        return cpuUsage ,memoryUsage


    #子方法
    def cutting_finishing(self,item,line):
        obj = []
        if re.findall(item, line): # 找到TOTAL 这一行
            lis = line.split(",")  #将这一行，按逗号分割成一个list
            del lis[0]
            del lis[-1]
            for line in lis:
                newline = str(line).lstrip()
                newline_list = newline.split(" ")
                obj.append(newline_list)
        return obj
            

    #获取cpu使用率和内存使用率
    def getCpu(self):
        cpuList = []
        cpu_data = os.popen("adb shell top -m 10 -n 1 -s 9").readlines()
        for cpu in cpu_data:
            if "idle" in cpu:
                cpuList = ",".join(cpu.split()).split(",")
                break
        if cpuList:
            for idlecpu in cpuList:
                if "idle" in idlecpu:
                    idle = idlecpu.split("%")[0]
                    cupNumber = self.getCpuNumber()
                    cupNumber = cupNumber * 100
                    utilization_rate = (cupNumber - int(idle)) / cupNumber * 100
                    if utilization_rate > 90:
                        log.critical("$$$===警报===CPU已使用: {}%".format(int(utilization_rate)))
                    else:
                        log.info("CPU已使用: {}%".format(int(utilization_rate)))
                    break

    def getCpuNumber(self):
        cpu_data = os.popen("adb shell command cat /proc/cpuinfo").readlines()
        i = 0
        for j in cpu_data:
            if "processor\t:" in j:
                i += 1
        return i
        

    def getMemory(self):
        memory_list = []
        memory_data = os.popen("adb shell procrank").readlines()
        for memoryObj in memory_data:
            if "ZRAM" in memoryObj:
                continue
            elif "RAM" in memoryObj:
                memory_list = memoryObj.split(",")
                break
        if memory_list:
            totol = int("".join(filter(str.isdigit, memory_list[0])))
            free = int("".join(filter(str.isdigit, memory_list[1])))
            cached = int("".join(filter(str.isdigit, memory_list[3])))
            surplus = (totol - free - cached) / totol * 100
            if surplus > 90:
                log.critical("$$$===警报===内存已使用: {}%".format(int(surplus)))
            else:
                log.info("内存已使用: {}%".format(int(surplus)))

    #获取指定包的app使用cpu和内存的方法
    def get_cpuAndMemory(self):
        use_memory = self.get_memoryUse()
        log.info("将要监测的包名为: {}".format(dpm.package_name))
        if use_memory:
            log.info("app使用内存: {}MB".format(int(use_memory)/1024))
        else:
            log.info("请确认您的电脑已连接被监控的设备，并打开app")
        cpu_usage,memoryUsage = dpm.getCpuUsage()
        log.info("app CPU使用率: %",cpu_usage)
        log.info("app 内存使用率: %",memoryUsage)

    #获取电池温度
    def get_battery_temperature(self):
        batterys = os.popen("adb shell dumpsys battery").readlines()
        name = "temperature"
        for battery_line in batterys:
            if re.findall(name,battery_line):
                batterytemperature = int(battery_line.split(":")[1]) * 0.1 
                if batterytemperature > 38:   
                    log.critical("$$$===警报===设备温度: {}℃".format(int(batterytemperature)))
                else:
                    log.info("设备温度: {}℃".format(int(batterytemperature)))


    def all_device_information(self):
        while True:
            self.getCpu()
            self.getMemory()
            self.get_battery_temperature()
            log.info("#################################################################")
            time.sleep(3)
if __name__ == '__main__':
    dpm = DevicePerformanceMonitoring()
    dpm.all_device_information()
    # dpm.getCpu()
    # dpm.getCpuNumber()
    