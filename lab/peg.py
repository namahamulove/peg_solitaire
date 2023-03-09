import re

def getsolution(qnum):
    all = []
    reall =[]
    index = []
    solution = []
    solution2 = []
    solutions = []
    solutions2 = []

    with open("data/clear{}.xtr".format(qnum), mode="r") as f:
        txt = f.read()
        txt = txt.splitlines()

    with open("data/make.txt", mode="w") as f:
        for i in txt:
            f.write(i) if i != "." else f.write("\n")

    with open("data/sol{}.txt".format(qnum), mode="w") as f:
        with open ("data/make.txt", mode="r") as u:
            txt2 = u.readlines()

        for i in txt2:
            t = re.findall("[0-2]{81}", i)
            if t != []:
                all.append(t)

        for i in all:
            for j in i:
                reall.append(j)

        for i in reall:
            solution = []
            for j in range(9):
                solution.append(i[0+9*j:9+9*j])
            solutions.append(solution)

        for i in solutions:
            for j in i:
                for k in j:
                    f.write(str(k))
                    index.append(int(k))
                f.write("\n")
                solution2.append(index)
                index = []
            f.write("\n")
            solutions2.append(solution2)
            solution2 = []

    return solutions2