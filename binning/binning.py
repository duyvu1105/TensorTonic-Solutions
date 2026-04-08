def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    w = (max(values) - min(values)) / num_bins
    if w == 0:
        return [0] * len(values)
    bin = []
    for i, x in enumerate(values):
        bin.append(int(min((x - min(values)) / w, num_bins - 1)))

    return bin