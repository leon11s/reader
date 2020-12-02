import feedparser
import html2text

from reader import URL

_CACHED_FFEDS = dict()


def _feed(url=URL):
    if url not in _CACHED_FFEDS:
        _CACHED_FFEDS[url] = feedparser.parse(url)
    return _CACHED_FFEDS[url]


def get_site(url=URL):
    info = _feed(url).feed
    return f"{info.title} ({info.link})"


def get_titles(url=URL):
    """List titles in feed"""
    articles = _feed(url).entries
    return [a.title for a in articles]


def get_article(article_id, url=URL):
    """Get article from feed with the given ID"""
    articles = _feed(url).entries
    article = articles[int(article_id)]
    html = article.content[0].value
    text = html2text.html2text(html)
    return f"# {article.title}\n\n{text}"
