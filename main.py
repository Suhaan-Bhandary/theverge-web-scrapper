from utils.scrapper import get_articles
from utils.csv_handler import create_articles_csv
from utils.database_handler import insert_articles_sqlite


def main():
    # Get the data from website "theverge.com"
    print("Getting Articles...")
    articles = get_articles()

    # Creating CSV file from the data
    print("Creating CSV...")
    create_articles_csv(articles)

    # Creating SQLite Database
    print("Inserting values in Database...")
    insert_articles_sqlite(articles)


if __name__ == "__main__":
    main()
