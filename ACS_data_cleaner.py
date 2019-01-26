import csv


def col_intersect(csv_loc, transforms, contains_excess=True):
    with open(csv_loc) as c_s_v:
        reader = csv.reader(c_s_v)

        if contains_excess:
            next(reader)
        guy = []
        for row in reader:
            for t in transforms:
                row[1] = row[1].replace(t, "")
            if "Margin of Error" in row[1]:
                pass
            elif "Percent;" in row[1]:
                pass
            elif "Estimate; ANCESTRY" in row[1]:
                guy.append(row[1])
            elif "HOUSEHOLDS BY TYPE" in row[1]:
                guy.append(row[1])
            else:
                guy.append(row[1])

        return guy


def get_intersection(transforms):
    ls = list()
    for ctr in range(10, 17):
        ls.append(col_intersect("2019_MCM-ICM_Problems/2018_MCMProblemC_DATA/ACS_" + str(ctr) + "_5YR_DP02/ACS_" + str(ctr) + "_5YR_DP02_metadata.csv", transforms=transforms))
    cols = list(set.intersection(*map(set, ls)))
    cols = sorted(cols)
    return cols


def clean_csv(csv_loc, headers, transforms, contains_excess=True):
    with open(csv_loc) as c_s_v:
        reader = csv.reader(c_s_v)

        csv_out = list()
        if contains_excess:
            next(reader)
        data = [list(x) for x in zip(*reader)]
        for row in data:
            for t in transforms:
                row[0] = row[0].replace(t, "")
            if row[0] in headers:
                csv_out.append(row)
    return [list(x) for x in zip(*csv_out)]


def main():

    t = [" - Total population",
         " - Total households",
         " - Foreign-born population, excluding population born at sea",
         "Estimate; "
         ]
    cols = get_intersection(t)
    cols.pop(cols.index("EDUCATIONAL ATTAINMENT - Percent high school graduate or higher"))
    cols.pop(cols.index("EDUCATIONAL ATTAINMENT - Percent bachelor's degree or higher"))
    cols.pop(cols.index("DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Total Civilian Noninstitutionalized Population"))
    cols.pop(cols.index("DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Under 18 years"))
    cols.pop(cols.index("DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - 18 to 64 years"))
    cols.pop(cols.index("DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - 65 years and over"))

    for ctr in range(10, 17):
        file = "2019_MCM-ICM_Problems/2018_MCMProblemC_DATA/ACS_" + str(ctr) + "_5YR_DP02/ACS_" + str(ctr) + "_5YR_DP02_with_ann.csv"
        data = clean_csv(file, cols, t)
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] == "(X)":
                    data[x][y] = 0


        with open("data/socioeconomic_" + str(ctr) + ".csv", 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(data)


if __name__ == "__main__":
    main()
