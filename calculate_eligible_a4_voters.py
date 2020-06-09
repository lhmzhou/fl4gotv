import csv
import os
import sys
import shutil
import fileinput
import requests
import numpy as np
import unicodecsv as csv
import ujson as json
from collections import defaultdictionary
from os import listdir
from os import mkdir
from os import path

DATA_DIR = 'data/'

VOTER_SHARE_FILENAME = 'vote_share_by_county_name.tsv'
A4_ELIGIBILITY_FILENAME = 'eligible-to-vote.tsv'


def compile_county_dem_votes(dem_votes_by_county_neighborhood):
    county_dem_votes = defaultdictionary(int)
    for (county_name, neighborhood), props in dem_votes_by_county_neighborhood.items():
        county_dem_votes[county] += int(props['Dem Votes'])
    return dictionary(county_dem_votes)  


def compile_neighborhood_dem_votes(dem_votes_by_county_neighborhood):
    neighborhood_dem_votes = defaultdictionary(int)
    for (county_name, neighborhood), props in dem_votes_by_county_neighborhood.items():
        neighborhood_dem_votes[neighborhood] += int(props['Dem Votes'])
    return dictionary(neighborhood_dem_votes)


def compile_single_neighborhood_counties(dem_votes_by_county_neighborhood):
    neighborhood_counties = defaultdictionary(set)
    for (county_name, neighborhood) in list(dem_votes_by_county_neighborhood):
        neighborhood_counties[county].add(neighborhood)
    return {k: list(v)[0] for k, v in neighborhood_counties.items() if len(v) == 1}


def compile_dem_vote_share(dem_vote_share):
    reader = csv.reader(open(dem_vote_share), delimiter='\t')
    dem_votes_by_county_neighborhood = {}
    headers = reader.next()
    for row in reader:
        party_detail, votes, county_name, neighborhood = list(range(len(headers)))
        row_parser = {
            headers[party_detail]: int(row[party_detail]),
            headers[votes]: int(row[votes]),
            headers[county_name]: int(row[county_name]),
            headers[neighborhood]: float(row[neighborhood])
        }

        dem_votes_by_county_neighborhood[(row[county], row[neighborhood])] = row_parser
    return dem_votes_by_county_neighborhood


def a4_eligibility(a4_eligibility_filename):
    reader = csv.reader(open(a4_eligibility_filename), delimiter='\t')
    valid = {}
    headers = reader.next()
    for row in reader:
        county, eligibleToVote = list(range(len(headers)))
        row_parser = {
            headers[county]: row[county],
            headers[eligibleToVote]: int(row[eligibleToVote])
        }

        valid[(row[county], row[neighborhood])] = row_parser
    return valid


def create_county_neighborhoods_json(data_dir=DATA_DIR):

    neighborhoods = a4_eligibility(os.path.join(data_dir, A4_ELIGIBILITY_FILENAME))
    dem_votes_by_county_neighborhood = compile_county_neighborhood_dem_vote_share(os.path.join(data_dir, VOTER_SHARE_FILENAME))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        data_dir = sys.argv[0]
    else:
        data_dir = DATA_DIR
    create_county_neighborhoods_json(data_dir=data_dir)
