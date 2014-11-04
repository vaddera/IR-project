'''
Created on Nov 3, 2014

@author: Ethan
'''
'''---------------------------------------------------------------
    Imports:
------------------------------------------------------------------'''
import math
import collections
import re
'''---------------------------------------------------------------
    Variable initialization
------------------------------------------------------------------'''
keywords = ['adams', 'lincoln', 'president', 'assassinated president', 'great president', 'first president', 'civil war president', 'second president', 'impeached', 'general', 'world war',
            'founding', 'democrat', 'republican', 'independent', 'congress', 'law']
# keywords = ['lincoln','civil war president','assassinated president']
textFiles = ['docs\AbrahamLincoln.txt', 'docs\AndrewJackson.txt', 'docs\AndrewJohnson.txt', 'docs\BarackObama.txt', 'docs\BenjaminHarrison.txt', 'docs\BillClinton.txt',
             'docs\CalvinCoolidge.txt', 'docs\ChesterArthur.txt', 'docs\DwightEisenhower.txt', 'docs\FranklinDRoosevelt.txt', 'docs\FranklinPierce.txt', 'docs\GeorgeBush.txt',
             'docs\GeorgeWashington.txt', 'docs\GeorgeWBush.txt', 'docs\GeraldFord.txt', 'docs\GroverCleveland.txt', 'docs\HarryTruman.txt', 'docs\HerbertHoover.txt',
             'docs\JamesBuchanan.txt', 'docs\JamesGarfield.txt', 'docs\JamesMadison.txt', 'docs\JamesMonroe.txt', 'docs\JamesPolk.txt', 'docs\JimmyCarter.txt',
             'docs\JohnAdams.txt', 'docs\JohnKennedy.txt', 'docs\JohnQuincyAdams.txt', 'docs\JohnTyler.txt', 'docs\LyndonJohnson.txt', 'docs\MartinVanBuren.txt', 'docs\MillardFillmore.txt',
             'docs\RichardNixon.txt', 'docs\RonaldReagan.txt', 'docs\RutherfordHayes.txt', 'docs\TheodoreRoosevelt.txt', 'docs\ThomasJefferson.txt', 'docs\UlyssesGrant.txt',
             'docs\WarrenHarding.txt', 'docs\WilliamHenryHarrison.txt', 'docs\WilliamMcKinley.txt', 'docs\WilliamTaft.txt', 'docs\WoodrowWilson.txt', 'docs\ZacharyTaylor.txt']
'''----------------------------------------------------------------
    Algorithms:
-------------------------------------------------------------------'''
def skipBiGrams():
    scores = []
    keys = makeBi()
    intersect = 0
    for j in range(len(textFiles)):
        terms = readFile(textFiles[j])
        
        for term in terms:
            if term in keys:
                intersect = intersect + 1
        
        scoreP = intersect / float(len(terms))
        scoreQ = intersect / float(len(keys))
        
        score = (2 * scoreP * scoreQ) / (scoreP + scoreQ)
        scores.append((textFiles[j], score))
        
    result = sorted(scores, key=lambda scores: scores[1],reverse=True)
    
    return result
        
def makeBi():
    keys = []
    for word1 in keywords:
        for word2 in keywords:
            word1 = word1.replace(" ", "")
            word2 = word2.replace(" ", "")
            keys.append(word1 + word2)
    return keys

def readFile(file_input):
    termsCount = []
    with open(file_input, 'r') as content_file:
        # lineContent = content_file.readlines()
        content = content_file.read()
        words = re.split("\W+", content.lower())
        for i in range(len(words)):
            if i+1 < len(words) and (words[i] + " " + words[i + 1]) in keywords:
                if (words[i + 2] + " " + words[i + 3]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 3])
                elif (words[i + 2] + " " + words[i + 3] + " " + words[i + 4]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 3] + words[i + 4])
                else:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2])
                    
                if (words[i + 3] + " " + words[i + 4]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 3] + words[i + 4])
                elif (words[i + 3] + " " + words[i + 4] + " " + words[i + 5]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 3] + words[i + 4] + words[i + 5])
                else:
                    termsCount.append(words[i] + words[i + 1] + words[i + 3])
                    
            elif i+2 < len(words) and (words[i] + " " + words[i + 1] + " " + words[i + 2]) in keywords:
                if (words[i + 3] + " " + words[i + 4]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 3] + words[i + 4])
                elif (words[i + 3] + " " + words[i + 4] + " " + words[i + 5]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 3] + words[i + 4] + words[i + 5])
                else:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 3])
                    
                if (words[i + 4] + " " + words[i + 5]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 4] + words[i + 5])
                elif (words[i + 4] + " " + words[i + 5] + " " + words[i + 6]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 4] + words[i + 5] + words[i + 6])
                else:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 4])
            else:
                if i+2 < len(words) and (words[i + 1] + " " + words[i + 2]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2])
                elif i+3 < len(words) and (words[i + 1] + " " + words[i + 2] + " " + words[i + 3]) in keywords:
                    termsCount.append(words[i] + words[i + 1] + words[i + 2] + words[i + 3])
                else:
                    if i+1 < len(words):
                        termsCount.append(words[i] + words[i + 1])
                if i+3 < len(words) and (words[i + 2] + " " + words[i + 3]) in keywords:
                    termsCount.append(words[i] + words[i + 2] + words[i + 3])
                elif i+4 < len(words) and (words[i + 2] + " " + words[i + 3] + " " + words[i + 4]) in keywords:
                    termsCount.append(words[i] + words[i + 2] + words[i + 3] + words[i + 4])
                else:
                    if i+2 < len(words):
                        termsCount.append(words[i] + words[i + 2])

    return termsCount
'''---------------------------------------------------------------
    Running algorithms:
------------------------------------------------------------------'''
    
out = skipBiGrams()
print out[:10] 
