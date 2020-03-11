from typing import Any

def FrequentWords(Text, k):
    FrequentPatterns = []  # output variable
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i + k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

def remove_duplicates(Text):
    ItemsNoDuplicates = []
    for item in Text:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates

def CountDict(Text, k):
    Count = {}  # output variable
    for i in range((len(Text)) - k + 1):
        Pattern = Text[i:i + k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def reverse(string):
    string = reversed(string)
    return string



def inversComplement(input):
    output = ''
    for letter in input:
        letter = letter.upper()

        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'

def Complement(input):
    """Returns a complement DNA sequence"""
    complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    seq_list = list(input)
    seq_list = [complement_dict[base] for base in seq_list]
    answer = ''.join(seq_list)
    return answer

def Reverse(string):
    string = "".join(reversed(string))
    return string

def RevComplement(Pattern):
    answer = []
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for nucleotide in Pattern:
        answer.append(complement[nucleotide])
        result = ''.join(answer[::-1])
    return result

def PatternMatching(Pattern, Genome):
    positions = []  # output variable
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions

def FrequencyMap(Text, k):
    freq: Int = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern not in freq:
            freq[Pattern] = 1  # if a pattern found is not already  in the dictionary freq{}, it is assigned a value of 1 and added to the list
        else:
            freq[Pattern] += 1  # however, if the pattern is already in the dictionary, its value should go up by 1 (so if it has been found, it is initially given a pattern of 1, and then this adds another 1 if it is found again
    return freq

def kmerPositions(k, sequence):
    """ returns the position of all k-mers in sequence as a dictionary"""
    kmerPosition = {}
    for i in range(1, len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmerPosition[kmer] = kmerPosition.get(kmer, []) + [i]
    # combine kmers and their reverse complements
    pairPosition = {}
    for kmer in iter(kmerPosition.keys()):
        krev = ''.join([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[base] for base in reversed(kmer)])
        if (krev in kmerPosition):
            if (kmer <= krev):
                pairPosition[kmer] = kmerPosition[kmer] + kmerPosition[krev]
        else:
            if (kmer <= krev):
                pairPosition[kmer] = kmerPosition[kmer]
            else:
                pairPosition[krev] = kmerPosition[kmer]
    return pairPosition


def findClumps(string, k, l, t):
    clumps = []
    kmers = kmerPositions(k, string)
    for kmer, posList in kmers.items():
        i = 0
        while (i < len(posList) - t - 1):
            foundSoFar = 1
            for j in range(i + 1, len(posList)):
                if (((posList[j] + k) - posList[i]) > l):
                    break
                foundSoFar += 1
            if (foundSoFar >= t):
                clumps.append((kmer, foundSoFar))
            i = j
    return clumps

def kmerFreq(k, sequence):
    """ returns the count of all k-mers in sequence as a dictionary"""
    kmerCount = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmerCount[kmer] = kmerCount.get(kmer, 0) + 1
    return kmerCount

def FrequentWords2(Text, k):
    words = []
    freq = FrequencyMap2(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words

def FrequencyMap2(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for j in range(n-k+1):
            if Pattern == Text[j:j+k]:
                freq[Pattern] += 1
    return freq

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern


def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for j in range(n-k+1):
            if Pattern == Text[j:j+k]:
                freq[Pattern] += 1
    return freq




# Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
# k = 4

# import sys
# output1 = FrequentWords2(Text, k)
# output2 = FrequencyMap2(Text, k)
# print(output1)
# print(output2)
print("Debug")
# print(ReverseComplement(Text))

# after this the code is identical for either data source

# K = 4
# L = 50
# T = 5
# oriC = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
# genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
# print("Here is your Clump List")
# clumpList = findClumps(genome, K, L, T)
# print(clumpList)
# print(len(clumpList))

# for k in range(1, 10):
#    print(clumpList[i] for i in range(min(10, len(clumpList))))
#    kmerCounts = kmerFreq(k, oriC).items()
#    kmerCounts = sorted(kmerCounts, reverse=True, key=lambda tup: tup[1])
#    mostFreq = []
#    most = kmerCounts[0][1]
#    for kmer, count in kmerCounts:
#      mostFreq.append((kmer, count))
#       if count != most:
#           break
#   print(k, mostFreq)
