import math


def main(lines):
    directions = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}
    head = {90: (1, 0), 0: (0, 1), 270: (-1, 0), 180: (0, -1)}
    rotate = {"L": -1, "R": 1}
    s = "NESW"

    def part2(lines):
        x, y = 0, 0
        wx, wy = 10, 1
        f = 1
        for line in lines:
            d = line[0]
            k = int(line[1:])

            if d in directions:
                dx, dy = directions[d]
                wx += k * dx
                wy += k * dy
            else:
                dc = k // 90
                dc %= 4
                if d == "L":
                    dc = 4 - dc
                if d in "LR":
                    for _ in range(dc):
                        wx, wy = wy, -wx
                else:
                    print("moving", s[f], directions[s[f]])
                    x += k * wx
                    y += k * wy
        print("Part #2", abs(x) + abs(y))

    def part1(lines):
        x, y = 0, 0
        h = 90

        for line in lines:
            command = line[0]
            amt = int(line[1:])
            if command in directions:
                dx, dy = directions[command]
                x += amt * dx
                y += amt * dy
                # print(command,amt,dx,dy,x,y)

                continue
            else:
                if command in rotate:
                    h = h + (amt * rotate[command])
                    print(h)
                    h %= 360
                    print("Heading %s" % h, command, amt)
                else:
                    dx, dy = head[h]
                    x += amt * dx
                    y += amt * dy
        print("Part #1", abs(x) + abs(y))

    part2(lines)
    part1(lines)


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    main(lines)
