# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hugo/Documents/dev/bolts/BOLTS/output/freecad/BOLTS/gui/property_widget.ui'
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

class Ui_PropertyWidget(object):
    def setupUi(self, PropertyWidget):
        PropertyWidget.setObjectName(_fromUtf8("PropertyWidget"))
        PropertyWidget.resize(152, 35)
        self.horizontalLayout = QtGui.QHBoxLayout(PropertyWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.prop = QtGui.QLabel(PropertyWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prop.sizePolicy().hasHeightForWidth())
        self.prop.setSizePolicy(sizePolicy)
        self.prop.setObjectName(_fromUtf8("prop"))
        self.horizontalLayout.addWidget(self.prop)
        self.value = QtGui.QLabel(PropertyWidget)
        self.value.setWordWrap(True)
        self.value.setObjectName(_fromUtf8("value"))
        self.horizontalLayout.addWidget(self.value)

        self.retranslateUi(PropertyWidget)
        QtCore.QMetaObject.connectSlotsByName(PropertyWidget)

    def retranslateUi(self, PropertyWidget):
        PropertyWidget.setWindowTitle(_translate("PropertyWidget", "Form", None))
        self.prop.setText(_translate("PropertyWidget", "TextLabel", None))
        self.value.setText(_translate("PropertyWidget", "TextLabel", None))

