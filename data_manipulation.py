from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "cpu_dataset.csv")
def avg_msrp():
    rounded_avg_price = round(df['MSRP_USD'].mean(), 2)
    print(f"The average cpu price is ${rounded_avg_price}.")
    return
def min_msrp_cpu():
    lowest_priced_cpu = df[df['MSRP_USD'] == df['MSRP_USD'].min()]['CPU'].tolist()
    print(f"The lowest priced cpu is the {', '.join(lowest_priced_cpu)}.")
    return
def max_msrp_cpu():
    highest_priced_cpu = df[df['MSRP_USD'] == df['MSRP_USD'].max()]['CPU'].tolist()
    print(f"The highest priced cpu is the {', '.join(highest_priced_cpu)}.")
    return
def intel_cpus_count():
    intel_count = (df['Manufacturer'] == 'Intel').sum()
    print(f"There are {intel_count} Intel CPUs in the data set.")
    return
def amd_cpus_count():
    amd_count = (df['Manufacturer'] == 'AMD').sum()
    print(f"There are {amd_count} AMD CPUs in the data set.")
    return
def intel_avg_msrp():
    intel_filtered_df = df[df['Manufacturer'] == 'Intel']
    intel_rounded_avg_price = round(intel_filtered_df['MSRP_USD'].mean(), 2)
    print(f"The average price of Intel CPUs in the data set is ${intel_rounded_avg_price}.")
    return
def amd_avg_msrp():
    amd_filtered_df = df[df['Manufacturer'] == 'AMD']
    amd_rounded_avg_price = round(amd_filtered_df['MSRP_USD'].mean(), 2)
    print(f"The average price of AMD CPUs in the data set is ${amd_rounded_avg_price}.")
    return
def price_filter():
    while True:
        price_range = input("Enter your maximum of the price range for the CPUs you want to look at.")
        try:
            price_range = float(price_range)
            if price_range < 0:
                print("There are no CPUs whose MSRP is negative.")
                return
            elif not np.isfinite(price_range):
                print("Please enter a finite number.")
                return
            price_filtered_df = df[df['MSRP_USD'] <= price_range]
            price_filtered_cpus = price_filtered_df[['CPU', 'MSRP_USD']]
            print(price_filtered_cpus)
            return
        except ValueError:
            print("Please enter a valid price range.")
def standard_deviation():
    standard_deviation = np.std(df['MSRP_USD']).round(2)
    print(f"The standard deviation of the data set is {standard_deviation}.")
    return
def cpu_architecture_graph_avg_msrp():
    cpu_architecture = df.groupby('Architecture', sort = False)['MSRP_USD'].mean()
    print(cpu_architecture.round(2))
    cpu_architecture.plot(kind = "bar", figsize=(12, 6))
    plt.xlabel("CPU Architecture")
    plt.ylabel("MSRP in USD")
    plt.title("Average MSRP of each CPU Architecture (USD)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("cpu_architecture_graph.png")
    print("Graph saved!")
    plt.show()
    return
def cores_graph_avg_msrp():
    cores = df.groupby('Cores')['MSRP_USD'].mean().reset_index()
    cores.plot(kind = 'scatter', x = 'Cores', y = 'MSRP_USD', figsize = (12, 6))
    plt.xlabel("Number of Cores")
    plt.ylabel("MSRP in USD")
    plt.title("Average MSRP of each number of cores (USD)")
    plt.tight_layout()
    plt.savefig("cores_graph.png")
    print("Graph saved!")
    plt.show()
    return

def main_menu():
    first_time = True
    while True:
        if first_time == True:
            print("Hello and Welcome to my CPU Data Manipulation Program")
            first_time = False
        print("The following are the operations you can use:")
        print("'Average CPU price', 'lowest CPU price', 'highest CPU price', 'number of Intel CPUs', 'number of AMD CPUs', 'average price of Intel CPUs', 'average price of AMD CPUs', 'price filter', 'Standard Deviation of data set', 'CPU architecture vs price graph', 'CPU cores vs price graph', or 'quit'")
        operation = input("What operation would you like to use?")
        if operation.lower().strip() == "average cpu price":
            avg_msrp()
        elif operation.lower().strip() == "lowest cpu price":
            min_msrp_cpu()
        elif operation.lower().strip() == "highest cpu price":
            max_msrp_cpu()
        elif operation.lower().strip() == "number of intel cpus":
            intel_cpus_count()
        elif operation.lower().strip() == "number of amd cpus":
            amd_cpus_count()
        elif operation.lower().strip() == "average price of intel cpus":
            intel_avg_msrp()
        elif operation.lower().strip() == "average price of amd cpus":
            amd_avg_msrp()
        elif operation.lower().strip() == "price filter":
            price_filter()
        elif operation.lower().strip() == "standard deviation of data set":
            standard_deviation()
        elif operation.lower().strip() == "cpu architecture vs price graph":
            cpu_architecture_graph_avg_msrp()
        elif operation.lower().strip() == "cpu cores vs price graph":
            cores_graph_avg_msrp()
        elif operation.lower().strip() == "quit":
            print("Program closed successfully")
            break
        else:
            print("Enter a valid operation.")
main_menu()