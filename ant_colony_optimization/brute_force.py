import itertools

class BruteForce():
    def __init__(self, towns_matrix):
        self.towns_matrix = towns_matrix
        for i in range(len(self.towns_matrix)):
            self.towns_matrix[i][i]=100000

    def run(self):
        m_len=len(self.towns_matrix)
        all_time_shortest_way=(None, 100000)

        for way in itertools.permutations(list(range(m_len)), m_len):
            if way[0]!=0:
                continue

            total_distance=0
            for i, town in enumerate(way[:-1]):
                next_town=way[i+1]
                total_distance+=self.towns_matrix[town][next_town]
            total_distance+=self.towns_matrix[way[-1]][0]

            if total_distance<all_time_shortest_way[1]:
                all_time_shortest_way=(way, total_distance)

        return all_time_shortest_way
