#!/usr/bin/env python

##############################################################################
##
# This file is part of SHG data fitting
##
# SHG data fitting is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
##
##############################################################################

__author__ = ["Aymen Mahmoudi"]
__license__ = "GPL"
__date__ = "01/02/2023"


from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtGui, QtCore
import numpy as np
import pandas as pd


 

import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


#  import the gui :
#ui, _ = loadUiType('gui.ui')      # from gui.ui
from gui import Ui_Form  as ui    # from gui.py




class MainWindow(QWidget, ui):

    def __init__(self):
        QWidget.__init__(self)
        #self.setWindowIcon(QtGui.QIcon('logo.jpg')) choose logo from the designer
        self.setupUi(self)
        # desactivate buttons
        #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        #self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        # First empty plot
        self.plot_layout()
        # self.essential_values()
        # self.plot()
        # function to setup buttons
        self.HandleButtons()

       
        
        
    def HandleButtons(self):
        self.update_pushButton.clicked.connect(self.essential_values)
        self.update_pushButton.clicked.connect(self.plot)
        self.browse_pushButton.clicked.connect(lambda: self.openFileNameDialog())
        self.export_pushButton.clicked.connect(lambda: self.open_save_dialog())

    def plot_layout(self):
        self.fig = plt.figure(facecolor='w')
        self.canvas = FigureCanvas(self.fig)
        toolbar = NavigationToolbar(self.canvas, self)
        self.plottingSpace_verticallayout.addWidget(toolbar)
        self.plottingSpace_verticallayout.addWidget(self.canvas)



    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.df = pd.read_csv(fileName, header = None,sep=',',names=['exp_angle', 'exp_intensity'])
            print(self.df.head(4))
            
            self.df["exp_angle"]=np.deg2rad(self.df["exp_angle"])
            self.exp_angle = self.df["exp_angle"]
            self.exp_angle = self.exp_angle.to_numpy()
            self.exp_intensity = self.df["exp_intensity"]
            self.exp_intensity = self.exp_intensity.to_numpy()

    def open_save_dialog(self):
        option = QFileDialog.Options()
        option |=  QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(self, "Save File Name Title", "data.csv", "All Files (*)", options=option)

        # Create a DataFrame
        df = pd.DataFrame({'Angle in radian': self.rads, 'Intensity Fitting': self.r})

        # Export the DataFrame to a CSV file
        df.to_csv(file[0], index=False)

        print('Data exported as: ',file[0])


        

    def plot(self):
        self.fig.clear()

        # creating an array
        plt.axes(projection='polar')
        # containing the radian values
        self.rads = np.arange(0, 2 * np.pi, 0.001)    
        self.r = []
        for rad in self.rads:
            #r.append(self.a*pow(np.cos((self.b*rad)-self.c),self.p)+self.d)
            self.r.append(self.a*pow(np.cos((self.b*rad)-self.c),self.p)+self.d)

        plt.polar(self.rads, self.r, 'g.')
        plt.polar(self.exp_angle,self.exp_intensity, 'r.')
        
        #plt.show()

        #plt.axis('scaled')
        #plt.autoscale(enable = True)
        #plt.axis("off")
        
        self.canvas.draw()

                

    
    def essential_values(self):
        # Global Varilables

        print ('essential values here')
        
        self.a = 0 ; self.b = 0 ; self.c = 0 ;  self.d = 0 ; self.p = 0
        
        
        self.a = float(self.get_a())
        self.b = float(self.get_b())
        self.c = float(self.get_c())
        self.d = float(self.get_d())
        self.p = float(self.get_p())    
        
     

       
        


    def get_a(self):
        a = self.a_lineEdit.text()
        return a

    def get_b(self):
        b = self.b_lineEdit.text()
        return b

    def get_c(self):
        c = self.c_lineEdit.text()
        return c

    def get_d(self):
        d = self.d_lineEdit.text()
        return d

    def get_p(self):
        p = self.p_lineEdit.text()
        return p


  

            
                
                



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # hold ui
    app.exec_()

if __name__ == "__main__" :
    main()



