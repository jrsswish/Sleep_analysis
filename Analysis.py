import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import random

def inputHandler(csvfile):
    df = pd.read_csv(csvfile)
    df_sample = df.sample(n=50, random_state=1)

    df_sorted = df_sample.sort_values(by='Stress_Level', ascending=True)

    sample_sleep = list(df_sorted['Sleep_Hours'].values)
    sample_stress = list(df_sorted['Stress_Level'].values)

    xmin = min(sample_stress)
    xmax = max(sample_stress)
    plt.scatter( sample_stress, sample_sleep)
    plt.ylabel('Sleep Hours')
    plt.xlabel('Stress Level')
    plt.xticks(np.arange(xmin, xmax, step=1))
    plt.show()
if __name__ == '__main__':
    csvfile = sys.argv[1]
    inputHandler(csvfile)