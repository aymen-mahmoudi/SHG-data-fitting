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


import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys


def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)


def write_to_file(self, file_path, data):
    """
    Write data to a file.

    Parameters:
    - file_path (str): The path to the file.
    - data (str): The data to be written to the file.

    Returns:
    - bool: True if the write operation is successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"Data successfully written to {file_path}")
        return True
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")
        return False
    
def open_save_dialog(self):
    option = QFileDialog.Options()
    option |=  QFileDialog.DontUseNativeDialog
    
    file = QFileDialog.getSaveFileName(self, "Save File Name Title", "default.txt", "All Files (*)", options=option)
    self.write_to_file(file[0], "Hello Aymen")