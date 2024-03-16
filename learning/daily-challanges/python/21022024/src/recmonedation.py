import json
import numpy as np 
from sklearn.neighbors import NearestNeighbors

class MovieRecommendation:
    def __init__(self, dataFileName):
        self.dataFileName = dataFileName