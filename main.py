ln = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
lr = ['A', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B']

destination = input('destination: ')

def distanceInLn():
    global ln
    global destination
    global distanceLn
    distanceLn = 1
    for x in ln[1:]:
        distanceLn += 1
        if x == destination:
            break
    print(f"route in Ln: {ln[:distanceLn]}")

def distanceInLr():
    global lr
    global destination
    global distanceLr
    distanceLr = 1
    for y in lr[1:]:
        distanceLr += 1
        if y == destination:
            break
    print(f"route in Lr: {lr[:distanceLr]}")
    

distanceInLn()
distanceInLr()

if distanceLr > distanceLn and distanceLr <= 20 and distanceLn <= 20: 
    print('Prefered route:')
    distanceInLn()
elif distanceLn > distanceLr and distanceLr <= 20 and distanceLn <= 20:
    print('Prefered route:')
    distanceInLr()
elif distanceLr == distanceLn:
    print('Both routes work.')
elif distanceLr <= 20 or distanceLn <= 20:
    print('Error!')
