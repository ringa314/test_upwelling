# test_upwelling
This repository contains the codes and data used to produce Figures for _"[TITLE]"_ by A. Ring (UDel), Y. Li (UDel), ,, ...

__Contact information:__ The [Computational Oceanography Lab](https://sites.udel.edu/yunli/) led by Dr. Yun Li (yunli@udel.edu) at the University of Delaware

## 1. Main Code
> ```
__The four scripts below (fig*.m) are used to generate Figures 1 to 4 in the paper's main text__
* __fig1_map.m__
  
  __Figure 1:__ (a) Map showing upwelling occurrence frequency in the EUS region, identifying the highly productive outer shelf region and the significant off-shelf upwelling region;
  (b) Map of three WHOI glider paths that pass through the study region during the bloom season to take _in situ_ measurements shown in Figure 2
  
* __fig2_glider_prof.m__
  
  __Figure 2:__ (a-c) _In situ_ temperature and density measurements and OfES-derived nitrate flux at the EUS shelf break between [TIME];
  (d-f) Temperature, density, and nitrate flux depth profiles between [TIME]; (g-i) Temperature, density, and nitrate flux depth profiles between [TIME]
  
* __fig3_yearmon.m__

  __Figure 3:__ (a) ; (b)
  
* __fig4_regress.m__
  
  __Figure 4:__ (a) ; (b)

__The four scripts below (figS*.m) are used to generate Figures S1 to S4 in the supplementary information__
* __figS1.m__

  __Figure S1:__
  
* __figS2.m__
  
  __Figure S2:__ (a-g) Time series of _SSS_ or _SST_ between underway measurements and data assimilation products (ECCO2 for SSS and OISST for SST);
  (h) 1:1 data density plot

* __Figure S3:__
  
  __Figure S3:__ (a-g) Time series of _SSS_ or _SST_ between underway measurements and data assimilation products (ECCO2 for SSS and OISST for SST);
  (h) 1:1 data density plot
  
* __figS4_RF_split.m__

  __Figure S4:__ (a) Learning curve; (b) Sensitivity experiments of training-testing splitting ratio

## 2. Functions and Subroutines
* __info_params.m__
  
  Information used by all the MATLAB scripts __*.m__ to specify parameters used for creating figures
  
* __SStats.m__ [Copyright (c) 2023, Zhaoxu Liu / slandarer]
  
  Subroutine used by __fig1_O2Ar_hist_map_yearly.m__ to calculate the statistics reported in the Taylor diagram
  
## 3. Data
__All the data used for figure generation can be found in the _"./MSdata"_ folder__
* __cmap_NCP.mat__
  
  The RGB data used by __fig1_O2Ar_hist_map_yearly.m__ and __fig2_NCP_yr_map.m__ to create a self-designed _NCP_ colormap

* __cmap_TSdens.mat__

  The RGB data used by __figS1S2_SSS_SST_match.m__ to create a the 1:1 data density plot for _SSS_ and _SST_


  
## Acknowledgment

