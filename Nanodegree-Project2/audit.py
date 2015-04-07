#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint


OSMFILE = "montevideo_uruguay.osm"
street_type_re = re.compile(r'\b[A-Z]+[.] |^Pbro|^Sbre|^Actr|^soriano')#, re.IGNORECASE)


expected = []

# UPDATE THIS VARIABLE
mapping = { "A.": " A ","B.":" B ","C.":" C ","D.":" D ","E.":" E "
			,"H.":" H ","J.":" J ","L.":" L ","M.":" M ","P.":" P " 
			,"T.":" T ","V.":" V ","Pbro":"Presbitero","Sbre":"Servidumbre","Actr":"Actriz","soriano":"Soriano"}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types


def update_name(name, mapping):
# As there are two different mappings, one looking at the beginning of names and one looking for abbreviations
# I use two different patterns as substitution string (substring)
    for elem in mapping:
    	substring="^"+elem
    	if len(elem)==2:
    		substring=" "+elem+" "
				
        name=re.sub(substring,mapping[elem],name,re.U)

    return name


def test():
    st_types = audit(OSMFILE)
    #assert len(st_types) == 3
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
       for name in ways:
           better_name = update_name(name, mapping)
           print name, "=>", better_name
           name=better_name



if __name__ == '__main__':
    test()