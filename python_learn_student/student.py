class Student(object):
    def __init__(self,name,id,tel):
        '''
        学生信息
        :param name: 姓名
        :param id: 学号
        :param tel: 电话号码
        '''
        self.name = name
        self.id = id
        self.tel = tel

    def __str__(self):
        return '%s %s %s' %(self.id,self.name,self.tel)

    
