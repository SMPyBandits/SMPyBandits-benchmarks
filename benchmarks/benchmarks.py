# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    params = [100, 500, 1000, 5000]

    def setup(self, n):
        self.n = n
        self.d = {}
        for x in range(self.n):
            self.d[x] = None

    def time_keys(self, n):
        for key in self.d.keys():
            pass

    def time_range(self, n):
        d = self.d
        for key in range(n):
            x = d[key]


class MemSuite:
    params = [100, 500, 1000, 5000]

    def setup(self, n):
        self.n = n

    def mem_list(self, n):
        return [0] * n
