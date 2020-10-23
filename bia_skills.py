#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:26:45 2020

@author: junior
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/home/junior/Documents/bia_skills_proj/chromedriver"

df = gs.get_jobs('business-intelligence-analyst-jobs', 500, False, path, 15)

