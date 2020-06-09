import csv
import os
import sys

DATA_DIR = 'data/'

VOTE_SHARE_FILENAME = 'vote_share_by_county_name.tsv'
A4_ELIGIBILITY_FILENAME = 'eligible-to-vote.tsv'


def compile_county_votes(dem_votes_by_county_neighborhood):


def compile_neighborhood_votes(dem_votes_by_county_neighborhood):


def compile_single_neighborhood_counties(dem_votes_by_county_neighborhood):


def compile_dem_vote_share(dem_vote_share):
    reader = csv.reader(open(dem_vote_share), delimiter='\t')


def a4_eligibility(a4_eligibility_filename):


def create_county_neighborhoods_json(data_dir=DATA_DIR):


if __name__ == '__main__':
