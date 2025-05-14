# ---------- TUPLES ---------- #

# parentheses instead of square brackets
# immutable, cannot be changed
# cannot append or remove to a tuple
# cannot reverse or sort

t = (4, 5, 6)
for e in t:
    print(e+1)

t[1] = 9  # doesn't work -> immutable

# due to immuntablity, tuples can be used as keys in a dictionary

# DNA sequence records can be useful as a tuple
# always want in the same order

t1 = ('actgctagt', 'ABC123', 1)
t2 = ('ttaggttta', 'XYZ456', 2)

# tuples can be considered as records
# lists for homogenous data


# ---------- SETS ---------- #

# useful for a list of items that share some common property
# long list of accession numbers for exmple
#    - however, we worry there may be some duplicates
#    - want to remove duplicates


# OPTION 1: make a list and check is the item has already been added to the list

processed_numbers = []
for acc in acc_list:
    if acc not in processed_numbers:
        acc_numbers.append(acc)

# bad method as it takes a long time with a long list


# OPTION 2: use a dictionary

processed_numbers = {}
for acc in acc_list:
    if acc not in processed_numbers:
        processed_numbers[acc] = 1

# Better method because it is much faster to look up a value in a dictionary
# Bad method as it takes up a lot of memory storing all the '1' values that we don't need later


# OPTION 3: use a set

processed_numbers = set()
for acc in acc_list:
    if not acc in processed_numbers:
        processed_numbers.add(acc)

# Best method because it doesn't take up a lot of memory
# Bad method as it takes a long time with a long list


# Can create a non empty set using curly brackets

set = {4, 7, 6, 12}

# Different from a dictionary as it's individual elements not value pairs

# There are useful methods associated with them for determining intersections, unions and differences
#   - questions like: Are all elements in my first list also present in my second set?



# ---------- Lists of lists ---------- #

# we have more flexibility than just lists of numbers and strings


# EXAMPLE 1: lists of file objects

[open('one.txt'), open('two.txt')]


# EXAMPLE 2: lists of regular expressions'

import re
[re.search(r'[^ATGC]', 'ACTRGGT'), re.search(r'[^ATGC]', 'ACTYGGT')]


# Main Point: lists of lists

[[1,2,3], [4,5,6], [7,8,9]]

# more readble

[[1,2,3],
 [4,5,6],
 [7.8.9]]

lol = [[1,2,3], [4,5,6], [7,8,9]]
print(lol[1])

lol = [[1,2,3], [4,5,6], [7,8,9]]
print(lol[1][2]) # prints 6

# Can store alignments this way

aln = [['A', 'T', '-', 'G', 'T'],
       ['G', 'C', 'T', 'A', 'C'],
       ['A', 'C', 'G', 'T', 'T']]

seq = aln[2]
print(seq)

# can get one column of each

first_character = []
for pos1 in aln:
    first_character.append(pos1[0])
print(first_character)

# This worked
# could have been written more cleanly as

first_character = [pos[0] for pos in aln]


# ---------- lists of dictionaries and lists of tuples ---------- #

# Example: list of dictionarries

records = [
    {'name' : 'actgctagt', 'accession' : 'ABC123', 'genetic_code' : 1},
    {'name' : 'ttaggttta', 'accession' : 'XYZ456', 'genetic_code' : 2},
    {'name' : 'atgctactg', 'accession' : 'PQR789', 'genetic_code' : 3}
]

# The dictionaries here are not assigned to a variable, known as 'anonymous dictionaries'
# similarly in the list [1,2,3] the elements are known as 'anonymous integers'

# Other different elements
#    - each value in one of the dicts stores a different type of information

# Example of previous dictionaries we saw

enzymes = {
    'EcoRI' : r'GAATTC',
    'AvaII' : r'GG(A|T)CC',
    'BisI'  : r'GC[ATCG]GC'
}

one_record = records[0]
print(one_record)

# use of label type keys leads to very readable processing of dicts

for record in records:
    print('accession number : ' + record['accession'])
    print('genetic code: ' + str(record['genetic_code']))


# Example: Storing this information as tuples instead

records = [
    ('actgctagt', 'ABC123', 1),
    ('ttaggttta', 'XYZ456', 2),
    ('atgctactg', 'PQR789', 3)
]

# This avoids storing strings like 'accession' multiple times in the code
# relies on the order of the tuple to identify them
# Arguably more readable as well

for record in records:
    print('accession number: ' + record[1])
    print('genetic code: ' + str(record[2]))

# A common technique is to assign all elements of a tuple to temporary variables

for record in records:
    (this_sequence, this_accesion, this_code) = record
    print('accession number: ' + this_accesion)
    print('genetic code: ' + str(this_code))

# This techniques is known as 'unpacking the tuple' and leads to readable code for when number of elements are small



# ---------- Dicts of sets ---------- #

# convienient for labeling multiple sets without creating a ton of extra variables

# EXAMPLE: lists of genes that are overexpressed when exposed to heavy metal contaminants
#    - Store the gene list as a dict of sets
#    - Keys are the dict and the names of heavy metals and the values are the sets of genes

gene_sets = {
    'arsenic' : {1,2,3,4,5,6,8,12},
    'lead' : {2,4,6,12},
    'mercury' : {7,6,4,10,8},
    'nickel' : {2,3,4,5,1}
}

# Question: is gene 3 overexpressed in response to arsenic?

3 in gene_sets['arsenic']


# checking which case gene 5 is overexpressed

for metal, genes in gene_sets.items():
    if 5 in genes:
        print(metal)

# or can use list comprehension

print([metal for metal, gene_list in gene_sets.items() if 5 in gene_list])

# SETS have submethods
#   - "issubset" will tell us hether one set is a subset of another

set_one.issubset(set_two)


for condition1, set1 in gene_sets.items():
    for condition2, set2 in gene_sets.items():
        if set1.issubset(set2) and condition1 != condition2:
            print(condition1 + ' is a subset of ' + condition2)



# ---------- Dictionaries of tuples ---------- #

# lists of tuples were good for iterating over
# lists of dictionaries are better for  retrieving specific information

# THIS

records = [
    ('actgctagt', 'ABC123', 1),
    ('ttaggttta', 'XYZ456', 2),
    ('atgctactg', 'PQR789', 3)
]

# BECOMES

records = {
    'ABC123' : ('actgctagt', 1),
    'XYZ456' : ('ttaggttta', 2),
    'PQR789' : ('atgctactg', 3)
}

# Now instead of needing to loop through searching for a specific value
# We can use the .get() method

my_record = records.get('XYZ456')
print(my_record)

# Can combine with tuple unpacking

(my_sequence, my_code) = records.get('XYZ456')
print(my_sequence, my_code)
print(my_sequence)


# ---------- Dictionaries of lists ---------- #

# Lists allow for the quick lookup of many values associtead with a single key

# EXAMPLE: kmer counting from the previous book

# Old method

dna = 'aattggaattggaattg'
k = 4
kmer2count = {}
for start in range(len(dna) - k+1):
    kmer = dna[start:start + k]
    current_count = kmer2count.get(kmer,0)
    kmer2count[kmer] = current_count + 1

print(kmer2count)


# New method

#  - Intead of building a dictionary where each value is a count
#  - We do it so each value is a list of start positions

dna = 'aattggaattggaattg'
k = 4
kmer2list = {}
for start in range(len(dna) - k + 1):
    kmer = dna[start:start + k]
    list_of_positions = kmer2list.get(kmer, [])
    list_of_positions.append(start)
    kmer2list[kmer] = list_of_positions
print(kmer2list)

# Now we can use dict comprehension to get the counts

counts = {kmer: len(start) for kmer, start in kmer2list.items()}
print(counts)

# HOW IT WORKS
# len(start) counts how long the list is
# so len([0, 6, 12]) is 3
# and 'aatt': 3 goes into a new dictionary called counts

