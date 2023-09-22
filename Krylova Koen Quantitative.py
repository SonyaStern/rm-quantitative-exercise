import pandas
import matplotlib
import seaborn

# Read from csv file
cpu_csv = pandas.read_csv("cpus.csv")

def create_line_plot(csv_name:str, x_axis: str, y_axis: str) -> None:

    matplotlib.pyplot.plot(csv_name[x_axis], csv_name[y_axis])
    matplotlib.pyplot.title(f"Line plot of {x_axis} vs. {y_axis}")
    matplotlib.pyplot.xlabel(f"Cpu {x_axis}")
    matplotlib.pyplot.ylabel(f"Cpu {y_axis}")
    matplotlib.pyplot.show()

def create_histogram(csv_name: str, column_name: str) -> None:
    
    matplotlib.pyplot.hist(csv_name[column_name])
    matplotlib.pyplot.title(f"Histogram of CPU {column_name}")
    matplotlib.pyplot.xlabel("Value")
    matplotlib.pyplot.ylabel("Frequency")
    matplotlib.pyplot.show()


def create_pair_plot(csv_name) -> None:
    seaborn.pairplot(csv_name)
    matplotlib.pyplot.show()

def create_scatter_plot(csv_name: str, x_axis: str, y_axis: str) -> None:
    
    matplotlib.pyplot.scatter(csv_name[x_axis], csv_name[y_axis])
    matplotlib.pyplot.title(f"Scatter plot of Cpu {x_axis} vs. Cpu {y_axis}")
    matplotlib.pyplot.xlabel(f"Cpu {x_axis}")
    matplotlib.pyplot.ylabel(f"Cpu {y_axis}")
    matplotlib.pyplot.show()


# This prints the csv. 
print(cpu_csv)

# create_scatter_plot(csv_name=cpu_csv, x_axis="name", y_axis="mmax")

# create_line_plot(csv_name=cpu_csv, x_axis="name", y_axis="mmax")

# create_histogram(csv_name=cpu_csv, column_name="mmax")

# create_pair_plot(csv_name=cpu_csv)

# cpu_csv_subset = cpu_csv.head(20)

matplotlib.pyplot.plot(cpu_csv["rownames"], cpu_csv["perf"], color="red", label="Actual Performance", marker="o")

matplotlib.pyplot.plot(cpu_csv["rownames"], cpu_csv["estperf"], color="blue", label="Estimated Performance", marker="x")

matplotlib.pyplot.xlabel("Now names")
matplotlib.pyplot.xticks(rotation=45)
matplotlib.pyplot.ylabel("Performance Value")
matplotlib.pyplot.title("Actual Performance vs Estimated Performance")
matplotlib.pyplot.legend()

matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()