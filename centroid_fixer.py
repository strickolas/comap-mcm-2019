import csv


def open_csv(csv_loc, contains_excess=True):
    with open(csv_loc) as c_s_v:
        reader = csv.reader(c_s_v)
        if contains_excess:
            next(reader)
        d = dict()
        for row in reader:
            row[1] = str(row[1])
            if len(row[1]) == 4:
                row[1] = "0" + row[1]
            d[row[1]] = [str(row[4]), str(row[5])]

        return d


def main():
    data = open_csv("data/county-geocodes.csv", contains_excess=True)
    with open("data/socioeconomic_with_opioid_use.csv") as c_s_v:
        reader = csv.reader(c_s_v)
        df = [["LAT", "LON"] + next(reader)[1:]]
        for row in reader:
            temp = row[1:]
            temp = data[temp[0]] + temp
            df.append(temp)

    with open("data/socioeconomic_with_drugs_and_coords.csv", 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(df)

if __name__ == "__main__":
    main()
