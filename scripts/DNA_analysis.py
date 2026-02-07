#countDNA() 
-Counts the occurences of A,T,G and C in a DNA sequence
-Returns a named tuple with sequence lengths and base counts.

from collections import namedtuple

# Create a named tuple type
DNASummary = namedtuple("DNASummary", ["length", "A", "T", "G", "C"])

def countDNA(DNAstring):
    """
    The function counts the DNA sequence's bases (A,T,G,C) and returns total sequence length.

    Parameters:
        DNAstring (string) : A DNA sequence string.

    Returns:
        DNASummary: A named tuple of DNA length (int) and A,T,G,C (int) nucleotide bases.
    """
    DNAstring = DNAstring.upper() #.upper ensures that any input in lower case will be converted into uppercase
    dna_vector = list(DNAstring) #the input string is converted to vector (separated into a list of bases)
   
    # Calculates length and bases
    length = len(dna_vector)
    A = dna_vector.count("A")
    T = dna_vector.count("T")
    G = dna_vector.count("G")
    C = dna_vector.count("C")

    # Return results as a named tuple DNASummary
    return DNASummary(length, A, T, G, C)

# Example input of a DNA sequence as a string
DNA_seq_string = "TTGGTCATCCTAGACACGCGCCCTACCTGTCAaaATCTAAAATTCATCATACCCTGCGGACGGTGCTTCTGTGCCGAGGcgcAGGCCGATATGTTTCTAC"
result_seq = countDNA(DNA_seq_string)
print(result_seq)

#sub_base()
-Substitutes one nucleotide for another in a DNA sequence. Default: replaces A with T.
-Returns a dictionary containing original and new sequence.

def sub_base(sequence, original_base="A", new_base="T"):
    """
    The function substitutes the input DNA sequence's base for another nucleotide.

    Parameters:
        sequence (str): DNA sequence input as string
        original_base(str): The nucleotide that will be replaced (default A)
        new_base(str): The nucleotide that is to be replaced (default T)

    Returns:
        dict: A dictionary containing original DNA sequence and new sequence with the substitutions
    """
    #.upper ensures that any lowercase inputs will be converted into uppercase
    sequence = sequence.upper()
    original_base = original_base.upper()
    new_base = new_base.upper()
    # Replace all instances of the original base with the new base
    New_Seq = sequence.replace(original_base, new_base)
    
    # Return both sequences in a dictionary
    return {
        "Original_Sequence": sequence,
        "New_Sequence": New_Seq
    }

# Example usage
DNA_seq_string = "TTGGTCATCCTAGACACGCGCCCTACCTGTCAaaATCTAAAATTCATCATACCCTGCGGACGGTGCTTCTGTGCCGAGGcgcAGGCCGATATGTTTCTAC"
new_base_result = sub_base(DNA_seq_string)
print(new_base_result)
