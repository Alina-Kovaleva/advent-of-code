def part1(file):
    try:
        with open(file, "r", encoding="utf-8") as file:
            line = file.readlines()
            floor = 0
            for char in line[0]:
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1

            print("Part 1")
            print("File name:", file.name)
            print("Floor:", floor)
    except FileNotFoundError:
        print(f"File not found: {file}")
    except Exception as e:
        print(f"An error occurred: {e}")


def part2(file):
    try:
        with open(file, "r", encoding="utf-8") as file:
            line = file.readlines()
            floor = 0
            position = 0
            for char in line[0]:
                position += 1
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1
                if floor == -1:
                    print("Part 2")
                    print("File name:", file.name)
                    print("Position:", position)
                    break
    except FileNotFoundError:
        print(f"File not found: {file}")
    except Exception as e:
        print(f"An error occurred: {e}")


part1("example.txt")
part1("input.txt")

part2("example.txt")
part2("input.txt")
