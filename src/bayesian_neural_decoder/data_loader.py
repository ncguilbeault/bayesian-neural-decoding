import pickle
import pandas as pd
import numpy as np
import track_linearization as tl
import replay_trajectory_classification as rtc
import os

class DataLoader:
    def __init__(self):
        super().__init__()

    @classmethod
    def load_sorted_spike_data(cls, 
                  dataset_path: str = "../../../datasets/decoder_data",
                  results_filename: str = "sorted_spike_decoding_results.pkl") -> dict:

        decoding_results_filename = os.path.join(dataset_path, results_filename)
        if not os.path.exists(decoding_results_filename):
            raise Exception("Dataset incorrect. Missing decoding results file.")

        with open(decoding_results_filename, "rb") as f:
            results = pickle.load(f)
            decoding_results = results["decoding_results"]
            position_bins = decoding_results.position.to_numpy()[np.newaxis]
            predictions = decoding_results.acausal_posterior.to_numpy()
            position_data = results["linear_position"]
            spike_times = results["spike_times"]

        return {
            "position_data": position_data,
            "spike_times": spike_times,
            "decoding_results": predictions,
            "position_bins": position_bins
        }
    
    @classmethod
    def load_clusterless_spike_data(cls, 
                  dataset_path: str = "../../../datasets/decoder_data",
                  results_filename: str = "clusterless_spike_decoding_results.pkl") -> dict:
        
        decoding_results_filename = os.path.join(dataset_path, results_filename)
        if not os.path.exists(decoding_results_filename):
            raise Exception("Dataset incorrect. Missing decoding results file.")

        with open(decoding_results_filename, "rb") as f:
            results = pickle.load(f)
            decoding_results = results["decoding_results"]
            position_bins = decoding_results.position.to_numpy()[np.newaxis]
            predictions = decoding_results.acausal_posterior.to_numpy()
            features = results["features"]
            position_data = results["linear_position"]

        return {
            "position_data": position_data,
            "features": features,
            "decoding_results": predictions,
            "position_bins": position_bins
        }
