# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget_NHP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QWidget)

class Ui_widget_NHP(object):
    def setupUi(self, widget_NHP):
        if not widget_NHP.objectName():
            widget_NHP.setObjectName(u"widget_NHP")
        widget_NHP.resize(734, 264)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_NHP.sizePolicy().hasHeightForWidth())
        widget_NHP.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(widget_NHP)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_noordhoekpathfinder = QLabel(widget_NHP)
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

        self.label_image_nhp = QLabel(widget_NHP)
        self.label_image_nhp.setObjectName(u"label_image_nhp")
        sizePolicy1.setHeightForWidth(self.label_image_nhp.sizePolicy().hasHeightForWidth())
        self.label_image_nhp.setSizePolicy(sizePolicy1)
        self.label_image_nhp.setMaximumSize(QSize(120, 60))
        self.label_image_nhp.setTextFormat(Qt.AutoText)
        self.label_image_nhp.setPixmap(QPixmap(u"NHP-removebg-preview.png"))
        self.label_image_nhp.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_image_nhp)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.label_UKcrewlist = QLabel(widget_NHP)
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

        self.pushButton_copyUKcrewlist = QPushButton(widget_NHP)
        self.pushButton_copyUKcrewlist.setObjectName(u"pushButton_copyUKcrewlist")
        sizePolicy2.setHeightForWidth(self.pushButton_copyUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_copyUKcrewlist.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.pushButton_copyUKcrewlist.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_copyUKcrewlist)

        self.pushButton_createUKcrewlist = QPushButton(widget_NHP)
        self.pushButton_createUKcrewlist.setObjectName(u"pushButton_createUKcrewlist")
        sizePolicy2.setHeightForWidth(self.pushButton_createUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_createUKcrewlist.setSizePolicy(sizePolicy2)
        self.pushButton_createUKcrewlist.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_createUKcrewlist)

        self.pushButton_infoUKcrewlist = QPushButton(widget_NHP)
        self.pushButton_infoUKcrewlist.setObjectName(u"pushButton_infoUKcrewlist")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_infoUKcrewlist.sizePolicy().hasHeightForWidth())
        self.pushButton_infoUKcrewlist.setSizePolicy(sizePolicy3)
        self.pushButton_infoUKcrewlist.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_infoUKcrewlist)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.label_NLcrewlist = QLabel(widget_NHP)
        self.label_NLcrewlist.setObjectName(u"label_NLcrewlist")
        sizePolicy2.setHeightForWidth(self.label_NLcrewlist.sizePolicy().hasHeightForWidth())
        self.label_NLcrewlist.setSizePolicy(sizePolicy2)
        self.label_NLcrewlist.setFont(font1)
        self.label_NLcrewlist.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_NLcrewlist)

        self.pushButton_freshNL = QPushButton(widget_NHP)
        self.pushButton_freshNL.setObjectName(u"pushButton_freshNL")
        sizePolicy2.setHeightForWidth(self.pushButton_freshNL.sizePolicy().hasHeightForWidth())
        self.pushButton_freshNL.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_freshNL.setFont(font3)

        self.horizontalLayout_2.addWidget(self.pushButton_freshNL)

        self.pushButton_arrivalNL = QPushButton(widget_NHP)
        self.pushButton_arrivalNL.setObjectName(u"pushButton_arrivalNL")
        sizePolicy2.setHeightForWidth(self.pushButton_arrivalNL.sizePolicy().hasHeightForWidth())
        self.pushButton_arrivalNL.setSizePolicy(sizePolicy2)
        self.pushButton_arrivalNL.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_arrivalNL)

        self.pushButton_departureNL = QPushButton(widget_NHP)
        self.pushButton_departureNL.setObjectName(u"pushButton_departureNL")
        sizePolicy2.setHeightForWidth(self.pushButton_departureNL.sizePolicy().hasHeightForWidth())
        self.pushButton_departureNL.setSizePolicy(sizePolicy2)
        self.pushButton_departureNL.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_departureNL)

        self.pushButton_createNL = QPushButton(widget_NHP)
        self.pushButton_createNL.setObjectName(u"pushButton_createNL")
        sizePolicy2.setHeightForWidth(self.pushButton_createNL.sizePolicy().hasHeightForWidth())
        self.pushButton_createNL.setSizePolicy(sizePolicy2)
        self.pushButton_createNL.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_createNL)

        self.pushButton_infoNL = QPushButton(widget_NHP)
        self.pushButton_infoNL.setObjectName(u"pushButton_infoNL")
        sizePolicy3.setHeightForWidth(self.pushButton_infoNL.sizePolicy().hasHeightForWidth())
        self.pushButton_infoNL.setSizePolicy(sizePolicy3)
        self.pushButton_infoNL.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_infoNL)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.label_resthours_and_timesheets = QLabel(widget_NHP)
        self.label_resthours_and_timesheets.setObjectName(u"label_resthours_and_timesheets")
        sizePolicy2.setHeightForWidth(self.label_resthours_and_timesheets.sizePolicy().hasHeightForWidth())
        self.label_resthours_and_timesheets.setSizePolicy(sizePolicy2)
        self.label_resthours_and_timesheets.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_resthours_and_timesheets)

        self.pushButton_generate_resthours = QPushButton(widget_NHP)
        self.pushButton_generate_resthours.setObjectName(u"pushButton_generate_resthours")
        sizePolicy2.setHeightForWidth(self.pushButton_generate_resthours.sizePolicy().hasHeightForWidth())
        self.pushButton_generate_resthours.setSizePolicy(sizePolicy2)
        self.pushButton_generate_resthours.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButton_generate_resthours)

        self.pushButton_info_resthours = QPushButton(widget_NHP)
        self.pushButton_info_resthours.setObjectName(u"pushButton_info_resthours")
        sizePolicy3.setHeightForWidth(self.pushButton_info_resthours.sizePolicy().hasHeightForWidth())
        self.pushButton_info_resthours.setSizePolicy(sizePolicy3)
        self.pushButton_info_resthours.setFont(font2)

        self.horizontalLayout_3.addWidget(self.pushButton_info_resthours)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


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
        self.label_resthours_and_timesheets.setText(QCoreApplication.translate("widget_NHP", u"Resthours and timesheets:", None))
        self.pushButton_generate_resthours.setText(QCoreApplication.translate("widget_NHP", u"Generate sheets", None))
        self.pushButton_info_resthours.setText(QCoreApplication.translate("widget_NHP", u"Instruction", None))
    # retranslateUi

