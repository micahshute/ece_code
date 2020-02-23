from crypto.functions import max_i_el
from crypto.frequency_analysis import *
from crypto.vigenere_cipher_cracker import *
from crypto.substitution_cipher_cracker import *
from crypto.column_cipher_cracker import *
from crypto.hill_cipher_cracker import *
from crypto.playfair_cipher_cracker import *

# SOLVED: 
# cipher1 - hill
# cipher2 - substitution
# cipher3 - playfair
# cipher4 - column xpose
# cipher5 - vigenere


cipher1 = "jtdjjmxlfmjhvpyhlzhzkzuwabeallvdlurzvtnloriyvmnkkkvqprimzuvikzluncvpeklhggmuvztgwzoqbevilzlhxoncduoaqsvtmghwrarslzlhxohwbsbekykzraimrznxgnradxjhpivdhjlpxvhzuidwoewihjmujmlzlhnaxvyhraimbllhzfbaooujoemxpuwopizyvdyolknaguhvrwmujplzsvjtjyfcmwaglbsaimyskymlgsilusradgramuxfpillbckgundwwfgyfptllpizhjbezbnabavtpiypxwrsakkrcqbnxvlnmwxfkzcegiugfcojdwzfdhmussjmnxyosvprmlvdrnwqrzgwfcncmqyhlziwnksvkzluwqrzfxfhblblugratgxkowxoypuiitvilzlhpuwqpbpincooatrzbnjfuchvlbhkfcjqksfioemlfhpbrzhvbeookzpicofhcnbezhfxfqbansiozkvnkywqdjfrabvigcnkfdwafhnvmuucmxvijyscklsmbrjmpilugutfjmvdkzseprwzywtgcgxmlphjtqqgceyhrwoeyv"
cipher2 = "apyuhxqjapouhjrjoqnrjmjjitnhjsdsxctnfjoqnhmjjindonshpdtnfsikxopymujtnfsikusdjtjnictnfsikxopymujsxcmyxusxxujkpphbpyuuhpnanxjosikxqjuncxbjnocgopexqjtsihqnctnibanxgqhpkccptjxstjcxqjbmnofyiijgjccnosubmyxnascjtniijrjoskipojcxqjsoanoisiktbtjnisikcsteubscxqnxaqnxjrjosqnrjxosjhxphpsiusdjsqnrjxosjhasxqnuutbqjnoxxphpajuuxqnxaqnxjrjosqnrjhjrpxjhtbcjudxpsqnrjhjrpxjhtbcjudxpgpteujxjubxqnxsikojnxnstcnihsictnuusqnrjnuanbcmjjixqpopykqubsijnoijcxdntjscnejnoutnibhsrjdponihpiubndjamosikyejrjiaqjixqjbhpsxscipxejodjgxnihxqjbcskqdpotpojnihupcjmjxxjoxqsikcsicxoykkusikdpoxqjtascjubnihcupaxqjbcxytmujxqnxoyidncxv"
cipher3 = "bhgetacdbhlmtdktcotxtuakysltacxaeyplcscoltutdspxilhaibplxcmwlocbgtlsexhpzmaxlsdlynplxcmwlocbgtdlrncpnclicrdaoabhgeaqcbnyioliyliclslsutcibadslcdodpudthdolaxoespeclycslaoslycmdborcebsuieizcatactkisuyecdmipausibpxivarpcshdsusytdoducpsuytgwyecdprwnidnsdpnblahothumycslaoslyecdbvlickpqsesupecrtmfwalfhusplpqtklcrfyhclyecdrcfdhmhpblcdfhtdbhlmahpeaztfcbybcbbtkedpuashtscbcmdektpcywbebtkedpyhabictklcuashacytbedodedpteltmtivcstldorphplptycdlmnbtpdpenoicvcdcodltncbidktidnwrbcllalokequoaodcdbhlmencdpehaicbtwbcbetidktedlisdtaidaoaoyecdnslemgdsdpnwtydolucllaqdiorttacdrcyhuspcydcdpaigpacmsaserntportdpxcbdrdlol"
cipher4 = "aobfyhrceireherrnhmttmorastohshethetaooercaaornsriatdstiwlopaehrniartyodwtaoetoodhedoeftebestesrstilueuowbsfphiounaenerneahatdivtehpbhsdrousirittrirdsiiindrgdtggoxatnahetcaottfhpaofyeornyjadefoaehhebtntiueaaaoariswtweosnuyntylrheahnabtetwewdntsortreeitnonrnowiumtinlnthcernhrysrmtietayarntdlettetktthhecihduleesoeusanknatsnentnlndseisiihdtnhgnayhtnmitwultrondnetwolptorlnieroeyitrsfndfteoethosnldriitiieetnegyondhntouerecennetgnzerensngbhoivomgefioinobothtdeidpteipeshanetwuoosjhhifehrlfascidvtnbnladjtwinahiritagnnnhnntardmwswydilhgtfioeycaoetoaghatyehcueaieuhhsinenlsauoeggigghractiao"
cipher5 = "rhzjeykdwemafgblsubspvxcyhsbvmkvyamvcgzgguavgzlokrnrltbclgnelkjkntmpgwfcsezfkzalbsdxkftngyzoglzrvteloqrvlxitjrxlrjhknrhcybpgyrukuekumguguwsycyvmabuignpmxmhwkvbywugyputkjomqydyclcyyzgnxmrebczjcytgzbaslflzvzstrzaizdjgvitqoamxvalgezvlmxgomcjhbxprjsxntvmoquklvzqcukkmzkrypuayrvzbmyknjyibcxpufmzryoqihszsukbnhpocgakygggkkzuonlmybrzamsdoktrmunnzewthyoyiyqofshzkobtppernntwqyweadxsmyguybnhgxzyhjkvteqlhpuxiydxbsfqyxajpvyrgajbvmlgntrqqgvjtvthzkywrgbrytzkdfzssxmatneghortoijuognxiikbzsixyygnxiougnpchpknzamkyvrdtxcgqytathpkdwgpoyetajlfklwkqinzmmxhqctxyrgxkttuqtztqknopqbvmxcoemyyrjgrazkrayyysgycaqiknrlvsq"


emails = [cipher1, cipher2, cipher3, cipher4, cipher5]
faobjs = [FrequencyAnalysis(txt) for txt in emails]

fa1, fa2, fa3, fa4, fa5 = faobjs

cracked_emails = {}

print('\n\n\n')
print('###############################################')
print('###############################################')
print('#########  BREAK VIGENERE CIPHER  #############')
print('###############################################')
print('###############################################')
print('\n\n\n')


vcracker1 = VigenereCipherCracker(fa1)
vcracker2 = VigenereCipherCracker(fa2)
vcracker3 = VigenereCipherCracker(fa3)
vcracker4 = VigenereCipherCracker(fa4)
vcracker5 = VigenereCipherCracker(fa5)

vctest1 = vcracker1.crack()

vctest2 = vcracker2.crack()
vctest3 = vcracker3.crack()
vctest4 = vcracker4.crack()
vctest5 = vcracker5.crack()

vc_poss_1 = FrequencyAnalysis(vctest1[1])
vc_poss_2 = FrequencyAnalysis(vctest2[1])
vc_poss_3 = FrequencyAnalysis(vctest3[1])
vc_poss_4 = FrequencyAnalysis(vctest4[1])
vc_poss_5 = FrequencyAnalysis(vctest5[1])

possibilities = [vc_poss_1, vc_poss_2, vc_poss_3, vc_poss_4, vc_poss_5]

i, el = max_i_el(possibilities, lambda a,b: abs(a.english_correlation() - 0.065) < abs(b.english_correlation() - 0.065))

print(f"\nEMAIL {i + 1} WAS ENCIPHERED WITH THE VIGENERE CIPHER\n\nKEY:\n{vctest5[0]}\nTEXT:\n{el.ciphertext}")

cracked_emails['vigenere'] = f"Email {i + 1}:\nKEY:{vctest5[0]}\nTEXT:\n{el.ciphertext}"

#
print('\n\n\n')
print('###############################################')
print('###############################################')
print('#########  BREAK SUBSTITUTION CIPHER  #########')
print('###############################################')
print('###############################################')
print('\n\n\n')


################ NOTTE ###################
# For this solution, I was able to get close using the automated crack functionality, so I programmed in
# functionality that let me input known correct key-value pairs and the algorithm would NOT swap those kv pairs.
# After getting a solution that was close, I was able to re-run the algorithm iteratively with new letters I could
# get from the previous output, which got me the solution after only a few runs
# Commented out below are some of the initial solutions you get when you run it with no known values

emails = emails[:-1]




crk = SubstitutionCipherCracker(fa2)
# key, soln = crk.crack() <-- RUN THIS FIRST to begin iterative cracking

gsoln = {
    "X": "T", 
    "J": "E", 
    "Q": "H", 
    "A": "W", 
    "P": "O", 
    "Y": "U", 
    "I": "N", 
    "H": "D", 
    "S": "I",
    "C": "S",
    "U": "L",
    "O": "R",
    "M": "B",
    "R": "V",
    "D": "F",
    "B": "Y",
    "F": "K",
    "T": "M"
    
    }
key, soln = crk.crack(gsoln)

print("EMAIL 2 WAS THE EMAIL ENCRYPTED WITH A SUBSTITUTION CIPHER. THE ANSWER IS:\n")
print(f"KEY:\n{key}\n")
print(f"TEXT:\n{soln}\n\n")
cracked_emails['substitution'] = f"Email 2\nKEY:{key}\nTEXT:\n{soln}"

# SOLUTION KEY / TEXT
# {'J': 'E', 'X': 'T', 'N': 'A', 'S': 'I', 'I': 'N', 'P': 'O', 'O': 'R', 'U': 'L', 'Q': 'H', 'C': 'S', 'T': 'M', 'H': 'D', 'B': 'Y', 'K': 'G', 'A': 'W', 'R': 'V', 'D': 'F', 'Y': 'U', 'M': 'B', 'E': 'P', 'F': 'K', 'G': 'C', 'V': 'J'}
# WOULDTHEWORLDEVERHAVEBEENMADEIFITSMAKERHADBEENAFRAIDOFMAKINGTROUBLEMAKINGLIFEMEANSMAKINGTROUBLEITSBUTLITTLEGOODYOULLDOAWATERINGTHELASTYEARSCROPTHEMINDHASMANYWATCHDOGSSOMETIMESTHEYBARKUNNECESSARILYBUTAWISEMANNEVERIGNORESTHEIRWARNINGMYMEANINGSIMPLYISTHATWHATEVERIHAVETRIEDTODOINLIFEIHAVETRIEDWITHALLMYHEARTTODOWELLTHATWHATEVERIHAVEDEVOTEDMYSELFTOIHAVEDEVOTEDMYSELFTOCOMPLETELYTHATINGREATAIMSANDINSMALLIHAVEALWAYSBEENTHOROUGHLYINEARNESTFAMEISAPEARLMANYDIVEFORANDONLYAFEWBRINGUPEVENWHENTHEYDOITISNOTPERFECTANDTHEYSIGHFORMOREANDLOSEBETTERTHINGSINSTRUGGLINGFORTHEMWISELYANDSLOWTHEYSTUMBLETHATRUNFASTJ



# PREVIOUS OUTPUTS WITHOUTT ENTERING KNOWN KV PAIRS:

# {'J': 'E', 'X': 'T', 'N': 'A', 'S': 'I', 'I': 'N', 'P': 'O', 'O': 'S', 'U': 'M', 'Q': 'H', 'C': 'C', 'T': 'F', 'H': 'D', 'B': 'V', 'K': 'G', 'A': 'W', 'R': 'R', 'D': 'Y', 'Y': 'U', 'M': 'P', 'E': 'B', 'F': 'L', 'G': 'K', 'V': 'J'}
# WOUMDTHEWOSMDERESHAREPEENFADEIYITCFALESHADPEENAYSAIDOYFALINGTSOUPMEFALINGMIYEFEANCFALINGTSOUPMEITCPUTMITTMEGOODVOUMMDOAWATESINGTHEMACTVEASCKSOBTHEFINDHACFANVWATKHDOGCCOFETIFECTHEVPASLUNNEKECCASIMVPUTAWICEFANNERESIGNOSECTHEISWASNINGFVFEANINGCIFBMVICTHATWHATERESIHARETSIEDTODOINMIYEIHARETSIEDWITHAMMFVHEASTTODOWEMMTHATWHATERESIHAREDEROTEDFVCEMYTOIHAREDEROTEDFVCEMYTOKOFBMETEMVTHATINGSEATAIFCANDINCFAMMIHAREAMWAVCPEENTHOSOUGHMVINEASNECTYAFEICABEASMFANVDIREYOSANDONMVAYEWPSINGUBERENWHENTHEVDOITICNOTBESYEKTANDTHEVCIGHYOSFOSEANDMOCEPETTESTHINGCINCTSUGGMINGYOSTHEFWICEMVANDCMOWTHEVCTUFPMETHATSUNYACTJ

# {'J': 'E', 'X': 'T', 'N': 'A', 'S': 'I', 'I': 'N', 'P': 'O', 'O': 'U', 'U': 'W', 'Q': 'H', 'C': 'S', 'T': 'Y', 'H': 'D', 'B': 'P', 'K': 'G', 'A': 'M', 'R': 'R', 'D': 'C', 'Y': 'F', 'M': 'J', 'E': 'V', 'F': 'L', 'G': 'K', 'V': 'B'}
# MOFWDTHEMOUWDEREUHAREJEENYADEICITSYALEUHADJEENACUAIDOCYALINGTUOFJWEYALINGWICEYEANSYALINGTUOFJWEITSJFTWITTWEGOODPOFWWDOAMATEUINGTHEWASTPEAUSKUOVTHEYINDHASYANPMATKHDOGSSOYETIYESTHEPJAULFNNEKESSAUIWPJFTAMISEYANNEREUIGNOUESTHEIUMAUNINGYPYEANINGSIYVWPISTHATMHATEREUIHARETUIEDTODOINWICEIHARETUIEDMITHAWWYPHEAUTTODOMEWWTHATMHATEREUIHAREDEROTEDYPSEWCTOIHAREDEROTEDYPSEWCTOKOYVWETEWPTHATINGUEATAIYSANDINSYAWWIHAREAWMAPSJEENTHOUOFGHWPINEAUNESTCAYEISAVEAUWYANPDIRECOUANDONWPACEMJUINGFVERENMHENTHEPDOITISNOTVEUCEKTANDTHEPSIGHCOUYOUEANDWOSEJETTEUTHINGSINSTUFGGWINGCOUTHEYMISEWPANDSWOMTHEPSTFYJWETHATUFNCASTB

print('\n\n\n')
print('###############################################')
print('###############################################')
print('#########  BREAK COLUMN CIPHER  ###############')
print('###############################################')
print('###############################################')
print('\n\n\n')

#########################
#NOTE: Just like with the substitution cipher, the original output gives good info but not enough.
# The original output will show how many columns there are, and from there you can use the output to determine
# which columns were likely correct. Then input into the `crack` method which columns you do NOT want changed
# Do that a few times, and the output is correct 

txt = fa4.ciphertext

col_breaker = ColumnCipherCracker(fa4)

# init_crack = col_breaker.crack() #<--- RUN THIS FIRST (it takes a while)
# The return value indicates that the key size is 10. 
# The code below gets the answer using iterative running of the code and adding more and more correct columns
# print(init_crack)
data = col_breaker.get_best_text(10, {0: 6, 1: 4, 2: 1, 3: 7, 4: 5, 5: 2, 7: 3, 9: 0})

print("EMAIL 4 WAS ENCRYPTED WITH A COLUMN CIPHER \n")
print(f"KEY:\n{data['key']}")
print(f"TEXT:\n{data['msg']}")

cracked_emails['column_transposition'] = f"Email 4\nKEY:{data['key']}\nTEXT:\n{data['msg']}"
# ANSWER KEY: [6, 4, 1, 7, 5, 2, 8, 3, 9, 0]

# ANSWER PLAINTEXT: YETNOTAHUNDREDPEOPLEINTHATBATTLEKNEWFORWHATTHEYFOUGHTORWHYNOTAHUNDREDOFTHEINCONSIDERATEREJOICERSINTHEVICTORYWHYTHEYREJOICEDNOTHALFAHUNDREDPEOPLEWERETHEBETTERFORTHEGAINORLOSSNOTHALFADOZENMENAGREETOTHISHOURONTHECAUSEORMERITSANDNOBODYINSHORTEVERKNEWANYTHINGDISTINCTABOUTITBUTTHEMOURNERSOFTHESLAINITISAFAIREVENHANDEDNOBLEADJUSTMENTOFTHINGSTHATWHILETHEREISINFECTIONINDISEASEANDSORROWTHEREISNOTHINGINTHEWORLDSOIRRESISTIBLYCONTAGIOUSASLAUGHTERANDGOODHUMOURNEXTTOTRYINGANDWINNINGTHEBESTTHINGISTRYINGANDFAILINGHAPPYARETHEYTHATHEARTHEIRDETRACTIONSANDCANPUTTHEMTOMENDINGWITISALWAYSATTHEELBOWOFWANT


#NOTE: Below are previous outputs that give information about which columns are correct
# {'key': [6, 5, 1, 7, 4, 2, 8, 3, 9, 0], 'msg': 'YETNTOAHUNDREDEPOPLEINTHTABATTLEKNWEFORWHATTEHYFOUGHTOWRHYNOTAHUDNREDOFTHENICONSIDERTAEREJOICESRINTHEVICOTRYWHYTHERYEJOICEDNTOHALFAHUNRDEDPEOPLEEWRETHEBETETRFORTHEGIANORLOSSNTOHALFADOZNEMENAGREEOTTHISHOURNOTHECAUSEROMERITSANNDOBODYINSOHRTEVERKNWEANYTHINGIDSTINCTABUOTITBUTTHMEOURNERSOTFHESLAINIITSAFAIREVNEHANDEDNOLBEADJUSTMNETOFTHINGTSHATWHILEHTEREISINFCETIONINDIESASEANDSORROWTHEREINSOTHINGINHTEWORLDSORIRESISTIBYLCONTAGIOSUASLAUGHTREANDGOODHMUOURNEXTTTORYINGANDIWNNINGTHEEBSTTHINGITSRYINGANDAFILINGHAPYPARETHEYTAHTHEARTHERIDETRACTINOSANDCANPTUTHEMTOMEDNINGWITISLAWAYSATTHEELBOWOFWATN', 'bigram_divergence': 6.932081911262787e-05}
# {'key': [4, 8, 1, 5, 9, 2, 6, 3, 7, 0], 'msg': 'YETNAHUNPEDREDOPLEATINTHBATTEWLEKNFORWHEHATTYFOURWGHTOHYNONDTAHUREDOINFTHECONSATIDEREREJRSOICEINTHTOEVICRYWHYRYTHEEJOIOTCEDNHALFDRAHUNEDPEWEOPLERETHTEEBETRFORAITHEGNORLOTOSSNHALFENADOZMENATOGREETHISONHOURTHECORAUSEMERIDNTSANOBODHOYINSRTEVEWERKNANYTDIHINGSTINOUCTABTITBEMUTTHOURNFTERSOHESLTIAINISAFAENIREVHANDBLEDNOEADJENUSTMTOFTSTHINGHATWTHHILEEREIECSINFTIONSEINDIASEARRNDSOOWTHSNEREIOTHITHNGINEWORIRLDSORESILYSTIBCONTUSAGIOASLAERUGHTANDGUMOODHOURNOTEXTTRYINWIGANDNNINBEGTHESTTHSTINGIRYINFAGANDILINPYGHAPARETHAHEYTTHEAIRRTHEDETRONACTISANDUTCANPTHEMNDTOMEINGWALITISWAYSEEATTHLBOWNTOFWAOT', 'bigram_divergence': 6.692832764504039e-06}


print('\n\n\n')
print('###############################################')
print('###############################################')
print('#########  BREAK HILL 2x2 CIPHER  #############')
print('###############################################')
print('###############################################')
print('\n\n\n')


hcracker = Hill2x2CipherCracker(faobjs[0])

key, soln = hcracker.crack()

print("EMAIL 1 WAS ENCRYPTED WITH A HILL 2X2 CIPHER\n")
print(f"KEY:\n{key}\n")
print(f"TEXT:\n{soln}\n")
cracked_emails['hill2x2'] = f"Email 1\nKEY:{key}\nTEXT:\n{soln}"



print('\n\n\n')
print('###############################################')
print('###############################################')
print('#########  BREAK PLAYFIAR CIPHER  #############')
print('###############################################')
print('###############################################')
print('\n\n\n')

# NOTE: I was not able to get an EXACT key from this. There is a relatively consistant output of text which is
# very close to the actual plaintext, with the key usually containing the proper letters in their row, but the 
# rows and letters are out of order. It gives you enough information to crack the key and text by hand the
# rest of the way. I wish I had been able to get a full solution with code but did not have time time. 

# My scoring function WILL score the correct answer the highest, but there are a lot of local maxima that
# require many iterations to actually find it. Much more than the amount running now
# I think to make this run faster and to be 100% accurate, I need a better scoring function.
# From what I can see, it looks like some people use pre-made tables to score that are specifically
# designed for the playfair 
# I think to get the actual answer faster if I updated my scoring function

# As of now, to get the answer, you have to either drastically increase the iterations or run the 
# below code a few times to get an answer that is close, then solve the rest by hand.

# The answers are:
key = [['Q', 'V', 'X', 'Z', 'K'], ['H', 'O', 'I', 'R', 'C'], ['D', 'T', 'A', 'L', 'E'], ['N', 'Y', 'P', 'M', 'S'], ['W', 'B', 'F', 'G', 'U']]
plaintext = "WOULDTHEWORLDEVERHAVEBEENMADEIFITSMAKERHADBEENAFRAIDOFMAKINGTROUBLEMAKINGLIFEMEANSMAKINGTROUBLEAHMISSHARRIETITWOULDDOUSNOHARMTOREMEMBEROFTENERTHANWEDOTHATVICESARESOMETIMESONLYVIRTUESCARRIEDTOEXCESSTHEPRAISEOFAFOOLISINCENSETOTHEWISESTOFUSTHEMINDHASMANYWATCHDOGSSOMETIMESTHEYBARKUNNECESSARILYBUTAWISEMANNEVERIGNORESTHEIRWARNINGTHEWIDEWORLDISALLABOUTYOUYOUCANFENCEYOURSELVESINBUTYOUCANNOTFOREVERFENCEITOUTTHELANDLADYLOOKEDATHIMINAMOTHERLYWAYANDSHOOKHERHEADYOUHAVEHADNOGREATTRUCKWITHTHEWORLDSHESAIDORYOUWOULDHAVELEARNEDTHATITISTHESMALLMENANDNOTTHEGREATWHOHOLDTHEIRNOSESINTHEAIRFAIRSPEECHMAYHIDEAFOULHEART"


# NOTE: Here are some examples of outputs of the crack() method - the keys and the associated plaintext. 
# As you can see, they are close enough to the correct answer that the rest is able to be done by hand
# [['C', 'H', 'O', 'I', 'F'], ['E', 'D', 'T', 'A', 'L'], ['S', 'N', 'Y', 'P', 'R'], ['U', 'W', 'B', 'G', 'M'], ['K', 'Z', 'V', 'X', 'Q']]
# WOUADTHEWOFRDEVEFHAVEBEENRADEIGITSRAKEFHADBEENAGFAIDOGRAKIGUTFOUBAERAKINQWIGEREANSRAKIGUTFOUBAEAPSISSHAFFSETITWOUALLOUSNOHAFRTOFERERBEFOGTENEFTHANWEDOTHATVICESAFESORETIRESOWLYVSFTUESCAHHIEDTOEXCESSTHEGFAISEOGAGOOLPSINCENSETOTHEWISESTOBUSTHEYPNDHASRANYWATCHDOMGSORETIRESTHEYBAFKURRECESSAFSLBHMTAICSERARREVEFLQNOFESTHESFHLFWINMTHEICDEWOFRDISADDLOOUTYOUYOUCANGENCEYOUFUELVESINBUTYOUCANNOTGOFEVEFGENCEITOUTTHELANDLADBLOOKEDATHPYINAROTHEFRYWAYANDSHOOKHEFHEADYOUHAVEHADNYMFEATTFUCKMITHTHEWOFRDSHESAIDOFYOUWOULDHAVELEAFNEDTHATITISTHESRALGBENANDNOTTHEMFEATZLOHYLDTHESFNOSESINTHEAIXPAIFUPEECPSAYFYDEAGOULNEAFT
# And, after run through "key refinement" method (which is usually a waste of time)
# [['C', 'H', 'O', 'I', 'R'], ['E', 'D', 'T', 'A', 'L'], ['S', 'N', 'Y', 'P', 'F'], ['U', 'W', 'B', 'G', 'M'], ['K', 'Q', 'V', 'X', 'Z']]
# WOUADTHEWORFDEVERHAVEBEENFADEIGITSFAKERHADBEENAGRAIDOGFAKIGUTROUBAEFAKINMFIGEFEANSFAKIGUTROUBAEAHFISSHARRIETITWOUADDOUSNOHARFTOREFEFBEROGTENERTHANWEDOTHATVICESARESOFETIFESOWLYVIRTUESCARRIEDTOEXCESSTHEGRAISEOGAGOOLISINCENSETOTHEWISESTOBUSTHEFINDHASFANYWATCHDOMGSOFETIFESTHEYBARKUNNECESSARILBNMTANRSEFANNEVERZLNORESTHEIRNLRWINMTHENRDEWORFDISALLLYOUTYOUYOUCANGENCEYOURUELVESINBUTYOUCANNOTGOREVERGENCEITOUTTHELANDLADBLOOKEDATHIFINAFOTHERFYWAYANDSHOOKHERHEADYOUHAVEHADNOMREATTRUCKWITHTHEWORFDSHESAIDORYOUWOULDHAVELEARNEDTHATITISTHESFALGBENANDNOTTHEMREATWHOHOLDTHEIRNOSESINTHEAIXPAIRUPEECHFAYHIDEAGOULHEART
crk = PlayfairCipherCracker(fa3)

bkey, faans = crk.crack()
print(f"A key that MIGHT BE close to the answer: {bkey}")
print(f"A plaintext which MIGHT BE able to be read: {faans.ciphertext}")


print("EMAIL 3 WAS ENCRYPTED WITH A PLAYFAIR CIPHER \n")
print(f"KEY:\n{key}")
print(f"TEXT:\n{plaintext}")
cracked_emails['playfair'] = f"Email 3\nKEY:{key}\nTEXT:\n{plaintext}"




answer = {f"{k}\n" + v for k,v in cracked_emails.items()}
print(answer)