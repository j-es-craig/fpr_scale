import os

# Define your paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data/Stage1')
DATA_OUT_DIR = os.path.join(BASE_DIR, 'data/post_processed/Stage1')
RESULTS_OUT_DIR = os.path.join(BASE_DIR, 'results/post_processed/Stage1')

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DATA_OUT_DIR, exist_ok=True)
os.makedirs(RESULTS_OUT_DIR, exist_ok=True)

# Set desired number of dominant colors
N_COLORS = 5