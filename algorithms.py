'''
Created on Oct 27, 2014

@author: vaddera
'''
'''---------------------------------------------------------------
    Imports:
------------------------------------------------------------------'''
from readFiles import readFile
import math
'''---------------------------------------------------------------
    Variable initialization
------------------------------------------------------------------'''
keywords = ['adams','lincoln','president','assassinated president','great president','first president','civil war president','second president','impeached','general','world war',
            'founding','democrat','republican','independent','congress','law']
textFiles = ['docs\AbrahamLincoln.txt','docs\AndrewJackson.txt','docs\AndrewJohnson.txt','docs\BarackObama.txt','docs\BenjaminHarrison.txt','docs\BillClinton.txt',
             'docs\CalvinCoolidge.txt','docs\ChesterArthur.txt','docs\DwightEisenhower.txt','docs\FranklinDRoosevelt.txt','docs\FranklinPierce.txt','docs\GeorgeBush.txt',
             'docs\GeorgeWashington.txt','docs\GeorgeWBush.txt','docs\GeraldFord.txt','docs\GroverCleveland.txt','docs\HarryTruman.txt','docs\HerbertHoover.txt',
             'docs\JamesBuchanan.txt','docs\JamesGarfield.txt','docs\JamesMadison.txt','docs\JamesMonroe.txt','docs\JamesPolk.txt','docs\JimmyCarter.txt',
             'docs\JohnAdams.txt','docs\JohnKennedy.txt','docs\JohnQuincyAdams.txt','docs\JohnTyler.txt','docs\LyndonJohnson.txt','docs\MartinVanBuren.txt','docs\MillardFillmore.txt',
             'docs\RichardNixon.txt','docs\RonaldReagan.txt','docs\RutherfordHayes.txt','docs\TheodoreRoosevelt.txt','docs\ThomasJefferson.txt','docs\UlyssesGrant.txt',
             'docs\WarrenHarding.txt','docs\WilliamHenryHarrison.txt','docs\WilliamMcKinley.txt','docs\WilliamTaft.txt','docs\WoodrowWilson.txt','docs\ZacharyTaylor.txt']

''' BM25 variables: '''
b = 0.75
k1 = 1.2 # can range from 1.2 to 2.0
N = len(textFiles)

'''----------------------------------------------------------------
    Algorithms:
-------------------------------------------------------------------'''

def BM25():
    contain = 0
    prevContain = 0
    n = 0
    lengthDocs = []
    idfList = []
    scores = []
    preScore = []
    #result = []
    
    for i in range(len(keywords)):
        for j in range(len(textFiles)):
            lenD, freq = readFile(textFiles[j], keywords[i])
            contain = contain + freq
            
            if contain != prevContain:
                n = n + 1
            
            prevContain = contain
            
            if i==0:
                lengthDocs.append(lenD)
        
        # Calculating the IDF:    
        tmp = (N - n + 0.5)/(n + 0.5)
        idf = math.log(abs(tmp))
        idfList.append(idf)
        
        # Clearing the accumulated values from the variables:
        contain = 0
        n = 0
    
    # Calculating avgdl:
    avgdl = sum(lengthDocs)/N # Makes no sense why there is an error here...
    
    for i in range(len(textFiles)):
        for j in range(len(keywords)):
            
            lengthD, frequency = readFile(textFiles[i], keywords[j])
            
            tmpScore = idfList[j]*((frequency * (k1 + 1))/(frequency + k1*(1 - b + b*(lengthD/avgdl))))
            
            preScore.append(tmpScore)
        
        score = sum(preScore) # sum all the calculated scores for the current document
        scores.append(score) # put each calculated score for each document in an array.
        preScore = [] # Clearing preScore list in order to not add old values

        
    #print scores
    
    toBeOrdered = zip(textFiles,scores)
    
    #print toBeOrdered
    
    result = sorted(toBeOrdered, key=lambda toBeOrdered: toBeOrdered[1],reverse=True)

    return result
    
'''---------------------------------------------------------------
    Running algorithms:
------------------------------------------------------------------'''
    
out = BM25()
print out 