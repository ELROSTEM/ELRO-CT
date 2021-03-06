from random import randint, random

# Plotting libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def normalizeType(type):
    """
    Normalize the type of the apartment
    :param type: type of the apartment
    :return: the normalized type
    """
    if type == 'coop':
        return 0
    else:
        return 1

def normalizeBedroom(bedroom):
    """
    Normalize the number of bedrooms
    :param bedroom: number of bedrooms
    :return: the normalized number of bedrooms
    """
    return (bedroom - 1)/6

def normalizeBathroom(bathroom):
    """
    Normalize the number of bathrooms
    :param bathroom: number of bathrooms
    :return: the normalized number of bathrooms
    """
    return (bathroom - 1)/5

def normalizeLivingroom(livingroom):
    """
    Normalize the number of livingrooms
    :param livingroom: number of livingrooms
    :return: the normalized number of livingrooms
    """
    return (livingroom)/2

def normalizeDiningroom(diningroom):
    """
    Normalize the number of diningrooms
    :param diningroom: number of diningrooms
    :return: the normalized number of diningrooms
    """
    return diningroom 

def normalizeCondition(condition):
    """
    Normalize the condition of the apartment
    :param condition: condition of the apartment
    :return: the normalized condition
    """
    return (condition - 2)/3

def normalizeArea(area):
    """
    Normalize the area of the apartment
    :param area: area of the apartment
    :return: the normalized area
    """
    return (area-900)/3600

def normalizePrice(price):
    """
    Normalize the price of the apartment
    :param price: price of the apartment
    :return: the normalized price
    """
    return (price - 1000000)/5000000

def unnormalizePrice(price):
    """
    Normalize the price of the apartment
    :param price: price of the apartment
    :return: the normalized price
    """
    return (price * 5000000) + 1000000


def calculateOutput(weights, house, error):
    """
    Calculate the output of the perceptron
    :param weights: weights of the perceptron
    :param house: house matrix
    :param error: error matrix
    :return: the output of the perceptron
    """
    # print("error in function: ", error)
    output = np.add(np.matmul(house , weights), error)
    # output = np.matmul(house , weights)

    return output
    


########################################################################################################################
#                                                                                                                      # 
#                                               APP START                                                              #
#                                                                                                                      #
########################################################################################################################


# Training Data
type = []
bedroom = []
bathroom = []
livingroom = []
diningroom = []
condition = []
area = []
bias = []
price = []
house = []

# Weights
weights = []
with open(f'./outputs/weights.txt', 'r') as f:
    for row in f:
        row = row.replace('\n', '')
        row = row.replace('[', '')
        row = row.replace(']', '')
        row = row.replace(' ', '')
        row = float(row)
        weights.append(row)


# Read the data from the file
with open('./inputs/validation.txt', 'r') as f:
    for row in f:
        row_lst = row.split()
        type.append(row_lst[0])
        bedroom.append(float(row_lst[1]))
        bathroom.append(float(row_lst[2]))
        livingroom.append(float(row_lst[3]))
        diningroom.append(float(row_lst[4]))
        condition.append(float(row_lst[5]))
        area.append(float(row_lst[6]))
        bias.append(1)
        price.append(float(row_lst[7]))


# Normalize the values
for i in range(0, len(type)):
    type[i] = normalizeType(type[i])
    bedroom[i] = normalizeBedroom(bedroom[i])
    bathroom[i] = normalizeBathroom(bathroom[i])
    livingroom[i] = normalizeLivingroom(livingroom[i])
    diningroom[i] = normalizeDiningroom(diningroom[i])
    condition[i] = normalizeCondition(condition[i])
    area[i] = normalizeArea(area[i])
    price[i] = price[i]
    house.append([type[i], bedroom[i], bathroom[i], livingroom[i], diningroom[i], condition[i], area[i], bias[i]])

# Calculate the output
with open('./outputs/validation_output.txt', 'w') as f:
    for i in range(0, len(price)):
        prediction = weights[0]*type[i] + weights[1]*bedroom[i] + weights[2]*bathroom[i] + weights[3]*livingroom[i] + weights[4]*diningroom[i] + weights[5]*condition[i] + weights[6]*area[i] + weights[7]*bias[i]
        prediction = unnormalizePrice(prediction)

        error = prediction - price[i]
        percent_error = (abs(error)/price[i])*100

        info = f'{i})    Price: {price[i]}   Prediction: {prediction}    Error: {error}   Percent Error: {percent_error}'
        f.write(f"{info}\n")
        print(info)






















# Calculate mean percent error
            # difference = np.subtract(output[i, 0], price[i])
            # percent_error = abs((difference*100)/price[i])


"""
# Data
sat = []
gpa = []
essay = []
rec = []
extra = []
result = []

# most recent run
with open(f'./outputs/weights.txt', 'r') as f:
    for row in f:
        weights = row.split()
        weights = [i.replace(',', '') for i in weights]
        weights = [float(i) for i in weights]
        
# Read the data from the file
with open('./inputs/testing.txt', 'r') as f:
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
err = []
for i in range(0, len(result)):
    out, error = calculateOutput(weights, sat[i], gpa[i], essay[i], rec[i], extra[i])
    val.append(out)
    err.append(error)



incorrect = 0
for i in range(0, len(result)):
    if result[i] == val[i]:
        print('Correct')
    else:
        print(f'Incorrect: {err[i]}')
        incorrect += 1

print(f'Error Rate:', 100*(incorrect/len(result)))

outputList = []

with open(f'./outputs/testing_output.txt', 'w') as f:
    f.write(f"Descision Boundry: {weights[1]} * s + {weights[2]} * g + {weights[3]} * e + {weights[4]} * r + {weights[5]} * c + {weights[0]} = 0\n\n")
    for i in range(0, len(result)):
        if val[i] == 1:
            val[i] = 'A'
        else:
            val[i] = 'R'
    for i in range(0, len(result)):
        if result[i] == 1:
            result[i] = 'A'
        else:
            result[i] = 'R'

        if result[i] == val[i]:
            f.write(f"{i}) SAT: {unnormalize_sat(sat[i])} GPA: {unnormalize_gpa(gpa[i])} Essay: {essay[i]} Rec: {rec[i]} ExtraC: {extra[i]} Descison: {val[i]} Class: {result[i]}\n")
        else:
            f.write(f"{i}) SAT: {unnormalize_sat(sat[i])} GPA: {unnormalize_gpa(gpa[i])} Essay: {essay[i]} Rec: {rec[i]} ExtraC: {extra[i]} Descison: {val[i]} Class: {result[i]} *** ERROR\n")
    f.write(f"\nError Rate = {100*(incorrect/len(result))} %")
    
"""
