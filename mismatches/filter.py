import re

__author__ = 'sam'
import itertools

base_reg_exp = 'TCGAN'

def get_mismatch_list(base_query,mismatch_n):
    input_list = list(base_query)
    idxs = itertools.combinations(range(len(input_list)),mismatch_n)
    for idx in idxs:
        str = input_list[:]
        for i in idx:
            str[i]='['+ base_reg_exp.replace(str[i],'') +']'
        yield ''.join(str)



def test_mismatch_list():
    out_l = get_mismatch_list("ACGTNAGAAAN", 3)
    for a in out_l:
        print a

def file_mismatch(data_filename,query_filename,mismatch_n):

    data_file = open(data_filename,'r')
    for r in data_file:
        #print 'r: ' , r
        query_file = open(query_filename,'r')
        for q in query_file:
            #print 'q: ' , q
            for c in get_mismatch_list(q,mismatch_n):
               # print 'c: ' , c
                if re.search(c, r, re.I):
                    print q , ' match ' , r , ' with ' , mismatch_n  ,'mismatches as ' , c
        query_file.close()
    data_file.close()

def test_file_mismatch():
    data_txt = 'mismatches/tests/sample_data.txt'
    queries_txt = 'mismatches/tests/queries.txt'
    for i in range(1,5):
        file_mismatch(data_txt, queries_txt,i)
