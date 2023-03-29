import requests
from bs4 import BeautifulSoup


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
        heading_anchor = top_story.select_one("h2 > a")
        authors_anchor = top_story.select("div > .inline-block > a")

        authors = list(map(lambda x: x.getText(), authors_anchor))
        author = " and ".join(authors)

        date_selector = "div > .inline-block:last-child > span"
        date = top_story.select_one(date_selector).getText()

        heading = heading_anchor.getText()
        link = "https://www.theverge.com{}".format(heading_anchor["href"])

        articles.append({
            "heading": heading,
            "link": link,
            "author": author,
            "date": date
        })

    return articles
