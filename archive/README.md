## Fundus Pigmentation Scale

1) Fundus images are parsed for dominant pixel color to determine the top 5 dominant colors per image
    - main3_V1.0.py
2) RGB values are joined with demographic and disease data
    - transform_excel.py
        dominant_colors.csv (convert to xlsx) + merged_zip_information.xlsx
3) Categorical data are recoded
    - OD = 0
    - OS = 1
    - Male = 0
    - Female = 1
    - recode.py
4) PCA / Clustering is performed

## Instructions by File
1) Use pre_process_V4.0.py if needed to remove black borders and save as PNG (remember to remove alpha channel in vector quantization step)
1) Use main3_V1.0.py to output a CSV of dominant colors per image
2) Use rearrange.py to spread data
3) Use recode.py to convert categorical data into binary
4) Use clustering to conduct PCA on matrix, including / excluding columns / data as necessary
5) Use parse_clusters.py to plot associations between cluster lables and variables of interest

To Do:
- Preprocess images and remove black border
    - See 'pre_processing.py'
- Determine better clustering method, investigate unsupervised cluster methods potentially
- Ensure dominant color data is sorted
