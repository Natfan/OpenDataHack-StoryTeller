# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Script to download ECMWF weather data

@author: Chris Fairless
adapted from ECMWF template

"""

from ecmwfapi import ECMWFDataServer
import datetime
import string

def get_ECMWF_data(year,month,day,params,):

    # Set up the date variables - add one day to get the range we'd like
    one_day = datetime.timedelta(days=1)
    date_start = datetime.date(year,month,day)
    date_end = date_start + one_day
    date_str = str(date_start) + "/to/" + str(date_end)

    # Set up the strings for the parameters we want
    params_str = string.join(params,"")

    date_start_str = date_start.strftime("%Y-%m-%d")
    out_filename = "./data/ERAInt_"+date_start_str+".nc"

    # Create a server object
    server = ECMWFDataServer()
    
    # Get the data
    server.retrieve({
        "class": "ei",
        "dataset": "interim",
        "date": date_str,
        "expver": "1",
        "grid": "0.75/0.75",
        "levtype": "sfc",
        "param": params_str,
        "step": "0",
        "stream": "oper",
        "time": "00:00:00/06:00:00/12:00:00/18:00:00",
        "type": "an",
        "format": "netcdf",
        "target": out_filename
    })

get_ECMWF_data( 1998, 9, 8, "167.128")