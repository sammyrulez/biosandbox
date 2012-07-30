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