import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Ensure inputs are numpy arrays
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # --- METHOD 1: The Optimized Shortcut ---
    # In a standard multi-class setting (where each sample has exactly one true label),
    # Micro-F1 is mathematically identical to Accuracy. 
    # Every false prediction is exactly 1 False Positive and 1 False Negative overall.
    # return np.mean(y_true == y_pred)
    
    # --- METHOD 2: The Explicit Calculation ---
    # Calculates global TP, FP, and FN across all classes.
    classes = np.unique(np.concatenate([y_true, y_pred]))
    
    total_tp = 0
    total_fp = 0
    total_fn = 0
    
    for c in classes:
        # True Positives: Predicted c, and actually c
        total_tp += np.sum((y_true == c) & (y_pred == c))
        # False Positives: Predicted c, but actually NOT c
        total_fp += np.sum((y_true != c) & (y_pred == c))
        # False Negatives: Actually c, but predicted NOT c
        total_fn += np.sum((y_true == c) & (y_pred != c))
        
    # Calculate global precision and recall
    precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
    recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
    
    # Calculate F1 score
    if precision + recall == 0:
        return 0.0
        
    f1 = 2 * (precision * recall) / (precision + recall)
    
    return float(f1)