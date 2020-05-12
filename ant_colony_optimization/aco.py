import sys
import numpy as np


class AntsColony():
	def __init__(self, towns_matrix, ants_count, interations_count, vaporization_coef, power_coef):
		self.towns_matrix = towns_matrix[:]	

		for i in range(len(self.towns_matrix)):
			self.towns_matrix[i][i]=100000

		self.pheromones = np.ones(self.towns_matrix.shape) / len(towns_matrix)			
		self.all_cities = range(len(towns_matrix))							
		self.ants_count = ants_count							
		self.interations_count = interations_count							
		self.vaporization_coef = vaporization_coef								
		self.power_coef = power_coef							
    

	def run(self):
		shortest_way = None
		all_time_shortest_way = ("route", np.inf)
		for _ in range(self.interations_count):
			all_route = self.gen_all_route()
			self.distribution_pheromone(all_route, self.ants_count, shortest_way=shortest_way)
			shortest_way = min(all_route, key=lambda x: x[1])
			
			
			if (shortest_way[1] < all_time_shortest_way[1]):
				all_time_shortest_way = shortest_way
			self.pheromones * self.vaporization_coef #Испарение феромонов
		
		return all_time_shortest_way
	
	# Добавление феромонов на участки по которым пробегали муравьи
	def distribution_pheromone(self, all_route, num_ants, shortest_way):	 
		sorted_way = sorted(all_route, key=lambda x: x[1])		# Вход: (Все маршруты муравьёв в этой итерации, количество муравьёв, кратчайший путь)
		for way, _ in sorted_way[:num_ants]:
			for move in way:
				self.pheromones[move] += 1/self.towns_matrix[move]
				
	def gen_path_dist(self, way):		
	# Считает длину пути муравья Вход:(Маршрут муравья)			
		total_distance = 0
		for l in way:
			 total_distance += self.towns_matrix[l]
		return total_distance	# Выход: (Длина маршрута)
	
	def gen_all_route(self):
	# Формируем маршруты всех муравёв						
		all_route = []
		for _ in range(self.ants_count):
			way = self.gen_way(0)			
			all_route.append((way, self.gen_path_dist(way)))
		return all_route
	
	def gen_way(self, start):	
	# Формируем муршрут каждого муравья											
		way = []
		visited = set()
		visited.add(start)
		prev = start
		for _ in range(len(self.towns_matrix)-1):
			move = self.pick_move(self.pheromones[prev], self.towns_matrix[prev], visited)
			way.append((prev, move))
			prev = move
			visited.add(move)
		way.append((prev, start))	# Возврат в начальную точку
		return way	# Выход: (список маршрута муравья)
	
	def pick_move(self, pheromone, dist, visited):
	# Функция выбора следующего города Вход: ( Массив феромонов в следующие города, Массив расстояний до след городов, кортеж с первым городом)	
		pheromone = np.copy(pheromone)
		pheromone[list(visited)] = 0
		
		choice = pheromone ** ((1.0/dist) ** self.power_coef)# Вероятность перехода из вершины i в вершину j 
		
		norm_choice = choice / choice.sum()		
		
		move = np.random.choice(self.all_cities, 1, p=norm_choice) [0]# Выбор маршрута
		return move

