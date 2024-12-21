def part1(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    totalWrappingPaper = 0
    for line in lines:
        dimensions = line.split("x")
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        squareFeet = 2 * l * w + 2 * w * h + 2 * h * l
        slack = min(l * w, w * h, h * l)
        totalForOnePresent = squareFeet + slack
        totalWrappingPaper += totalForOnePresent

    print("Part 1")
    print("File name:", file)
    print("Total wrapping paper:", totalWrappingPaper)


def part2(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    totalRibbon = 0
    for line in lines:
        dimensions = line.split("x")
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        sortedDimensions = sorted([l, w, h])
        ribbonPerPresent = 2 * sortedDimensions[0] + 2 * sortedDimensions[1]
        bow = l * w * h
        totalRibbon += ribbonPerPresent + bow

    print("Part 2")
    print("File name:", file)
    print("Total ribbon:", totalRibbon)


part1("example.txt")
part1("input.txt")

part2("example.txt")
part2("input.txt")
