## Tkinter的GUI应用-实现一个翻页的心理测试题 ##
### 完成功能 ###

本次程序是设计一个心理小测试，实现的功能点如下：  
1. 使用Tkinter设计GUI界面，实现一个简单的心里测试题的功能，界面上每次只有一道题目，还有两个按钮，可以进行 下一页和上一页的翻页功能。  
2. 当测试题做到最后的时候有一个提交按钮进行提交。  
3. 若任何一个题目没有做，单击“提交”按钮时弹出窗口提示还没有填完。  
4. 测试结果显示出对应的测试结果  
5. 可以通过翻页对之前作出的选择进行修改，只有最后的提交按钮才是最终的答案。  

### 实现方案 ###
1. 程序是使用python的Tkinter进行GUI应用程序的编写，在进行图形化应用设计上，Tkinter有着比较丰富的控件可以进行设计开发。  
2. 采用Tkinter模块进行程序的开发设计，具有可行性。  
3. 面向对象的编程方法可以实现GUI应用程序的开发  

### 设计思路（给出关键代码）和涉及的知识点 ###

1.首先考虑选用控件，因为设计心理测试应用程序，只需要考虑题目和选项的要求，因此选择了python中的Label控件和单选按钮控件RadioButton。  
2. 考虑布局方式，python中有三种布局方式:grid网格布局，pack包布局，还有一个place布局。考虑到题目的阅读，使用比较简单的pack()布局。  
3. 除了界面的题目之外，我们还要设计翻页的功能，这样可以进行前一页，后一页的翻页功能，最后的还有提交按钮的按钮设计。  
4. 上面的是布局的控件要求，下面我们还要进行事件响应，主要有四个功能函数的设计：  

* 点击题目的选项得到对应的得分数值

		def getChoice(self):
	        self.result.append(self.v.get())

* 点击下一页进行向后翻页的功能

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

* 点击上一页进行向前翻页的功能

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

* 提交按钮，进行判断心理测试结果

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


5.使用面向对象编程的方法来进行程序的设计  
最重要的是类的初始化方法，里面设计界面的空间布局和一些参数的设计，并且对于数据的存储和显示有自己的数据结构：  
（1）题目的存储使用一个列表来进行存储  
（2）每个题目的选项使用二维列表进行存储，每个选项使用python的元组进行存储  
（3）对于答案也是通过列表来进行存储，最后通过选择语句进行心理测试的结果的输出。  
6 在程序的时间里还包括了其他控件的使用，包括了属性和布局。  

### 程序运行截图 ###
程序运行界面

![](http://i.imgur.com/PYOZ1Jv.png)

测试结果  

![](http://i.imgur.com/YWvNoqv.png)

最后一页

![](http://i.imgur.com/HTNpdpm.png)

不同的测试结果

![](http://i.imgur.com/BH7Lqe0.png)