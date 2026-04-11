def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    n = len(y_pred)
    if n == 0 or n_bins ==0:
        return None
    ece = 0
    for i in range(n_bins):
        b_m = sum(1 if (i / n_bins) <= b < (i + 1) / n_bins else 0 for b in y_pred)
        if b_m == 0:
            continue
        acc = (1 / b_m) * sum(y_true[b] if (i / n_bins) <= y_pred[b] < (i + 1) / n_bins else 0 for b in range(n))
        conf = (1 / b_m) * sum(y_pred[b] if (i / n_bins) <= y_pred[b] < (i + 1) / n_bins else 0 for b in range(n))
        ece += (b_m / n) * abs(acc - conf)
    return ece