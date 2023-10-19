import pandas
import matplotlib
import seaborn

# Read from csv file
rf1_1_read = pandas.read_csv("csv/RF1_1_read.csv")
rf1_1_write = pandas.read_csv("csv/RF1_1_write.csv")
rf1_1_total = pandas.read_csv("csv/RF1_1_total.csv")

rf3_1_read = pandas.read_csv("csv/RF3_1_read.csv")
rf3_1_write = pandas.read_csv("csv/RF3_1_write.csv")
rf3_1_total = pandas.read_csv("csv/RF3_1_total.csv")

rf1_q_read = pandas.read_csv("csv/RF1_Q_read.csv")
rf1_q_write = pandas.read_csv("csv/RF1_Q_write.csv")
rf1_q_total = pandas.read_csv("csv/RF1_Q_total.csv")

rf3_q_read = pandas.read_csv("csv/RF3_Q_read.csv")
rf3_q_write = pandas.read_csv("csv/RF3_Q_write.csv")
rf3_q_total = pandas.read_csv("csv/RF3_Q_total.csv")

print(rf1_1_read)


def create_line_plot(csv_name: str, x_axis: str, y_axis: str) -> None:
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

matplotlib.pyplot.scatter(rf3_q_write["total ops"], rf3_q_write["op/s"], color="red", marker="o")


matplotlib.pyplot.xlabel("Total number of operations")
matplotlib.pyplot.xticks(rotation=45)
matplotlib.pyplot.ylabel("Operations per second")
matplotlib.pyplot.title("Total number of write operations VS operation rate")
# matplotlib.pyplot.legend()

matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()