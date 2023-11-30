from dataclasses import dataclass


@dataclass(frozen=True)
class Group:
    start_time: float
    end_time: float
    mean_flux: float
    peak_flux: float
    min_flux: float

    def middle_time(self):
        """
        :return: The midpoint of self.start_time and self.end_time
        """

        return (self.end_time - self.start_time) / 2
