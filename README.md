# BTP

Summer Research Project by Team (Arjan singh bal, Mathew Sachin, Vipul Barodiya) under mentorship of Prof. Aditya Trivedi and Dr. Sunil Kumar at ABV-IIITM Gwalior. 

This is an work focused on implementing ( and experimenting new Models) parts of methods suggested by R. Vera et.al. in their paper Comparative Analysis and Fusion of Spatio-Temporal Information for Footstep Recognition", in IEEE Pattern Analysis and Machine Intelligence, 2012 (DOI: 10.1109/TPAMI.2012.164) ". 

The basic idea of project is to capture and finding features of the pressure signature of a human being to classifying them on client vs impostor classes based in various scenarios (Datasets of different size - Lab, Airport security, Home). 

The Database SFOOTBD was used for research and academic purpose with permissions from the Biometrics and Data Pattern Analytics - BiDA Lab. 

### Images descibing a pressure signature and processings to make images from signal both by spatial information and temporal information.

#### Pressure difference on a sensor plate at various times (landing or lifting of foot)

![Presure difference over a piezoelectric sensor plate](https://raw.githubusercontent.com/sonumeewa/sonumeewa.github.io/master/assets/img/projects/1.png?token=AFK57JTV33I27NGEVOYNSGK66BQFA)

<br/>

#### Raw signal readings collected by sensor plates arranged in a 2D matrix of 13x7 (sensors).
![Processed signal into footstep images based on Spatial Processing](https://github.com/sonumeewa/BTP/blob/master/signal_images/right.png)


#### Spatially processed signal (after shifting, rotating and smoothening) by taking GRF over all frames
<img src="https://github.com/sonumeewa/BTP/blob/master/signal_images/rotated.png"/>

#### Shifted and Rotated processed signal at various times (Temporal frames)

<img src="https://raw.githubusercontent.com/sonumeewa/BTP/master/signal_images/temporal0.png"/>

Frame- 1

<img src="https://raw.githubusercontent.com/sonumeewa/BTP/master/signal_images/temporal1.png"/>

Frame-2

<img src="https://raw.githubusercontent.com/sonumeewa/BTP/master/signal_images/temporal1_12.png"/>

Frame-3


#### Features 
Global GRF, upper contour, lower contour and various other features were experimented and thier effect on the overall resukts were analysed. 

Global GRF Profile - 

<img src="https://raw.githubusercontent.com/sonumeewa/BTP/master/signal_images/global_grf.png"/>

Upper contour -

<img src="https://raw.githubusercontent.com/sonumeewa/BTP/master/signal_images/upper_contour.png"/>

Lower contour -

<img src="https://raw.githubusercontent.com/sonumeewa/BTP/master/signal_images/lower_contour.png"/>

Standard deviation -

<img src="https://raw.githubusercontent.com/sonumeewa/BTP/master/signal_images/stddev.png"/>

Signal Average -

<img src="https://raw.githubusercontent.com/sonumeewa/BTP/master/signal_images/s_avg.png"/>



#### Findings

Using XGBoost over SVM had significant improvements in the classifying Spatially processed signatures which also contributed to overal classification after ensembling.

##Quick-start
Download `SFootBD.zip` and extract in this folder.

```
SFootBD
  - IndexFiles
  - SFootBD
BTP.ipynb
```

## References

[PAMI2012] R. Vera-Rodriguez, J. Mason, J. Fierrez and J. Ortega-Garcia, "Comparative Analysis and Fusion of Spatio-Temporal Information for Footstep Recognition", in IEEE Pattern Analysis and Machine Intelligence, 2012 (DOI: 10.1109/TPAMI.2012.164).

[IET2011] R. Vera-Rodriguez, J. Mason, J. Fierrez and J. Ortega-Garcia, "Analysis of Spatial Domain Information for Footstep Recognition", IET Computer Vision, 5, 380-388, 2011 (DOI: 10.1049/iet-cvi.2010.0189).
