def assembly(text,k):
    return sorted([text[i:i+k] for i in range(len(text)-k+1)])

#print(assembly('CAATCCAAC',5))
print(*assembly('CAATCCAAC',5), sep=' ')

def skew(sequence):
    count=0
    skew=[]
    skew.append(count)
    for i in range(len(sequence)):
        if(sequence[i]=='G'):
            count=count+1
        elif(sequence[i]=='C'):
            count=count-1
        skew.append(count)
    return(skew)

print(*skew('CATGGGCATCGGCCATACGCC'), sep=' ')

#find the minimum skew
def minimumSkew(sequence):
    sk=skew(sequence)
    mins=[]
    msk=min(sk)
    for i in range(len(sk)):
        if(sk[i]==msk):
            mins.append(i)
    return(mins)

#%% Pruebas
seq="TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
sk=skew(seq)
print(*minimumSkew(seq), sep=' ')

infile = open('/Users/Tanya/Desktop/dataset_7_6.txt') # read sequence from file
sequence = infile.read()
print(*minimumSkew(sequence), sep=' ')

#http://www.saltycrane.com/blog/2008/04/how-to-use-pythons-enumerate-and-zip-to/
def HammingDistance(p,q):
     count = 0
     for i, j in zip(p, q):
         if(i != j):
             count += 1
     return count
p = 'GTACCGTGGTTCGTCTTAAGTTGAAACCACGATGTCAATCCGACCAAATGAAGAGGACGTGGTGGGCTGGACGCGAATTGATATCTAGCATTCTTATGGGTAAGGGGTTTCCAAAAGTAGATCCTCTATAATATCTACCGAAAACATAAGCGTTAGCGCGCTTGTCAACCGTTGGCTACCTTATTGTGGTATTTCCGCGCCCCAATAGGGTATGTCCTACCTCCGTCCCTTAACTTTAACGAGTCTAGGGCAACCTCAAATTAAATGATCATTCAGGTTCTCCATTAGCCCAGGCCGTAGAGTCCATGTCAGTCCGCAAGCAAAGAACCGTTGAGCCAGCTACCATGATTGGTCCCCCCTGCCTTTCACGCCGGCCCCGACCGGTCCTCTACAAATCCACGCAGATATATCGCTGTTTATAGCTTTATTCCAAAAATGATCGTTCAGGTAACTTGCCAGACAGCGGGCTCTGGGAACTGACATTGGGAACCACCTAGTATCGACGCCTTGTCTTAATTTCGAATTAGGCAGAGGAACCGACGTTCCGTTTTTCAGATCGCCCGAGCAGAAAAGGACCTAGTATCTTGGATTGTGAATACAAGCAAGGCCAGCTTACCAACACTCACAAAGATTATAGAGAAATCTCCTCTCTTTCATGCTTTTAAGTCCGCCCCCGAATACTTCGTACACTACGCATAAAGGGGACGGATGACCCATATAGAAAAAGGCTACATCGGCCAATAATGCAATTAGTGACAGAGAATGGAAGTAAATAATATTCTCACCGATCTCGGGAGAAGCACATCTCAGATGGGGTACTACTGTACAAATGAGTGGACGAATGCGCGAATGTCTGGCACTTTGTTTGCCTTTCATTCACAACCTGTTCACTGGGAGTGTCAAGTAACGTATGGCGGCCTTTGACGAATGAATCAACGGTACGAAATGGAATTGCGTTGTCTCGGCTAGGCACTCCGGTTGTAGTTGCGAGAAAATGGTTATATTCGCTACCTGCGTCCCTTGAAGACATCCGCGACGTGGCTGAGCGTTCTCGTGCAACCCCTCC'
q = 'ATCCAACTCTGGGTTGCGCTCTAGCTTCTGTGATAGGGCGCTGAAAACGGGGGATTGAACCAATCGCCGTAAGTAGGGCGGCACTGCGGTTGACGTAAGTGATGGGGAGAACGATGGCGGGTCTCTTTAGTCAAATCATGGCGCCAACTGCTCCGTCGCTAGAGCGCAACTTAAGTATAGTGTTCAAACCGTGTCTATCAGGGTCGCTGCAGCCCACCATCAGGTTAGACACTTCTCAAACCTGACACAAGTCTTTTTCGCCACAGAAGCCTCAAATGTCTACTAGAGTACACACTTGGCACGCAGACAACTATGTACATGCTTTCCTACGTGTTGACTAACCACAACTGTAGGGCTAGCGTCTGAGGCCTGTAGTATGCTGGCGGGTCTGCGGGAGTCTCGCCACCGATCGCTAGGTGCATCCTAATTAGCTTCCAGCGGTTTGCTCTGGTTAGCAGCGTGCGCCGCTGCCCTTTGCATGTCCGTAACACTAATTAATGCTGTGCTAGGAAGGGGATATGTTAGGCCCAGTCCAAACTACTATCTGGGTCCGCGAAGACCGATGGTGGTCTAAGGCGTGCAAGATCTCAACAGAGCAGAGCGTATACCATGGGTTCCCGGACGGGGTTTACTCCGACGCGCCCCACATTGCTGACATAGCTACAAATTTCGGCATCGTCGTTGGCTATTTTTGACCATCTAATCCAGAGGGTCTTAGCACTCCGTGGGCGGGTTGGCCGCTAAATAATGCTTGCGCTTCGTCAGCCGCTATGAGTATTATAATGTTCCGGATAACACACAAAGGGCTTGATCTTCGCGTACAACACGAGCCAGTTATTTGTCCGCAGATCCAGTGTATGTGCATGTCACCTACGAGATGTCTCATTTCCGTGTTCACAGTGCGAAGCATAGCTCCCCACCGTGTGCATCCGTGTTGACGAGCATTCTCGTTGCCCTAAGGGAACATGGTATAATTTTTTGGCACAGAGGTGGGCTCCTTTACCATCGTGTGCAACATCTTACGACAGACGCGTACTATCGTTACTAATAATTAAGTGGTCTCCCT'

print (HammingDistance(p, q))

query = "CTGCTGCTA"
sequence = "AAGGGTATACTTGTGGTTATTTGCCGGCCCATGCTGCATCCATATTCGTACCCATCATGCTTCCAATCCACAGGACTGATCGCCTAGGCCTTACCAAATGGTAGCAGAGCTGAACTTACCGCTATCGTGGTTAGTTAATCCGATTAGACCTTACCTTCTCTACACATAGGTACCGTCTCTATAGACCATCGTGCCTACACAAGTCTGTATACACAACGGCGAAAATCAACTTCCGGGTGAATCGATCGGTGCGTATTGGAAAAGTTTACGAGAAGACAATCTATGATACCTGCGCACCAGTGAGTGCTAAGGACTATAAAGGAACGGCGCACGATAGATGGAAGTAATACAGTGCACCCCCCGGCCTAATTAAAGAATCACTCCTGTAGCTATACCCATCTGAAGCATAACTTGCAAGATTGCTTGTTGTAACAGAAAATTATGCATCAGCTACCGCAACCTTCGCACTCCCAACTTGCGCTACTATAGTGTTTCAACACGACTGCATCGCCCTTAGACCTCCGGAATATCAAGTATGGATACCCGTAGACCTAGTCGCCCTATCTTCCTAAACATATTCTCTGCGACGATACTATTGGCTCCGAATCGGGTGTTTCATCCCATGTAATTAACCTTTGTGGGCCCGGATCCTTCCCGATCAAGTGAATACGCGGTTATTCAACGTTAACCCCGGCTGCGGTATACTTGATACTGGCGTGATCTGTCTTGGCGATAAGACTTCGAGCAAAGGACGGGTCTACTCAGCTGGAGTCTGTGTCACCGGCAAACAATCATAGTGCAACGGATTACCCCCTCCTTTGCCCGACAGTGGGTCGGTGCAAGAAAGCGAGACACATCTGATTGGGTGGAATACAGGCTTTCAACGCGGCGCTGTGGGTTCTGTCTCTTACCCGTTAGACAGGTCAGTCCAGGGCCGATCGTCATAGAGCCCGTCGGTTGTGAACGATCGCCCATTATGCGTGTAATTGCATTGCAGCTCGCGTTCCCCTATCCCCAGCGTATATGACAAACCCAGCGTTTCGTTGAAAACGTGGTTCGATCCGCTTGAGTAAGTCATCACTGGAAGGCGCATAAAAGGGCCGGCCCGACCGCGACACTCCCATGTCCTACCCCAGCGTCAAAGCGTTACGGAGTTTGACCGGGTTGAAGTTCAATTGTGCACTCAGCTTAGACCCTTACAACGAGCGAGGAAGATTCCATACTTCACTATTACCGGTACGGGAACGTCTCCCAGCTCCTGGGTTTTTACTTGTCGAGGCGGAAAAATTGGCGACATACGAGCCTAGTTACATATATTTTCATCCTCTTTTGACATATGCAGGAGAAACTAACAACTTAAAACAAGTTAAATAACTATTGTTCCGCTAAAGAGGGACCTTGGTCGAGGAACAGGGTTATTTCCCGTGGGGATTGCGAGCCAGGAGATAGCCGCGACTCGCGAGGATGACCCAGCATGGGCCAGTCTTACTTAGACCCCCGCAACCGGGAAGTCAATCGGTACGAATTGGGTCGGTCAACACCTCGACCAGCAAAGTCCATGAAGTACACCGGGCAATTGATATTCATCTCGATTAAGTATTAAAACCTCTACGGAAATGTTCTGCAGTCGCCGGCGTTTCTGCAGAGACAGTGAAGCCAGATGAGAACCCGAGTAATCCCATAGCGCGAGGCTGATTGCTTTGGTACAGCGATTCTGGACGGTTCGTATAATGTACCGATAGGAGCATGCTACCCCGATTCGAGAAGCGGGAGTCCAGATCAGACAAACCGATATCAAAAATCCACAGAGGGAGACTAGAAACAATAGAAGTCGACGCGTTTACTGTTCGCAACACGTTCAGTGTTGCTACGTTCTCGTCTTGCTTAACCACCGTCTAACATGAGTGCCACCAACTCGACCTAACCTCCTGTGCGGACGACCGTAGACTACGCCGCATTGCCATGTTGGGCTCACCACAAGCCTCGAAGCAGAGATCGTGGGAGCGATTCCTGCGAGTAAACACGGGAACAATACAACACCGCCTACGTATGAGCGTACCTCCTGCCATTCAGCGACCTTTTGCCATGGCGTGGTGAGTAAAGTGGACTCACGAGTTGTACTTTCGCATTACGCGAGTATTCACGGCATAGAGGTGAATTTCCGAGGGCGTCTACTGAGAGTGGAGAAGGGACATTAACCCATGGAGCTAAGCACCGCGAACGATGTACATGCCATGCCGAGTAGTTCTACAAAAGTTATATCATGATCCAATACGCTCCCTTTGTCTGTGTAAGATAACTGAGTCTGCGTAAAGTGACAGGGGGGAGAAAGATTGCAAGGACTTTTTACAATTTCGTCCTCTGATCTGCGGAACCGTTTCCTTCCGCCGTAATTCTGACCACTAAGTAAAATTTTTTGTTGGAAACCCTGATGAAAGGGTGAGCAGCAGGATACATGACAGATTTAGAGAGGAGGATCACATATGAGGCTTATGCAAGAATGCATATAGAACTGGGCTCGCCTCAGCTGTTAGAATTGCACCAGTTTACAACCGTTGCAGATCACAAACTTATCTAGTAGGTACCTCCGGACCGCCCGTTCAGTCGATACTATTCGCTCCGGCCGCTGGAGGAGTGCCCAAACTAGCATAGTGGGCCGTTTACCACAGGATTATGAACCATCGGCAGCCGACAGTAAATCAGTCACGTGTTACCGCCGACGAGTTATATATAAGTTATAATTAAGGTGAAGACGGTAAATCCTAGTCAGCGAATAAGGTGCTGACAGATCTGCACCGATACGAACTTTAATGAATGCCTAATGTACATTTTATTCGCTCAATAATCACGAGGTTGTATTGGCCCCACAGTCACATTCTAGCATACGCCGAAACTCCTCTAGCTAATCGGGCTTAAGCTTTGCATTTAATCCCAACCTTTTTTGACTGCTGCTCTATTGTAGGCATCCACGCAGCCTTGTCGCTTTCACAGTAAGGTCCCATTTCTTCGACTTTCGGTTCCACGGGTATTTTCGTTATGAGGAACAGAGTTTAGAAGTAATTACGATACGTTCTCCTGGTATGCTATCGGCGGTCGTAGGGGCAAGCTCGGCGTCGGGCGATAGTTGGGTTGGCGGGAAGACTGCCCAAACAGTGCGGGGAAGCAGAAACATCAAGCGCCTTCAGGGAAACTTCCTCAATCGTCCTTCAGTCCATTACGATCACTCGTGTTACTCTCACCAAGCTTTCAACTCCTTACCGTTGTTGATGGCACTCTCCTTCTCGTGTTCAGTGGATCCACGTGCATGAATAGTTGCCCGCCAGTATTCCCTTCGATTGGGAGATGTACCTGCTCCTCGCGCTTGGTATGAGTTCTAATGCAGATCTTGATCTAGCCTTTTCTTCGCCTTCTGTAGTTTTTGGCTCGAGCACCGCAAACGTTGTTAGGCAGATTAAGTCTTGCTTAGTGCCGTGACTGTAACTATGAGTCACGCGAAGGGGTGTACCATTAGTGTGGGCACCACTTAGACGAATATGCACCTGAGCCTCGGAGCCCGCCTTTCGAACCAGCATTTGGGTAGCCTGGTAAGCGATTATTTGCGCGTGGTTTATCGAACGTAGACCAATCGCCGTCGGCAGGCTCATGACTAAGTGTATTTTGCGGCAGCTATTCGGCCACAGCTTATTGTCCACCCCTTGAATTGGTTAAGCTTCGGGCATCGGGAACTCGGAGGATACTCCCCCCACGCTGGGTCTGCTTCGATACCCGAGTTCTGCGGCTATGAGTCCGAGAAATTCTATCCCGGCAACTCATCACGCGATGCCAGGGGGAACCGCCACTATTGGTATCCGGTCTCTGGAGGCCCCTGATGCAGCACGGGACTGCCGAGCCAGTTATTGCTCGCGTCCTAGCAGCGACTCTATCTACCTAAGGATTGTTGGCGGCAAGATGCCCTAGCCTTAGACTGTCACAGATTGCATCGGCGGGTGAGCCCAGTAGGGGCTCTTCCGTACTAATTCCCAGTGTTCCGTGACTATATAACGGGGATAAGCTCGCTTTATTGGGCTGGTAATAACCGGAGCTGACTATCATTCTGGAATGTCTCAACGGCCACTTACCGTACCTCGCAGTCTAGCGTCAGAACATTTACAACCGTCGATCGTAATCGACCCAATCGGGCCTAATGGGGGGTAAGCACTCGTCTCCAGAATTTACCTAGTCCGTAACCGACAGAGGGCTTGTCGGGCATGTGACTCTGGTGGGCAACCGGCGGCACATACCCACGCGTTGAGCAGTACGGTAGATCGAGCCGATTGCGTGTGTGCATTGACAGCAGACGCCGTTGCCATACTAAGGATCTTTTCGTTGTGGATCAATTACCACTTATTTGATCGCACCCAAGGGAAGCACAGTGACATATCTGGGTGAGTTTCATAGCTTGTACAGGGACCCTGTCTAGGCTGCGACCACCCTGCCCCTAATGTAAAGCGTCATTCATCGCGATCGGCTCAGATCTCAGCTTCGGCTACGTATTCCAACGACTCCCTGGCCGCGAAGACCACGGGCTTTAATAACTAAGGCTCCCTGGGTCTTACACATCTCTCCCTCGTCTACGAGTTTATTTCCGACCTTATCCTTGGGGCGGTGGGGAAGAGAGGAATGTGATTCACGTCTCTGCAACTCGAGGGTCCATTGCGGAAACTCAATTTACGTAGTTTTAAATCTACACGCATGCGCTACTAATGGTGCCGATGGCGTACGTTGGTAATGTTGGCGTTTATTTGCTTGTTGTCTTTATGTGGCCCACTCTTTCATGCCTTTCTGGCACGGAACGGTGCCGGATACCAACCAGATGCAGCGGCCAGCCCACTTTGCCCACACGCGGCTCGTTGTCAAGTTCCAGTCCGTACTAGAATCGCTAACCCATCAAAACTCCGCGGCCATGTAACGGGGCAGTAGGGGATTTGCTTCTCATCCCACTACCATGTTACCCGATACAGCTGATAAGTAGAGTCCGCGATCTATTAGTTGCGATAAGGGTAACGGCATGCTGGTTGCTCGATAGCGCGACACTCTTATAGCCCCCAGTTATATCTCGAACGGGCAGGGGCATCGTTTCAGAAACGACCCCATTCTCGACACGGACTGACGGATGAGTGAAATCTTTTCTGTACCAGGATCTCCGCGAATTAGCTTAAACTTAAGTGGCGTTCGGATGTAGTGTGAATCGAGAACCGGGGCATATGAAGCCGACCAACTACTTACGTAACCAGAGTAACAACACAGCAACTTCATGAGGTCCTCATTGGCAAAGCCAAGCATAGCGGGTTCGTCATTACAACAGCCCGATCAGTTCCTTGCCGTTGCGAACAACAATGTGAGTCAAGGCAAGACATCCCGATTGGTAGTGGGTCCTCTATCAAAGTCTTGAGTTACCGACGGGTCTCTAAATGTACAAGAACTCTTGCTGTGCTCCCGCTGAAACGACTCACGGCGTATTGTCTTGCAGTATGTACGGTGTTATGCTGGGCTCGTCGCCCCGAGAAGTCACCGAGTACCAATCGATCCAGCATTCTTACGAGTCCAAACACCTCCCGTTAACCAAAGCAGCCACCTGGCTTTAGAGTCTAAGACTTACAACTACGAGCAAGAGTACCCGACGGGTGACACTGAGCAATTCGTGCCGCCAAGTTTCAGCCGGGGTCTCAAGTAACTAACTAGATTCGGACCGTCTCTCGGATCTCCAGGCAGAGCAGCGGCCAGTTCACAACGAGAGATGCGGGGTTAAATCACTAGAGAATATTCCTCGCCCAACCTTAGACCCCGATCTATGTTCCGCGGGGGCGATCGGCCGGACTGTTGAACTTACGTTAATGATCGAAGTGAAAGATGGTTGAACTTGGAACTCGTTTCAAGCGATAGTCTGTTCTAAGCAGGCCAGTGGTGTACGCAAAGAGCTCAGTCACTAAGCTAGGCTCTCCTTACCAGAAACTGTATGCGACAAAGATGCAAACTGAATTAAGACTTGTGTTGTCGACCGGGATGATAGCCTGCAGACGAGTCTTAGCGCCAAAATTAACCCTCAGGACGTGAAGGCCGCCTGTAAGGCGCTCGACCGTCCTGAGCCCATACGACGATGCTACATGATGAGAGACCAAATTCGCTAAGGACCTACGTCATTGCTACACAGGGCAATTTACGGTCAGATAGGTTGGTTCTGGGGCCTAAAGCCAGAGTGGCCACGGATAAGGGGGGAGCACTGATAGGTCTTGCATACAACAGGGGTCTCGGCCGACCTACAATCAAATTGTTGGCCTGATTCAGAGCACAGATCGATGTCATCGCGGATGCGCTGACAAAGACAGTGGGATTGTAAGTGCAATGACTGAAGACTGCTCAGCCATGCACTAGATTCCGGGAGACCGGTTCATTCGATGGCGCGGCAGCCAATCTGTGCAATATCGCAGCCTTCGGAAGTGAGGTGATCGGCCGTAACATAAAAGCAATGCTGCTTACTATGTTTCCTCGTGCTGTTTAAAGAACTTTGGCAAAGAAATGGCGTTTATTAGTATCAAAATCAGTGTATCCTATAAAGTGACGGACACCCACTGACGCCCCAACCGAGACCCGTCTTCGCGAATACGCGTCTGCACCTTGGATAATGATCTACAAGTGTCTTGATGGACTCGTACACTTCCACACTCGTCGTGAATCCATTCGCTGCTCTTATCAAGCGAGGGTCCTCCGCACTTGAACGACATGCAGATAACGAACCGTCGTGGGGATAAACATTCGGGAAGGCCCTTTGGCTACTGACATTGTTTGTTCTTATTCGCCAAGATTCCTGCTTCAAGGGATTATTAGAGGGTGCAGGGAGACCCGCCGGCGGGAGAGCACCCAAGATACATACGATGATACAGTATAATGAAACAAAACATCTGCGGGCTGCAACATAAGGATAATTATCTCTCGTGAAATAAAACTCGAGTCACCTCAATTCTGCGACTGAGTCTTAATTGTTTTTAGCCGATGTCATCATTCGGGGGGATGGATCAGCTACATCTACGCTGTGAGCTCATTTTGCCATGTAAACTTGGGGAGATATCCTCAGGTGGAAAGTCCTAATCGGTACATTAATGGCGGATCACGGCCTGAGAATTCAGTGAAGCCCCTTGATCTATAAGCAACACTAACGGGGCGTTCCAGCTGGGTCTGATGGTAGCGAGTGTACGGGATATCCATCGCCGCACACGACTCCCCCAAGTTAGTAGGTGGGTGTTGGAGATGTATTCCCCCATAAGCTAGTGAACACAACAGGTATTGGATTATCTGTCCCGTACGCATAGTATGTGCTCTAAGGATTTCCGGCAGCAAGCAAGACCCTCCGGGAGAACGTACGAACTAGTACAAGCATGCTAGACAGACCTAATTGGACCACGATCCCTAAACTTGCGTCCCCAAGTGAAAAAATAAGATACCGAGTAGTCCACACTAATAAGTATTAATCAACCCTAGGCGATTTTCACATGCTACAGTGATCCAATTATCGAGAACCTTTTTTCCCGCGAGCCCTCAGATCCGCTGTCTCCCGTGCCTACGAAAGCTTTTCGATACCGACGAGCTATCCTTCACGCCCAGCCTATGCGTGCTGTAGAATGAAGGGCGGTATGGATCTCATGATCTACTGAGTATTCCGAGACCTATCGAGCTCGAGCACAGTCGGTCCATAGTCTAATTAGCGGGCTTTCCATCCCTCCTCTAACCTGTATCCACAGATGTCTTGCAGTACATTAGAAGGCTCCCACTGACCAAGTCCTGCTAACTGCATTTTTTTTGATTAGGTATCAAGCACACCAACTGAACCATGGATTACGCAAAATTCTCTTTTATCCCCCGTCAGTTTGCCATCTTGACGCACTCCGGGTAACGGGACGTTTGTGTGTCGACAAACGAGAATGAGACTGAGAGCCGTGATCTCTGATATATATCCCGATTGGTGCATCGCTATGCTTGCTTTGTCGAAATACTACCCACAGACGATCTCCTATTGGATCGACCCGGGCGGGTCACAAATGGTGGGGCTGATGTCACTGAGTCCAAAATGGCCCCCATGAGGGAATCCGCTAGACTAAGCTTTGTCAAGTCAGCCAAGCGCCTCACCTGCGCCTGTCGGGCATTTTTAATTGCAACGAGACACTTAGGTCACTAATGACCCTGCGTGAATCTGCGGCAGGCAACTTCGGCATTAGTGGAGTCGATACTGAATCTTTATAGCTGAGCGCGTTTATCTACATTGAGACACGGGATCCGGAGCGCCACTTACTCCGTCATTTCGCCCTTGGGGTATTACTAGTCTGGTTACCTGCCGCGTTATCTATTATGCAAGGAAAGCAAAAGTATCCTATGATAAAATCTCACTGGACCTCACACATTTTGCCCTCGGCGATTGTGTTTTAGTATAAGCAGAGGACCGCCTAGAAAGGCGAACTCATTCGAAGAGAAAGATCGTAGGACGAGGGATCATGATTCTGATTTCACTCGGGACAGACGAGCGACCACGTCTACTCGTGACCAATTTTCGGAACCTTTTGCATGAAGCCGATAATACCTGTTTCATAGAGGGTATTCCGGCTGCTTTACCCTTATCCTTTAAACGGGCACTCTGATCAACTTAAGGAAGTATGTTCTTGGATAAGCTGCAAGTCCAGCCACATTGCCCGCGGGCGGCATGAATTTACGACACGAACTCGGCAAATACATCCCGCCCCTGGCTCCGGGCTGTCTTCTATCCAATGTAACGTAGTCGTGCACATTAGTAATATAGATGCCGATTGACATTGATTACGTTTTGGTCACTGAAGGTTCCTGGGAACAAGGTACCTTGCACTTAGTAACTAATCCTCGGTCGTATTTGCCGGCCGGAGGCTGTTATTAATAGTCATATTGGCGAGGCTGCAGACTGCGTAGCCCTTGTGTCTTTCGATAGCCGCGTCCCAGGGCTTCCCCATACCGGACACTAGGATGCCCGCTGTGTCAGATTAATATATGCCCAAGTACACGTAGGCCTTAGCAGTCCCCTGTTGCGGTGGGCACGAATCGCCTCACCCTCTGACCAACTAGTCGTATAAGCACAGGCGCCCACCGGTTTTATATAGAGGTTCTCCCTTGAATACCTACGTAACAAGCCTAGAGGTAAGACTCACCGGTCGGCCGCTAGAGAAACCTGGCGGAGCGATAGAGTACTATCTGCGTCTTCTCTATCCGGTCGTCCTGGTTACACCTCAGTGATAGCGCGTCTCTCATATTTTAGGACCGGCGTAGAGATCCCACGCGCCCTGCGAGCTCTAAGTGTTTGAAGTCAAAGTGATAATAATCGAAGCTCTTGGTTCAGCAATTGCAACTGCTACCACTGTCATCGGATGGTGACGCGGAATGGTACAGGTGCGCCCTCACTCATCGGACGCATAGTCTCCCGTCCTAACTACAGTCCCATACGGATTCGAACACACGAAGCTTGTCAGTTGTGCCTCAGCAGGAATTGCGGCACGTGGAGCTCGGAACTGTAGTTGGGTTCACCGCAGGGAGTCGAATTGCGGCGCAACGTACTCTATGTGACCGGATCATTAGTAAGTGACTCGATTCGATAATGCCTGTTCTTAAGTGCAAGATAGAAGCGCGATCGTGAGCATGCACCGCAGTGAAAGTTGCTCCTATATGCTCATTTGACAGGATACTGCGCTTACTAGATTGGTGGTTCCTCGAAGCTTCGAGTACAAGTGGCGCCTGACCGCTTTGCGGGGTTCGTCCAAGCTGCGTTAATGAACAACTCGTCGATCAGGCTATACGAATAGCGTCATTGTTGACCTTGGTAATAGAGATCTAGGAGGGCGCTCCATCGGCACACAACAAGTCCAATCACTCTCGCTGTAGTCTGCCATGCTACCAGCAGGTACTGGTCGATACCTTCTCCCTCCCACGACATAAATCGCTTCTGGGACTAACCTGCAGCCTCAAGCAGCTCCGTAGGACGATTATTCGTACGAGCCTGTTAGCACAGCATGTACGTTTGTTGGATAACTTACCTGAGCAATTAGCGCCAGGACAACATGAGTCCAACCGCACATGTTGTTTCTTGGTATAATGGCCTTGTACGATATCTACCCGGGTCTTCGGCAAGGTAGCCCGTGCAAGCCGATAGATAGAGATAGGGCCCTTCATGAAACGGGTTCTTCAGAGATAGCGGCTAATAGAGTGATATGTTGACAGCACTATCTATGCGCAGCTATAATTGTCGAATTTACCATAAATTTGTGCGCTCCGCAACGATAGCGGACTTCTCACGGATAACGATCTTAATCTCTGTTGGAATACTTGTGCGAGACGTTGTAGACAGCTGATTTGCCGCAATAACTTGTTTAATATTTTGACTCACTTACAGGCAGGCGCAACCTTGAGGAAGCGGTGCCCCGAGTGACCACTGTGAGAAGCAATCTAAATCAATGAGCATATGTATTACGGTTCATCTAGCCGACGAATTTGCTTGGAAGTCGGCTCCAAAGATTCAAGGAAAAATAAGACTCCTCTTCATTTACTTTCATAACAGCTCCGCAGCCTCTATTGCGTTACGGACTGTGCTTATTCAGGCGGCTCGATCCCATATTTATGGGACTCCATGTTATAACCCCACCTTTTACAAGCACATTAATCGATACTGCTCTTTAGGCAAATAACTACAAATCATTGAATCCCGGCCGTGACTGAATTTATTAGACTATCACAAGTCCGTCCAAGAGGCAGCAGCCATGGTAGCTGCAAGGTCTGCCTTTTCTTAGCATCGCCTTGGCCGACATCGCAAGTATCGACAGGTGTCTCTCCCCCATCACTCAGAGAAGGGTAGCTGCGAAGTGGGTCTGGCGACCTTCATTTACAGGCGCGAACTCTAATCTCATTCGCAAGGCATCAACCGGCTAGTTTGCTGCTGTGAAGCCGCGAGGGGTTACCTATGTGGCCTAGCTAAAAAGGTAACAGCCCACAGCCTTTGGGTTCGTCTGTCAGGGCTCAGACAGAGGACCGTCAATGCAGGTTATCAAACTGCTGGGCGTTAGTCACGCATATATTCGGTGTTCAGCCGCACAGAACTGTATAGGAAGGGATCCGGCTTCGACTGGGACGATGAGAACCATCTCAGCAAGATCTACTCTTAAGTTCAACTTTCAATAGCGCATGCCCTGCGTCTACCTGACCGGCGATCGTTAAGAGAACCGCTCTAACTCAGCCCTCGGCGTCTCTTCAGCGCATATATTTCTCTATCGCGAGAAAGTTTTGGCCCTCTCTACTCCCTAAGGCAGATTACATCGGGCAATGTTGTCGAAAGAATCGTGCCCACCGAAAACACGCTTCTCCCACGTATCGATTGCACTGACCCTACGTATGCTTTACTCCAATGCCGTGTGAAATGAGGCCGTACGGATGGCTCCAGCAACATTCAAAGGGGTTGACGTAACCACACTATTATCTGCTCAGGATCGCGGATGTCTCTGCAGCCGAGGGCGGGGCATTTGCGTGTGAGTGTGTGCCTTTAATTGACTCGCCGGCTACAGACCTCGCGTCACCCGTTTTTTCCAGAATTAACTGGGGTTCTAACGGGCTGATATTCCAGTAACCTGATTGTTTATACACATTACCTCCCCAGCTATATACAATTCATTGGAAATAGATACCTAGTTCGATTTGTAGTGGGGCCAGAACCCTTCCAATACCCTGAGGCTACCCTCACGCCAGTGCACTTCTAAGTACCCGTCGAAACCACCGTTCCGTTCCTCTATGCCACCGAAGTCATTTCGGTTGTGGCAATTCGGGGAGAACCTACTCAGGGGCTTGTGACCTGACTAATTATGATCAAAATAGCTGGGGATGGGTCAGGCTGTCCATTCGACAGCTTTCAACTTGCGTTCGATCCTTTCATCGCAAATTACCTTAGGTGCTATACAAGCGTCAGGCCCCGAAGGCGACGTGAGAAAAAAAGCGCCTTATGCTGCCGACTGATTTTGCCAGGCTGCGAACCGCAGCCCCCACGAGAACGCGAGTCTAGGGATGGGACACTAACACCCCGGCATCTCGCAACCGGCGCGTAAGACTAAGACTAGAGTTGATATTACGGTAGCCAATTTATTATATCAGCACACTCGAAATTTGCTATGCATATAAGAGCGCTGGCGCACGCGATATGGAGACATTCGAGATTGTACCACCTACCGCTGGGTCATGGAAGAAAAAGTTATCGCCACCGAGCTCATATCCATTATGCAGGAATTCTTGCTTGAAATGCACTTACGGTGTTCTTTCAATCTTCTCTGTCAAAGTGAAAATGCTTTAGAGGGCTCGGCTCTGATTCTATGCCTTAGATGGCGGAGACCTGAGGGTATACCCAACGCGAGCACATCTGGCCATGGAATAGCCCACAGAGCTTTTTAGTTCGTCTCATCAGGTCACGTGTGGCTGTTATATGAGCGGACTGCTACACGGTCTGTAATCGATAGGTGGTGGAGCCCAGGTGGGTGGGATCCAAACGATTGTTCTCGGCCGGCACGCTGCCGGTCTGTGGGACAGCCTACATTTTACAATAGCCTCATGAGGATGCTGAACGAACCGTTCAACTGGCGTTCAAACAAGCGCCACAACTTAGACTTCGAGGACGGGGTAGGCCAAAATAGTCCAATTTCCGGAAAACTCGTGAACACGAACTATGTTTTGTATGCAGTCAAACCGCCCTGAGTACTATCAAGTAGGCTATCTAGTCGCCTGCGGCACAGCGCCCAACACTTTGCGGGCCTGACAGTTAACAGTGTTGCACATTTCAATATCCTCGCTCTCTTTCAGGCGAGGAGGCCACTCATGTTCAAGTAGTTTAGCGCATAAGCTTTTGGCGTTAGCTAATGTCCGCTCTAATGAACCGTGGTACACGGGTTGTGCCTTTGACATTCGAGCAACCAACCCACCCGGTTGCATACCCTATCCGTAGATGCGGAAAGGAGTAATGGACTTTTCGCCGTAAATGCCATATAGGCCCGTTTGCGGATAAGGTCCAACCATTCCCATCCTCGTGGCGCCCGGGGATCAGGTATCAACGCAGACCCTTGACAGCCTGACAGTGGGAACCTCGAGGGGACTTTAGTGTACCGTCCGGTGTTCTAGAGTCACGTGGATTAGCTTCTTATATAGCGTGCTACAGGGCGAGGTGACCACTGGAGACACTCCGAGTTACATCCTGCTATTGGCGCTAGATTGGACAAGGGTCACACTCCGCAAACCTTGTTCAGCATACATCCCACCGTAATAAGTACTATTAGGTCCAGATTTCACGCACAAGTTAAACTGCCCAACGAGAGAGTCTGCGTTCATACAGGATATTGGTACCGCTTCGAAACGATTGGAGACTCGCTGGACGTGACGGTCCATGGGCTTCGTGAAAGACCGGCTGACCCAAGCTCATTTACAACGGACAATAACCCGTCCCCTGCAACCCCGGGAATCCACGCAACACAGTTGCGTTCCGGGATCCCAGGCGTCTTTTTTAACCGCCGATCGATACCCTAGCTGGGTACTATCACTCTGAGATTTAGAAGACACGAATAGCTCATAAATCTGGAAAATTACCCCTGCAGACGCAGTATCGCGGCGATCCATTAGCTGTCCCATACCAATGTCCTAGGACCTATCCCAGGCGGAGCAGCAGGGTATTTCGCAGGTGACAAAGACGGCAATATCCAACGGGGGGTGCCGTACATTCGATAGGCAACGTTCAATATACCCTATTATGATGCAGCATTTGGAGGAAAGGGCACTGTAACCCTACAACCTAGGCGGCAAGAACGAATTTACGCCTTGAAAAGCGCTCTCGCGAACTTCTCCCTCCTGTGTGTTATAGTAATACCGTGCGGTACAAGTGGAAGCGTAACAGCGCTGGTAAAACTGGTCTGTCCCCTCCGTTGACGAACACATGCGAAGAGAACTCACGTTCAGGAGATCGCATATTCTAATGCCTTTTCTTGCGCTCTACATTCGGGCTGCATCTCGGGTCTGGTTGCCGCGCATGCGGTCTAGCGGAAACAACTCGACGAGAGGAGGGAGCTAGCGCCTTGGTTACAACAGATAGACGGAGACAGACTCGGGCCAATGAGCAATTTCGCAGGCGTCTAAAGAGCCTGGCTTCCCATTGTACGCTTTAATCTAAATCTACCCACAGGCACACCCAGTCAGGGCTCGGGAAATCCATGGGAGGTTCGGCTCTACTGTGAAAGAACCGTCCAAGGGCGCAGGGCCAGCTAATCTGCGGCGTACGGCAAGGCTGGTGTACATAGAACTTTGTCAGCAAACGACGGGGAACCTAACCCGTTAGGCCTTACGCAGAATCAAGGTTATCCGAGTGGAACGTCAAGAACAAGTACAAGAGGACTGTCGGTAAAACCCCCAGCCGGGGGGACTGCCCAATTTCGTTTCATAGAGCGGGCCGACAGCCTGAACAGGGGCTTGTTCGATGTGGCTGTTATGCCGAATGCCCAATAAGAGGCGTGGCCTGCATAGTACACTGAGGTACACGTCAAGTGACCAGTGGGGCTGAAGGGAGCGAGTGCCATGCGTTACTGCAGAGAACTTACCGGAGACGCTGATAAGATACGGCAAAATATAATAACAACAGTGAACCGGCAGACCCAATCGTGCGGTTCCTGGAGTGATTATTAAGGGACATCGACTTCTTGACGACGTTAGCTAGATCCAGTCCCAGGCTTCGTGGCCCGGATGCTCCATGCCTGAACCTGTGGCCCGCGTCTCGGAAAAGGCGACAACATGCCTAAATTTATCTATCATGTGCACGTAGCTGATCCATTGAACCACGATGAGCTTGCGCCACTCAACAACAGTTGGTCCCCTGCGGAGAGGAATCACGGCAGTTTTCTGTTAGTTCTTCACCGTCCGTTTACGTTTTCAACCTCTTGTCGAACGTTAGCTCGCCACAAATGAAAAGCCCAAAGTACTGTAATTCCATGACATGGAACGGAATGATCAACGCACATGGCCCTTTCGACCGGCGAAAACATTAAACTGTGACGCATCAGAGGCATAGGTCGACTGGCAAGGTACAAATCTCCCGAGACCAATTAAACGCATGCCGGCTCAAGGTATGGGATCCAACCCTCAGGTCACATAGACCACGATCGTTCTAAAGTGGTTTGGGCCTAGCTGTAGACGCCAGTTCGACAGTACTGAAGTGAGAAACTGTGATAAGTCGGCTCTCGGATTAAGAATCAAAAAAATTATGATTACTATGGTATCCCTCAAATTTGTTCTTCCAAAGCGACTTTTGACTCATGGCAGCGGATGCAGTCCCAGCATATTTGATAGAACCAACGTAATAGCTCGAAACTTGTAGCGCTGGCCTCACTACGGGGTATTACAGGCCGTCTGGGAGCGATGCTCGAGAATATTTAGTAACGCTACTTAAACGTCCATGATGAGATAGCTTCCATTTAGAGTACACTTTCTTTTGGGGTCGGCTATGTCTGGCGGACGGTGTGCTCCTCGACGGTTCCACCAGGAGAGGCTGCATTAGCCACAGCCAAACCAGAGCTCGGGTTTGTCCCTCAGATGTCTCATACGGGGATAGAGAGAAATGTCGAATCGAATGAACATAAGCTTCAATTGAGGCGTATTAGAGGATACTTGTTTAAAGCAATTGAGTACAACTGACCTGACTCAGGGCACGACCATCGATATGACCGCCACGTACACTTTCGCAATCTAGAGGCTACTCTAGCATATCGCCCTCTTCTACAACGATACGTAGGTACCGGCCAGGAGTGCCGTGTCAGTGCAAGACGTCGTCGAATATGATATAGCCCCGCGGCTCAAGCGATTACTGGACCGGCGCCAAGTGTATCCTCTACAGTCATGTGGCAACTGTCACATTCGAGGTTGATATACCGTTCATTTATGCCTCCGAGCTGTGGAACGACGGCATGAGGTTCCACGACTGTAGTCAAGCATTTCGGGATCATAAGAGACCTTCTCGCCTATGTTCCTTCCGCGGACCCCAACCCGCTCGCGGACGTACGAGGCAAGCGCGCGTAAATCTCCCTAGTTCCTGCTGCTA"

max_mismatch = 4

def approx_pattern_match(query, sequence, max_mismatch):
	index= []
	for i in range(len(sequence)-len(query)+1):
		pattern = sequence [i:i+len(query)]
		if HammingDistance(query,pattern) <= max_mismatch:
			index.append(i)
	#print type(index)
	return ' '.join(map(str, index))


print(approx_pattern_match(query, sequence, max_mismatch))

def patterndcount(st, substr,d):
    count = 0
    for i in range(len(st)-len(substr)+1):
        if HammingDistance(st[i:i+len(substr)],substr) <= d:
            count += 1
    return count

#print(patterndcount('ACGAAGAACAGCCTATATAAGGTGGAATACGACTCTGTGGCTCATCATCGGGACTTTGCCCCAGGCGAAGCCACTGGAGTCAGCATGGATTTACTTTTCCTTACATGGTCTGTTTATCAGCGTCGTGGAGCAGCTCCACACCGGATGCGAGCGGCGGCTTTTGCTGCCGCAGGAGATCGCGACAACGTGGTCAACCATCTGCTGGGCGAGCAACTAGCTCCAGTACCCGCTTGCCAATCATACCTCTTGCACATGCCGATTGCCCGAGGCGCGAACCGCGTTCTGGTTTGGCGCGAAATGAAGAAATGTCCTTTGGAGTCACCAGTGAAAATTACAGTCTACGAGACAGAAGCGCTGTTTCCGTGCTATTTAGGTTT', 'GTCAC', 2))

def mostFrequentKmers(seq,d,k):
     kmers={}
     for i in range(len(seq)-k+1):
        kmer=seq[i:(i+k)]
        pos=approx_pattern_match(kmer,seq,d)
        kmers[kmer]=len(pos)
     kfinals=set()
     for i in kmers:
        if(kmers[i]==max(kmers.values())):
            kfinals.add(i)
     return kfinals

print(*minimumSkew(sequence), sep=' ')
print (*mostFrequentKmers("AAATGGGAAAAAATGAGCTTTGGGCTTCTTTGAGAAAAAATGGGTGGGAAACGATGAGCTTTGGGAAACGACGAAAATGAGTGGGTGAGCGAAAACTTCGATGGGTGAGTGAGTGGGCGAAAATGAGTGGGTGAGAAATGGGAAACGACGATGGGTGAGAAATGGGCTTTGGGCTTCGACGATGAGCTTCGACGATGAGTGAGAAATGAGCTTTGGGCTTCTTCTTCGATGAGAAATGAGTGGGTGAGTGGGCTTCTTTGAGTGGGAAACTTAAACTTCTTTGAGTGAGAAATGGGAAACTTCGAAAATGAGTGAGTGGGCGA", 3,5), sep=' ')

def mostFrequentKmers(seq,d=3,k=9):
     kmers={}
     for i in range(len(seq)-k+1):
        kmer=seq[i:(i+k)]
        pos=approx_pattern_match(kmer,seq,d)
        kmers[kmer]=len(pos)
     kfinals=set()
     for i in kmers.keys():
        if(kmers[i]==max(kmers.values())):
            kfinals.add(i)
     return kfinals

print(*mostFrequentKmers("ACGTTGCATGTCGCATGATGCATGAGAGCT", 1,4), sep=' ')

#print(*Frequent_Words_With_Mismatches_and_ReverseComplements("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4,1), sep=' ')

#http://www.saltycrane.com/blog/2008/04/how-to-use-pythons-enumerate-and-zip-to/
def HammingDistance(p,q):
     count = 0
     for i, j in zip(p, q):
         if(i != j):
             count += 1
     return count
p = 'CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG'
q = 'ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'

print (HammingDistance(p, q))


def skew(sequence):
    count=0
    skew=[]
    skew.append(count)
    for i in range(len(sequence)):
        if(sequence[i]=='G'):
            count=count+1
        elif(sequence[i]=='C'):
            count=count-1
        skew.append(count)
    return(skew)

print(*skew('CATTCCAGTACTTCATGATGGCGTGAAGA'), sep=' ')

def patterndcount(st, substr,d):
    count = 0
    for i in range(len(st)-len(substr)+1):
        if HammingDistance(st[i:i+len(substr)],substr) <= d:
            count += 1
    return count

print(patterndcount('TACGCATTACAAAGCACA','AA',1))




#find the minimum skew
def maximumSkew(sequence):
    sk=skew(sequence)
    mins=[]
    msk=max(sk)
    for i in range(len(sk)):
        if(sk[i]==msk):
            mins.append(i)
    return(mins)

#%% Pruebas
seq="CATTCCAGTACTTCATGATGGCGTGAAGA"
sk=skew(seq)
print(*maximumSkew(seq), sep=' ')

def frequentWordsWithMismatchesAndReverseComplements( s, k, d ):
    counts = {}
    for i in xrange(len(s)-k+1):
        for sub in [s[i:i+k],reverseComplement(s[i:i+k])]:
            for neighbor in neighbors(sub,d):
                if neighbor not in counts:
                    counts[neighbor] = 0
                counts[neighbor] += 1
    m = max(counts.values())
    return [kmer for kmer in counts if counts[kmer] == m]

def neighbors( s, d ):
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    out = []
    for neighbor in neighbors(s[1:],d):
        if hamming(s[1:],neighbor) < d:
            out.extend(['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor])
        else:
            out.append(s[0] + neighbor)
    return out

def hamming( s, t ):
    return sum([s[i] != t[i] for i in range(len(s))])

def reverseComplement( s ):
    return ''.join([complement(s[i]) for i in range(len(s)-1,-1,-1)])

def complement( s ):
    return {'A':'T','T':'A','C':'G','G':'C'}[s]

s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
print ((frequentWordsWithMismatchesAndReverseComplements(s,k,d)))


def frequentWordsWithMismatches( s, k, d ):
    counts = {}
    for i in xrange(len(s)-k+1):
        for neighbor in neighbors(s[i:i+k],d):
            if neighbor not in counts:
                counts[neighbor] = 0
            counts[neighbor] += 1
    m = max(counts.values())
    return [kmer for kmer in counts if counts[kmer] == m]

def neighbors( s, d ):
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    out = []
    for neighbor in neighbors(s[1:],d):
        if hamming(s[1:],neighbor) < d:
            out.extend(['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor])
        else:
            out.append(s[0] + neighbor)
    return out

def hamming( s, t ):
    return sum([s[i] != t[i] for i in xrange(len(s))])

s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
print (frequentWordsWithMismatches(s,k,d))