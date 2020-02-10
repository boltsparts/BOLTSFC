# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/bolts_widget.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BoltsWidget(object):
    def setupUi(self, BoltsWidget):
        BoltsWidget.setObjectName(_fromUtf8("BoltsWidget"))
        BoltsWidget.resize(333, 316)
        self.content = QtGui.QWidget()
        self.content.setEnabled(True)
        self.content.setObjectName(_fromUtf8("content"))
        self.verticalLayout = QtGui.QVBoxLayout(self.content)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.partsTree = QtGui.QTreeWidget(self.content)
        self.partsTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.partsTree.setAutoExpandDelay(1)
        self.partsTree.setExpandsOnDoubleClick(False)
        self.partsTree.setColumnCount(2)
        self.partsTree.setObjectName(_fromUtf8("partsTree"))
        self.partsTree.headerItem().setText(0, _fromUtf8("Name"))
        self.partsTree.header().setDefaultSectionSize(150)
        self.partsTree.header().setMinimumSectionSize(50)
        self.partsTree.header().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.partsTree)
        self.props = QtGui.QWidget(self.content)
        self.props.setMinimumSize(QtCore.QSize(0, 0))
        self.props.setObjectName(_fromUtf8("props"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.props)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.props_layout = QtGui.QVBoxLayout()
        self.props_layout.setObjectName(_fromUtf8("props_layout"))
        self.verticalLayout_5.addLayout(self.props_layout)
        self.verticalLayout_2.addWidget(self.props)
        self.params = QtGui.QWidget(self.content)
        self.params.setObjectName(_fromUtf8("params"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.params)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.param_layout = QtGui.QVBoxLayout()
        self.param_layout.setObjectName(_fromUtf8("param_layout"))
        self.verticalLayout_3.addLayout(self.param_layout)
        self.verticalLayout_2.addWidget(self.params)
        self.addButton = QtGui.QPushButton(self.content)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.verticalLayout_2.addWidget(self.addButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        BoltsWidget.setWidget(self.content)

        self.retranslateUi(BoltsWidget)
        QtCore.QMetaObject.connectSlotsByName(BoltsWidget)

    def retranslateUi(self, BoltsWidget):
        BoltsWidget.setWindowTitle(_translate("BoltsWidget", "Standard Parts Selector", None))
        self.partsTree.headerItem().setText(1, _translate("BoltsWidget", "Description", None))
        self.addButton.setText(_translate("BoltsWidget", "Add Part", None))

