class City:
    #   the City class contains:
    #       city name
    #       distance to B
    #       frontier cities of the city
    def __init__(self, name, distance, frontier=list()):
        self.name = name
        self.distance = distance
        self.frontier = frontier

    #   the function to give a list of frontier cities
    def setfrontier(self, frontier_city):
        self.frontier = frontier_city


#   use given distances to implement
#       the greedy best-first search
#    which is going to find the nearest city recursively
def greedybestfirstsearch(initialcity):
    if initialcity == Bucharest:
        print("Reached Destination: Bucharest!")
        return
    j = {}
    for i in range(len(initialcity.frontier)):
        j[initialcity.frontier[i]] = initialcity.frontier[i].distance;
    now = min(j, key=j.get)
    print("now ->", now.name)
    greedybestfirstsearch(now)


Arad = City("Arad", 366)
Bucharest = City("Bucharest", 0)
Craiova = City("Craio", 160)
Drobeta = City("Drobeta", 242)
Eforie = City("Eforie", 161)
Fagaras = City("Fagaras", 176)
Giurgiu = City("Giurgiu", 77)
Hirsova = City("Hirsova", 151)
Iasi = City("Iasi", 226)
Lugoj = City("Lugoj", 244)
Mehadia = City("Mehadia", 241)
Neamt = City("Neamt", 234)
Oradea = City("Oradea", 380)
Pitesti = City("Pitesti", 100)
RimnicuVilcea = City("RimnicuVilcea", 193)
Sibiu = City("Sibiu", 253)
Timisoara = City("Timisoara", 329)
Urziceni = City("Urzicent", 80)
Vaslui = City("Vaslui", 199)
Zerind = City("Zerind", 374)

Arad.setfrontier([Zerind, Sibiu, Timisoara])
Bucharest.setfrontier([Pitesti, Giurgiu, Urziceni])
Craiova.setfrontier([Drobeta, Pitesti, RimnicuVilcea])
Drobeta.setfrontier([Mehadia, Craiova])
Eforie.setfrontier([Hirsova])
Fagaras.setfrontier([Sibiu, Bucharest])
Giurgiu.setfrontier([Bucharest])
Hirsova.setfrontier([Urziceni, Eforie])
Iasi.setfrontier([Neamt, Vaslui])
Lugoj.setfrontier([Timisoara, Mehadia])
Mehadia.setfrontier([Lugoj, Drobeta])
Neamt.setfrontier([Iasi])
Oradea.setfrontier([Zerind, Sibiu])
Pitesti.setfrontier([RimnicuVilcea, Bucharest])
RimnicuVilcea.setfrontier([Sibiu, Pitesti])
Sibiu.setfrontier([Oradea, Arad, Fagaras])
Timisoara.setfrontier([Arad, Lugoj])
Urziceni.setfrontier([Bucharest, Hirsova])
Vaslui.setfrontier([Iasi, Vaslui])
Zerind.setfrontier([Arad, Oradea])

greedybestfirstsearch(Lugoj)
