"""
adTCell_model.py

A Python class modeling a T-cell extending a generic Cell class.
Includes methods to add organelles, genes, proteins, and grow the cell conditionally.

"""

class Cell:
    """ A class representing a cell"""
    
    # Constructor 
    def __init__(self, name):
        """Input layer"""
        self.name = name
        self.organelles = []    # creates a new empty list for each cell
        self.genes = []         # same as above
    
    # The string method
    def __str__(self):
        return ("A model of a cell, current instance is {} ".format(self.name))
    
    # Methods
    def add_organelle(self, organelle):
        self.organelles.append(organelle)
    
    def add_gene(self, gene):
        self.genes.append(gene)
        
    def view_cell(self):
        return self.organelles, self.genes
      
class adTCell(Cell):
    """A class extending the Cell class from above"""

    #Constructor
    def __init__(self, name, size): 
        Cell.__init__(self, name) #Includes the parameters and the methods from Cell class that will be inherited in the adTCell subclass 
        #New attributes added
        self.size = size #The input size defines the self.size
        self.max_rate = 0.5 #set default max_rate as 0.5
        self.protein = []  # An empty protein list

    def __str__(self):
        return f"A model of a T-cell named {self.name}, size {self.size}" #extending the Cell class' string method
    
    #Methods
    def add_protein(self, protein_name): 
        #Adds protein into a list
        """.append adds protein to the self.protein attribute"""
        self.protein.append(protein_name)

    def summary(self):
        """Prints the total number of organelles, genes, and proteins"""
        print (
            f"Total Organelles: {len(self.organelles)}, "
            f"Total Genes: {len(self.genes)}, "
            f"Total Proteins: {len(self.protein)} "
            )

    def grow(self, growth_rate):
        """A conditional function, where the self.size attribute increases by input growth_rate if growth_rate less than the self.max_rate. 
        This is the new growth_rate value. If growth_rate exceeds self.max_rate, it shows an error message prompting user to input a 
        different value."""
        if growth_rate <= self.max_rate:
            initial_size = self.size
            self.size = self.size + growth_rate
            print(f"Growth rate increased the size from {initial_size} to {self.size}")
        else:
            print(f"Invalid. The growth rate {growth_rate} exceeds max rate {self.max_rate}. Please try again!")

if __name__ == "__main__":
    # Example usage
    T_Cell = adTCell("Cytotoxic T-cell", 1) 

    # Add organelles
    T_Cell.add_organelle("Endoplasmic Reticulum")
    T_Cell.add_organelle("Nucleus")
    T_Cell.add_organelle("Ribosome")

    # Add genes
    T_Cell.add_gene("AKT1")
    T_Cell.add_gene("MAP2K1")

    # Add proteins
    T_Cell.add_protein("CD3")
    T_Cell.add_protein("MAF")
    T_Cell.add_protein("FOXP3")

    print(T_Cell)
    T_Cell.summary()
    T_Cell.grow(0.5)  # Will trigger error if > max_rate
