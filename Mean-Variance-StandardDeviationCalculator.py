import numpy as np

def calculate(liste):

    if len(liste) < 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(liste).reshape(3,3)

    calculations = dict()
    mean = list()
    variance = list()
    std = list()
    max = list()
    min = list()
    sum = list()

    mean1 = np.mean(a, axis=0, dtype="float64")
    mean1 = mean1.tolist()
    mean.append(mean1)

    mean2 = np.mean(a, axis=1, dtype="float64")
    mean2 = mean2.tolist()
    mean.append(mean2)

    mean3 = np.mean(a, dtype="float64")
    mean3 = mean3.tolist()
    mean.append(mean3)

    calculations["mean"] = mean

    variance1 = np.var(a, axis=0, dtype="float64")
    variance1 = variance1.tolist()
    variance.append(variance1)

    variance2 = np.var(a, axis=1, dtype="float64")
    variance2 = variance2.tolist()
    variance.append(variance2)

    variance3 = np.var(a, dtype="float64")
    variance3 = variance3.tolist()
    variance.append(variance3)

    calculations["variance"] = variance

    std1 = np.std(a, axis=0, dtype="float64")
    std1 = std1.tolist()
    std.append(std1)

    std2 = np.std(a, axis=1, dtype="float64")
    std2 = std2.tolist()
    std.append(std2)

    std3 = np.std(a, dtype="float64")
    std3 = std3.tolist()
    std.append(std3)

    calculations["standard deviation"] = std

    max1 = a.max(axis=0)
    max1 = max1.tolist()
    max.append(max1)

    max2 = a.max(axis=1)
    max2 = max2.tolist()
    max.append(max2)

    max3 = a.max()
    max3 = max3.tolist()
    max.append(max3)

    calculations["max"] = max

    min1 = a.min(axis=0)
    min1 = min1.tolist()
    min.append(min1)

    min2 = a.min(axis=1)
    min2 = min2.tolist()
    min.append(min2)

    min3 = a.min()
    min3 = min3.tolist()
    min.append(min3)

    calculations["min"] = min

    sum1 = np.sum(a, axis=0)
    sum1 = sum1.tolist()
    sum.append(sum1)

    sum2 = np.sum(a, axis=1)
    sum2 = sum2.tolist()
    sum.append(sum2)

    sum3 = np.sum(a)
    sum3 = sum3.tolist()
    sum.append(sum3)

    calculations["sum"] = sum

    return calculations