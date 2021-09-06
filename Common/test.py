'''
@File    :  test.py    
@Contact :  fangfang.song@asiainnovations.com

@Modify Time    2021/4/12 5:08 下午    
@Author  :  songfang  
@Version :  1.0
@Desciption : 
'''


class a:
    # cc = 1
    def b(self, count=4):

        if count <= 0:
            print(count)
        else:
            print(count)
            count -= 1
            self.b(count=count)


aaa = a()
aaa.b()
aaa.b()
