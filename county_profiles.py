import csv


def open_csv(csv_loc, contains_excess=True, transpose=False):
    with open(csv_loc) as c_s_v:
        reader = csv.reader(c_s_v)

        if contains_excess:
            next(reader)

        if transpose:
            return [list(x) for x in zip(*reader)]
        return list(reader)


def main():
    guy = dict()
    for ctr in range(10, 17):
        data = open_csv("data/socioeconomic_" + str(ctr) + ".csv", transpose=False)
        for row in data:
            if row[1] in guy:
                temp = [row[0]]
                temp.extend(tuple(row[2:]))
                for ele in range(len(guy[row[1]])):
                    try:
                        guy[row[1]][ele] += float(temp[ele])
                    except:
                        print(temp[ele])
            else:
                guy[row[1]] = [float(row[0])]
                guy[row[1]].extend([float(i) for i in row[2:]])

        for k in guy:
            key, val = k, guy[k]
            for x in range(len(val)):
                val[x] = round(val[x]/7, 2)
            print(key, " -> ", val)


if __name__ == "__main__":
    main()
