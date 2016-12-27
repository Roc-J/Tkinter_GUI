# -*- coding=utf-8 -*-
from Tkinter import *
from SimpleDialog import *

class workDemo:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x300')
        self.root.maxsize(800, 600)
        self.root.title("心理测试题")
        self.page = 0
        self.v = IntVar()

        self.itemList = [
            [("a、草莓", 2), ("b、苹果", 3), ("c、西瓜", 5), ("d、菠萝", 10), ("e、橘子", 15)],
            [("a、郊外", 2), ("b、电影院", 3), ("c、公园", 5), ("d、商场", 10), ("e、酒吧", 15)],
            [("a、有才气的人", 2), ("b、依赖你的人", 3), ("c、优雅的人", 5), ("d、善良的人", 10), ("e、性情豪放的人", 15)],
            [("a、猫", 2), ("b、马", 3), ("c、大象", 5), ("d、猴子", 10), ("e、狗", 15)],
            [("a、开风扇", 2), ("b、吃冰激凌", 3), ("c、游泳", 5), ("d、喝冷饮", 10), ("e、开空调", 15)],
            [("a、蛇", 2), ("b、鸡", 3), ("c、猪", 5), ("d、老鼠", 10), ("e、苍蝇", 15)],
            [("a、悬疑推理类", 2), ("b、童话神话类", 3), ("c、自然科学类", 5), ("d、伦理道德类", 10), ("e、战争枪战类", 15)],
            [("a、打火机", 2), ("b、口红", 3), ("c、记事本", 5), ("d、纸巾", 10), ("e、手机", 15)],
            [("a、火车", 2), ("b、自行车", 3), ("c、汽车", 5), ("d、飞机", 10), ("e、步行", 15)],
            [("a、紫", 2), ("b、黑", 3), ("c、蓝", 5), ("d、白", 10), ("e、红", 15)],
            [("a、瑜伽", 2), ("b、自行车", 3), ("c、乒乓球", 5), ("d、足球", 10), ("e、蹦极", 15)],
            [("a、湖边", 2), ("b、草原", 3), ("c、海边", 5), ("d、森林", 10), ("e、城中区", 15)],
            [("a、雪", 2), ("b、风", 3), ("c、雨", 5), ("d、雾", 10), ("e、雷电", 15)],
            [("a、七层", 2), ("b、一层", 3), ("c、二十三层", 5), ("d、十八层", 10), ("e、三十层", 15)],
            [("a、丽江", 2), ("b、拉萨", 3), ("c、昆明", 5), ("d、杭州", 10), ("e、北京", 15)],
        ]

        self.problemLabel = ["1、你更喜欢吃那种水果？ ","2、你平时休闲经常去的地方?"," 3、你认为容易吸引你的人是？","4、如果你可以成为一种动物，你希望自己是哪种？",
                             "5、天气很热，你更愿意选择什么方式解暑？","6、如果必须与一个你讨厌的动物或昆虫在一起生活，你能容忍哪一个？",
                             "7、你喜欢看哪类电影、电视剧？","8、以下哪个是你身边必带的物品？"," 9、你出行时喜欢坐什么交通工具？","10、以下颜色你更喜欢哪种？",
                             "11、下列运动中挑选一个你最喜欢的(不一定擅长)？ "," 12、如果你拥有一座别墅，你认为它应当建立在哪里？ ","13、你更喜欢以下哪种天气现象？",
                             "14、你希望自己的窗口在一座30层大楼的第几层？"," 15、你认为自己更喜欢在以下哪一个城市中生活？ "
                             ]
        self.result = []
        self.label = Label(self.root, text=self.problemLabel[self.page], justify=LEFT, padx=20)
        self.label.pack(anchor=W)

        self.itema = Radiobutton(self.root, text=self.itemList[self.page][0][0], padx=20, variable=self.v,
                                 val=self.itemList[self.page][0][1])
        self.itema.pack(anchor=W)
        self.itemb = Radiobutton(self.root, text=self.itemList[self.page][1][0], padx=20, variable=self.v,
                                 val=self.itemList[self.page][1][1])
        self.itemb.pack(anchor=W)
        self.itemc = Radiobutton(self.root, text=self.itemList[self.page][2][0], padx=20, variable=self.v,
                                 val=self.itemList[self.page][2][1])
        self.itemc.pack(anchor=W)
        self.itemd = Radiobutton(self.root, text=self.itemList[self.page][3][0], padx=20, variable=self.v,
                                 val=self.itemList[self.page][3][1])
        self.itemd.pack(anchor=W)
        self.iteme = Radiobutton(self.root, text=self.itemList[self.page][4][0], padx=20, variable=self.v,
                                 val=self.itemList[self.page][4][1])
        self.iteme.pack(anchor=W)

        self.preBt = Button(self.root, text="上一页", command=self.prePage)
        self.preBt.pack()
        self.nextBt = Button(self.root, text="下一页", command=self.nextPage)
        self.nextBt.pack()
        self.submitBt = Button(self.root, text="提交",command=self.submit)
        mainloop()

    def submit(self):
        if 0 in self.result:
            # 创建一个SimpleDialog
            # buttons:显示的按钮
            # default:默认选中的按钮
            dlg = SimpleDialog(self.root,
                               text='你有未选择的题目！',
                               buttons=['确定'],
                               default=0,
                               )
            # 执行对话框
            dlg.go()
        else:
            self.label.destroy()
            self.itema.destroy()
            self.itemb.destroy()
            self.itemc.destroy()
            self.itemd.destroy()
            self.iteme.destroy()
            self.preBt.destroy()
            self.submitBt.destroy()
            score = sum(self.result)
            if score >180:
                label = Message(self.root,text="心理测试结果 :")
                label.place(x=20,y=40)
                message = Message(self.root, text="意志力强，头脑冷静，有较强的领导欲，事业心强，不达目的不罢休。外表和善，内心自傲，对有利于自己的人际关系比较看重，有时显得性格急噪，咄咄逼人，得理不饶人，不利于自己时顽强抗争，不轻易认输。思维理性，对爱情和婚姻的看法很现实，对金钱的欲望一般。 ")
                message.pack()
            elif score >140:
                label = Message(self.root, text="心理测试结果 :")
                label.place(x=20, y=40)
                message = Message(self.root,
                                  text="聪明，性格活泼，人缘好，善于交朋友，心机较深。事业心强，渴望成功。思维较理性，崇尚爱情，但当爱情与婚姻发生冲突时会选择有利于自己的婚姻。金钱欲望强烈。")
                message.pack()
            elif score > 100:
                label = Message(self.root, text="心理测试结果 :")
                label.place(x=20, y=40)
                message = Message(self.root,
                                  text="爱幻想，思维较感性，以是否与自己投缘为标准来选择朋友。性格显得较孤傲，有时较急噪，有时优柔寡断。事业心较强，喜欢有创造性的工作，不喜欢按常规办事。性格倔强，言语犀利，不善于妥协。崇尚浪漫的爱情，但想法往往不切合实际。金钱欲望一般")
                message.pack()
            elif score > 70 :
                label = Message(self.root, text="心理测试结果 :")
                label.place(x=20, y=40)
                message = Message(self.root,
                                  text="好奇心强，喜欢冒险，人缘较好。事业心一般，对待工作，随遇而安，善于妥协。善于发现有趣的事情，但耐心较差，敢于冒险，但有时较胆小。渴望浪漫的爱情，但对婚姻的要求比较现实。不善理财。")
                message.pack()
            elif score >40:
                label = Message(self.root, text="心理测试结果 :")
                label.place(x=20, y=40)
                message = Message(self.root,
                                  text="性情温良，重友谊，性格塌实稳重，但有时也比较狡黠。事业心一般，对本职工作能认真对待，但对自己专业以外事物没有太大兴趣，喜欢有规律的工作和生活，不喜欢冒险，家庭观念强，比较善于理财。")
                message.pack()
            else:
                label = Message(self.root, text="心理测试结果 :")
                label.place(x=20, y=40)
                message = Message(self.root,
                                  text="散漫，爱玩，富于幻想。聪明机灵，待人热情，爱交朋友，但对朋友没有严格的选择标准。事业心较差，更善于享受生活，意志力和耐心都较差，我行我素。有较好的异性缘，但对爱情不够坚持认真，容易妥协。没有财产观念。")
                message.pack()


    def getChoice(self):
        self.result.append(self.v.get())

    def prePage(self):
        if self.page>=1:
            self.page -= 1
            self.result.pop()
            if self.page == 13:
                self.submitBt.destroy()
                self.nextBt = Button(self.root, text="下一页", command=self.nextPage)
                self.nextBt.pack()

            self.label["text"] = self.problemLabel[self.page]
            self.itema["text"]=self.itemList[self.page][0][0]
            self.itema["val"]=self.itemList[self.page][0][1]
            self.itemb["text"] = self.itemList[self.page][1][0]
            self.itemb["val"] = self.itemList[self.page][1][1]
            self.itemc["text"] = self.itemList[self.page][2][0]
            self.itemc["val"] = self.itemList[self.page][2][1]
            self.itemd["text"] = self.itemList[self.page][3][0]
            self.itemd["val"] = self.itemList[self.page][3][1]
            self.iteme["text"] = self.itemList[self.page][4][0]
            self.iteme["val"] = self.itemList[self.page][4][1]

    def nextPage(self):
        if self.page< len(self.problemLabel)-1:
            self.getChoice()
            self.page += 1
            if self.page == 14:
                self.getChoice()
                self.nextBt.destroy()
                self.submitBt = Button(self.root, text="提交",command=self.submit)
                self.submitBt.pack()
            self.label["text"] = self.problemLabel[self.page]
            self.itema["text"] = self.itemList[self.page][0][0]
            self.itema["val"] = self.itemList[self.page][0][1]
            self.itemb["text"] = self.itemList[self.page][1][0]
            self.itemb["val"] = self.itemList[self.page][1][1]
            self.itemc["text"] = self.itemList[self.page][2][0]
            self.itemc["val"] = self.itemList[self.page][2][1]
            self.itemd["text"] = self.itemList[self.page][3][0]
            self.itemd["val"] = self.itemList[self.page][3][1]
            self.iteme["text"] = self.itemList[self.page][4][0]
            self.iteme["val"] = self.itemList[self.page][4][1]

workDemo()