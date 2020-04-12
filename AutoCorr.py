AutoPerodic = []
Auto_Out_signal = []

def Auto_Correlation(Signal1_Y):
    global AutoPerodic
    AutoPerodic = []
    for i in range(len(Signal1_Y)):
        sum = 0
        for j in range(len(Signal1_Y)):
            if (i == 0):
                sum = sum + (Signal1_Y[j] * Signal1_Y[j])
            else:

                if (j == 0):
                    storeVar = Signal1_Y[i - 1]
                    for x in range(len(Signal1_Y)):
                        if (x + 1 == len(Signal1_Y)):
                            Signal1_Y[len(Signal1_Y) - 1] = 0
                            continue
                        Signal1_Y[x] = Signal1_Y[x + 1]
                    sum = sum + (Signal1_Y[j] * Signal1_Y[j])

                else:
                    z = (Signal1_Y[j] * Signal1_Y[j])
                    sum = sum + z
        AutoPerodic.append(sum / len(Signal1_Y))
        sum = 0
    return AutoPerodic

