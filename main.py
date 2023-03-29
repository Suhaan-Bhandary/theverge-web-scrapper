from utils.scrapper import get_articles
from pprint import pprint  # print object in pretty format


def main():
    # Get the data from website "theverge.com"
    articles = get_articles()
    pprint(articles)


if __name__ == "__main__":
    main()
