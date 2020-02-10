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


# based on https://github.com/FreeCAD/Workbench-Starterkit


import os
import FreeCAD
import FreeCADGui
__dirname__ = os.path.dirname(__file__)


class BOLTS(FreeCADGui.Workbench):
    "BOLSTS workbench object, gets initiated at startup of the gui"

    Icon = os.path.join(__dirname__, "BOLTS", "icons", "BOLTS.svg") 
    # Icon =  os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "BOLTSFC", "icons", "BOLTS.svg")
    MenuText = "BOLTS"
    ToolTip = "BOLTS"

    toolbox = ["BOLTS_ShowWidget"]

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self) :
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        from freecad.bolts import BOLTS  # __init__.py in BOLTS will be imported
        FreeCAD.Console.PrintMessage("switching to BOLTS\n")
        FreeCAD.Console.PrintMessage("BOLTS will be imported\n")

        self.appendToolbar("BOLTS", self.toolbox)
        self.appendMenu("BOLTS", self.toolbox)

    def Activated(self):
        """
        code which should be computed when a user switch to this workbench
        """
        pass

    def Deactivated(self):
        """
        code which should be computed when this workbench is deactivated
        """
        pass


class ShowBoltsWidget():
    """
    tool to start BOLTS widget
    """

    def IsActive(self):
        return True

    def Activated(self):
        from . import BOLTS
        BOLTS.show_widget()

    def GetResources(self):
        return {
            "Pixmap"  : os.path.join(__dirname__, "BOLTS", "icons", "BOLTS_logo.svg"),
            "MenuText": "Start BOLTS",
            "ToolTip": "Start BOLTS"
        }


FreeCADGui.addWorkbench(BOLTS())
FreeCADGui.addCommand("BOLTS_ShowWidget", ShowBoltsWidget())
