from sys import exit,argv
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from decimal import Decimal


def is_chinese(string):
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

class Ui_q_mw(object):
    def setupUi(self, q_mw):
        if not q_mw.objectName():
            q_mw.setObjectName(u"q_mw")
        font = QFont()
        font.setPointSize(20)
        q_mw.setFont(font)
        self.centralwidget = QWidget(q_mw)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.title.setFont(font1)

        self.horizontalLayout_8.addWidget(self.title)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_4.setToolTipDuration(0)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.title_2 = QLabel(self.centralwidget)
        self.title_2.setObjectName(u"title_2")

        self.horizontalLayout_8.addWidget(self.title_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tip1_lb = QLabel(self.centralwidget)
        self.tip1_lb.setObjectName(u"tip1_lb")
        self.tip1_lb.setFont(font)

        self.horizontalLayout.addWidget(self.tip1_lb)

        self.mid_sb = QSpinBox(self.centralwidget)
        self.mid_sb.setObjectName(u"mid_sb")
        self.mid_sb.setMinimumSize(QSize(150, 0))
        self.mid_sb.setFont(font)
        self.mid_sb.setMinimum(-1000000)
        self.mid_sb.setMaximum(0)
        self.mid_sb.setSingleStep(5)
        self.mid_sb.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout.addWidget(self.mid_sb)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.tip2_lb = QLabel(self.centralwidget)
        self.tip2_lb.setObjectName(u"tip2_lb")
        self.tip2_lb.setMaximumSize(QSize(11111111, 16777215))
        self.tip2_lb.setFont(font)

        self.verticalLayout.addWidget(self.tip2_lb)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.max_sb = QSpinBox(self.centralwidget)
        self.max_sb.setObjectName(u"max_sb")
        self.max_sb.setMinimumSize(QSize(150, 0))
        self.max_sb.setFont(font)
        self.max_sb.setMaximum(1000000)
        self.max_sb.setSingleStep(5)
        self.max_sb.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout.addWidget(self.max_sb)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_7.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        q_mw.setCentralWidget(self.centralwidget)

        self.retranslateUi(q_mw)

        QMetaObject.connectSlotsByName(q_mw)
    # setupUi

    def retranslateUi(self, q_mw):
        q_mw.setWindowTitle(QCoreApplication.translate("q_mw", u"R-xget v0.0.16", None))
        self.title.setText(QCoreApplication.translate("q_mw", u"R-xget", None))
        self.label_4.setText(QCoreApplication.translate("q_mw", u"v0.0.16", None))
        self.title_2.setText(QCoreApplication.translate("q_mw", u"\u89e3\u4e00\u5143\u4e00\u6b21\u65b9\u7a0b\u7684\u597d\u5e2e\u624b", None))
        self.tip1_lb.setText(QCoreApplication.translate("q_mw", u"\u8f93\u5165\u8303\u56f4\uff1a", None))
        self.tip2_lb.setText(QCoreApplication.translate("q_mw", u"~", None))
        self.label.setText(QCoreApplication.translate("q_mw", u"\u8f93\u5165\u7cbe\u5ea6\uff1a", None))
        self.textEdit.setHtml(QCoreApplication.translate("q_mw", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\"></span></p></body></html>", None))
        self.textEdit.setPlaceholderText("输入一元一次方程")
        self.pushButton.setText(QCoreApplication.translate("q_mw", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.label_2.setText(QCoreApplication.translate("q_mw", u"\u7b49\u5f85\u4e2d...", None))
        self.label_3.setText(QCoreApplication.translate("q_mw", u"\u7ed3\u679c\uff1a", None))
    # retranslateUi




class Rxget(QMainWindow, Ui_q_mw):
    def __init__(self):
        super().__init__()
        self.text_1 = ""
        self.text_2 = ""
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.xget)
        self.textEdit.textChanged.connect(self.t)

    def t(self):
        if self.text_1:
            self.text_2 = self.textEdit.toPlainText()
            if " " in self.text_2:
                self.textEdit.setText(self.text_1)
                QMessageBox.warning(self, "warn", "方程内不能有空格")
            elif is_chinese(self.text_2):
                self.textEdit.setText(self.text_1)
                QMessageBox.warning(self, "warn", "方程内不能有中文")
            else:
                self.text_1 = self.text_2
        else:
            self.text_1 = self.textEdit.toPlainText()
            if " " in self.text_1:
                self.textEdit.setText("")
                self.text_1 = ""
                QMessageBox.warning(self, "warn", "方程内不能有空格")
            elif is_chinese(self.text_1):
                self.textEdit.setText("")
                self.text_1 = ""
                QMessageBox.warning(self, "warn", "方程内不能有中文")

    def xget(self):
        try:
            self.x = False
            if self.mid_sb.value() == 0:
                mid = -1000
            else:
                mid = self.mid_sb.value()
            if self.max_sb.value() == 0:
                max_ = 1000
            else:
                max_ = self.max_sb.value()
            if self.lineEdit.text() == "":
                text = 1/21
            else:
                text = eval(self.lineEdit.text())

            for i in range(int((max_ - mid) / text)):
                x = mid + i * text
                get = self.textEdit.toPlainText().split("=")
                x_1 = Decimal(str(eval(get[0]))).quantize(Decimal("0.000001"), rounding = "ROUND_HALF_UP")
                x_2 = Decimal(str(eval(get[1]))).quantize(Decimal("0.000001"), rounding = "ROUND_HALF_UP")
                if x_1 == x_2:
                    self.x = True
                    break

            if self.x == True:
                self.label_2.setText("寻找完成")
                x = Decimal(str(x)).quantize(Decimal("0.000001"), rounding = "ROUND_HALF_UP")
                self.label_3.setText("结果：{}".format(x))
            else:
                self.label_2.setText("寻找失败")
        except:
            QMessageBox.warning(self, "Errow", "请检查你的输入精度和方程")

if __name__ == "__main__":
    app = QApplication(argv)
    window = Rxget()
    exit(app.exec_())
