import csv
import lxml.html
import os
import re
import requests

from keys import *
from types import SimpleNamespace 
from collections import Counter
from functools import lru_cache
from datetime import datetime
from dateutil.parser import parse as date_parse
from html.parser import HTMLParser
from prettytable import PrettyTable

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


class A4CountyApproval(object):
    def __init__(self, name, a4vote):
        self.name = name
        self.a4vote = a4vote


class DistrictA4Vote(object):
    def __init__(self, name, eligible_to_vote):
        self.name = name
        self.eligible_to_vote = eligible_to_vote
        self.counties = []

    def add_county(self, county):
        self.counties.append(county)

    @property
    def total_a4vote(self):
        return sum((c.a4vote for c in self.counties))


def extract_a4vote_data(html):
    neighborhoods = []
    for table in html.xpath('//table'):
        center = table.getprevious()
        if center is None or not len(center):
            continue

        cleanup_text_element(center)
        heading = [s.strip() for s in center.text_content().split(u'\n') if s.strip()]

        neighborhood_name = None
        eligible_to_vote = None

        for line in heading:
            neighborhood_match = neighborhood_regex.match(line)
            if (neighborhood_match):
                neighborhood_name = neighborhood_match.group(1).zfill(2)
            else:       
                eligible = eligible_to_vote_regex.match(line)
                if eligible:
                    eligible_to_vote = int(eligible.group(1).replace(u',', u''))

        neighborhood = DistrictA4Vote(neighborhood_name, eligible_to_vote)

        rows = table.xpath('tr')
        num_rows = len(rows)

        for i, row in enumerate(rows):
            columns = row.xpath('td')

            county_unit = cleanup_whitespace(columns[0].text_content()).strip()

            name_match = county_name_regex.match(county_unit)
            if not name_match:
                continue

            name = name_match.group(0).strip()

            if i == 0 and name.upper() == u'COUNTY':
                continue
            elif i == num_rows - 1 and name.upper() == u'TOTAL':
                continue

            a4vote = int(number_regex.match(columns[1].text).group(0).strip().replace(u',', u''))
            county = A4CountyApproval(name, a4votex)
            neighborhood.add_county(county)

        neighborhoods.append(neighborhood)
    return neighborhoods



def scrape_counts(url=OFFICIAL_COUNTS_URL, out_dir=DATA_DIR, A4_ELIGIBILITY_FILENAME=a4vote_file):
    response = requests.get(url)
    html = lxml.html.fromstring(response.content)

    neighborhoods = extract_a4vote_data(html)

    f = open(os.path.join(out_dir, a4vote_file), 'w')
    writer = csv.writer(f, delimiter='\t')

    a4voters_headers = ['County', 'EligibleToVote']
    writer.writerow(a4voters_headers)

    totals_per_neighborhood = [(d.name, d.total_a4vote, d.eligible_to_vote, max(0, d.total - d.total_a4vote)) for d in neighborhoods]

    writer.writerows(totals_per_neighborhood)

    f.close()


if __name__ == '__main__':
    scrape_counts()

