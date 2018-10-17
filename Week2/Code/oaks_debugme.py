import csv
import sys
#import pdb
#import doctest


#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' """
    #pdb.set_trace()
    return (name.lower().startswith('quercus') and len(name)<8)

def main(argv):
    """Find whether a number x is even or odd.
    >>> is_an_oak('Fagus sylvatica') 
    False
    """

    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()
    for row in taxa:
        #print(row[0])
        if row[0] == "Genus":
            csvwrite.writerow([row[0], row[1]]) 
        else:
            print ("The genus is: ")
            print(row[0] + '\n')
            if is_an_oak(row[0]):
                print('FOUND AN OAK!\n')
                csvwrite.writerow([row[0], row[1]])    



    return 0
    


#import pdb; pdb.set_trace()
if (__name__ == "__main__"):
    status = main(sys.argv)



#doctest.testmod()

