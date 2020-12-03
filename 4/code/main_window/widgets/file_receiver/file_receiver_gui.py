# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_receiver_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_file_reciever(object):
    def setupUi(self, file_reciever):
        if not file_reciever.objectName():
            file_reciever.setObjectName(u"file_reciever")
        file_reciever.resize(869, 606)
        self.gridLayoutWidget = QWidget(file_reciever)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 851, 571))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 3, 5, 1, 1)

        self.label_attach = QLabel(self.gridLayoutWidget)
        self.label_attach.setObjectName(u"label_attach")

        self.gridLayout.addWidget(self.label_attach, 1, 7, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pushButton_exit = QPushButton(self.gridLayoutWidget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")

        self.horizontalLayout_4.addWidget(self.pushButton_exit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 7, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 5, 1, 1)

        self.listWidget_attch_files = QListWidget(self.gridLayoutWidget)
        self.listWidget_attch_files.setObjectName(u"listWidget_attch_files")

        self.gridLayout.addWidget(self.listWidget_attch_files, 2, 7, 4, 1)

        self.plainTextEdit_message_text = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_message_text.setObjectName(u"plainTextEdit_message_text")

        self.gridLayout.addWidget(self.plainTextEdit_message_text, 2, 3, 5, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 5, 1, 1)

        self.label_content = QLabel(self.gridLayoutWidget)
        self.label_content.setObjectName(u"label_content")

        self.gridLayout.addWidget(self.label_content, 1, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 5, 5, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 5, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 6, 5, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.commandLinkButton_to_sender = QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton_to_sender.setObjectName(u"commandLinkButton_to_sender")
        self.commandLinkButton_to_sender.setAutoRepeat(False)

        self.horizontalLayout_3.addWidget(self.commandLinkButton_to_sender)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 7, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.listWidget_new_mess = QListWidget(self.gridLayoutWidget)
        self.listWidget_new_mess.setObjectName(u"listWidget_new_mess")

        self.gridLayout.addWidget(self.listWidget_new_mess, 2, 1, 4, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.pushButton_update_new_mess = QPushButton(self.gridLayoutWidget)
        self.pushButton_update_new_mess.setObjectName(u"pushButton_update_new_mess")

        self.horizontalLayout.addWidget(self.pushButton_update_new_mess)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)


        self.retranslateUi(file_reciever)

        QMetaObject.connectSlotsByName(file_reciever)
    # setupUi

    def retranslateUi(self, file_reciever):
        file_reciever.setWindowTitle(QCoreApplication.translate("file_reciever", u"Form", None))
        self.label_attach.setText(QCoreApplication.translate("file_reciever", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b", None))
        self.pushButton_exit.setText(QCoreApplication.translate("file_reciever", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("file_reciever", u"\u041d\u043e\u0432\u044b\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.label_content.setText(QCoreApplication.translate("file_reciever", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.commandLinkButton_to_sender.setText(QCoreApplication.translate("file_reciever", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043f\u0438\u0441\u044c\u043c\u043e", None))
        self.pushButton_update_new_mess.setText(QCoreApplication.translate("file_reciever", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

