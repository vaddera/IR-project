'''
Created on Oct 27, 2014

@author: vaddera
'''
import collections
import re
'''
count = 0
prevCount = 0
foundInDocument = 0

textFiles = ['docs\AbrahamLincoln.txt','docs\AndrewJackson.txt','docs\AndrewJohnson.txt','docs\BarackObama.txt','docs\BenjaminHarrison.txt','docs\BillClinton.txt',
             'docs\CalvinCoolidge.txt','docs\ChesterArthur.txt','docs\DwightEisenhower.txt','docs\FranklinDRoosevelt.txt','docs\FranklinPierce.txt','docs\GeorgeBush.txt',
             'docs\GeorgeWashington.txt','docs\GeorgeWBush.txt','docs\GeraldFord.txt','docs\GroverCleveland.txt','docs\HarryTruman.txt','docs\HerbertHoover.txt',
             'docs\JamesBuchanan.txt','docs\JamesGarfield.txt','docs\JamesMadison.txt','docs\JamesMonroe.txt','docs\JamesPolk.txt','docs\JimmyCarter.txt',
             'docs\JohnAdams.txt','docs\JohnKennedy.txt','docs\JohnQuincyAdams.txt','docs\JohnTyler.txt','docs\LyndonJohnson.txt','docs\MartinVanBuren.txt','docs\MillardFillmore.txt',
             'docs\RichardNixon.txt','docs\RonaldReagan.txt','docs\RutherfordHayes.txt','docs\TheodoreRoosevelt.txt','docs\ThomasJefferson.txt','docs\UlyssesGrant.txt',
             'docs\WarrenHarding.txt','docs\WilliamHenryHarrison.txt','docs\WilliamMcKinley.txt','docs\WilliamTaft.txt','docs\WoodrowWilson.txt','docs\ZacharyTaylor.txt']

lengthDocs = []
'''

def readFile(file_input, matchingWord):
    #termsCount = 0
    
    with open(file_input,'r') as content_file:
        content = content_file.read()
        words = re.split("\W+",content.lower())
        #if matchingWord in content:
            #termsCount = termsCount + 1

    wordsCount = len(words)        
    termsCount = collections.Counter(words)

    return (int(wordsCount),int(termsCount[matchingWord]))
    #return (int(wordsCount),termsCount)

'''---------------------------------------------------------------------
    Here the function is called and tested for each of the documents:
------------------------------------------------------------------------'''
'''
for i in range(len(textFiles)):
    lenDoc, newCount = readFile(textFiles[i],'the')
    lengthDocs.append(lenDoc)
    count = count + newCount
    
    if count != prevCount:
        foundInDocument = foundInDocument + 1
    
    prevCount = count
    print 'Length of the ' + str(i + 1) + ' document is ' + str(lengthDocs[i])
    print newCount
    
print 'Number of the counted specified words: ' + str(count)
print 'Keyword was found in ' + str(foundInDocument) + ' documents.'
'''