# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 479)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 681, 461))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_login = QLabel(self.gridLayoutWidget)
        self.label_login.setObjectName(u"label_login")

        self.gridLayout.addWidget(self.label_login, 1, 0, 1, 1)

        self.lineEdit_adress = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_adress.setObjectName(u"lineEdit_adress")

        self.gridLayout.addWidget(self.lineEdit_adress, 0, 2, 1, 1)

        self.lineEdit_login = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_login.setObjectName(u"lineEdit_login")

        self.gridLayout.addWidget(self.lineEdit_login, 1, 2, 1, 1)

        self.label_adress = QLabel(self.gridLayoutWidget)
        self.label_adress.setObjectName(u"label_adress")

        self.gridLayout.addWidget(self.label_adress, 0, 0, 1, 1)

        self.tableView_result_type_and_size = QTableView(self.gridLayoutWidget)
        self.tableView_result_type_and_size.setObjectName(u"tableView_result_type_and_size")

        self.gridLayout.addWidget(self.tableView_result_type_and_size, 3, 0, 1, 3)

        self.label_size = QLabel(self.gridLayoutWidget)
        self.label_size.setObjectName(u"label_size")

        self.gridLayout.addWidget(self.label_size, 4, 2, 1, 1)

        self.lineEdit_port = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_port.setObjectName(u"lineEdit_port")

        self.gridLayout.addWidget(self.lineEdit_port, 0, 5, 1, 1)

        self.label_final_size = QLabel(self.gridLayoutWidget)
        self.label_final_size.setObjectName(u"label_final_size")

        self.gridLayout.addWidget(self.label_final_size, 4, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 1, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.label_port = QLabel(self.gridLayoutWidget)
        self.label_port.setObjectName(u"label_port")

        self.gridLayout.addWidget(self.label_port, 0, 4, 1, 1)

        self.pushButton_connect = QPushButton(self.gridLayoutWidget)
        self.pushButton_connect.setObjectName(u"pushButton_connect")

        self.gridLayout.addWidget(self.pushButton_connect, 4, 3, 1, 1)

        self.label_password = QLabel(self.gridLayoutWidget)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 1, 4, 1, 1)

        self.label_by_type = QLabel(self.gridLayoutWidget)
        self.label_by_type.setObjectName(u"label_by_type")

        self.gridLayout.addWidget(self.label_by_type, 2, 0, 1, 3)

        self.label_directory = QLabel(self.gridLayoutWidget)
        self.label_directory.setObjectName(u"label_directory")

        self.gridLayout.addWidget(self.label_directory, 2, 3, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_login.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_adress.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.label_size.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_final_size.setText(QCoreApplication.translate("Form", u"\u0418\u0442\u043e\u0433\u043e\u0432\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440:", None))
        self.label_port.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0440\u0442", None))
        self.pushButton_connect.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u0441\u043e\u0435\u0434\u0438\u043d\u0438\u0442\u044c\u0441\u044f", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_by_type.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u0444\u0430\u0439\u043b\u043e\u0432 \u0438 \u0437\u0430\u043d\u0438\u043c\u0430\u0435\u043c\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c", None))
        self.label_directory.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438", None))
    # retranslateUi

