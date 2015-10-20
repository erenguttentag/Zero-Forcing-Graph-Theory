import copy


class graph:
	def __init__(self, incident, colored):
		self.incident = incident
		self.colored = colored
		self.vertexlist = list(incident.keys())
		for vertex in self.colored:
			if not vertex in self.incident:
				 raise (Exception("coloring non-existent vertex"))
	def is_colored(self, verticy):
		return self.colored[verticy]
	def print_graph(self):
		for vertex in self.incident:
			print(vertex, self.colored[vertex], self.incident[vertex])
	def do_color_change_step(self):
		for vertex in self.colored:
			if self.colored[vertex] == True:
				non_c_adj_count = 0
				for neighbor in self.incident[vertex]:
					if self.colored[neighbor] == False:
						 non_c_adj_count +=1
				if non_c_adj_count == 1:
					for neighbor in self.incident[vertex]:
						if self.colored[neighbor] == False:
							self.colored[neighbor] = True
							print("colored " + neighbor)
	def check_if_zfs(self): #checks if the graph is a zero forcing set
		maxiters = len(self.incident)
		i = 0
		tempgraph = copy.deepcopy(self)
		while i < maxiters:
			tempgraph.do_color_change_step()
			i += 1
		for vertex in tempgraph.colored:
			if tempgraph.colored[vertex] != True:
				return False
		return True
	def try_all_possible_colorings(self): #that return as a zfs
		blankgraph = copy.deepcopy(self)
		for vertex in blankgraph.colored:
			blankgraph.colored[vertex] = False
		zfsgraphcolorings = []
		for vertex in blankgraph.vertexlist:
			result = None
			for i in (range(0, len(blankgraph.vertexlist))):
				result = blankgraph.colornextvertex(vertex)
				if result != None:
					zfsgraphcolorings.append(result)
			
		return zfsgraphcolorings
	def colornextvertex(self, vertex):
		self.colored[vertex] = not self.colored[vertex]
		# print("reversed color of vertex " + vertex) debug line
		# self.print_graph() # debug line
		if self.check_if_zfs() == True:
			return copy.deepcopy(self)
		else:
			#print("not a zfs") #debug line
			pass	
		if self.colored[vertex] == False:
			try:
				nextvertex = self.vertexlist[self.vertexlist.index(vertex) + 1]			
				return self.colornextvertex(nextvertex)
			except:
				pass
		return None
	def num_colored_verticies(self):
		numcolored = 0 
		for vertex in self.colored:
			if self.colored[vertex]:
				 numcolored +=1 
			else:
				pass
		return numcolored
	def get_zfn(self):
		zfn = len(self.vertexlist)
		zfsofzfn = None
		zfses = self.try_all_possible_colorings()
		for zfs in zfses:
			thisone = zfs.num_colored_verticies()
			if zfn >= thisone:
				zfn = thisone
				zfsofzfn = zfs
		return zfn
		
coloredgraph = graph({'a' : ["b", "c"], 'b' : ["a", "c"], 'c' : ["a", "b"]},
{'a' : True, 'b' : True, 'c' : False})
print(coloredgraph.is_colored('c'))
print(coloredgraph.check_if_zfs())	
print(coloredgraph.is_colored('c'))
coloredgraph.print_graph()
print("now trying every possible coloring")
print(coloredgraph.get_zfn())
petersontest = graph({'a' : ["b", "e", 'g'],
'b' : [ 'a', 'c', 'h'],
'c' : [ 'b', 'd', 'h'],
'd' : [ 'c', 'e', 'j'],
'e' : [ 'a', 'd', 'f'],
'f' : [ 'e', 'h', 'i'],
'g' : [ 'a', 'i', 'j'],
'h' : [ 'b', 'f', 'j'],
'i' : [ 'c', 'i', 'g'],
'j' : [ 'd', 'i', 'g']},
{'a' : False,
'b' : False,
'c' : False,
'd' : False,
'e' : False,
'f' : False,
'g' : False,
'h' : False,
'i' : False ,
'j' : False})
print(petersontest.get_zfn())