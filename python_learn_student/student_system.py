from student import Student

#继承object对象
#继承了object对象，拥有了好多可操作对象，这些都是类中的高级特性
#在python 3 中已经默认就帮你加载了object了（即便你没有写上object）
#类名 首字母大写
class StudentSystem(object):

# 初始化方法, 注意前后各有两个下划线,
#__init__ 是 创建好实例后 立即就要 执行 的方法，所以称之为初始化方法。
#__init__ 方法的第一个参数是 self
#解释器执行实例化代码，会先在内存中创建该类实例对象，然后调用类 的__init__方法
#调用 __init__方法时，就将实例对象 传递给 self参数。
    def __init__(self):
        #dict 字典
        self.student_dict = {}

    #类的静态方法要在方法定义 上面加上 @staticmethod 的修饰
    # 静态方法是不能访问实例属性的
    @staticmethod
    def init_print():
        print('''
===========欢迎来到学生管理系统===========
1.新增学生
2.删除学生
3.修改(修改手机号)
4.查看某个学生
5.查看所有学生
6.退出系统
=======================================''') 

    @staticmethod
    def check_phone(tel):
        '''
        检查手机号码是否合格
        :param tel:
        :return:
        '''
        if len(tel) != 11:
            return False
        else:
            if tel[0] != '1':
                return False
            elif tel[1] != '3' and tel[1] != '5' and tel[1] != '7' and tel[1] != '8':
                return False
            for n in tel [2:12]:
                if n < '0' or n > '9':
                    return False
        return True

    #函数后面的第一个参数是self，实例本身
    def find_student(self,id):
        if id in self.student_dict.keys():
            return True
        return False


    def add_student(self,student):
        self.student_dict[student.id]=student
        print('添加成功')


    def delete_student(self,id):
        if self.find_student(id):
            del self.student_dict[id]
            print('删除成功')
        else:
            print('查无此人，无法删除！')


    def update_student(self):
        id = input('请输入需要修改的学生学号：')
        if self.find_student(id):
            tel = input('请输入新的手机号')
            if self.check_phone(tel):
                stuent = self.student_dict[id]
                student.tel = tel
                print('修改成功')
            else:
                print('手机号格式错误！')
        else:
            print('查无此人，无法修改手机号码')


    def        query_student(self,id):
        if find_student(id):
            student = self.student_dict[id]
            #https://www.runoob.com/python/att-string-format.html format的使用，使用{} 和 : 代替之前% 的使用
            print('查询成功，该学生姓名：{}，学号：{}，电话号码：{}'.format(student.name, student.id, student.tel))
        else:
            print('系统无此学生信息！')

    def show_student(self):
        if len(self.student_dict.keys()) > 0:
            '''
                  https://www.runoob.com/python/att-string-ljust.html        
            ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
            str.ljust(width[, fillchar])
            width -- 指定字符串长度。     fillchar -- 填充字符，默认为空格。 
            '''
            print('学号'.ljust(12) + '姓名'.ljust(15) + '电话号码'.ljust(15))
            print('-' * 45)
            for student in self.student_dict.values():
                print(str(student.id).ljust(13) + str(student.name).ljust(15) + str(student.tel).ljust(15))
            print('-' * 45)
            print('查询完毕，以上是所有学生的信息！')
        else:
            print('此系统暂无任何学生信息！')

            
    


    def save_to_file(self,file):
        f = open(file, 'w', encoding='UTF-8')        
#f = open(file,'w' encoding='UTF-8')
        #https://www.runoob.com/python3/python3-att-dictionary-values.html
        #Python 字典 values() 方法返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。  
        for student in self.student_dict.values():
            f.write(student.id + ' ' + student.name + ' ' + student.tel + '\n')
        f.close()

    def load_to_file(self,file):
        f = open(file, 'r', encoding='UTF-8')
        for line in f.readlines():
            #.split 切片 返回分割后的字符串列表。
            student = line[:-1].split(' ')
            id = student[0]
            name = student[1]
            tel = student[2]
            self.student_dict[id] = Student(name,id,tel)
        f.close()
        

    def start_up(self):
        self.load_to_file('student.txt')
        while True:
            self.init_print()
            operate = input('请选择功能：')
            '''            
            if operate in ['1', '2', '3', '4', '5']:
                if operate == '1':
                    name = input('请输入姓名：')
                    if name:
                        id = input('请输入id：')
                        if self.find_student(id):
                            print('该学号已被使用，无法添加！')


                        Python isalnum() 方法检测字符串是否由字母和数字组成。
                        https://www.runoob.com/python/att-string-isalnum.html
                        如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False


                        #elif id.isalnum():
                        #elif id.isalnum():
                        elif id.isalnum():
                            tel = input('请输入电话号码：')
                            if self.check_phone(tel):
                                self.add_student(Student(name, id, tel))
                            else:
                                print('手机号格式错误！')
                         else:
                                print('非法的学号')
                    else:
                        print('姓名不能为空')
                elif oprate == '2':
                    id = input(’请输入需要删除的学生学号：‘)
                    delete_student(id)           
                elif oprate == '3'
                    update_student()
                elif oprate == '4'
                    id = input('请输入需要查询的学生学号：')
                    self.query_student(id)
                else:
                    self.show_student()
            elif operate == '6':
                out = input('是否要退出系统（Y/N）：')
                if out == 'y' or out == 'Y':
                    print('{}已退出，欢迎下次再来！'.format(self))
                    self.save_to_file('student.txt')
                    break
                else:
                    print('退出失败，操作继续！')
            else:
                print('输入错误，请重新输入！')
            '''
            if operate in ['1', '2', '3', '4', '5']:
                if operate == '1':
                    name = input('请输入姓名：')
                    if name:
                        id = input('请输入学号：')
                        if self.find_student(id):
                            print('该学号已被使用，无法添加！')
                        elif id.isalnum():
                            tel = input('请输入电话号码：')
                            if self.check_phone(tel):
                                self.add_student(Student(name, id, tel))
                            else:
                                print('手机号格式错误！')
                        else:
                            print('非法的学号！')
                    else:
                        print('姓名不能为空！')
                elif operate == '2':
                    id = input('请输入需要删除的学生学号：')
                    self.del_student(id)
                elif operate == '3':
                    self.update_student()
                elif operate == '4':
                    id = input('请输入需要查询的学生学号：')
                    self.query_student(id)
                else:
                    self.show_student()
            elif operate == '6':
                out = input('是否要退出系统（Y/N）：')
                if out == 'y' or out == 'Y':
                    print('{}已退出，欢迎下次再来！'.format(self))
                    self.save_to_file('student.txt')
                    break
                else:
                    print('退出失败，操作继续！')
            else:
                print('输入错误，请重新输入！')
    def __str__(self):
        return '学生管理系统'

