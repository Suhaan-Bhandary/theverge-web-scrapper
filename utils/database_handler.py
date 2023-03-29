import sqlite3


def create_table_if_not_exits(table_name):
    try:
        db = sqlite3.connect("data/database/web_scrapper.sqlite")
        cursor = db.cursor()

        # Since every article has a unique url we use it to reduce duplicates
        sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} ( 
            id VARCHAR PRIMARY KEY,
            url VARCHAR NOT NULL,
            headline VARCHAR NOT NULL,
            author VARCHAR NOT NULL,
            date DATE,
            UNIQUE(url)
        );
        """

        # print(sql)
        cursor.execute(sql)
        db.commit()

        cursor.close()
    except Exception as e:
        print(f"Failed to Create Table {table_name}", e)
    finally:
        if db:
            db.close()


def insert_articles_in_table(articles, table_name):
    record_list = []
    for article in articles:
        record = (article["id"], article["url"],
                  article["headline"], article["author"], article["date"])
        record_list.append(record)

    try:
        db = sqlite3.connect("data/database/web_scrapper.sqlite")
        cursor = db.cursor()

        # Since every article has a unique url we use it to reduce duplicates
        sql = f"""
        INSERT OR IGNORE INTO {table_name}
        (id, url, headline, author, date) 
        VALUES (?, ?, ?, ?, ?);
        """

        # print(sql)
        cursor.executemany(sql, record_list)
        db.commit()
        cursor.close()
    except Exception as e:
        print(f"Failed to insert many records in {table_name}", e)
    finally:
        if db:
            db.close()


def insert_articles_sqlite(articles):
    table_name = "articles"

    # Creating table if not already present in database
    create_table_if_not_exits(table_name)

    # Insert the articles in the database
    insert_articles_in_table(articles, table_name)
