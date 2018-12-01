def validiate_base_sequence(base_sequence, RNAflag = False):
    valid_bases = 'UCAG' if RNAflag else 'TCAG'
    return all([(base in valid_bases)
                for base in base_sequence.upper()])

from random import randint

def random_base(RNAflag = False):
    return('UCAG' if RNAflag else 'TCAG')[randint(0, 3)]

def random_codon(RNAflag = False):
    return random_base(RNAflag) + random_base(RNAflag) + random_base(RNAflag)

def random_codons(minlength = 3, maxlength = 10, RNAflag = False):
    """Generate a random list of codons(RNA if RNAflag, else DNA)
    between minlength and maxlength,inclusive"""
    return [random_codon(RNAflag)
            for n in range(randint(minlength, maxlength))]

def random_codons_translation(minlength = 3, maxlength = 10):
    """Generate a random list of codons between minlength and maxlength, inclusive"""
    return [translate_RNA_codon(codon) for codon in random_codons(minlength, maxlength, True)]

