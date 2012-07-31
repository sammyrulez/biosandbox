import sys, re



def output_fasta_filename(fastq_name):

    return fastq_name + "_viral.out" # occhio che funziona solo se i file stanno tutti nella stessa cartella



def read_line_in_file(fastq):

    line = fastq.readline() #leggi la prima riga

    line = line.strip() #togliamo gli spazi

    return line





def filter_fastaq(fastq_name,queries_name):

    fastq = open(fastq_name, 'r') #apri il file in lettura ('r')



    fasta = open(output_fasta_filename(fastq_name), 'w')  #apri il file di output in scrittura ('w')

    line = read_line_in_file(fastq)

    

    while line != '': #fino a quando la riga non e' vuota

        #print 'Examinig: ' , line

        if line[0] == '@': #la riga comincia per '@'

            line_out = '>'+line

            line = read_line_in_file(fastq)

            queries = open(queries_name, 'r')

            query = read_line_in_file(queries)

            while query !='':

                #print 're ' , query ,' vs ' , line
                query_parts = query.split(' ')
                if re.search(query_parts[1], line, re.I):  # se la riga contiene REpattern

                    fasta.write(query_parts[0] + '\t')

                    fasta.write(line_out + '\t')

                    fasta.write(line + '\n')

                query = read_line_in_file(queries)

            #print 'finished re matching'        

            queries.close()

        line = read_line_in_file(fastq)#leggiamo la riga successiva alla ricerca di una nuovo record e vine  nuovamente valutato il while


    fasta.close() #chiudo il file in output

    fastq.close() #chiudo il file in input







if __name__ == '__main__':

    queries_name = sys.argv[1]

    for fastq_name in sys.argv[2:]: #per ogni parametro passato

        filter_fastaq(fastq_name,queries_name) #chiamo la funzione di filtro