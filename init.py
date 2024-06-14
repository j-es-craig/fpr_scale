import os

# Define your paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data/laser_scars')
DATA_OUT_DIR = os.path.join(BASE_DIR, 'data/post_processed/laser_scars')
RESULTS_OUT_DIR = os.path.join(BASE_DIR, 'results/post_processed/laser_scars')

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DATA_OUT_DIR, exist_ok=True)
os.makedirs(RESULTS_OUT_DIR, exist_ok=True)

# Set number of desired dominant colors

# Set number of clusters