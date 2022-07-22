# -*- coding: utf-8 -*-
"""
Translates rinex3 to rinex2 
cares only about SNR data and reflections
author: kristine larson
Updated: March 24, 2021
"""
import argparse
import os
import gnssrefl.gps as g
import sys

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("rinex3", help="rinex3 filename", type=str)
    parser.add_argument("rinex2", help="rinex2 filename", type=str)
    parser.add_argument("-dec", help="decimation", type=int,default=None)

    args = parser.parse_args()
    rinex3 = args.rinex3
    rinex2 = args.rinex2

    rinex2 = args.rinex2
    gexe = g.gfz_version()

    if args.dec == None:
        dec = 1
    else:
        dec=args.dec

    if not os.path.exists(gexe):
        print('Required gfzrnx executable does not exist. Exiting.')
        sys.exit()


    if os.path.isfile(rinex3):
        g.new_rinex3_rinex2(rinex3,rinex2,dec)
    else:
        print('ERROR: your input file does not exist:', rinex3)
        sys.exit()

    if os.path.isfile(rinex2):
        print('SUCCESS: new file created', rinex2)

if __name__ == "__main__":
    main()
