import exospotter

import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv("../data/wasp-126.csv")
    data.rename(columns={"julian_date": "time"}, inplace=True)

    plt.scatter(data["time"], data["flux"])
    plt.show()

    groups = exospotter.grouping.group_datapoints(data, 0.3)

    new_df = pd.DataFrame([group.asdict() for group in groups])
    plt.scatter(new_df["start_time"], new_df["min_flux"])
    plt.show()


if __name__ == "__main__":
    main()
