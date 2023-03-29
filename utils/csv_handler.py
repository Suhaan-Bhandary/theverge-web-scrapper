from datetime import date
import pandas as pd


def create_articles_csv(articles):
    df = pd.DataFrame(articles)

    filename = f'data/csv_records/{date.today().strftime("%d%m%Y")}_verge.csv'
    df.to_csv(filename, index=False)
