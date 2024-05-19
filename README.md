# Machine Learning for classifying Multiple Sclerosis


In this project, I'm using the Pytorch model for classifying images from a kaggle dataset, \
the objective of this project is to create a *POC* (Proof-Of-Concept) system that could help in the diagnosis of a specific neurodegenerative condition like Multiple Sclerosis.\
 The inference will be conducted by a Neural Network\
 From now on, the term `MS` will substitute `Multiple Sclerosis`  
---
### Dataset
The used dataset is downloaded from kaggle: <center>
### [Here](https://www.kaggle.com/datasets/buraktaci/multiple-sclerosis/) </center>

The dataset is composed of 2 type of scans for the 2 type of conditions:
1. Control MRIs (Total Control MRIs: 2016)
2. Multiple Sclerosis MRIs (Total MS MRIs: 1411)

\
For each of these two conditions, the MRIs are divided in:
1. Sagittal MRIs (Total: 774)
2. Axial MRIs (Total: 1652)

This particular dataset was used in the study conducted by 
_Macin, G.; Tasci, B.; Tasci, I.; Faust, O.; Barua, P.D.;
Dogan, S.; Tuncer, T.; Tan, R.-S.; Acharya, U.R._

Linked here: _[Accurate Multiple Sclerosis Detection Model Based on Exemplar Multiple Parameters Local Phase Quantization: ExMPLPQ. Appl. Sci. 2022, 12, 4920.](https://doi.org/10.3390/app12104920)_
