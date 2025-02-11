import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv("laptop_prices.csv")
 
def men():
    print("***Laptop Price Checker***\n1.Brand-wise Price Distribution (Box Plot)\n2.Average Laptop Prices by Brand (Line Plot)\n3.Impact of RAM on Price (Box Plot)\n4.Storage Type Influence (Box Plot)\n5.Screen Resolution vs. Price (Box Plot)\n6.Most Common Processors (Bar Plot)\n7.Most Common GPUs (Bar Plot)\n8.Battery Life vs. Laptop Weight (Scatter Plot)\n9.Operating System Influence on Price (Box Plot)\n10.exit")
    choice = int(input("Please enter your selection ---: "))
    if choice == 1:
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="Brand", y="Price ($)", data=df)
        plt.xticks(rotation=45)
        plt.title("Laptop Price Distribution by Brand")
        plt.show()
    if choice == 2:
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=df.groupby("Brand")["Price ($)"].mean().index,
             y=df.groupby("Brand")["Price ($)"].mean().values, marker="o")
        plt.xticks(rotation=45)
        plt.title("Average Laptop Price by Brand")
        plt.ylabel("Average Price ($)")
        plt.show()
    if choice == 3:
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="RAM (GB)", y="Price ($)", data=df)
        plt.title("Impact of RAM on Laptop Price")
        plt.show()
    if choice == 4:
        df["Storage Type"] = df["Storage"].apply(lambda x: "SSD" if "SSD" in x else "HDD")
        plt.figure(figsize=(6, 6))
        sns.boxplot(x="Storage Type", y="Price ($)", data=df)
        plt.title("Impact of Storage Type on Price")
        plt.show()
    if choice == 5:
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="Resolution", y="Price ($)", data=df)
        plt.xticks(rotation=45)
        plt.title("Impact of Screen Resolution on Price")
        plt.show()
    if choice == 6:
        plt.figure(figsize=(12, 6))
        top_cpus = df["Processor"].value_counts().nlargest(10).index
        sns.countplot(y=df[df["Processor"].isin(top_cpus)]["Processor"], order=top_cpus)
        plt.title("Top 10 Most Common Processors")
        plt.show()
    if choice == 7:
        plt.figure(figsize=(12, 6))
        top_gpus = df["GPU"].value_counts().nlargest(10).index
        sns.countplot(y=df[df["GPU"].isin(top_gpus)]["GPU"], order=top_gpus)
        plt.title("Top 10 Most Common GPUs")
        plt.show()
    if choice == 8:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="Weight (kg)", y="Battery Life (hours)", data=df, alpha=0.5)
        plt.title("Battery Life vs. Laptop Weight")
        plt.show()
    if choice == 9:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x="Operating System", y="Price ($)", data=df)
        plt.title("Operating System Influence on Laptop Price")
        plt.xticks(rotation=45)
        plt.show()
    if choice == 10:
        exit()
    men()
 
men()
 