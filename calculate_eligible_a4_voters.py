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


def compile_dem_vote_share(dem_vote_share):
    reader = csv.reader(open(dem_vote_share), delimiter='\t')


def a4_eligibility(a4_eligibility_filename):
    reader = csv.reader(open(a4_eligibility_filename), delimiter='\t')
    

def create_county_neighborhoods_json(data_dir=DATA_DIR):

    
if __name__ == '__main__':
    data_dir = DATA_DIR
    create_county_neighborhoods_json(data_dir=data_dir)
