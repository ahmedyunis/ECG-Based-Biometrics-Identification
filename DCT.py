import math
def DCT(vector):
    result = []
    factor = math.pi / len(vector)
    for i in range(len(vector)):
        sum = 0.0
        for (j, val) in enumerate(vector):
            sum += val * math.cos((j + 0.5) * i * factor)
        result.append(sum)
    return result