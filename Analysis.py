import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import random

def inputHandler(csvfile):
    df = pd.read_csv(csvfile)
    sleep = df['Sleep_Hours'].values
    stress = df['Stress_Level'].values
    sleep_category = []
    n = len(sleep)
    for i in range(n):
        if sleep[i] < 5:
            sleep_category.append("low")
        elif sleep[i] > 5 and sleep[i] < 8:
            sleep_category.append("norm")
        elif sleep[i] > 8:
            sleep_category.append("high")
        else:
            sleep_category.append("NA")
    df['Sleep_Category'] = sleep_category

    print(df)
    sns.boxplot(x='Sleep_Category', y='Stress_Level', data=df)
    plt.xlabel("Sleep Hours")
    plt.ylabel("Stress Level")
    plt.show()

if __name__ == '__main__':
    csvfile = sys.argv[1]
    inputHandler(csvfile)