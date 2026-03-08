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


def Daily_phone_hours_analysis(csvfile):
    df = pd.read_csv(csvfile)
    sleep = df['Sleep_Hours']
    daily_phone_hours = df['Daily_Phone_Hours']
    phone_hours_category = []
    n = len(daily_phone_hours)
    for i in range(n):
        if daily_phone_hours[i] <= 6:
            phone_hours_category.append("low")
        elif daily_phone_hours[i] > 6 and daily_phone_hours[i] < 8:
            phone_hours_category.append("norm")
        elif daily_phone_hours[i] > 8:
            phone_hours_category.append("high")
        else:
            phone_hours_category.append("NA")
    df['Phone_Hours_Category'] = phone_hours_category
    phone_hours = df.groupby('Phone_Hours_Category')['Sleep_Hours'].mean()
    print(phone_hours)

    sns.boxplot(x='Phone_Hours_Category', y='Sleep_Hours', data=df)
    plt.xlabel("Daily Phone Hours Category")
    plt.ylabel("Sleep Hours")
    plt.show()

if __name__ == '__main__':
    csvfile = sys.argv[1]
    Daily_phone_hours_analysis(csvfile)