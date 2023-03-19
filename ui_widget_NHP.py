# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget_NHP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_widget_NHP(object):
    def setupUi(self, widget_NHP):
        if not widget_NHP.objectName():
            widget_NHP.setObjectName(u"widget_NHP")
        widget_NHP.resize(854, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_NHP.sizePolicy().hasHeightForWidth())
        widget_NHP.setSizePolicy(sizePolicy)
        self.widget = QWidget(widget_NHP)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 836, 430))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.label_noordhoekpathfinder = QLabel(self.widget)
        self.label_noordhoekpathfinder.setObjectName(u"label_noordhoekpathfinder")
        self.label_noordhoekpathfinder.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_noordhoekpathfinder.sizePolicy().hasHeightForWidth())
        self.label_noordhoekpathfinder.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(36)
        self.label_noordhoekpathfinder.setFont(font)
        self.label_noordhoekpathfinder.setLayoutDirection(Qt.LeftToRight)
        self.label_noordhoekpathfinder.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_noordhoekpathfinder)

        self.label_image_nhp = QLabel(self.widget)
        self.label_image_nhp.setObjectName(u"label_image_nhp")
        sizePolicy1.setHeightForWidth(self.label_image_nhp.sizePolicy().hasHeightForWidth())
        self.label_image_nhp.setSizePolicy(sizePolicy1)
        self.label_image_nhp.setMaximumSize(QSize(120, 60))
        self.label_image_nhp.setTextFormat(Qt.AutoText)
        self.label_image_nhp.setPixmap(QPixmap(u"NHP-removebg-preview.png"))
        self.label_image_nhp.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_image_nhp)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.label_UKcrewlist = QLabel(self.widget)
        self.label_UKcrewlist.setObjectName(u"label_UKcrewlist")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_UKcrewlist.sizePolicy().hasHeightForWidth())
        self.label_UKcrewlist.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(30)
        self.label_UKcrewlist.setFont(font1)

        self.horizontalLayout.addWidget(self.label_UKcrewlist)

        self.pushButton_copyUKcrewlist = QPushButton(self.widget)
        self.pushButton_copyUKcrewlist.setObjectName(u"pushButton_copyUKcrewlist")
        sizePolicy2.setHeightForWidth(self.pushButton_copyUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_copyUKcrewlist.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.pushButton_copyUKcrewlist.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_copyUKcrewlist)

        self.pushButton_createUKcrewlist = QPushButton(self.widget)
        self.pushButton_createUKcrewlist.setObjectName(u"pushButton_createUKcrewlist")
        sizePolicy2.setHeightForWidth(self.pushButton_createUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_createUKcrewlist.setSizePolicy(sizePolicy2)
        self.pushButton_createUKcrewlist.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_createUKcrewlist)

        self.pushButton_infoUKcrewlist = QPushButton(self.widget)
        self.pushButton_infoUKcrewlist.setObjectName(u"pushButton_infoUKcrewlist")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_infoUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_infoUKcrewlist.setSizePolicy(sizePolicy3)
        self.pushButton_infoUKcrewlist.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_infoUKcrewlist)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.label_NLcrewlist = QLabel(self.widget)
        self.label_NLcrewlist.setObjectName(u"label_NLcrewlist")
        sizePolicy2.setHeightForWidth(self.label_NLcrewlist.sizePolicy().hasHeightForWidth())
        self.label_NLcrewlist.setSizePolicy(sizePolicy2)
        self.label_NLcrewlist.setFont(font1)
        self.label_NLcrewlist.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_NLcrewlist)

        self.pushButton_freshNL = QPushButton(self.widget)
        self.pushButton_freshNL.setObjectName(u"pushButton_freshNL")
        sizePolicy2.setHeightForWidth(self.pushButton_freshNL.sizePolicy().hasHeightForWidth())
        self.pushButton_freshNL.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_freshNL.setFont(font3)

        self.horizontalLayout_2.addWidget(self.pushButton_freshNL)

        self.pushButton_arrivalNL = QPushButton(self.widget)
        self.pushButton_arrivalNL.setObjectName(u"pushButton_arrivalNL")
        sizePolicy2.setHeightForWidth(self.pushButton_arrivalNL.sizePolicy().hasHeightForWidth())
        self.pushButton_arrivalNL.setSizePolicy(sizePolicy2)
        self.pushButton_arrivalNL.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_arrivalNL)

        self.pushButton_departureNL = QPushButton(self.widget)
        self.pushButton_departureNL.setObjectName(u"pushButton_departureNL")
        sizePolicy2.setHeightForWidth(self.pushButton_departureNL.sizePolicy().hasHeightForWidth())
        self.pushButton_departureNL.setSizePolicy(sizePolicy2)
        self.pushButton_departureNL.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_departureNL)

        self.pushButton_createNL = QPushButton(self.widget)
        self.pushButton_createNL.setObjectName(u"pushButton_createNL")
        sizePolicy2.setHeightForWidth(self.pushButton_createNL.sizePolicy().hasHeightForWidth())
        self.pushButton_createNL.setSizePolicy(sizePolicy2)
        self.pushButton_createNL.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_createNL)

        self.pushButton_infoNL = QPushButton(self.widget)
        self.pushButton_infoNL.setObjectName(u"pushButton_infoNL")
        sizePolicy3.setHeightForWidth(self.pushButton_infoNL.sizePolicy().hasHeightForWidth())
        self.pushButton_infoNL.setSizePolicy(sizePolicy3)
        self.pushButton_infoNL.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_infoNL)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.label_resthours_and_timesheets_2 = QLabel(self.widget)
        self.label_resthours_and_timesheets_2.setObjectName(u"label_resthours_and_timesheets_2")
        sizePolicy2.setHeightForWidth(self.label_resthours_and_timesheets_2.sizePolicy().hasHeightForWidth())
        self.label_resthours_and_timesheets_2.setSizePolicy(sizePolicy2)
        self.label_resthours_and_timesheets_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_resthours_and_timesheets_2)

        self.pushButton_generate_resthours = QPushButton(self.widget)
        self.pushButton_generate_resthours.setObjectName(u"pushButton_generate_resthours")
        sizePolicy2.setHeightForWidth(self.pushButton_generate_resthours.sizePolicy().hasHeightForWidth())
        self.pushButton_generate_resthours.setSizePolicy(sizePolicy2)
        self.pushButton_generate_resthours.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButton_generate_resthours)

        self.pushButton_info_resthours = QPushButton(self.widget)
        self.pushButton_info_resthours.setObjectName(u"pushButton_info_resthours")
        sizePolicy3.setHeightForWidth(self.pushButton_info_resthours.sizePolicy().hasHeightForWidth())
        self.pushButton_info_resthours.setSizePolicy(sizePolicy3)
        self.pushButton_info_resthours.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButton_info_resthours)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 10)
        self.label_NTM = QLabel(self.widget)
        self.label_NTM.setObjectName(u"label_NTM")
        self.label_NTM.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_NTM)

        self.pushButton_selectNTM = QPushButton(self.widget)
        self.pushButton_selectNTM.setObjectName(u"pushButton_selectNTM")
        sizePolicy2.setHeightForWidth(self.pushButton_selectNTM.sizePolicy().hasHeightForWidth())
        self.pushButton_selectNTM.setSizePolicy(sizePolicy2)
        self.pushButton_selectNTM.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_selectNTM)

        self.pushButton_extractNTM = QPushButton(self.widget)
        self.pushButton_extractNTM.setObjectName(u"pushButton_extractNTM")
        sizePolicy2.setHeightForWidth(self.pushButton_extractNTM.sizePolicy().hasHeightForWidth())
        self.pushButton_extractNTM.setSizePolicy(sizePolicy2)
        self.pushButton_extractNTM.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_extractNTM)

        self.pushButton_infoNTM = QPushButton(self.widget)
        self.pushButton_infoNTM.setObjectName(u"pushButton_infoNTM")
        sizePolicy3.setHeightForWidth(self.pushButton_infoNTM.sizePolicy().hasHeightForWidth())
        self.pushButton_infoNTM.setSizePolicy(sizePolicy3)
        self.pushButton_infoNTM.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_infoNTM)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.label_QinsyVP = QLabel(self.widget)
        self.label_QinsyVP.setObjectName(u"label_QinsyVP")
        self.label_QinsyVP.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_QinsyVP)

        self.pushButton_selectVP = QPushButton(self.widget)
        self.pushButton_selectVP.setObjectName(u"pushButton_selectVP")
        sizePolicy2.setHeightForWidth(self.pushButton_selectVP.sizePolicy().hasHeightForWidth())
        self.pushButton_selectVP.setSizePolicy(sizePolicy2)
        self.pushButton_selectVP.setFont(font3)

        self.horizontalLayout_6.addWidget(self.pushButton_selectVP)

        self.pushButton_createCSV = QPushButton(self.widget)
        self.pushButton_createCSV.setObjectName(u"pushButton_createCSV")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_createCSV.sizePolicy().hasHeightForWidth())
        self.pushButton_createCSV.setSizePolicy(sizePolicy4)
        self.pushButton_createCSV.setFont(font3)

        self.horizontalLayout_6.addWidget(self.pushButton_createCSV)

        self.pushButton_instructionQinsy = QPushButton(self.widget)
        self.pushButton_instructionQinsy.setObjectName(u"pushButton_instructionQinsy")
        sizePolicy3.setHeightForWidth(self.pushButton_instructionQinsy.sizePolicy().hasHeightForWidth())
        self.pushButton_instructionQinsy.setSizePolicy(sizePolicy3)
        self.pushButton_instructionQinsy.setFont(font3)

        self.horizontalLayout_6.addWidget(self.pushButton_instructionQinsy)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(widget_NHP)

        QMetaObject.connectSlotsByName(widget_NHP)
    # setupUi

    def retranslateUi(self, widget_NHP):
        widget_NHP.setWindowTitle(QCoreApplication.translate("widget_NHP", u"Form", None))
        self.label_noordhoekpathfinder.setText(QCoreApplication.translate("widget_NHP", u"Noordhoek Pathfinder App", None))
        self.label_image_nhp.setText("")
        self.label_UKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"UK crew list:", None))
        self.pushButton_copyUKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"Select NHP format crewlist", None))
        self.pushButton_createUKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"Create an UK crewlist", None))
        self.pushButton_infoUKcrewlist.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
        self.label_NLcrewlist.setText(QCoreApplication.translate("widget_NHP", u"NL crew list:", None))
        self.pushButton_freshNL.setText(QCoreApplication.translate("widget_NHP", u"Start fresh", None))
        self.pushButton_arrivalNL.setText(QCoreApplication.translate("widget_NHP", u"Arrival crew list", None))
        self.pushButton_departureNL.setText(QCoreApplication.translate("widget_NHP", u"Departure crew list", None))
        self.pushButton_createNL.setText(QCoreApplication.translate("widget_NHP", u"Create a NL crew list", None))
        self.pushButton_infoNL.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
        self.label_resthours_and_timesheets_2.setText(QCoreApplication.translate("widget_NHP", u"Resthours and timesheets:", None))
        self.pushButton_generate_resthours.setText(QCoreApplication.translate("widget_NHP", u"Generate sheets", None))
        self.pushButton_info_resthours.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
        self.label_NTM.setText(QCoreApplication.translate("widget_NHP", u"Notices To Mariners:", None))
        self.pushButton_selectNTM.setText(QCoreApplication.translate("widget_NHP", u"Select NTM", None))
        self.pushButton_extractNTM.setText(QCoreApplication.translate("widget_NHP", u"Extract corrections", None))
        self.pushButton_infoNTM.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
        self.label_QinsyVP.setText(QCoreApplication.translate("widget_NHP", u"Qinsy voyage planning:", None))
        self.pushButton_selectVP.setText(QCoreApplication.translate("widget_NHP", u"Select voyage plan", None))
        self.pushButton_createCSV.setText(QCoreApplication.translate("widget_NHP", u"Create csv", None))
        self.pushButton_instructionQinsy.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
    # retranslateUi

