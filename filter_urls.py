urls = []
with open("urls.txt", "r") as f:
    urls = f.readlines()

filtered_urls = set(urls)

with open("filtered_urls.txt", "a") as f:
    for url in filtered_urls:
        f.write(url)
