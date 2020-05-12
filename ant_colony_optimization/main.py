import time
import numpy as np

from aco import AntsColony
from brute_force import BruteForce


def test_algs(towns_matrix):   
    print("\nAnts colony algorithm started...")
    start=time.monotonic()
    ac = AntsColony(towns_matrix=towns_matrix, 
                    ants_count=5, 
                    interations_count=10000, 
                    vaporization_coef=0.95,
                    power_coef=2
                    )                   
    shortest_way = ac.run()
    print("Shortest way:", shortest_way, "Time: ", time.monotonic()-start)


    print("\nBrute Force algorithm started...")
    start=time.monotonic()
    bf=BruteForce(towns_matrix=towns_matrix)
    shortest_way = bf.run()
    print("Shortest way:", shortest_way, "Time: ", time.monotonic()-start)


towns_matrix = np.array([[0, 2, 30, 9, 1],
                        [4, 0, 47, 7, 7],
                        [31, 33, 0, 33, 36],
                        [20, 13, 16, 0, 28],
                        [9, 36, 22, 22, 0]]
                        )
test_algs(towns_matrix)

towns_matrix = np.array([[0,2,30,9,1,18,52,11,74,16],
                        [4,0,47,7,7,63,11,2,15,9],
                        [31,33,0,33,36,8,16,4,13,7],
                        [20,13,16,0,28,11,14,18,6,2],
                        [9,36,22,22,0,14,70,34,9,26],
                        [17,26,12,32,1,0,40,14,19,66],
                        [10,2,15,19,7,38,0,1,4,36],
                        [14,18,47,17,4,63,8,0,15,19],
                        [20,16,16,7,28,3,14,16,0,52],
                        [9,26,22,30,11,14,31,34,16,0]]
                        )
test_algs(towns_matrix)
