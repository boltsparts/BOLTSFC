# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/value_widget.ui'
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

class Ui_ValueWidget(object):
    def setupUi(self, ValueWidget):
        ValueWidget.setObjectName(_fromUtf8("ValueWidget"))
        ValueWidget.resize(150, 50)
        self.horizontalLayout = QtGui.QHBoxLayout(ValueWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(ValueWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.valueEdit = QtGui.QLineEdit(ValueWidget)
        self.valueEdit.setObjectName(_fromUtf8("valueEdit"))
        self.horizontalLayout.addWidget(self.valueEdit)

        self.retranslateUi(ValueWidget)
        QtCore.QMetaObject.connectSlotsByName(ValueWidget)

    def retranslateUi(self, ValueWidget):
        ValueWidget.setWindowTitle(_translate("ValueWidget", "Form", None))
        self.label.setText(_translate("ValueWidget", "TextLabel", None))

