#!/usr/bin/python
#coding=utf-8

tas = ['Peter', 'Andy', 'Sarah', 'Gundega', 'Job', 'Sean']

uppercase_tas = [name.upper() for name in tas]

ta_data = [('Peter', 'USA', 'CS262'),
           ('Andy', 'USA', 'CS212'),
           ('Sarah', 'England', 'CS101'),
           ('Gundega', 'Latvia', 'CS373'),
           ('Job', 'USA', 'CS387'),
           ('Sean', 'USA', 'CS253')]
ta_facts = [name + ' lives in ' + country + ' and is the TA for ' + 
            course for name, country, course in ta_data]
ta_300 = [name + ' is the TA for ' + course for name, country, course
          in ta_data if course.find('CS3') != -1]
#print uppercase_tas
for row in ta_300:
    print row
