with open ("input3") as f:
    lines = f.read()
lines = lines.split("\n")


def priority(item: str) -> int:
    o = ord(item)
    if 65 <= o <= 90:
        return o - 38
    if 97 <= o <= 122:
        return o - 96
    raise ValueError(f"Unexpected item: {item}")


def part1(data: list[str]) -> int:

    def compartments(r: str):
        h = len(r) // 2
        return [r[:h], r[h:]]

    def items(r: str):
        print(map(set, compartments(r)))
        print(compartments(r))
        # return map(set, compartments(r))
        return compartments(r)

    def missplaced(r: str):
        # print((*items(r)))
        # print(f"this {set.intersection(*items(r)).pop()}")
        print (f"haha {items(r)}")
        #eine methode es in [{a,b,c},{c,d,e}] zu kriegen
        #hier muss inter in das return anstatt von *test
        inter = []
        newlist1 = set(items(r)[0])
        newlist2 = set(items(r)[1])
        inter.append(newlist1)
        inter.append(newlist2)
        # eine andere methode es in [{a,b,c},{c,d,e}] zu kriegen
        # *test im return gibt die einzelnen eintäge {} wieder
        test = map(set,items(r))
        test2 = map(set, items(r))
        print(f"meinsettt  {test} ")
        resull = list(test2)
        print(newlist2)
        print (f"meinsettt  {test} {resull} ")
        return set.intersection(*test).pop()

    return sum(priority(missplaced(r)) for r in data)


def part2(data: list[str], n: int = 3) -> int:
    def items(group: list[str]):
        return map(set, group)

    def badge(group: list[str]):
        return set.intersection(*items(group)).pop()

    return sum(priority(badge(data[i : i + n])) for i in range(0, len(data), n))


print(part1(lines))
printpart2(lines)