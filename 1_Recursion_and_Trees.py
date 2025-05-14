#----------------- Recursion and Tree's ------------------------#


# -------Recursion--------

# code which call itself
# Useful for code with tree like structures


## -----Initial example-----: Recusively generating kmers


# ---Question: if we pick a small number for kmer like 3
# Then: can we write a series of nested for loops to generate all possible sequences?

bases = ['A', 'T', 'C', 'G']

result = []
for base1 in bases:
    for base2 in bases:
        for base3 in bases:
            result.append(base1 + base2 + base3)
print(result)

# ---Problem: A function capable of searching for any k length would be tough with this method
# Here: One possible solution

def generate_kmers(length):
    result = [""]
    for i in range(length):
        new_result = []
        for kmer in result:
            for base in ['A', 'T', 'G', 'C']:
                new_result.append(kmer + base)
        result = new_result
    return result

# ---Explanation:

# Start with a list containing an empty string - for the final sequences
# Then we extend each element in that list in an iterative process
#   - Controlled using a for loop and range
# The result string holds the result after each loop through
# The new results is reinitialized as empty at the start of every loop
# The new_result grabs each result and adds each of the bases to them
# Then it sends the results back to the results list


# ---Idea: Equivalent of nesting code an arbitrary amount of times

generate_kmers(5)  # Success


# ---Another method

def generate_kmers_rec(length):
    if length == 1:
        return ['A', 'T', 'G', 'C']
    else:
        result = []
        for seq in generate_kmers_rec(length - 1):
            for base in ['A', 'T', 'G', 'C']:
                result.append(seq + base)
        return result

generate_kmers_rec(5)

# This is a recursive function because it calls upon itself!

# ---EXPLANATION (think of it like a story):
# 1) Check if length is 1:
#    - If it is, just return the four basic DNA letters.
# 2) If length is greater than 1:
#    - First, call this same function with length-1 to get all shorter k-mers.
#      If length-1 is still not 1, that call will itself make another call with
#      length-2, and so on, until we eventually reach the base case (length=1).
#    - For each of those shorter k-mers, add each base (A, T, G, C) to the end,
#      to build up the list of k-mers at the current length.
# 3) Return the complete list of k-mers of the requested length.
#
# ---WHAT I DIDNT UNDERSTAND:
# 1) When we hit the "for seq in generate_kmers_rec(length - 1):"
#    - The function pauses here and restarts from the top
# 2) The function calls itself down to 1
#    - then feeds that information back up to whichever instance called it
# 3) Each funcion called for different lengths have different results = [] lists
#    - generate_kmers_rec(3) is different from generate_kmers_rec(2)
#    - Python can have the same names because of their scoping rules


# ------- Processing Tree-like data -------


# ---Child-to-parent trees vs parent-to-child

# EXAMPLE: Homo sapiens in a child-to-parent way
#   - Dictionary

tax_dict = {
    'Homo Sapines' : 'Homo',
    'Homo' : 'Hominae'
}

# Different for parent-to-child relationships
#   - List

primates_children = ['Haplorrhini', 'Strepsirrhini']

# PROBLEM: Less satisfying to work with, and worse when needing to add info
#   - Would need to create new variables

homo_children = ['Homo sapiens', 'Homo neanderthalensis']

# whereas dictionaries can always be added to

# PROBLEM: Even dictionaries can be hard to read
# EXAMPLE

tax_dict = {
    'Pongo abelii': 'Hominidae',
    'Pan troglodytes': 'Hominidae',
    'Hominidae': 'Simiiformes',
    'Simiiformes': 'Haplorhini',
    'Tarsius tarsier': 'Tarsiiformes',
    'Tarsiiformes': 'Haplorhini',
    'Haplorhini': 'Primates',
    'Loris tardigradus': 'Lorisidae',
    'Lorisidae': 'Strepsirrhini',
    'Allocebus trichotis': 'Lemuriformes',
    'Lemuriformes': 'Strepsirrhini',
    'Strepsirrhini': 'Primates',
    'Galago allenii': 'Lorisiformes',
    'Galago moholi': 'Lorisiformes',
    'Lorisiformes': 'Strepsirrhini'
}

# TASK: write a function that will list the parents of a given taxon
#   - Input being the name of a taxon


# SIMPLEST ITERATIVE METHOD WE'VE LEARNT
def get_parent(taxon):
    first_parent = tax_dict.get(taxon)
    second_parent = tax_dict.get(first_parent)
    third_parent = tax_dict.get(second_parent)
    return[first_parent, second_parent, third_parent]

get_parent("Pongo abelii")

# PROBLEM: Requires us to know the maximum numbers of ancestors in advance

# ADVANCED INTERATIVE METHOD FROM FIRST BOOK
def get_ancestors(taxon):
    result = [taxon]
    while taxon != 'Primates':
        result.append(tax_dict.get(taxon))
        taxon = tax_dict.get(taxon)
    return result

get_ancestors("Pongo abelii")

# NEW ADVANCED RECURSIVE METHOD

def get_ancestors_rec(taxon):
    if taxon == 'Primates':
        return [taxon]
    else:
        parent = tax_dict.get(taxon)
        parent_ancestor = get_ancestors_rec(parent)
        return [parent] + parent_ancestor

get_ancestors_rec("Pongo abelii")

# PROBLEM: This ran too many times without an ends
#   - Adding in print statements to troubleshoot

def get_ancestors_rec(taxon):
    print('Getting the ancestor for ' + taxon)
    if taxon == 'Primates':
        print('taxon is primates, returning an empty list')
        return []
    else:
        print('taxon is not primates, looking up the parent')
        parent = tax_dict.get(taxon)
        print('The parent is ' + parent)
        print('looking up ancestors for ' + parent)
        parent_ancestor = get_ancestors_rec(parent)
        print('parent ancestors are ' + str(parent_ancestor))
        result = [parent] + parent_ancestor
        print('About to return the result: ' + str(result))
        return result

get_ancestors_rec("Galago allenii")

# This worked, the issue was I didn't have primates capitalized
#   - Thus it wasn't showing up as being on the dictionary
#   - Parent is a dictionary key thus already a string
#   - Parents is a list which is why we must str(parent_ancestors)


# CONCEPT: Adding indents to recursive functions allow indication to cycles

def get_ancestors_rec(taxon, depth):
    spacer = ' ' * depth
    print(spacer + 'Getting the ancestor for ' + taxon)
    if taxon == 'Primates':
        print(spacer + 'taxon is primates, returning an empty list')
        return []
    else:
        print(spacer + 'taxon is not primates, looking up the parent')
        parent = tax_dict.get(taxon)
        print(spacer + 'The parent is ' + parent)
        print(spacer + 'looking up ancestors for ' + parent)
        parent_ancestor = get_ancestors_rec(parent, depth + 4)
        print(spacer + 'parent ancestors are ' + str(parent_ancestor))
        result = [parent] + parent_ancestor
        print(spacer + 'About to return the result: ' + str(result))
        return result

get_ancestors_rec("Galago allenii", 0)

# Looks much clearer


# ---Parent to child trees

# QUESTION: why can we not store parent-to-child data in dicts
#   - because keys in a dictionary need to be unique!
#   - Parents often have multiple children

# SOLUTION: key is parent taxon, value is list of children

tax_dict = {
    'Strepsirrhini' : ['Lorisdae', 'Lemuriformes', 'Lorisformes']
}

print(tax_dict)

# Using this method we can clean up our previous dictionary

new_tax_dict = {
    'Primates': ['Haplorrhini', 'Strepsirrhini'],
    'Tarsiiformes': ['Tarsius tarsier'],
    'Haplorrhini': ['Tarsiiformes', 'Simiiformes'],
    'Simiiformes': ['Hominoidea'],
    'Lorisidae': ['Loris tardigradus'],
    'Lemuriformes': ['Allocebus trichotis'],
    'Lorisiformes': ['Galago alleni','Galago moholi'],
    'Hominoidea': ['Pongo abelii', 'Pan troglodytes'],
    'Strepsirrhini': ['Lorisidae', 'Lemuriformes', 'Lorisiformes']
}

# QUESTION: given a taxon, how do we find all of its children?

# ITERATIVE SOLUTION

def get_children(taxon):
    result = []
    stack = [taxon]
    while len(stack) != 0:
        current_taxon = stack.pop()
        current_taxon_children = new_tax_dict.get(current_taxon, [])
        stack.extend(current_taxon_children)
        result.append(current_taxon)

    return result

get_children('Strepsirrhini')


# RECURSIVE SOLUTION

def get_children_rec(taxon):
    result = [taxon]
    children = new_tax_dict.get(taxon, [])
    for child in children:
        result.extend(get_children_rec(child))
    return result

get_children_rec('Strepsirrhini')

# Much simpler for parent to child relationship



#-------------- EXERCISES --------------


# ----- Last common ancestor


# IDEA: common task last common ancestor in a group of nodes


# TASK: Write a function that will take two arguments
#   1) a dictionary of child->parent relationships
#   2) a list of taxa
# And return the last common ancestor

# TASK: come up with an iterative and a recursive solution


# Initial advice:
#   - Find the last common ancestor of the first and second taxa and call that LC1
#   - Then find the last common ancestor of LC1 and the third taxon and call that LC2
#   - Then find the last common acestor of LC2 and the fourth taxon
#   - The final last common ancestor will also be the last common ancestor of all the taxa in the list


# --- Iterative Solution


# 1: Defining the function inputs

def last_common_ancestor_iter(tax_dict, ancestor1, ancestor2):

# 2: Initializaing the variable answer

ancestor1 = ""
ancestor2 = ""
while ancestor1 != ancestor2:
    ancestor1 = tax_dict.get(ancestor1)
    ancestor2 = tax_dict.get(ancestor2)
print(ancestor1, ancestor2)


# --- Recursive solution

def last_common_ancestor_rec(tax_dict, ancestor1, ancestor2):
    older_generation_left = tax_dict.get(ancestor1)
    older_generation_right = tax_dict.get(ancestor2)
    result = (older_generation_left, older_generation_right)
    while older_generation_left != older_generation_right:
        result = result.append(last_common_ancestor_rec)


# SOLUTION:

# Write in two parts
#       1. A function that will calculate the last common ancestor of any two taxa
#       2. Convert into a function that will calculate the last common ancestor of a list of any number of functions


# TWO TAXON SCENARIO
#   - Always a good idea to ground to reality
#   - Use Pan Troglodytes and Tarsius Tarsier as example / tools to work through this problem
#   - Keep the example simple enough that we can know the answer by looking it up outselves
#   - The answer in this case is 'Haplorrhini'


# SOLUTION KEY: We already created a function that returns a list of parents
#   - Go through the second list one element at a time and return as soon as we find an element also in the first list



def get_ancestors(taxon):
    result = [taxon]
    while taxon != 'Primates':
        result.append(tax_dict.get(taxon))
        taxon = tax_dict.get(taxon)
    return result

get_ancestors("Pan troglodytes")
get_ancestors("Tarsius tarsier")

def get_lca(taxon1, taxon2):  # lca = last common ancestor
    taxon1_ancestors = [taxon1] + get_ancestors(taxon1)
    for taxon in [taxon2] + get_ancestors(taxon2):
        if taxon in taxon1_ancestors:
            return taxon

get_lca("Pan troglodytes", "Tarsius tarsier")
get_lca("Pan troglodytes", "Pongo abelii")
get_lca("Pan troglodytes", "Strepsirrhini")


# NUANCES
#   - Input taxa don't have the same number of parents
#   - Need to make sure the list of ancestors considered for a taxon includes the taxon itself (see below)

get_lca("Haplorrhini", "Pan troglodytes")


# NEXT STEP
#   - Use function above to return lca for a list of taxa

def get_lca_list(taxa):
    taxon1 = taxa.pop()
    while len(taxa) > 0:
        taxon2 = taxa.pop()
        lca = get_lca(taxon1, taxon2)
        print('LCA of ' + taxon1 + ' and ' + taxon2 + ' is ' + lca)
        taxon1 = lca
    return taxon1

print(get_lca_list(['Pan troglodytes', 'Tarsius tarsier', 'Pongo abelii']))


# Add print statements to see what is happening through different steps


def get_lca_list_visual(taxa):
    taxon1 = taxa.pop() # removes and returns the last element of a list
    print(f"taxon1 is): {taxon1}")
    while len(taxa) > 0:
        taxon2 = taxa.pop()
        print(f"taxon2 is): {taxon2}")
        lca = get_lca(taxon1, taxon2)
        print('LCA of ' + taxon1 + ' and ' + taxon2 + ' is ' + lca)
        taxon1 = lca # because we need taxon1 to be set in the 'while' loop
    return taxon1

print(get_lca_list_visual(['Pan troglodytes', 'Tarsius tarsier', 'Pongo abelii']))



# NOW A RECURSIVE VERSION

def get_lca_rec_pop(taxa):
    print("getting lca for " + str(taxa))
    if len(taxa) == 2:
        return get_lca(taxa[0], taxa[1])
    else:
        taxon1 = taxa.pop()
        lca_rest = get_lca_rec(taxa)
        return get_lca(taxon1, lca_rest)

print(get_lca_rec_pop(['Pan troglodytes', 'Tarsius tarsier', 'Pongo abelii']))


# PROBLEM: This ran too many times without an ends
#   FIXED IT: forgot the brackets after pop, solution below works as well though


def get_lca_rec(taxa):
    print("getting lca for " + str(taxa))
    if len(taxa) == 2:
        return get_lca(taxa[0], taxa[1])
    else:
        taxon1 = taxa[-1]  # get the last item
        rest = taxa[:-1]   # everything except the last
        lca_rest = get_lca_rec(rest)
        return get_lca(taxon1, lca_rest)

# This worked with 'slicing'
# Creates a new list each time rather than modifying the original list















