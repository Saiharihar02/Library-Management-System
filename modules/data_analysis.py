import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

file_path = "datasets/library_occupancy.csv"

df = pd.read_csv(file_path)

df["date"] = pd.to_datetime(df["date"])

print("Dataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe())

print("\nAverage Occupancy by Hour:")

hourly = df.groupby("hour")["occupancy_rate"].mean()

print(hourly)

plt.figure(figsize=(10, 5))

hourly.plot(marker="o")

plt.title("Average Library Occupancy by Hour")
plt.xlabel("Hour")
plt.ylabel("Occupancy Rate (%)")
plt.grid(True)

plt.savefig("outputs/hourly_occupancy.png")
plt.show()


area_occupancy = (
    df.groupby("area")["occupancy_rate"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10, 5))

area_occupancy.plot(kind="bar")

plt.title("Average Occupancy by Library Area")
plt.xlabel("Library Area")
plt.ylabel("Occupancy Rate (%)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("outputs/area_occupancy.png")
plt.show()


daily = (
    df.groupby("date")["occupancy_rate"]
    .mean()
)

plt.figure(figsize=(12, 5))

daily.plot()

plt.title("Daily Library Occupancy Trend")
plt.xlabel("Date")
plt.ylabel("Average Occupancy Rate (%)")
plt.grid(True)

plt.tight_layout()

plt.savefig("outputs/daily_occupancy_trend.png")
plt.show()


exam_comparison = (
    df.groupby("exam_period")["occupancy_rate"]
    .mean()
)

print("\nAverage Occupancy During Exam Period:")
print(exam_comparison)

resource_demand = (
    df.groupby("resource")["resource_demand"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10, 5))

resource_demand.plot(kind="bar")

plt.title("Average Resource Demand")
plt.xlabel("Resource")
plt.ylabel("Demand")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("outputs/resource_demand.png")
plt.show()

print("\nData analysis completed.")