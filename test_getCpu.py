import re,os
class GetCPU():
# def getTotalPss():
#     lines = os.popen("adb shell dumpsys meminfo com.ourydc.yuebaobao ").readlines() #逐行读取
#     # print("lines========",lines)
#     returnList= ""
#     total = "TOTAL"
#     for line in lines:
#         print("line=======",line)
#         if re.findall(total, line): # 找到TOTAL 这一行
#             lis = line.split(" ")  #将这一行，按空格分割成一个list
#             while '' in lis:       # 将list中的空元素删除
#                 lis.remove('')
#             returnList = lis[1] #返回总共内存使用
#             # break
#             return returnList
    def cutting_finishing(self,Mem,line):
        print(type(line))
        obj = []
        if re.findall(Mem, line): # 找到TOTAL 这一行
            lis = line.split(",")  #将这一行，按逗号分割成一个list
            del lis[0]
            del lis[-1]
            for line in lis:
                newline = str(line).lstrip()
                newline_list = newline.split(" ")
                obj.append(newline_list)
            if obj[0][1] =="used" and obj[1][1] =="free":
                print("已使用内存:{}, 剩余可用内存:{}".format(obj[0][0],obj[1][0]))


    def getCpu(self):
        returnList2 = ""
        li = os.popen("adb shell top -m 10 -n 1 -s 9").readlines()
        print(li[2],type(li[2]))
        memory = li[2].replace("\n","")
        Mem = "Mem"
        self.cutting_finishing(Mem, memory)
        


if __name__ == "__main__":
    GetCPU().getCpu()