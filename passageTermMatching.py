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
#keywords = ['lincoln','civil war president','assassinated president']
textFiles = ['docs\AbrahamLincoln.txt','docs\AndrewJackson.txt','docs\AndrewJohnson.txt','docs\BarackObama.txt','docs\BenjaminHarrison.txt','docs\BillClinton.txt',
             'docs\CalvinCoolidge.txt','docs\ChesterArthur.txt','docs\DwightEisenhower.txt','docs\FranklinDRoosevelt.txt','docs\FranklinPierce.txt','docs\GeorgeBush.txt',
             'docs\GeorgeWashington.txt','docs\GeorgeWBush.txt','docs\GeraldFord.txt','docs\GroverCleveland.txt','docs\HarryTruman.txt','docs\HerbertHoover.txt',
             'docs\JamesBuchanan.txt','docs\JamesGarfield.txt','docs\JamesMadison.txt','docs\JamesMonroe.txt','docs\JamesPolk.txt','docs\JimmyCarter.txt',
             'docs\JohnAdams.txt','docs\JohnKennedy.txt','docs\JohnQuincyAdams.txt','docs\JohnTyler.txt','docs\LyndonJohnson.txt','docs\MartinVanBuren.txt','docs\MillardFillmore.txt',
             'docs\RichardNixon.txt','docs\RonaldReagan.txt','docs\RutherfordHayes.txt','docs\TheodoreRoosevelt.txt','docs\ThomasJefferson.txt','docs\UlyssesGrant.txt',
             'docs\WarrenHarding.txt','docs\WilliamHenryHarrison.txt','docs\WilliamMcKinley.txt','docs\WilliamTaft.txt','docs\WoodrowWilson.txt','docs\ZacharyTaylor.txt']

''' Passage Term Matching variables: '''
N = len(textFiles)

'''----------------------------------------------------------------
    Algorithms:
-------------------------------------------------------------------'''

def passageTermMatching():
    contain = 0 #ok
    prevContain = 0 #ok
    n = 0 #ok
    #lengthDocs = []
    idfList = []
    wList = []
    #termInPassage = []
    scores = []
    nList = []
    #preScore = []
    #result = []
    
    for i in range(len(keywords)):
        for j in range(len(textFiles)):
            lenD, freq = readFile(textFiles[j], keywords[i])
            contain = contain + freq
            
            if contain != prevContain:
                n = n + 1
                #termInPassage.append(1)
            #else:
                #termInPassage.append(0)
            
            prevContain = contain
            
            #if i==0:
            #    lengthDocs.append(lenD)
        
        
        # Calculating the IDF:
        nList.append(n)    
        tmp = N/(n + 1)
        idf = math.log(tmp) #may need to use abs(x)
        idfList.append(idf)
        
        #clearing some variables:
        contain = 0
        n = 0
        
        
    for i in range(len(textFiles)):
        for j in range(len(keywords)):
            lengthD, frequency = readFile(textFiles[i], keywords[j])
            if frequency > 0:
                tmp1 = N/(nList[j] + 1)
                w = math.log(tmp1)
            else:
                w = 0
                
            wList.append(w)
            frequency = 0
            
        score = sum(wList)/sum(idfList)
        scores.append(score)
        
        #Clearing some variables:
        wList = []
        
    toBeOrdered = zip(textFiles,scores)
    
    result = sorted(toBeOrdered, key=lambda toBeOrdered: toBeOrdered[1],reverse=True)
    
    return result
    

    
'''---------------------------------------------------------------
    Running algorithms:
------------------------------------------------------------------'''
    
out = passageTermMatching()
print out[:10] 