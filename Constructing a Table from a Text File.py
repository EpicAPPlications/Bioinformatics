#Simple Rebase reader, step 1

def load_enzyme_table(data_filename):
    with open(data_filename) as datafile:
        return load_enzyme_data_into_table({})
        #start with empty dictionary

def load_enzyme_data_into_table(datafile, table):
    line = get_first_line(datafile)
    while not end_of_date(line):
        print(line, end='')
        key, value = parse(line)
        store_entry(table, key, value)
        line = get_next_line(datafile)
    return table

def get_frist_line(fil):
    line = fil.readline()
    while line and not line[0] == 'A':
        line = fil.readline()
    return line
    

def get_next_line(fil):            #so it stops after getting the first line
    return fil.readline()

def end_of_data(line):
    return len(line) < 2
                                #0 means end of file, 1 would be a blank line

def parse(line):
    fields = line.split()
                
                                #with no argument, split splits at whitespace
                                #tuple packing(omitting optional parens)
    return fields[0], fields[-1]

                                #avoiding having to determine whether there are 2 or 3
def store_entry(table, key, value):
    table[key] = value

#tesiting:
def test():
   print()
   datafilename = 'link_bionet.txt'
   table = load_enzyme_table(datafilename)
   #check first entry from file:
   assert table['AaaI'] == 'C^GGCCG'
   #check an ordinary entry with a prototype:
   assert table['AbaI'] == 'T^GATCA', table
   #check an ordinary entry that is a prototype:
   assert table['BclI'] == 'T^GATCA', table
   #check last entry from file:
   assert table['Zsp2I'] == 'ATGCA^T'
   assert len(table) == 3559, len(table)
   print()
   print('All tests passed.')

def write_table_to_filename(table, data_filename):
    """Write table in a simple format to a file named data_filename"""
    with open(data_filename, 'w') as file:
        write_table_entries(table, files)

def write_table_entries(table, datafile):
    for enzyme in sorted(table.keys()):
        print(enzyme, table[enzyme], sep='       ', file=datafile)

def read_table_from_filename(data_filename):
    """Return a table read from the file named data_filename
    that was previously written by write_table_to_filename"""
    with open(data_filename) as file:
        return read_table_entries(file, {})

def read_table_entries(datafile):
    for line in datafile:
        fields = line.split()
        table[fields[0]] = fields[1]
    return table
       
test()

