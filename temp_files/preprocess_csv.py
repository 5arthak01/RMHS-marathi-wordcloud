import csv

articles = []

with open("./mt_times/all_mt_times_articles.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter="|")
    count = 0
    for row in spamreader:
        articles.append(row[-1])
        count += 1
        if count > 100:
            break

with open("temp.txt", "a") as f:
    for article in articles:
        f.write(f"{article}\n")
