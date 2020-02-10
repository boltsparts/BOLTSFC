# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/bool_widget.ui'
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

class Ui_BoolWidget(object):
    def setupUi(self, BoolWidget):
        BoolWidget.setObjectName(_fromUtf8("BoolWidget"))
        BoolWidget.resize(114, 42)
        self.horizontalLayout = QtGui.QHBoxLayout(BoolWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox = QtGui.QCheckBox(BoolWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)

        self.retranslateUi(BoolWidget)
        QtCore.QMetaObject.connectSlotsByName(BoolWidget)

    def retranslateUi(self, BoolWidget):
        BoolWidget.setWindowTitle(_translate("BoolWidget", "Form", None))
        self.checkBox.setText(_translate("BoolWidget", "CheckBox", None))

