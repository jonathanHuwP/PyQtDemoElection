# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './resources/designer_ui/electiondemo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ElectionDemo(object):
    def setupUi(self, ElectionDemo):
        ElectionDemo.setObjectName("ElectionDemo")
        ElectionDemo.resize(800, 821)
        self.centralwidget = QtWidgets.QWidget(ElectionDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self._constituencyTableView = QtWidgets.QTableView(self.centralwidget)
        self._constituencyTableView.setObjectName("_constituencyTableView")
        self.verticalLayout.addWidget(self._constituencyTableView)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self._partyTableView = QtWidgets.QTableView(self.centralwidget)
        self._partyTableView.setObjectName("_partyTableView")
        self.verticalLayout_2.addWidget(self._partyTableView)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        ElectionDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ElectionDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ElectionDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ElectionDemo)
        self.statusbar.setObjectName("statusbar")
        ElectionDemo.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(ElectionDemo)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(ElectionDemo)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(ElectionDemo)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ElectionDemo)
        self.actionExit.triggered.connect(ElectionDemo.close)
        self.actionOpen.triggered.connect(ElectionDemo.load_data)
        self.actionSave.triggered.connect(ElectionDemo.save_data)
        QtCore.QMetaObject.connectSlotsByName(ElectionDemo)

    def retranslateUi(self, ElectionDemo):
        _translate = QtCore.QCoreApplication.translate
        ElectionDemo.setWindowTitle(_translate("ElectionDemo", "Election Data"))
        self.label.setText(_translate("ElectionDemo", "Constituencies"))
        self.label_2.setText(_translate("ElectionDemo", "Party Share"))
        self.menuFile.setTitle(_translate("ElectionDemo", "File"))
        self.actionOpen.setText(_translate("ElectionDemo", "Open"))
        self.actionSave.setText(_translate("ElectionDemo", "Save"))
        self.actionExit.setText(_translate("ElectionDemo", "Exit"))

