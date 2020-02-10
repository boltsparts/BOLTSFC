# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/tableindex_widget.ui'
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

class Ui_TableIndexWidget(object):
    def setupUi(self, TableIndexWidget):
        TableIndexWidget.setObjectName(_fromUtf8("TableIndexWidget"))
        TableIndexWidget.resize(207, 68)
        self.horizontalLayout = QtGui.QHBoxLayout(TableIndexWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(TableIndexWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(TableIndexWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)

        self.retranslateUi(TableIndexWidget)
        QtCore.QMetaObject.connectSlotsByName(TableIndexWidget)

    def retranslateUi(self, TableIndexWidget):
        TableIndexWidget.setWindowTitle(_translate("TableIndexWidget", "Form", None))
        self.label.setText(_translate("TableIndexWidget", "TextLabel", None))

