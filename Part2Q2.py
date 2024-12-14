import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_laptop_prices(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    price_column = "Price (Euro)"

    # Plot the prices
    plt.figure(figsize=(10, 6))
    plt.plot(data[price_column].values, marker="o", linestyle="-", label="Laptop Price")
    plt.title("Laptop Prices")
    plt.xlabel("Laptop Index")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()


def analyze_average_laptop_price(file_path):
    data = pd.read_csv(file_path)

    company_column = "Company"
    price_column = "Price (Euro)"

    # Group by company and compute the average price
    average_prices = data.groupby(company_column)[price_column].mean()

    # Find the company with the most expensive laptops on average
    most_expensive_company = average_prices.idxmax()
    print(f"The company with the most expensive laptops on average is: {most_expensive_company}")

    # Plot the average laptop prices by company
    plt.figure(figsize=(12, 6))
    average_prices.sort_values(ascending=False).plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Average Laptop Price by Company")
    plt.xlabel("Company")
    plt.ylabel("Average Price")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def find_different_os(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)    

    # initialize a set to hold the different os types in the file
    os_types = np.unique(np.array(data["OpSys"].values))
    
    print(os_types)
    print(len(os_types))


def distribute_price_per_os(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    op_sys_groups = data.groupby("OpSys")

    # Create a plot for each 'OpSys' group
    for op_sys, group in op_sys_groups:
        plt.figure(figsize=(8, 6))
        plt.hist(group["Price (Euro)"], bins=20, edgecolor="black", alpha=0.7)
        plt.title(f"Distribution of Price for {op_sys}")
        plt.xlabel("Price")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()


def relationship_ram_price(file_path):
    data = pd.read_csv(file_path)
    
    print("The relationship is that if we want more RAM the PRICE will usually be higher")
    plt.figure(figsize=(8, 6))
    plt.scatter(data["RAM (GB)"], data["Price (Euro)"], alpha=0.5, color="blue")
    plt.title("Relationship between RAM and Price")
    plt.xlabel("RAM (GB)")
    plt.ylabel("Price (Euro)")
    plt.grid(True)
    plt.show()


def create_storage_type_column(file_path):
    data = pd.read_csv(file_path)

    # Split the values in 'Memory' by space and create a new column 'Storage type'
    arr = data["Memory"].apply(lambda x: " ".join(x.split(" ")[1:]) if isinstance(x, str) else '')
    # check if there is more than one memeory, if yes split by '+' and take the last value and combine the first and the last
    arr = arr.apply(lambda x: "+ ".join([x.split("+")[0], x.split("+")[-1].split(" ")[-1]]) if len(x.split("+")) > 1 else x)
    data['Storage type'] = arr

    # create a new file with the new column
    data.to_csv("laptop_price - dataset-modified.csv", index=False)




# Call the function with the provided file
file_path = "laptop_price - dataset.csv"
plot_laptop_prices(file_path)
analyze_average_laptop_price(file_path)
find_different_os(file_path)
distribute_price_per_os(file_path)
relationship_ram_price(file_path)
create_storage_type_column(file_path)