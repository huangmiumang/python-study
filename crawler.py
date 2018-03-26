#!~/.jumbo/bin/python
#coding=utf-8
import urllib

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ''

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url, end_pos = get_next_target(page)
        if url:
            links.append(url)
            page=page[end_pos:]
        else:
            break
    return links

def crawl_wed(seed):
    to_crawl = [seed]
    crawled = []
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled:
            union(to_crawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

crawl_wed('https://xkcd.com/353/')
