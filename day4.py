f = open("input4", "r").read()

pair_elves = f.split("\n")
print(pair_elves)

def transform_range(read_elve):
    """Returns list [0] =startrange [1] = endrange"""
    elve_work = []
    elverange = read_elve.split("-")
    for i in range (0,100):
        if i < int(elverange[0]) or i > int(elverange[1]):
            elve_work.append(".")
        else:
            elve_work.append(i)
    return  set(filter(lambda filt: filt !=".",elve_work))


def overlap(range1, range2):
   if range1.intersection(range2):
       return 1
   else:
       return 0


def transform_range2(read_elve):
    """Returns list [0] =startrange [1] = endrange. works wiuth overlap2"""
    elve_work = []
    elverange = read_elve.split("-")
    for i in range (0,100):
        if i < int(elverange[0]) or i > int(elverange[1]):
            elve_work.append(".")
        else:
            elve_work.append(i)
    return elve_work


def overlap2(range1, range2):
    """overlap variant 2. works with transform_range2 variant 2"""
    for i in range1:
        for b in range2:
            if i==b and i!=".":
                return 1
    return 0


def read_range(read_elve):
    """Returns list [0] =startrange [1] = endrange"""
    elverange = read_elve.split("-")
    elvestart = int(elverange[0])
    elveend = int(elverange[1])
    elve_range_int=[elvestart, elveend]
    return elve_range_int

def compare_range(range1, range2):
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        print("this is entirly contained by elve numero 1")
        return 1
    elif range2[0] <= range1[0] and range2[1] >= range1[1]:
        print("this is entirly contained by elve numero 2")
        return 1
    else:
        print("maybe lot of work for each")
        return 0





sum_fully_contains = 0
sum_overlap = 0
sum_overlap2 = 0
i=0
for elve in pair_elves:
    elve = elve.split(",")
    elve1_range = read_range(elve[0])
    elve2_range = read_range(elve[1])
    elve1_longrange = transform_range((elve[0]))
    elve2_longrange = transform_range((elve[1]))
    elve1_longrange2 = transform_range((elve[0]))
    elve2_longrange2 = transform_range((elve[1]))
    sum_fully_contains += compare_range(elve1_range, elve2_range)
    sum_overlap += overlap(elve1_longrange, elve2_longrange)
    sum_overlap2 += overlap2(elve1_longrange2, elve2_longrange2)
    print(sum_fully_contains)
    print(sum_overlap)
    print(sum_overlap2)


