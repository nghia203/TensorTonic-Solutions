import numpy as np

def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    ref = np.asarray(reference_counts)
    prod = np.asarray(production_counts)
    p_ref = ref / np.sum(ref)
    p_prod = prod / np.sum(prod)
    drift_score = 0.5 * np.sum(np.abs(p_ref - p_prod))
    drift_detect = bool(drift_score > threshold)
    return {
        'score': drift_score,
        'drift_detected': drift_detect
    }
    pass