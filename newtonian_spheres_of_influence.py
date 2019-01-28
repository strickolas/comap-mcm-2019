import csv
from math import radians, sin, asin, cos, sqrt


def haversine(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c, r = 2 * asin(sqrt(a)), 3956
    dist = c * r
    return dist


def get_influence_value(state, col):
    with open("data/socioeconomic_with_drugs_and_coords.csv") as c_s_v:
        reader = csv.reader(c_s_v)
        ls, d = [], {}
        for row in reader:
            if row[3] == state:
                ls.append(row)
        for x in range(len(ls) - 1):
            summ, county = 0, ls[x]
            lat1, lon1 = county[0], county[1]
            for y in range(1, len(ls)):
                focus = ls[y]
                lat2, lon2 = focus[0], focus[1]
                dist = haversine(float(lat1), float(lon1), float(lat2), float(lon2))
                if dist != 0.0:
                    names = sorted([focus[4], county[4]])
                    key = names[0] + " <-> " + names[1]
                    val = (float(focus[col]) * float(county[col])) / dist
                    d[key] = summ + val

    return dict(sorted(d.items(), key=lambda kv: kv[1]))


def main():
    # states = ["KY", "PA", "WV", "VA", "OH"]
    states = ["PA"]
    for state in states:
        d = get_influence_value(state, 14)
        for x in d:
            print(x, "->", d[x])
    print(len(d))


if __name__ == "__main__":
    main()
