# fpr_scale
 Piloting the development of a Fitzpatrick scale analogue for intraocular pigmentation

## Instructions
 1) pre_process.py
    - Removes black borders from fundus images and returns a PNG with a transparent background

    ![example 1](bin/img_1.png)
    ![example 2](bin/img_2.png)

 2) main3_V1.3_png_wout_border_noblack.py
    - Extracts dominant colors from fundus images, filters out black
    - Returns file with RGB values (and count) per dominant color, per image
    - Ensure to remove alpha channel if using PNGs w/ transparent elements

    ![example 3](bin/fig_3.png)

 3) rearrange.py
    - Spreads dominant_colors.csv into single row entries (per image)

    ![example 5](bin/fig_5.png)

 4) recode.py
    - Will encode eye side and gender as 0 and 1
 
 At some point, 'merged_zip_information.xlsx' [needs to be joined with the rearranged data](results/merged_output.xlsx).
 The data is now ready for cluster analysis. [For example:](clustered_output.xlsx)

 ![example 4](bin/fig_4.png)

## Next Steps and Considerations
- EXIF metadata will allow us to control for inconsitencies among images, and isolate pigmentation
- Considering demographic data, eye side, age, and weight could be informative in cluster analysis
- Other means of clustering should be investigated, including bootstrapping methods, unsupervised machine learning methods, or alternate means of thresholding

## Dependencies
 - numpy
 - opencv
 - scikit-learn
 - matplotlib
 - seaborn
