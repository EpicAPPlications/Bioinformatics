#function for recognizing a binding site for a protein
from pprint import pprint as pp

def recognition_site(base_seq, recognition_seq):
    return base_seq.find(recognition_seq)

def validate_base_sequence(base_sequence):
    #seq == base_sequence.upper()
    #return len(seq) == (seq.count('T') + seq.count('C') +
                    #seq.count('A') + seq.count('G'))

def validate_base_sequence1(base_sequence):
    #seq = base_sequence.upper()
    #return len(seq) == \
           #seq.count('A') + seq.count('G') + \
           #seq.count('T') + seq.count('C')

def validate_base_sequence2(base_sequence):
    #"""Return True if the string base_sequence only upper- or lowercase
    #T, C, A, and G characters, otherwise False"""
    #seq = base_seq.upper()
    #return len(seq) == (seq.count('T') + seq.count('C') +
                        #seq.count('A') + seq.count('G'))

def gc_content(base_seq):
    """Return the percentatge of G and C characters in base_seq"""
    seq = base_seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)

def gc_content1(base_seq):
    """Return the percentage of G and C characters in base_seq"""
    assert validate_base_sequence2(base_seq),\
    'argument has invalid characters'
    seq = base_seq.upper()
    return ((base_seq.count('G') + base_seq.count('C')) /
            len(base_seq))

def validate_base_sequence(base_sequence, RNAflag):
    "Return True if the string base_sequence contains only upper- or lowercase T(or U, if RNAflag), C, A, and G characters, otherwise False"""
    seq = base_sequence.upper()
    return len(seq) == (seq.count('U' if RNAflag else 'T') +
                        seq.count('C') +
                        seq.count('A') +
                        seq.count('G'))

from random import randint

def random_base(RNAflag = False):
    return ('UCAG' if RNAflag else 'TCAG')[randint(0, 3)]

def random_codon(RNAflag = False):
    return random_ase(RNAflag) + random_base(RNAflag) + random_base(RNAflag)

def replace_base_randomly_using_names(base_seq):
    """Return a sequence with the base at a randomly selected position of base_seq replaed
    by a base chosen randomly from the three bases that are not at that position"""
    position = randint(0, len(base_seq) - 1)

    base = base_seq[position]
    bases = 'TCAG'
    bases.replace(base, '')         #replaces the base with an empty string
    newbase = bases[randint(0,2)]
    beginning = base_seq[0:position]    #up to position
    end = base_seq[position+1:]         #omitting the base at position
    return beginning + newbase + end

def replace_base_randomly_using_expression(base_seq):
    position = randit(0, len(base_seq) - 1)
    return (base_seq[0:position] +
            'TCAG'.replace(base_seq[position], '')[randit(0, 2)] +
            base_seq[position+1:])

def replace_base_randomly(base_seq):
    position = randint(0, len(base_seq) - 1)
    bases = 'TCAG'.replace(base_seq[position], '')
    return (base_seq[0:position] +
            bases [randint(0,2)] +
            base_seq[position+1:])

DNAbases = set('TCAGtcag')
RNAbases = set('UCAGucag')
def validate_base_sequence(base_sequence, RNAflag = False):
    """Return True if the string base_sequence contains only upper- or lowercase
    T(or U, if RNAflag), C, A, and G characters, otherwise False"""
    return set(base_sequence) <= (RNAbases if RNAflag else DNAbases)

def restriction_cut(base_seq, recognition_seq, offset = 0):
    """Return a pair of sequences derived from base_seq by splitting it at the first appearance
    of recognition_seq; offset, which may be negative, is the number of bases relative to the
    beginning of the site where teh sequence is cut"""
    site = recognition_site(base_seq, recognition_seq)
    return base_seq[:site+offset], base_seq[site+offset:]

RNA_codon_table = {
#                        Second Base
#        U             C             A             G
# U
    'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',     # UxU
    'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',     # UxC
    'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',     # UxA
    'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Urp',     # UxG
# C
    'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',     # CxU
    'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',     # CxC
    'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',     # CxA
    'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',     # CxG
# A
    'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',     # AxU
    'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',     # AxC
    'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',     # AxA
    'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',     # AxG
# G
    'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',     # GxU
    'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',     # GxC
    'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',     # GxA
    'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'      # GxG
}


def translate_RNA_codon(codon):
    return RNA_codon_table[codon]
