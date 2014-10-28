'''
Created on Oct 27, 2014

@author: vaddera
'''
import collections
import re
#import sys

count = 0

textFiles = ['docs\AbrahamLincoln.txt','docs\AndrewJackson.txt','docs\AndrewJohnson.txt','docs\BarackObama.txt','docs\BenjaminHarrison.txt','docs\BillClinton.txt',
             'docs\CalvinCoolidge.txt','docs\ChesterArthur.txt','docs\DwightEisenhower.txt','docs\FranklinDRoosevelt.txt','docs\FranklinPierce.txt','docs\GeorgeBush.txt',
             'docs\GeorgeWashington.txt','docs\GeorgeWBush.txt','docs\GeraldFord.txt','docs\GroverCleveland.txt','docs\HarryTruman.txt','docs\HerbertHoover.txt',
             'docs\JamesBuchanan.txt','docs\JamesGarfield.txt','docs\JamesMadison.txt','docs\JamesMonroe.txt','docs\JamesPolk.txt','docs\JimmyCarter.txt',
             'docs\JohnAdams.txt','docs\JohnKennedy.txt','docs\JohnQuincyAdams.txt','docs\JohnTyler.txt','docs\LyndonJohnson.txt','docs\MartinVanBuren.txt','docs\MillardFillmore.txt',
             'docs\RichardNixon.txt','docs\RonaldReagan.txt','docs\RutherfordHayes.txt','docs\TheodoreRoosevelt.txt','docs\ThomasJefferson.txt','docs\UlyssesGrant.txt',
             'docs\WarrenHarding.txt','docs\WilliamHenryHarrison.txt','docs\WilliamMcKinley.txt','docs\WilliamTaft.txt','docs\WoodrowWilson.txt','docs\ZacharyTaylor.txt']

def readFile(file_input, matchingWord):
    
    with open(file_input,'r') as content_file:
        content = content_file.read()
        words = re.split("\W+",content.lower())
        
    words_count = collections.Counter(words)

    return int(words_count[matchingWord])

'''---------------------------------------------------------------------
    Here the function is called and tested for each of the documents:
------------------------------------------------------------------------'''

for i in range(len(textFiles)):
    newCount = readFile(textFiles[i],'the')
    count = count + newCount
    
print 'Number of the counted specified words: ' + str(count)