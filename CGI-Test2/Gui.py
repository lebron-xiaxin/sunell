import easygui as g
import os

# 自定义类
class ConfigData:
    file = ''  # 原始用例路径
    ipcUrl = ''  # 用于替换设备ip地址
    filepath = ''  # 图片保存地址
    resultCol = 0 #执行结果输出列
    username = 'admin' #用户名
    password = 'admin' #密码

    # CGI自动化窗口---Start
    def message(self):
        msg = "请填写一下信息(其中带*号的项为必填项)"
        title = "CGI自动化"
        # 弹窗输入框集合
        fieldNames = ["*ip地址", "*执行结果输出列","*用户名","*密码"]
        # 弹窗输入框集合的值
        fieldValues = g.multenterbox(msg, title, fieldNames)

        # 弹窗点击确认时执行
        while True:
            if fieldValues == None:
                break
            errmsg = ""
            for i in range(len(fieldNames)):
                option = fieldNames[i].strip()
                if fieldValues[i].strip() == "" and option[0] == "*":
                    errmsg += ("【%s】为必填项   " % fieldNames[i])
            if errmsg == "":
                break;
            fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

        # 弹窗点击取消时执行
        while False:
            exit(0)

        # 将输入的IP地址赋值
        ConfigData.ipcUrl = str(fieldValues[0])
        # 将执行结果输出列赋值
        ConfigData.resultCol = str(fieldValues[1])
        #用户名
        ConfigData.username = str(fieldValues[2])
        # 密码
        ConfigData.password = str(fieldValues[3])


        # 调用选择测试用例窗口
        ConfigData.choosePapers(self);

    # 选择测试用例窗口方法
    def choosePapers(self):
        if g.ccbox("请选择测试用例", choices=("选择文件", "退出")):
            # 获取文件的绝对路径，赋值给ConfigData.file
            ConfigData.file = str(g.fileopenbox(multiple=True)[0])
            #调用封装图片路径的方法
            ConfigData.GetImgPath(ConfigData.file)
        else:
            exit(0)

    # 封装图片路径的方法
    def GetImgPath(pathname):
        # 分离文件路径和文件名  filepath（F:\CGI-Test2）  tempfilename（NVR用例.xlsx）
        filepath, tempfilename = os.path.split(pathname)
        # 组装CGI测试结果为图片的路径(F:\CGI-Test2\TestImg_192.168.0.11\)  赋值给ConfigData.filepath
        ConfigData.filepath = filepath + '\TestImg_' + ConfigData.ipcUrl + '\\'



# 输出的对象
    # file = ''  # 原始用例路径
    # ipcUrl = ''  # 用于替换设备ip地址
    # filepath = ''  # 图片保存地址
    # resultCol = 0  # 执行结果输出列
    # username = 'admin'  # 用户名
    # password = 'admin'  # 密码