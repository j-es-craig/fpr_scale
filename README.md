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
    - Before this step, merge [patient data](results/merged_zip_information.xlsx) with the [rearranged data](results/post_processed/Normal/rearranged_rgb_values.csv)
    - Recode will encode eye side and gender as 0 and 1
    - Recode will also sum birth week and day into a single figure
 
 The data is now ready for cluster analysis. Specific dimensions can be included or included in analysis. [After labelling](results/clustered_output.xlsx), you can plot. For example:

 ![example 4](bin/fig_4.png)

## Next Steps and Considerations
- EXIF metadata will allow us to control for inconsitencies among images, and isolate pigmentation
- Considering demographic data, eye side, age, and weight could be informative in cluster analysis
- Associations between clusters and specific dimensions should be investigated (i.e., color, demographics, etc.)
- Other means of clustering should be investigated, including bootstrapping methods, unsupervised machine learning methods, or alternate means of thresholding

Sorry about the excel files, these will be fixed later. 

## Dependencies
 - numpy
 - opencv
 - scikit-learn
 - matplotlib
 - seaborn
