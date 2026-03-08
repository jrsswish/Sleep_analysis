import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import random

def Sleep_Stress_Analysis(csvfile):
    df = pd.read_csv(csvfile)
    sleep = df['Sleep_Hours'].values
    stress = df['Stress_Level'].values
    sleep_category = []
    n = len(sleep)
    for i in range(n):
        if sleep[i] <= 6:
            sleep_category.append("low")
        elif sleep[i] > 6 and sleep[i] < 8:
            sleep_category.append("norm")
        elif sleep[i] > 8:
            sleep_category.append("high")
        else:
            sleep_category.append("NA")
    df['Sleep_Category'] = sleep_category

    sns.boxplot(x='Sleep_Category', y='Stress_Level', data=df)
    plt.xlabel("Sleep Hours")
    plt.ylabel("Stress Level")
    num_low = sum(1 for i in range(n) if sleep_category[i] == "low")
    mean_low = (sum(stress[i] for i in range(n) if sleep_category[i] == "low"))/num_low
    num_norm = sum(1 for i in range(n) if sleep_category[i] == "norm")
    mean_norm = (sum(stress[i] for i in range(n) if sleep_category[i] == "norm"))/num_norm
    num_high= sum(1 for i in range(n) if sleep_category[i] == "high")
    mean_high = (sum(stress[i] for i in range(n) if sleep_category[i] == "high")) / num_high

    print("Average Mean for low:", mean_low)
    print("Average Mean for norm:", mean_norm)
    print("Average Mean for high:", mean_high)
    plt.show()

def Occupation_Analysis(csvfile):
    df = pd.read_csv(csvfile)
    occupation = df.groupby('Occupation')['Sleep_Hours'].mean()
    print(occupation)
    sns.boxplot(x='Occupation', y='Stress_Level', data=df)
    plt.xlabel("Occupation")
    plt.ylabel("Stress Level")
    plt.show()
if __name__ == '__main__':
    csvfile = sys.argv[1]
    Sleep_Stress_Analysis(csvfile)
    Occupation_Analysis(csvfile)