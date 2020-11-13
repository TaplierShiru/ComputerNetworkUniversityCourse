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


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(989, 482)
        self.gridLayoutWidget = QWidget(MainWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 967, 441))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 6, 1, 1)

        self.lineEdit_adress = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_adress.setObjectName(u"lineEdit_adress")

        self.gridLayout.addWidget(self.lineEdit_adress, 0, 1, 1, 1)

        self.label_port = QLabel(self.gridLayoutWidget)
        self.label_port.setObjectName(u"label_port")

        self.gridLayout.addWidget(self.label_port, 0, 2, 1, 1)

        self.lineEdit_depth = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_depth.setObjectName(u"lineEdit_depth")

        self.gridLayout.addWidget(self.lineEdit_depth, 0, 5, 1, 1)

        self.label_by_other_sites = QLabel(self.gridLayoutWidget)
        self.label_by_other_sites.setObjectName(u"label_by_other_sites")

        self.gridLayout.addWidget(self.label_by_other_sites, 1, 3, 1, 1)

        self.label_show_by_adress = QLabel(self.gridLayoutWidget)
        self.label_show_by_adress.setObjectName(u"label_show_by_adress")

        self.gridLayout.addWidget(self.label_show_by_adress, 1, 1, 1, 1)

        self.pushButton_search = QPushButton(self.gridLayoutWidget)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.gridLayout.addWidget(self.pushButton_search, 4, 0, 1, 1)

        self.label_depth = QLabel(self.gridLayoutWidget)
        self.label_depth.setObjectName(u"label_depth")

        self.gridLayout.addWidget(self.label_depth, 0, 4, 1, 1)

        self.label_adress = QLabel(self.gridLayoutWidget)
        self.label_adress.setObjectName(u"label_adress")

        self.gridLayout.addWidget(self.label_adress, 0, 0, 1, 1)

        self.lineEdit_port = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_port.setObjectName(u"lineEdit_port")

        self.gridLayout.addWidget(self.lineEdit_port, 0, 3, 1, 1)

        self.pushButton_quit = QPushButton(self.gridLayoutWidget)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.gridLayout.addWidget(self.pushButton_quit, 4, 5, 1, 1)

        self.label_process = QLabel(self.gridLayoutWidget)
        self.label_process.setObjectName(u"label_process")

        self.gridLayout.addWidget(self.label_process, 5, 0, 1, 1)

        self.label_what_process = QLabel(self.gridLayoutWidget)
        self.label_what_process.setObjectName(u"label_what_process")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_what_process.sizePolicy().hasHeightForWidth())
        self.label_what_process.setSizePolicy(sizePolicy)
        self.label_what_process.setMaximumSize(QSize(160, 22))

        self.gridLayout.addWidget(self.label_what_process, 5, 1, 1, 1)

        self.label_max_depth = QLabel(self.gridLayoutWidget)
        self.label_max_depth.setObjectName(u"label_max_depth")
        sizePolicy.setHeightForWidth(self.label_max_depth.sizePolicy().hasHeightForWidth())
        self.label_max_depth.setSizePolicy(sizePolicy)
        self.label_max_depth.setMaximumSize(QSize(200, 50))

        self.gridLayout.addWidget(self.label_max_depth, 1, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_progress = QLabel(self.gridLayoutWidget)
        self.label_progress.setObjectName(u"label_progress")

        self.horizontalLayout.addWidget(self.label_progress)

        self.progressBar_of_found = QProgressBar(self.gridLayoutWidget)
        self.progressBar_of_found.setObjectName(u"progressBar_of_found")
        self.progressBar_of_found.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar_of_found)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 3, 1, 1)

        self.plainTextEdit_by_other_sites = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_by_other_sites.setObjectName(u"plainTextEdit_by_other_sites")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit_by_other_sites.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_by_other_sites.setSizePolicy(sizePolicy1)
        self.plainTextEdit_by_other_sites.setReadOnly(True)

        self.gridLayout.addWidget(self.plainTextEdit_by_other_sites, 2, 3, 3, 1)

        self.plainTextEdit_by_adress = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_by_adress.setObjectName(u"plainTextEdit_by_adress")
        sizePolicy1.setHeightForWidth(self.plainTextEdit_by_adress.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_by_adress.setSizePolicy(sizePolicy1)
        self.plainTextEdit_by_adress.setReadOnly(True)

        self.gridLayout.addWidget(self.plainTextEdit_by_adress, 2, 1, 3, 1)

        self.lineEdit_max_depth = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_max_depth.setObjectName(u"lineEdit_max_depth")

        self.gridLayout.addWidget(self.lineEdit_max_depth, 1, 5, 1, 1)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.label_port.setText(QCoreApplication.translate("MainWidget", u"\u041f\u043e\u0440\u0442:", None))
        self.label_by_other_sites.setText(QCoreApplication.translate("MainWidget", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043d\u0430 \u0434\u0440\u0443\u0433\u0438\u0445 \u0430\u0434\u0440\u0435\u0441\u0430\u0445:", None))
        self.label_show_by_adress.setText(QCoreApplication.translate("MainWidget", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u0430\u0434\u0440\u0435\u0441\u0443:", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWidget", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_depth.setText(QCoreApplication.translate("MainWidget", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.label_adress.setText(QCoreApplication.translate("MainWidget", u"\u0421\u044b\u043b\u043b\u043a\u0430/\u0430\u0434\u0440\u0435\u0441:", None))
        self.pushButton_quit.setText(QCoreApplication.translate("MainWidget", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label_process.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f:", None))
        self.label_what_process.setText(QCoreApplication.translate("MainWidget", u"Site", None))
        self.label_max_depth.setText(QCoreApplication.translate("MainWidget", u"Max \u041a\u043e\u043b-\u0432\u043e \u0441\u044b\u043b\u043b\u043e\u043a \u043d\u0430 \u0433\u043b\u0443\u0431\u0438\u043d\u0435", None))
        self.label_progress.setText(QCoreApplication.translate("MainWidget", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441:", None))
    # retranslateUi

