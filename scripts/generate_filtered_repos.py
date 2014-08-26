#!/usr/bin/env python

from buildfarm.ros_distro import Rosdistro
import argparse


def filter_repos(rd, search_string):
    filtered = {}
    for repo_name in rd.get_repo_list():
        repo = rd.get_repo(repo_name)
        if search_string in repo.url:
            filtered[repo_name] = repo
    return filtered

def parse_options():
    parser = argparse.ArgumentParser(description='Create a set --repos options for creating jobs filtering  the repo url (e.g. to only get repos of one GH organisation.')
    parser.add_argument('--url-filter', default='strands-project',
                        help='the url component filtered for. Default: "strands-project"')
    parser.add_argument('--rosdistro', default='hydro',
                        help='The ros distro. fuerte, groovy, hydro, .... Default="hydro"')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_options()
    rd = Rosdistro(args.rosdistro)
    fr = filter_repos(rd, args.url_filter)
    cmd_options = '--repos'

    for k, v in fr.iteritems():
        cmd_options += ' ' + k
    print cmd_options
