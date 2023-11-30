from collections.abc import Iterable
from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class Datapoint:
    """
    Used to represent a lightcurve datapoint.
    """

    flux: float
    time: float


@dataclass(frozen=True)
class Group:
    """
    Used to represent a group of lightcurve datapoints between two time intervals.
    """

    start_time: float
    end_time: float
    mean_flux: float
    peak_flux: float
    min_flux: float

    def middle_time(self) -> float:
        """
        :return: The midpoint of self.start_time and self.end_time
        """

        return (self.end_time + self.start_time) / 2

    @staticmethod
    def generate_group(data: pd.DataFrame):
        """
        Generates a group from a list of datapoints sorted by time.

        :param data: The datapoints to convert into a group. There must be two columns: flux and time.
        :return: A group object that references the datapoints
        """

        if data.shape[0] == 0:
            raise ValueError("Data must have at least one row")

        start_time = data.iloc[0].time
        end_time = data.iloc[-1].time

        mean_flux = data.flux.mean()
        peak_flux = data.flux.max()
        min_flux = data.flux.min()

        return Group(start_time, end_time, mean_flux, peak_flux, min_flux)


def group_datapoints(datapoints: pd.DataFrame, max_gap: float) -> Iterable[Group]:
    """
    Groups datapoints into groups of datapoints that are within max_gap of each other.
    The datapoints must be sorted by time.

    :param datapoints: The datapoints to group. There must be two columns: flux and time.
    :param max_gap: The maximum gap between two datapoints to be considered in the same group.
    :return: A list of groups of datapoints.
    """

    last_time = datapoints.time[0]
    for index, row in datapoints.iterrows():
        if row.time - last_time > max_gap:
            try:
                group = Group.generate_group(datapoints[:index])
            except ValueError:
                continue

            yield group

            datapoints = datapoints[index:]
            last_time = row.time
