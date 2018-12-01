#one-alternative conditional
if __name__ == '_main_':
    do_tests()
else:
    print(__name__, 'has been imported.')
    
def aa_generator(rnaseq):
    """Return a generator object that produces an amino acid by translating
    the next three characters of rnaseq each time next is called on it"""
    return (translate_RNA_codon(rnaseq[n:n+3])
            for n in range(0, len(rnaseq), 3))

#loops
def echo():
    """Echo the user's input until an empty line is entered"""
    while echo1():
        pass

def echo1():
    "Prompt the user for a string, 'echo' it, and return it"""
    line = input('Say something: ')
    print('You said', line)
    return line

def polite_echo():
    """Echo the user's input until it equls 'bye'"""
    while echo1() != 'bye':
        pass

def recording_echo():
    """Echo the user's input until it equals 'bye', then return a list of all the inputs received"""
    #initialize entry and lst
    lst = []

    #get the first input
    entry = echo1()

    #test entry
    while entry != 'bye':

        #use entry
        lst.append(entry)

        #change entry
        entry = echo1()

        #repeat

    #return result    
    return lst

def recording_echo_with_conditional():
    """Echo the user's input until it equals 'bye', then return a list of all the inputs received"""
    seq = []
    #no need to initialize a value to be tested since nothing is tested!
    while True:
        entry = echo1()
        if entry == 'bye':
            return seq
        seq.append(entry)
  
def aa_generator(rnaseq):
    """Return a generator object that produces an amino acid by translating
    the next three characters of rnasqe each time next is called on it"""
    return (translate_RNA_codon(rnaseq[n:n+3])
            for n in range(0, len(rnaseq), 3))

def translate(rnaseq):
    """Translate rnaseq into amino acid symbols"""
    gen = aa_generator(rnaseq)
    seq = ''
    aa = next(gen, None)
    while aa:
        seq += aa
        aa = next(gen, None)
    return seq

def read_sequence(filename):
    """Given the name of a FASTA file named filename, read and return
    irs first sequence, ignoring the sequence's description"""
    seq = ''
    with open(filename) as file:
        line = file.readline()
        while line and line[0] == '>':
            line = file.readline()
        while line and line[0] != '>':
            seq += line
            line = file.readline()
    return seq

def read_FASTA_iteration(filename):
    sequences = []
    descr = None
    with open(filename) as file:
        if line[0] == '>':
            if descr:
                sequences.append((descr, seq))
            descr = line[1:-1].split('|')
            seq = ''
        else:
            seq += line[:-1]
        sequences.append ((descr, seq))
    return sequences

def read_FASTA(filename):
    with open(filename) as file:
        return[(part[0].split('|'),
                part[2].replace('\n', ''))
               for part in
               [entry.partition('\n')
                for entry in file.read().split('>')[1:]]]

def read_FASTA_loop(filename):
    sequences = []
    descr = None
    with open(filename) as file:
        line = file.readline()[:-1]
        while line:
            if line[0] == '>':
                if descr:
                    sequences.append((descr, seq))
                descr = line[1:].split('|')
                seq = ''
            else:
                seq += line
            line = file.readline()[:-1]
        sequences.append((descr, seq))
    return sequences

def product(coll):
    """Return the product of the elements of coll converted to floats, including
    elements that are string representations of numbers; if coll has an element
    that is a string but doesn't represent a number, an error will occur"""
    result = 1.0
    for elt in coll:
        result *= float(elt)
    return result

#combine:identifying the longest FASTA sequence

def longest_sequence(filename):
    longest_seq = ''
    for info, seq in read_FASTA(filename):
        longest_seq = max(longest_seq, seq, key=len)
    return longest_seq

def extract_gi_id(description):
    """Given a FASTA file description line, return its GenInfo ID if it has one"""
    if line[0] != '>':
        return None
    fields = description[1:].split('|')
    if 'gi' not in fields:
        return None
    return fields[1 + fields.index('gi')]

def get_gi_ids(filename):
    """Return a list of the GenInfo IDs of all sequences found in the file named filename"""
    with open(filename) as file:
        return [extract_gi_id(line) for line in file if line[0] == '>']

    def get_gi_ids_from_files(filenames):
        """Return a list of the GenInfo IDS of all sequences found in the file name filename"""
        with open(filename) as file:
            return [extract_gi_id(line) for line in file if line[0] == '>']

def get_gi_ids_from_files(filenames):
    """Return a list of the GenInfo IDs of all sequences found in the
    files whose names are contained in the collection filenames"""
    idlst = []
    for filename in filenames:
        idlst += get_gi_ids(filename)
    return idlst

def search_FASTA_file_by_gi_id(id, filename):
    """Return the sequence with the GenInfo ID ID from the FASTA file
    named filename, reading one entry at a time until it is found"""
    id = str(id)
    with open(filename) as file:
        return FASTA_search_by_gi_id(id, file)

def rna_sequence_is_valid(seq):
    for base in seq:
        if base not in 'UCAGucag':
            return False
        return True

def dna_sequence_contains_N(seq):
    for base in seq:
        if base == 'N':
            return True

def print_FASTA_headers(filename):      #with open(filename) as file:
    for line in file:
        if line[0] == '>':
            print(line[1:-1])

#def extract_matching_sequencseq = (filename, string):
    """From a FASTA file named filename, extract all sequences whose descriptions contain string"""
    sequences = []
    seq = ''
    with open(filename) as file:
        for line in file:
            if line[0] == '>':
                if seq:                         #not first time through
                    sequences.append(seq)
                seq = ''            #next sequence detected
                includeflag = string in line    #flag for later iterations
            else:
                if includeflag:
                    seq += line[:-1]
        if seq:
            sequences.append(seq)
    return sequences

def is_number(value):
    """Return True if value is an int or a float"""
    return isinstance(elt, int) or isinstance(elt, float)

def product(coll):
    """Return the product of the numeric elements of coll"""
    result = 1.0
    for elt in coll:
        if is_number(elt):
            result = result * float(elt)
    return result

#generalized combine function

def combine(coll, initval, action, filter=None):
    """Starting at initval, perform action on each element of coll, finally returing the result. If
    filter is not None, only include elements for which filter(element) is true. action is a function
    of two arguements--the interim result and the element--which returns a new interim result."""
    result = initval
    for elt in coll:
        if not filter or filter(elt):
            result = action(result, elt)
    return result

#nested iteration
def list_sequences_in_files(filelist):
    """For each file whose name is contained in fileist,
    list the description of each sequence it contains"""
    for filename in filelist:
        print(filename)
        with open(filename) as file:
            for line in file:
                if line[0] == '>':
                    print('\t', line[1:-1])

def list_sequences_in_files1(filelist):
    """For each file whose name is contained in filelist,
    list the description of each sequence it contains"""
    for filename in filelist:
        print(filename)
        with open(filename) as file:
            list_sequences_in_file(file)

def list_sequences_in_file(file):
    for line in file:
        if line[0] == '>':
            print('\t', line[1:-1])

#use of nested iterations for codons because they have 3 bases

def print_codon_table():
    """Print the DNA codon table in a nice, but simple, arrangement"""
    for base1 in DNA_bases:                                 #horizontal section (or "group")
        for base3 in DNA_bases:                            #line (or "row")
            for base2 in DNA_bases:                         #vertical section (or "column")
                #the base2 loop is inside the base3 loop!
                print(base1+base2+base3,
                      translate_DNA_codon(base1+base2+base3),
                      end= '  ')
            print()
        print() 

#collecting GenInfo IDs of the sequences in FASTA files

def extract_gi_id(description):
    """Given a FASTA file description line, return its GenInfo ID if it has one"""
    if line[0] != '>':
        return None
    fields = description[1:].split('|')
    if 'gi' not in fields:
        return None
    return fields[1 + fields.index('gi')]

def get_gi_ids(filename):
    """Return a list of GenInfo IDs from the sequences in the FASTA file named filename"""
    with open(filename) as file:
        return [extract_gi_id(line) for line in file if line[0] == '>']

def get_gi_ids_from_files(filenames):
    """Return a list of GenInfo IDs from the sequences in the
    FASTA files whose names are in the collection filenames"""
    idlst = []
    for filename in filenames:
        idlst += get_gi_ids(filename)
    return idlst

def get_gi_ids_from_user_files():
    response = input("Enter FASTA file names, separated by spaces: ")
    lst = get_gi_ids_from_files(response.split())
    lst.sort()
    print(lst)

def get_gi_ids(filename):
    try:
        with open(filename) as file:
            return [extract_gi_id(line) for line in file
                                        if line[0] == '>']
    except IOError:
        print('File', filename, 'not found or not readable.')
        return []

def get_field(contents, pattern, endpos):
    endpos = contents.rfind(pattern, 0, endpos)
    if endpos < 0:
        raise StopIteration
    startpos = contents.rfind('>', 0, endpos)
    return (endpos, contents[startpos+1:endpos])

def get_next(contents, endpos):
    fields = []
    for pattern in patterns:
        endpos, field = get_field(contents, pattern, endpos)
        fields.append(field)
    fields.reverse()
    return endpos, fields

def get_gene_info(contents):
    lst = []
    endpos = contents.rfined(endresults, 0, len(contents))
    try:
        while(True):
            endpos, fields = get_next(contents, endpos)
            lst.append(fields)
    except StopIteration:
        pass
    lst.reverse()
    return lst

def get_gene_info_from_file(filename):
    with open(filename) as file:
        contents = file.read()
    return get_gene_info(contents)

def show_gene_info_from_file(filename):
    infolst = get_gene_info_file(filename)
    for info in infolst:
        print(info[0], info[1], info[2], sep='\n    ')

if __name__ == ' __main__':
    show_gene_info_from_file(sys.argv[1]
                             if len(sys.argv) > 1
                             else 'EntrezGeneResults.html')
    
def get_items_from_file(filename, testfn=None):
    """Return all the items in the file named filename; if testfn
    then include only those items for which testfn is true"""
    with open(filename) as file:
        return get_items(file, testfn)

def find_item_in_file(filename, testfn=None):
    """Return the first item in the file named filename; if testfn
    then return the first item for which testfn is true"""
    with open(filename) as file:
        return find_item(file, testfn)

def find_item(src, testfn):
    """Return the first item in src; if testfn then return the first item for which testfn is true"""
    gen = item_generator(src, testfn)
    item = next(gen)
    if not testfn:
        return item
    else:
        try:
            while not testfn(item):
                item = next(gen)
            return item
        except StopIteration:
            return None

def get_items(src, testfn=None):
    """Return all the items in src; if testfn then include
    only those items for which testfn is true"""
    return [item for item in item_generator(src)

def item_generator(src):
    """Return a generator that produces a FASTA sequence from src each time it is called"""
    skip_intro(src)
    seq = ''
    description = src.readline().split('|')
    line = src.readline()
    while line:
        while line and line[0] != '>':
            seq += line
            line = src.readline()
        yield (description, seq)
        seq = ''
        description = line.split('|')
        line = src.readline()

def item_generator(src):
    """Return a generator that produces a FASTA sequence from src each time it is called"""
    skip_intro(src)
    seq = ''
    description = src.readline().split('|')
    line = src.readline()
    while line:
        while line and line[0] != '>':
            seq += line
            line = src.readline()
        yield (description, seq)
        seq = ''
        description = line.split('|')
        line = src.readline()

def skip_intro(src):
    """Skip introductory text that appears in src before the first item"""
    pass
            
def get_GenBank_items_and_sequence_from_file(filename):
    with open(filename) as file:
        return [get_ids(file), get_items(file), get_sequence(file)]

def get_ids(src):
    line = src.readline()
    while not line.startswith('VERSION'):
        line = src.readline()
    parts = line.split()
    assert 3 == len(parts), parts
    giparts = parts[2].partition(':')
    assert giparts[2], giparts
    assert giparts[2].isdigit()
    return (parts[1], giparts[2])

def get_ids(src):
    line = src.readline()
    while not line.startswith('VERSION'):
        line = src.readline()
    parts = line.split()
    assert 3 == len(parts), parts
    giparts = parts[2].partition(':')
    assert giparts[2], giparts
    assert giparts[2].isdigit()
    return (parts[1], giparts[2])
            
