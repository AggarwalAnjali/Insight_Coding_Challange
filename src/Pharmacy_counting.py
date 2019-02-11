# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:56:45 2019

@author: Anjali Aggarwal
"""

import sys

input_file, output_file = sys.argv[1:]

drug_cost = dict()
doc_names = dict(set())

n_lines = 0 
with open(input_file, 'rb') as file:
    pharmacy = file.readline()
    while len(pharmacy) > 0:
        pharmacy = pharmacy.decode('utf8')#converting to string
        n_lines += 1
        #spliting into 5 columns
        pharmacy = pharmacy.split(',')

        # checking if there are 5 columns
        if len(pharmacy) != 5:
            print('A row must have 5 columns')
            print(','.join(pharmacy))
            sys.exit(0)
            
        # Doctor full name by joing first and last name
        doctor = ' '.join(pharmacy[1:3])

        
        doc_names[pharmacy[3]].add(doctor)
        drug_cost[pharmacy[3]] += float(pharmacy[-1])
        pharmacy = file.readline()

# output file
with open(output_file, 'wb') as output:
    # columns of the file
    output.write(b'drug_name,num_prescriber,total_cost\n')

    # oderering with drug_cost and drug_name
    for drug, value in sorted(drug_cost.items(), key=lambda x: (x[1], x[0]), reverse=True):
        # descending order
        next_line = ','.join([drug, str(len(doc_names[drug])), str(round(drug_cost[drug], 2))])
        next_line += '\n'
        output.write(bytes(next_line, 'utf8'))


