# SHG data fitter


## Description

Second harmonic generation (SHG) is a second-order nonlinear optical process often used to evaluate the materials' crystallographic symmetry. The typical signal response of such an experiment will be a flower-like 360 curve with a number of petals related to the corresponding probed structure's symmetry group.
<br>
<br> 
In this project, I developed a GUI allowing a manual fitting process via a general cosinus function. 
      
## Installation
To run the files free_plot.py or fitter.py, I recommend to setup a python 3.10 virtual environment and add the required libraries using the following command: *pip install -r requirements.txt* 
<br>
Otherwise, you can download and directly run the files free_plot.exe or fitter.exe on a Windows X64 machine to use the executable format. 

## Usage
For the free plot case, nothing is needed as entries. You can edit the plot parameter and enjoy updating the general cosinus shape. To use the fitter, you must provide the experimental data in CSV format containing two columns of the angles (in degrees or radians) and the intensity values. You can choose this file via the browsing dialog by pushing the browse button. Then, you can edit the parameter to fit the theoretical curve with your loaded experimental data. After getting the wanted curve, you can save the plot or export the fitting data via the export button in case you prefer re-plot them using another software. 


## Support and Contributing
In case of a problem, It is strongly recommended to post an issue. For a more confidential demand, you can email to mahmoudi7050@gmail.com
<br>
Let me know if you have any suggestions/ideas to enhance those scripts or add further settings. Your suggestions are warmly welcomed.
