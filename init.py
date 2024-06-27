import os

# Define your paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data/raw/Combined')
DATA_OUT_DIR = os.path.join(BASE_DIR, 'data/post_processed/Combined')
RESULTS_OUT_DIR = os.path.join(BASE_DIR, 'results/Combined')

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DATA_OUT_DIR, exist_ok=True)
os.makedirs(RESULTS_OUT_DIR, exist_ok=True)

# Set number of desired dominant colors
N_COLORS = 40

# Set number of clusters
N_CLUSTERS = 3