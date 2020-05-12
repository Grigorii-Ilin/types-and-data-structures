import time
import numpy as np

from aco import AntColony


RUNS_FOR_MEAN_TIME=20

towns_matrix = np.array([[0, 2, 30, 9, 1],
                        [4, 0, 47, 7, 7],
                        [31, 33, 0, 33, 36],
                        [20, 13, 16, 0, 28],
                        [9, 36, 22, 22, 0]]
                        )

#code_to_test ="""
start=time.monotonic()
ant_colony = AntColony(towns_matrix=towns_matrix, 
                       ants_count=5, 
                       interations_count=1000, 
                       vaporization_coef=0.95,
                       power_coef=2
                       )                   
shortest_path = ant_colony.run()
print(shortest_path)
print("time: ", time.monotonic()-start)
#"""

# elapsed_time = timeit.timeit(code_to_test, number=RUNS_FOR_MEAN_TIME)/RUNS_FOR_MEAN_TIME
# print(elapsed_time)