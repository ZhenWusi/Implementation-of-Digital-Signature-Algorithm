from tkinter import Tk, Label, filedialog, Button, Text, Toplevel, END, Grid
from crypto_functions import generatePublicKey, generatePrivateKey, sign, check
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showwarning, showinfo
from hashlib import md5
from tkinter import Tk, Label, Button

class MainAppWindow(Tk):
    """ 应用程序主窗口类 """
    def __init__(self):
        Tk.__init__(self)
        self.title("RSA数字签名系统--甄五四")  # 设置窗口标题
        self.geometry("600x400+660+340")  # 设置窗口大小和位置
        self.resizable(True, True)  # 允许调整窗口大小
        self.configure(background='white')  # 设置背景颜色为白色

        self.generateKeysLabelField()  # 创建生成密钥标签区域
        self.generateKeysButtonField()  # 创建生成密钥按钮区域
        self.signLabelField()  # 创建签名标签区域
        self.signButtonField()  # 创建签名按钮区域
        self.checkLabelField()  # 创建检查签名和完整性标签区域
        self.checkButtonField()  # 创建检查按钮区域

    def generateKeysLabelField(self):
        """ 生成密钥标签区域 """
        generateKeysLabel = Label(self,
                                  text="生成密钥对，用于对您的进行消息签名",
                                  font="Helvetica 12 bold",  # 设置文本字体大小
                                  bg="white"
                                  )
        generateKeysLabel.pack(anchor='n', pady=(20,0))  # 使用相对值调整位置

    def generateKeysButtonField(self):
        generateKeysButton = Button(self,
                                    text="生成密钥",
                                    relief="groove",
                                    bg="#87cefa",
                                    width=15,  # 设置按钮宽度
                                    height=2,  # 设置按钮高度
                                    command=self.openGeneratorWindow
                                    )
        generateKeysButton.pack(anchor='center', pady=(10,5))  # 使用相对值调整位置
    def signLabelField(self):
        """ 签名标签区域 """
        signLabel = Label(self,
                          text="为您的消息生成签名",
                          font="Helvetica 12 bold",
                          bg="white"
                          )
        signLabel.pack(anchor='n', pady=(20, 0))

    def checkLabelField(self):
        """ 检查签名和完整性标签区域 """
        checkLabel = Label(self,
                           text="验证消息的签名和完整性",
                           font="Helvetica 12 bold",
                           bg="white"
                           )
        checkLabel.pack(anchor='n', pady=(20, 0))

    def signButtonField(self):
        signButton = Button(self,
                            text="数字签名",
                            relief="groove",
                            bg="#87cefa",
                            width=15,  # 设置按钮宽度
                            height=2,  # 设置按钮高度
                            command=self.openSignWindow
                            )
        signButton.pack(anchor='center', pady=(10, 5))

    def checkButtonField(self):
        checkButton = Button(self,
                             text="数字签名验证",
                             relief="groove",
                             bg="#87cefa",
                             width=15,  # 设置按钮宽度
                             height=2,  # 设置按钮高度
                             command=self.openCheckWindow
                             )
        checkButton.pack(anchor='center', pady=(10, 5))

    def openGeneratorWindow(self):
        GeneratorWindow()  # 打开生成密钥窗口

    def openSignWindow(self):
        SignWindow()  # 打开签名窗口

    def openCheckWindow(self):
        CheckWindow()  # 打开检查签名窗口
class ParentDSAWindow(Toplevel):
    """ 这个类包含所有类型窗口（除MainAppWindow外）的公共设置。"""
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("600x400+660+340")
        # 这里的参数是窗口的宽度为600像素、高度为400像素，且位于屏幕坐标(660, 340)的位置
        self.resizable(True, True)
        # 窗口大小可以调，背景颜色为白色
        self.configure(background='white')
class FirstTypeWindow(ParentDSAWindow):
    """ 这个类是需要生成密钥的类的模板。"""
    def __init__(self):
        ParentDSAWindow.__init__(self)
        self.geometry("600x295+660+393")
        self.focus_force()

    def firstTextField(self):
        """第一部分公钥的文本框"""
        firstText = Text(self,
                         relief="solid"
                         )
        firstText.place(x=70,
                        y=50,
                        width=460,
                        height=20
                        )
        return firstText

    def secondTextField(self):
        """第二部分公钥的文本框"""
        secondText = Text(self,
                          relief="solid"
                          )
        secondText.place(x=70,
                         y=90,
                         width=460,
                         height=40
                         )
        return secondText

    def thirdTextField(self):
        """私钥的文本框"""
        thirdText = Text(self,
                         relief="solid"
                         )
        thirdText.place(x=70,
                        y=150,
                        width=460,
                        height=40
                        )
        return thirdText

    def firstLabelField(self, text="第一部分公钥(e)"):
        """第一个文本框的描述。
           默认文本 = "第一部分公钥"
        """
        firstLabel = Label(self,
                           text=text,
                           bg="white",
                           anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                           )
        firstLabel.place(x=70,
                         y=30,
                         width=110,
                         height=20
                         )

    def secondLabelField(self, text="第二部分公钥(n)"):
        """第二个文本框的描述
           默认文本 = "第二部分公钥"
        """
        secondLabel = Label(self,
                            text=text,
                            bg="white",
                            anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                            )
        secondLabel.place(x=70,
                          y=70,
                          width=124,
                          height=20
                          )

    def thirdLabelField(self, text="私钥(d)"):
        """第三个文本框的描述
           默认文本 = "私钥"
        """
        thirdLabel = Label(self,
                           text=text,
                           bg="white",
                           anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                           )
        thirdLabel.place(x=70,
                         y=130,
                         width=60,
                         height=20
                         )

    def firstButtonField(self, command, text="生成密钥对"):
        """生成密钥对的按钮。
           默认文本 = "生成密钥对"
        """
        firstButton = Button(self,
                             text=text,
                             relief="groove",
                             bg="#87cefa",
                             command=command
                             )
        firstButton.place(x=175,
                          y=210,
                          width=250,
                          height=30
                          )

    def secondButtonField(self, command, text="保存私钥"):
        """保存私钥的按钮
           默认文本 = "保存私钥"
        """
        secondButton = Button(self,
                              text=text,
                              relief="groove",
                              bg="#87cefa",
                              command=command
                              )
        secondButton.place(x=175,
                           y=245,
                           width=124,
                           height=30
                           )

    def thirdButtonField(self, command, text="保存公钥"):
        """保存公钥的按钮
           默认文本 = "保存公钥"
        """
        thirdButton = Button(self,
                             text=text,
                             relief="groove",
                             bg="#87cefa",
                             command=command
                             )
        thirdButton.place(x=301,
                          y=245,
                          width=124,
                          height=30
                          )
class GeneratorWindow(FirstTypeWindow):
    """ 生成密钥的窗口类 """
    def __init__(self):
        FirstTypeWindow.__init__(self)
        self.title("生成密钥")
        self.firstLabelField()
        self.firstPubKeyText = self.firstTextField()

        self.secondLabelField()
        self.secondPubKeyText = self.secondTextField()

        self.thirdLabelField()
        self.privateKeyText = self.thirdTextField()

        self.firstButtonField(self.showKeys)
        self.secondButtonField(self.writePrivKeyToFile)
        self.thirdButtonField(self.writePubKeyToFile)

    def showKeys(self):
        """ 显示生成的密钥在文本框中 """
        self.firstPubKeyText.delete(1.0, END)
        self.secondPubKeyText.delete(1.0, END)
        self.privateKeyText.delete(1.0, END)

        publicKey = generatePublicKey()

        firstPartPubKey = publicKey[0]
        secondPartPubKey = publicKey[1]
        numberFuncEuler = publicKey[2]
        privateKey = generatePrivateKey(firstPartPubKey, numberFuncEuler)

        self.firstPubKeyText.insert(1.0, hex(firstPartPubKey)[2:])
        self.secondPubKeyText.insert(1.0, hex(secondPartPubKey)[2:])
        self.privateKeyText.insert(1.0, hex(privateKey)[2:])

    def writePubKeyToFile(self):
        firstPubKeyText = self.firstPubKeyText.get(1.0, END).rstrip()
        secondPubKeyText = self.secondPubKeyText.get(1.0, END).rstrip()

        if firstPubKeyText != '' and secondPubKeyText != '':
            dlg = asksaveasfilename(defaultextension=".txt",
                                    confirmoverwrite=False,
                                    filetypes=(("Text file", "*.txt"), ("All Files", "*.*")), parent=self)
            filename = dlg
            if filename != '':
                file = open(filename, "w")
                file.write("...PUBLIC KEY START...\n")
                file.write(firstPubKeyText + "\n")
                file.write(secondPubKeyText + "\n")
                file.write("...PUBLIC KEY END...")

                file.close()
        else:
            showwarning("警告！", "请生成密钥！", parent=self)

    def writePrivKeyToFile(self):
        secondPubKeyText = self.secondPubKeyText.get(1.0, END).rstrip()
        privateKeyText = self.privateKeyText.get(1.0, END).rstrip()

        if secondPubKeyText != '' and privateKeyText != '':
            dlg = asksaveasfilename(defaultextension=".txt",
                                    confirmoverwrite=False,
                                    filetypes=(("Text file", "*.txt"), ("All Files", "*.*")), parent=self)
            filename = dlg
            if filename != '':
                file = open(filename, "w")
                file.write("...PRIVATE KEY START...\n")
                file.write(secondPubKeyText + "\n")
                file.write(privateKeyText + "\n")
                file.write("...PRIVATE KEY END...")

                file.close()
        else:
            showwarning("警告！", "请生成密钥！", parent=self)


class SecondTypeWindow(ParentDSAWindow):
    """ 签名和检查数据的窗口类 """
    def __init__(self):
        ParentDSAWindow.__init__(self)

        self.geometry("+665+345")

    def firstTextField(self):
        """ 用户消息的文本框 """
        firstText = Text(self, relief="solid")
        firstText.place(x=70,
                        y=30,
                        width=460,
                        height=60
                        )
        return firstText

    def secondTextField(self):
        """ 文件路径的文本框 """
        secondText = Text(self, relief="solid")
        secondText.place(x=70,
                         y=110,
                         width=360,
                         height=20
                         )
        return secondText

    def thirdTextField(self):
        """ 第一个密钥的文本框 """
        thirdText = Text(self, relief="solid")
        thirdText.place(x=70,
                        y=170,
                        width=360,
                        height=20
                        )
        return thirdText

    def fourthTextField(self):
        """ 第二个密钥的文本框 """
        fourthText = Text(self, relief="solid")
        fourthText.place(x=70,
                         y=210,
                         width=360,
                         height=40
                         )
        return fourthText

    def fifthTextField(self):
        """ 签名的文本框 """
        fifthText = Text(self, relief="solid")
        fifthText.place(x=70,
                        y=290,
                        width=360,
                        height=40
                        )
        return fifthText

    def firstLabelField(self, text="填写消息字段"):
        """ 第一个字段的描述，用于消息文本 """
        firstLabel = Label(self,
                           text=text,
                           bg="white",
                           anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                           )
        firstLabel.place(x=70,
                         y=10,
                         width=94,
                         height=20
                         )

    def secondLabelField(self, text="或者选择本机上的文件"):
        """ 第二个字段的描述，用于文件路径 """
        secondLabel = Label(self,
                            text=text,
                            bg="white",
                            anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                            )
        secondLabel.place(x=70,
                          y=90,
                          width=206,
                          height=20
                          )

    def thirdLabelField(self, text="公钥第二部分(n)"):
        """ 第三个字段的描述，用于公钥/私钥 """
        thirdLabel = Label(self,
                           text=text,
                           bg="white",
                           anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                           )
        thirdLabel.place(x=70,
                         y=150,
                         width=94,
                         height=20
                         )
    def fourthLabelField(self, text="私钥(d)"):
        """ 第四个字段的描述，用于公钥/私钥 """
        fourthLabel = Label(self,
                            text=text,
                            bg="white",
                            anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                            )
        fourthLabel.place(x=70,
                          y=190,
                          width=60,
                          height=20
                          )

    def fifthLabelField(self, text="加载已\n有私钥"):
        """ 第二个按钮的描述，按钮从文件加载现有密钥 """
        fifthLabel = Label(self,
                           text=text,
                           bg="white",
                           relief="groove"
                           )
        fifthLabel.place(x=436,
                         y=170,
                         width=98,
                         height=70
                         )

    def sixthLabelField(self, text="签名"):
        """ 第五个字段的描述，用于签名 """
        sixthLabel = Label(self,
                           text=text,
                           bg="white",
                           anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                           )
        sixthLabel.place(x=70,
                         y=270,
                         width=60,
                         height=20
                         )

    def seventhLabelField(self, text="保存到文件\n"):
        """ 第三个按钮的描述，按钮将签名保存到文件 """
        seventhLabel = Label(self,
                             text=text,
                             bg="white",
                             relief='groove',
                             )
        seventhLabel.place(x=436,
                           y=290,
                           width=98,
                           height=30
                           )

    def firstButtonField(self, command, text="选择"):
        """ 第一个按钮，用于从桌面获取文件路径 """
        firstButton = Button(self,
                             text=text,
                             command=command,
                             relief="groove",
                             bg="#87cefa"
                             )
        firstButton.place(x=440,
                          y=110,
                          width=90,
                          height=20)

    def secondButtonField(self, command, text="加载"):
        """ 第二个按钮，用于从文件加载现有密钥 """
        secondButton = Button(self,
                              text=text,
                              relief="groove",
                              bg="#87cefa",
                              command=command
                              )
        secondButton.place(x=440,
                           y=230,
                           width=90,
                           height=20
                           )

    def thirdButtonField(self, command, text="保存"):
        """ 第三个按钮，用于将签名保存到文件 """
        thirdButton = Button(self,
                             text=text,
                             relief="groove",
                             bg="#87cefa",
                             command=command
                             )
        thirdButton.place(x=440,
                          y=310,
                          width=90,
                          height=20
                          )

    def fourthButtonField(self, command, text="签名"):
        """ 第四个按钮，用于签署某个项目或文档 """
        fourthButton = Button(self,
                              text=text,
                              relief="groove",
                              bg="#87cefa",
                              command=command
                              )
        fourthButton.place(x=225,
                           y=350,
                           width=150,
                           height=30)
class SignWindow(SecondTypeWindow):
    """ 签名数据的窗口类 """
    def __init__(self):
        SecondTypeWindow.__init__(self)

        self.title("签名")

        # 设置界面元素
        self.firstLabelField()
        self.mesText = self.firstTextField()

        self.secondLabelField()
        self.pathFileText = self.secondTextField()
        self.firstButtonField(self.choosePathToFile)

        self.thirdLabelField()
        self.pubKeySecondPartText = self.thirdTextField()

        self.fourthLabelField()
        self.privateKeyText = self.fourthTextField()

        self.fifthLabelField()
        self.secondButtonField(self.loadExistingPrivKey)

        self.sixthLabelField()
        self.signatureText = self.fifthTextField()

        self.seventhLabelField()
        self.thirdButtonField(self.saveSignature)

        self.fourthButtonField(self.signItem)

    def choosePathToFile(self):
        """ 选择文件路径的方法 """
        filename = filedialog.askopenfilename(parent=self)
        self.pathFileText.delete(1.0, END)
        self.pathFileText.insert(1.0, filename)

    def loadExistingPrivKey(self):
        """ 从文件加载现有私钥的方法 """
        filename = filedialog.askopenfilename(parent=self)
        if filename != '':
            file = open(filename)

            rows = file.readlines()

            # 验证文件格式是否正确
            if rows[0].rstrip() == "...PRIVATE KEY START..." \
                    and rows[-1].rstrip() == "...PRIVATE KEY END..." \
                    and len(rows) == 4:

                secondPartPubKey = rows[1].rstrip()
                privateKey = rows[2].rstrip()

                self.pubKeySecondPartText.delete(1.0, END)
                self.privateKeyText.delete(1.0, END)

                self.pubKeySecondPartText.insert(1.0, secondPartPubKey)
                self.privateKeyText.insert(1.0, privateKey)
            else:
                showwarning("警告！", "私钥文件无效！", parent=self)

    def signItem(self):
        """ 签署消息或文件的方法 """
        mesText = self.mesText.get(1.0, END).rstrip()
        pathFileText = self.pathFileText.get(1.0, END).rstrip()
        privateKeyText = self.privateKeyText.get(1.0, END).rstrip()
        pubKeyFirstText = self.pubKeySecondPartText.get(1.0, END).rstrip()

        if mesText == '' and pathFileText == '':
            showwarning("警告！", "请填写消息字段或文件路径字段！", parent=self)

        elif mesText != '' and pathFileText != '':
            showwarning("警告！", "您只能填写一个字段。消息或文件路径！", parent=self)

        elif privateKeyText == '' or pubKeyFirstText == '':
            showwarning("警告！", "请填写密钥的所有字段。", parent=self)

        elif mesText != '' and pathFileText == '':
            # 对消息进行签名
            message = self.mesText.get(1.0, END).rstrip()
            hashMes = md5(message.encode('utf-8')).hexdigest()

            signature = sign(hashMes, self.privateKeyText.get(1.0, END).rstrip(),
                             self.pubKeySecondPartText.get(1.0, END).rstrip())
            self.signatureText.insert(1.0, hex(signature)[2:])

            showinfo("信息", "您的消息已签名！", parent=self)

        elif mesText == '' and pathFileText != '':
            # 对文件进行签名
            pathToFile = self.pathFileText.get(1.0, END).rstrip()

            try:
                file = open(pathToFile, 'rb').read()

                fileHash = md5(file).hexdigest()

                signature = sign(fileHash, privateKeyText, pubKeyFirstText)
                self.signatureText.insert(1.0, hex(signature)[2:])
                showinfo("信息", "您的文件已签名！", parent=self)
            except FileNotFoundError:
                showwarning("警告！", "要签名的文件不存在！", parent=self)

    def saveSignature(self):
        """ 保存签名到文件的方法 """
        signatureText = self.signatureText.get(1.0, END).rstrip()

        if signatureText != '':
            dlg = asksaveasfilename(defaultextension=".txt",
                                    confirmoverwrite=False,
                                    filetypes=(("Text file", "*.txt"), ("All Files", "*.*")),
                                    parent=self)
            filename = dlg
            if filename != '':
                file = open(filename, "w")

                file.write("...SIGNATURE START...\n")
                file.write(signatureText + "\n")
                file.write("...SIGNATURE END...")
                file.close()
                showinfo("信息", "您的签名已保存到文件！", parent=self)
        else:
            showwarning("警告！", "请在保存签名之前签署您的项目！", parent=self)

class CheckWindow(SecondTypeWindow):
    """ 检查签名的窗口类 """

    def __init__(self):
        SecondTypeWindow.__init__(self)

        self.title("验证签名")
        self.grab_set()

        # 设置界面元素
        self.firstLabelField()
        self.mesText = self.firstTextField()

        self.secondLabelField()
        self.pathFileText = self.secondTextField()
        self.firstButtonField(self.choosePathToFile)

        self.thirdLabelField("公钥的第一部分(e)")
        self.pubKeyFirstText = self.thirdTextField()

        self.fourthLabelField("公钥的第二部分(n)")
        self.pubkeySecondText = self.fourthTextField()

        self.fifthLabelField("加载已\n有公钥")
        self.secondButtonField(self.loadExistingPubKey)

        self.sixthLabelField()
        self.signatureText = self.fifthTextField()

        self.seventhLabelField("从文件中加载\n")
        self.thirdButtonField(self.loadSignature, "加载")

        self.fourthButtonField(self.checkItem, "验证")

    def thirdLabelField(self, text):
        """ 第三个字段的描述，用于公钥的第一部分 """
        thirdLabel = Label(self,
                           text=text,
                           bg="white",
                           anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                           )
        thirdLabel.place(x=70,
                         y=150,
                         width=120,
                         height=20
                         )

    def fourthLabelField(self, text):
        """ 第四个字段的描述，用于公钥的第二部分 """
        fourthLabel = Label(self,
                            text=text,
                            bg="white",
                            anchor="w"  # 将锚点设置为 "w"（西）以进行左对齐
                            )
        fourthLabel.place(x=70,
                          y=190,
                          width=136,
                          height=20
                          )

    def choosePathToFile(self):
        """ 选择文件路径的方法 """
        SignWindow.choosePathToFile(self)

    def loadExistingPubKey(self):
        """ 从文件加载现有公钥的方法 """
        filename = filedialog.askopenfilename(parent=self)

        if filename != '':
            file = open(filename)

            rows = file.readlines()
            file.close()

            # 验证文件格式是否正确
            if rows[0].rstrip() == "...PUBLIC KEY START..." \
                    and rows[-1].rstrip() == "...PUBLIC KEY END..." \
                    and len(rows) == 4:
                firstPartPubKey = rows[1].rstrip()
                secondPartPubKey = rows[2].rstrip()

                self.pubKeyFirstText.delete(1.0, END)
                self.pubkeySecondText.delete(1.0, END)

                self.pubKeyFirstText.insert(1.0, firstPartPubKey)
                self.pubkeySecondText.insert(1.0, secondPartPubKey)
            else:
                showwarning("警告！", "带有公钥的文件无效！", parent=self)

    def loadSignature(self):
        """ 从文件加载签名的方法 """
        filename = filedialog.askopenfilename(parent=self)

        if filename != '':
            file = open(filename)

            rows = file.readlines()

            # 验证文件格式是否正确
            if rows[0].rstrip() == "...SIGNATURE START..." and rows[
                -1].rstrip() == "...SIGNATURE END..." and len(
                    rows) == 3:
                signature = rows[1].rstrip()

                self.signatureText.delete(1.0, END)
                self.signatureText.insert(1.0, signature)
            else:
                showwarning("警告", "带有您的签名的文件无效！", parent=self)

    def checkItem(self):
        """ 检查签名的方法 """
        mesText = self.mesText.get(1.0, END).rstrip()
        pathFileText = self.pathFileText.get(1.0, END).rstrip()
        pubKeyFirstText = self.pubKeyFirstText.get(1.0, END).rstrip()
        pubkeySecondText = self.pubkeySecondText.get(1.0, END).rstrip()
        signatureText = self.signatureText.get(1.0, END).rstrip()

        if mesText == '' and pathFileText == '':
            showwarning("警告！", "请填写消息字段或文件路径字段！", parent=self)

        elif mesText != '' and pathFileText != '':
            showwarning("警告！", "只能填写一个字段。消息或文件路径！", parent=self)

        elif pubKeyFirstText == '' or pubkeySecondText == '':
            showwarning("警告！", "请填写密钥的所有字段。", parent=self)

        elif signatureText == '':
            showwarning("警告！", "请填写签名字段。", parent=self)

        elif mesText != '' and pathFileText == '':
            # 对消息进行验证
            hashMes = md5(mesText.encode('utf-8')).hexdigest()
            hashInt = int(hashMes, 16)

            calculatedHash = check(signatureText, pubKeyFirstText, pubkeySecondText)

            if calculatedHash == hashInt:
                showinfo("信息", "签名有效！", parent=self)
            else:
                showinfo("信息", "签名无效！", parent=self)
        elif mesText == '' and pathFileText != '':
            # 对文件进行验证
            try:
                file = open(pathFileText, 'rb').read()

                fileHash = md5(file).hexdigest()
                fileHashInt = int(fileHash, 16)

                calculatedHash = check(signatureText, pubKeyFirstText, pubkeySecondText)

                if calculatedHash == fileHashInt:
                    showinfo("信息", "签名有效！", parent=self)
                else:
                    showinfo("信息", "签名无效！", parent=self)

            except FileNotFoundError:
                showwarning("警告！", "要检查的文件不存在！", parent=self)
