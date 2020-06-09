import csv
import lxml.html
import os
import re
import requests

OFFICIAL_COUNTS_URL = 'http://dos.elections.myflorida.com/initiatives/initSignDetailCounty.asp?account=64388&seqnum=1&ctype=CSV&elecyear=2018'
DATA_DIR = 'data'

DEM_VOTE_SHARE_FILENAME = 'vote_share_by_county_name.tsv'
A4_ELIGIBILITY_FILENAME = 'eligible-to-vote.tsv'

county_name_regex = re.compile('^\s*(?:(?:[\w]+[\.]?)(?:[\-][\w]+[\.]?)*\s*)+')
date_regex = re.compile('\(\s*as of ([\d]{2}/\d{2}/\d{4})\s*\)', re.I)

html_whitespace_regex = re.compile('(?:\s+|(?:&nbsp;)+)')
number_regex = re.compile('[\d,]+')

neighborhood_regex = re.compile('NEIGHBORHOOD\s*([\d]+)', re.I)
eligible_to_vote_regex = re.compile(' Eligible To Vote\s*([\d,]+)', re.I)


def cleanup_whitespace(text):
    return html_whitespace_regex.sub(u' ', text).strip()


def cleanup_text_element(tree):
    for element in tree:
        if element.tag == 'br':
            element.tail = u'\n' + element.tail
            element.drop_tree()
        else:
            element.text = cleanup_whitespace(element.text)


def extract_a4vote_data(html):
    neighborhoods = []
    for table in html.xpath('//table'):
        center = table.getprevious()
        if center is None or not len(center):
            continue

        cleanup_text_element(center)
        heading = [s.strip() for s in center.text_content().split(u'\n') if s.strip()]

    return neighborhoods


def scrape_counts(url=OFFICIAL_COUNTS_URL, out_dir=DATA_DIR, A4_ELIGIBILITY_FILENAME=a4vote_file):
    

if __name__ == '__main__':


