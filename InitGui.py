# ***************************************************************************
# *   Copyright (c) 2020 Bernd Hahnebach <bernd@bimstatik.org>              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************


import os


class BOLTS(Workbench):
    "BOLSTS workbench object"

    bolts_path = os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "BOLTSFC")
    Icon =  os.path.join(bolts_path, "BOLTS", "icons", "BOLTS.svg")
    MenuText = "BOLTS"
    ToolTip = "BOLTS"

    def Initialize(self) :
        self.appendToolbar("BOLTS",["BOLTS_ShowWidget"])
        self.appendMenu("BOLTS",["BOLTS_ShowWidget"])

    def GetClassName(self):
        return "Gui::PythonWorkbench"


class ShowBoltsWidget():
    """
    start BOLTS widged
    """

    def IsActive(self):
        return True

    def Activated(self):
        import BOLTS
        BOLTS.show_widget()

    def GetResources(self):
        bolts_path = os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "BOLTSFC")
        return {
            "Pixmap"  : os.path.join(bolts_path, "BOLTS", "icons", "BOLTS_logo.svg"),
            "MenuText": "Start BOLTS",
            "ToolTip": "Start BOLTS"
        }


Gui.addWorkbench(BOLTS())
Gui.addCommand("BOLTS_ShowWidget", ShowBoltsWidget())
