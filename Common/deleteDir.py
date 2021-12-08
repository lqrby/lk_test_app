'''
Author: your name
Date: 2021-09-06 15:59:47
LastEditTime: 2021-09-17 18:59:58
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/Common/test.py
'''
# import random
# a = [1,2,3,4,5]
# #1
# print(random.choice(a))

__author__ = 'Administrator'

import os,sys,time,shutil

class DeleteLog:

    def __init__(self,filename,days):

        self.filename=filename

        self.days=days

    def delete(self):

        if os.path.exists(self.filename)==False:

            print(self.filename+ ' is not exists!!')

        elif os.path.isfile(self.filename):

            print(self.filename)

        elif os.path.isdir(self.filename):

            print(self.filename + ' is a path!')

        for i in [os.sep.join([self.filename,v]) for v in os.listdir(self.filename)]:
            
            if self.compare_isdir_time(i) and (os.path.isdir(i)):

                shutil.rmtree(i)

                print(i+' is removed!')


    def compare_isdir_time(self,file):
        
        if "log" in file:

            return False
            
        time_of_last_mod=os.path.getatime(file)

        days_between=(time.time()-time_of_last_mod)/(24*60*60)
        
        if days_between>self.days:

            return True

        return False

if __name__=='__main__':

    path='/home/renbaoyu/testReport'

    obj=DeleteLog(path,0)

    obj.delete()