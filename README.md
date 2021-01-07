# Connection-Points
There is one starting point. Each point is connected to 2 other points. There are a total of 20 points (including the starting point). This is a code to find out the shortest route between any two points

STARTING POINT: [A]

ALL CONNECTIONS:    ['A', 'B'];['B', 'C'];['C', 'D'];['D', 'E']['E', 'F'];['F', 'G'];['G', 'H'];['H', 'I'];['I', 'J'];['J', 'K'];['K', 'L'];['L', 'M'];['M', 'N'];['N', 'O'];['O', 'P'];['P', 'Q'];['Q', 'R'];['R', 'S'];['S', 'T'];['T', 'A']

Idea of the Solution: 
There are only two ways to get to a particular point. In the problem I have taken the two possible routes as 'ln' and 'lr'. Basic idea for finding the shortest route is first finding the distance of either routes, comparing the distance between them, and then return the route with the smaller distance. 

I have not focussed on efficiency of the code here so feel free to comment wherever you think I can improve the code. 
