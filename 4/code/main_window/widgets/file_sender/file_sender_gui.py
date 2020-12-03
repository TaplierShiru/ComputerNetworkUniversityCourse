# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_sender_gui.ui'
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


class Ui_File_sender(object):
    def setupUi(self, File_sender):
        if not File_sender.objectName():
            File_sender.setObjectName(u"File_sender")
        File_sender.resize(869, 602)
        self.gridLayoutWidget = QWidget(File_sender)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 851, 571))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.commandLinkButton_to_recieve = QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton_to_recieve.setObjectName(u"commandLinkButton_to_recieve")
        self.commandLinkButton_to_recieve.setAutoRepeat(False)

        self.horizontalLayout_3.addWidget(self.commandLinkButton_to_recieve)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 5, 1, 1)

        self.lineEdit_header = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_header.setObjectName(u"lineEdit_header")

        self.gridLayout.addWidget(self.lineEdit_header, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.pushButton_send_message = QPushButton(self.gridLayoutWidget)
        self.pushButton_send_message.setObjectName(u"pushButton_send_message")

        self.gridLayout.addWidget(self.pushButton_send_message, 8, 5, 1, 1)

        self.label_attach = QLabel(self.gridLayoutWidget)
        self.label_attach.setObjectName(u"label_attach")

        self.gridLayout.addWidget(self.label_attach, 2, 5, 1, 1)

        self.lineEdit_to = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_to.setObjectName(u"lineEdit_to")

        self.gridLayout.addWidget(self.lineEdit_to, 0, 1, 1, 1)

        self.label_content = QLabel(self.gridLayoutWidget)
        self.label_content.setObjectName(u"label_content")

        self.gridLayout.addWidget(self.label_content, 2, 1, 1, 1)

        self.label_header = QLabel(self.gridLayoutWidget)
        self.label_header.setObjectName(u"label_header")

        self.gridLayout.addWidget(self.label_header, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_attch_file = QPushButton(self.gridLayoutWidget)
        self.pushButton_attch_file.setObjectName(u"pushButton_attch_file")

        self.horizontalLayout_2.addWidget(self.pushButton_attch_file)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pushButton_exit = QPushButton(self.gridLayoutWidget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")

        self.horizontalLayout_4.addWidget(self.pushButton_exit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_4, 10, 5, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 3, 1, 1)

        self.label_to = QLabel(self.gridLayoutWidget)
        self.label_to.setObjectName(u"label_to")

        self.gridLayout.addWidget(self.label_to, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 7, 3, 1, 1)

        self.plainTextEdit_message_text = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_message_text.setObjectName(u"plainTextEdit_message_text")

        self.gridLayout.addWidget(self.plainTextEdit_message_text, 3, 1, 5, 2)

        self.listWidget_attch_files = QListWidget(self.gridLayoutWidget)
        self.listWidget_attch_files.setObjectName(u"listWidget_attch_files")

        self.gridLayout.addWidget(self.listWidget_attch_files, 3, 5, 4, 1)


        self.retranslateUi(File_sender)

        QMetaObject.connectSlotsByName(File_sender)
    # setupUi

    def retranslateUi(self, File_sender):
        File_sender.setWindowTitle(QCoreApplication.translate("File_sender", u"Form", None))
        self.commandLinkButton_to_recieve.setText(QCoreApplication.translate("File_sender", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043f\u0438\u0441\u0435\u043c", None))
        self.pushButton_send_message.setText(QCoreApplication.translate("File_sender", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_attach.setText(QCoreApplication.translate("File_sender", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b", None))
        self.label_content.setText(QCoreApplication.translate("File_sender", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.label_header.setText(QCoreApplication.translate("File_sender", u"\u0422\u0435\u043c\u0430:", None))
        self.pushButton_attch_file.setText(QCoreApplication.translate("File_sender", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.pushButton_exit.setText(QCoreApplication.translate("File_sender", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label_to.setText(QCoreApplication.translate("File_sender", u"\u041a\u043e\u043c\u0443:", None))
    # retranslateUi

