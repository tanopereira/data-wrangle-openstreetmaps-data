import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
        a=ET.iterparse(filename)
        tags={} #create empty tag dictionary
        for item in a:
            tag=item[1].tag
            if tag in tags:
                tags[tag]+=1 #increase count by one if 'tag' already exists
            else:
                tags[tag]=1 #create tag item and initialize to one
        return tags

def test():

    tags = count_tags('montevideo_uruguay.osm')
    pprint.pprint(tags)

if __name__ == "__main__":
    test()