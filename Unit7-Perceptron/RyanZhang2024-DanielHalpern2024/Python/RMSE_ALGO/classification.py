
import os
from random import random


def normalize_gpa(gpa):
    """
    Normalize the gpa score
    :param gpa: gpa score
    :return: normalized gpa score
    """
    return (gpa) * 2.5

def normalize_sat(sat, max_sat, min_sat):
    """
    Normalize the SAT score
    :param sat: SAT score
    :param max_sat: maximum SAT score
    :param min_sat: minimum SAT score
    :return: normalized SAT score
    """
    return (10*((sat - min_sat) / (max_sat - min_sat)))

def calculateOutput(weights, sat, gpa, essay, rec, extra):
    """
    Calculate the output of the perceptron
    :param weights: weights of the perceptron
    :param sat: SAT score
    :param gpa: GPA score
    :param essay: essay score
    :param rec: recommendation score
    :param extra: extra score
    :return: the output of the perceptron
    """

    sum =  weights[1] * sat + weights[2] * gpa + weights[3] * essay + weights[4] * rec + weights[5] * extra + weights[0]
    if sum >= 0:
        return 1
    else:
        return -1


########################################################################################################################
#                                                                                                                      # 
#                                               APP START                                                              #
#                                                                                                                      #
########################################################################################################################


# Data
sat = []
gpa = []
essay = []
rec = []
extra = []
result = []

# most recent run
run = os.listdir('./runs')[-1]
with open(f'./runs/{run}', 'r') as f:
    for row in f:
        weights = row.split()
        weights = [i.replace(',', '') for i in weights]
        weights = [float(i) for i in weights]
        
# Read the data from the file
with open('validation.txt', 'r') as f:
    for row in f:
            row_lst = row.split()
            sat.append(float(row_lst[0]))
            gpa.append(float(row_lst[1]))
            essay.append(float(row_lst[2]))
            rec.append(float(row_lst[3]))
            extra.append(float(row_lst[4]))
            if row_lst[5] == 'A':
                result.append(1)
            else:
                result.append(-1)


# Normalize the sat score
for i in range(0, len(sat)):
    sat[i] = normalize_sat(sat[i], max(sat), min(sat))

# Normalize the gpa score
for i in range(0, len(gpa)):
    gpa[i] = normalize_gpa(gpa[i])

# Calculate the output
val = []
for i in range(0, len(result)):
    val.append(calculateOutput(weights, sat[i], gpa[i], essay[i], rec[i], extra[i]))


correct = 0
for i in range(0, len(result)):
    if result[i] == val[i]:
        print('Correct')
        correct += 1
    else:
        print('Incorrect')

print('Accuracy:', 100*(correct/len(result)))
    
