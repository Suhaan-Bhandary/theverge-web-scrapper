import uuid
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date


def get_formatted_date(date_string):
    # The function is used to take date and return formatted date
    parts_count = len(date_string.split(" "))
    if parts_count == 2:
        current_year = datetime.now().year
        date_object = datetime.strptime(
            f"{date_string} {current_year}", "%b %d %Y")
        return date_object.strftime("%Y/%m/%d")
    else:
        return date.today().strftime("%Y/%m/%d")


def get_articles():
    # !For now only top articles are fetched
    url = "https://www.theverge.com"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    top_stories_container = soup.find(
        "h2", string="Top Stories").find_next_sibling()

    main_content_selector = "li > div:nth-of-type(2) > div:nth-of-type(2) > div"
    top_stories_list = top_stories_container.select(main_content_selector)

    articles = []
    for top_story in top_stories_list:
        headline_anchor = top_story.select_one("h2 > a")
        authors_anchor = top_story.select("div > .inline-block > a")

        authors = list(map(lambda x: x.getText(), authors_anchor))
        author = " and ".join(authors)

        date_selector = "div > .inline-block:last-child > span"
        date_string = top_story.select_one(date_selector).getText()

        headline = headline_anchor.getText()
        url = "https://www.theverge.com{}".format(headline_anchor["href"])

        articles.append({
            "id": str(uuid.uuid4()),
            "headline": headline,
            "url": url,
            "author": author,
            "date": get_formatted_date(date_string)
        })

    return articles
