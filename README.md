# SHG data fitter


## Description

Second harmonic generation (SHG) is a second-order nonlinear optical process often used to evaluate the materials' crystallographic symmetry. The typical signal response of such an experiment will be a flower-like 360 curve with a number of petals related to the corresponding probed structure's symmetry group.
<br>
<br> 
In this project, I developed a GUI allowing a manual fitting process via a general cosinus function. 

## Installation
To run the files free_plot.py or fitter.py, I recommend to setup a python virtual environment (tested and verified under 3.8.0 version) and adding the required libraries using the following command after cloning the rep (you can just download the rep in case you don't use git):
```console
pip install -r requirements.txt
```
## Usage
For the free plot case, nothing is needed as entries. You can edit the plot parameter and enjoy updating the general cosinus shape. To use the fitter, you must provide the experimental data in CSV format containing two columns of the angles (in degrees or radians) and the intensity values. You can choose this file via the browsing dialog by pushing the browse button. Then, you can edit the parameter to fit the theoretical curve with your loaded experimental data. After getting the wanted curve, you can save the plot or export the fitting data via the export button in case you prefer re-plot them using another software. 

## Roadmap
 <ul>
  <li>Avoid the crash of the app in case of empty value</li>
  <li>Add a check button to accept radians and degrees</li>
  <li>Extract the parameters from the experimental data use them by default</li>
  <li>Integrate an optimization to fully modelize the fitting plot</li>
  <li>Transform the project on a desktop application</li>
</ul> 

## Support and Contributing
Let me know if you have any suggestions/ideas to enhance those scripts or add further settings. Your suggestions are warmly welcomed.
<br><br>
In case of a problem, It is strongly recommended to post an issue. For a more confidential demand, don't hesitate to email me.


