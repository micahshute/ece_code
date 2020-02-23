from python_resources.substitution_cipher_cracker import *
from python_resources.frequency_analysis import *

# SOLVED: 
# XXcipher1 - hill
# XXcipher2 - SUBS
# cipher3 - playfair *****
# XXcipher4 - column xpose
# XXcipher5 - vigenere

def subcipher(key, msg):
    return "".join([key[char] for char in msg])

cipher1 = "jtdjjmxlfmjhvpyhlzhzkzuwabeallvdlurzvtnloriyvmnkkkvqprimzuvikzluncvpeklhggmuvztgwzoqbevilzlhxoncduoaqsvtmghwrarslzlhxohwbsbekykzraimrznxgnradxjhpivdhjlpxvhzuidwoewihjmujmlzlhnaxvyhraimbllhzfbaooujoemxpuwopizyvdyolknaguhvrwmujplzsvjtjyfcmwaglbsaimyskymlgsilusradgramuxfpillbckgundwwfgyfptllpizhjbezbnabavtpiypxwrsakkrcqbnxvlnmwxfkzcegiugfcojdwzfdhmussjmnxyosvprmlvdrnwqrzgwfcncmqyhlziwnksvkzluwqrzfxfhblblugratgxkowxoypuiitvilzlhpuwqpbpincooatrzbnjfuchvlbhkfcjqksfioemlfhpbrzhvbeookzpicofhcnbezhfxfqbansiozkvnkywqdjfrabvigcnkfdwafhnvmuucmxvijyscklsmbrjmpilugutfjmvdkzseprwzywtgcgxmlphjtqqgceyhrwoeyv"
cipher2 = "apyuhxqjapouhjrjoqnrjmjjitnhjsdsxctnfjoqnhmjjindonshpdtnfsikxopymujtnfsikusdjtjnictnfsikxopymujsxcmyxusxxujkpphbpyuuhpnanxjosikxqjuncxbjnocgopexqjtsihqnctnibanxgqhpkccptjxstjcxqjbmnofyiijgjccnosubmyxnascjtniijrjoskipojcxqjsoanoisiktbtjnisikcsteubscxqnxaqnxjrjosqnrjxosjhxphpsiusdjsqnrjxosjhasxqnuutbqjnoxxphpajuuxqnxaqnxjrjosqnrjhjrpxjhtbcjudxpsqnrjhjrpxjhtbcjudxpgpteujxjubxqnxsikojnxnstcnihsictnuusqnrjnuanbcmjjixqpopykqubsijnoijcxdntjscnejnoutnibhsrjdponihpiubndjamosikyejrjiaqjixqjbhpsxscipxejodjgxnihxqjbcskqdpotpojnihupcjmjxxjoxqsikcsicxoykkusikdpoxqjtascjubnihcupaxqjbcxytmujxqnxoyidncxv"
cipher3 = "bhgetacdbhlmtdktcotxtuakysltacxaeyplcscoltutdspxilhaibplxcmwlocbgtlsexhpzmaxlsdlynplxcmwlocbgtdlrncpnclicrdaoabhgeaqcbnyioliyliclslsutcibadslcdodpudthdolaxoespeclycslaoslycmdborcebsuieizcatactkisuyecdmipausibpxivarpcshdsusytdoducpsuytgwyecdprwnidnsdpnblahothumycslaoslyecdbvlickpqsesupecrtmfwalfhusplpqtklcrfyhclyecdrcfdhmhpblcdfhtdbhlmahpeaztfcbybcbbtkedpuashtscbcmdektpcywbebtkedpyhabictklcuashacytbedodedpteltmtivcstldorphplptycdlmnbtpdpenoicvcdcodltncbidktidnwrbcllalokequoaodcdbhlmencdpehaicbtwbcbetidktedlisdtaidaoaoyecdnslemgdsdpnwtydolucllaqdiorttacdrcyhuspcydcdpaigpacmsaserntportdpxcbdrdlol"
cipher4 = "aobfyhrceireherrnhmttmorastohshethetaooercaaornsriatdstiwlopaehrniartyodwtaoetoodhedoeftebestesrstilueuowbsfphiounaenerneahatdivtehpbhsdrousirittrirdsiiindrgdtggoxatnahetcaottfhpaofyeornyjadefoaehhebtntiueaaaoariswtweosnuyntylrheahnabtetwewdntsortreeitnonrnowiumtinlnthcernhrysrmtietayarntdlettetktthhecihduleesoeusanknatsnentnlndseisiihdtnhgnayhtnmitwultrondnetwolptorlnieroeyitrsfndfteoethosnldriitiieetnegyondhntouerecennetgnzerensngbhoivomgefioinobothtdeidpteipeshanetwuoosjhhifehrlfascidvtnbnladjtwinahiritagnnnhnntardmwswydilhgtfioeycaoetoaghatyehcueaieuhhsinenlsauoeggigghractiao"
cipher5 = "rhzjeykdwemafgblsubspvxcyhsbvmkvyamvcgzgguavgzlokrnrltbclgnelkjkntmpgwfcsezfkzalbsdxkftngyzoglzrvteloqrvlxitjrxlrjhknrhcybpgyrukuekumguguwsycyvmabuignpmxmhwkvbywugyputkjomqydyclcyyzgnxmrebczjcytgzbaslflzvzstrzaizdjgvitqoamxvalgezvlmxgomcjhbxprjsxntvmoquklvzqcukkmzkrypuayrvzbmyknjyibcxpufmzryoqihszsukbnhpocgakygggkkzuonlmybrzamsdoktrmunnzewthyoyiyqofshzkobtppernntwqyweadxsmyguybnhgxzyhjkvteqlhpuxiydxbsfqyxajpvyrgajbvmlgntrqqgvjtvthzkywrgbrytzkdfzssxmatneghortoijuognxiikbzsixyygnxiougnpchpknzamkyvrdtxcgqytathpkdwgpoyetajlfklwkqinzmmxhqctxyrgxkttuqtztqknopqbvmxcoemyyrjgrazkrayyysgycaqiknrlvsq"

emails = [cipher1, cipher2, cipher3, cipher4, cipher5]

faobjs = [FrequencyAnalysis(txt) for txt in emails]

fa1, fa2, fa3, fa4, fa5 = faobjs

crk = SubstitutionCipherCracker(fa2)
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

print(key)
print(soln)

# {'J': 'E', 'X': 'T', 'N': 'A', 'S': 'I', 'I': 'N', 'P': 'O', 'O': 'R', 'U': 'L', 'Q': 'H', 'C': 'S', 'T': 'M', 'H': 'D', 'B': 'Y', 'K': 'G', 'A': 'W', 'R': 'V', 'D': 'F', 'Y': 'U', 'M': 'B', 'E': 'P', 'F': 'K', 'G': 'C', 'V': 'J'}
# WOULDTHEWORLDEVERHAVEBEENMADEIFITSMAKERHADBEENAFRAIDOFMAKINGTROUBLEMAKINGLIFEMEANSMAKINGTROUBLEITSBUTLITTLEGOODYOULLDOAWATERINGTHELASTYEARSCROPTHEMINDHASMANYWATCHDOGSSOMETIMESTHEYBARKUNNECESSARILYBUTAWISEMANNEVERIGNORESTHEIRWARNINGMYMEANINGSIMPLYISTHATWHATEVERIHAVETRIEDTODOINLIFEIHAVETRIEDWITHALLMYHEARTTODOWELLTHATWHATEVERIHAVEDEVOTEDMYSELFTOIHAVEDEVOTEDMYSELFTOCOMPLETELYTHATINGREATAIMSANDINSMALLIHAVEALWAYSBEENTHOROUGHLYINEARNESTFAMEISAPEARLMANYDIVEFORANDONLYAFEWBRINGUPEVENWHENTHEYDOITISNOTPERFECTANDTHEYSIGHFORMOREANDLOSEBETTERTHINGSINSTRUGGLINGFORTHEMWISELYANDSLOWTHEYSTUMBLETHATRUNFASTJ




# {'J': 'E', 'X': 'T', 'N': 'A', 'S': 'I', 'I': 'N', 'P': 'O', 'O': 'S', 'U': 'M', 'Q': 'H', 'C': 'C', 'T': 'F', 'H': 'D', 'B': 'V', 'K': 'G', 'A': 'W', 'R': 'R', 'D': 'Y', 'Y': 'U', 'M': 'P', 'E': 'B', 'F': 'L', 'G': 'K', 'V': 'J'}
# WOUMDTHEWOSMDERESHAREPEENFADEIYITCFALESHADPEENAYSAIDOYFALINGTSOUPMEFALINGMIYEFEANCFALINGTSOUPMEITCPUTMITTMEGOODVOUMMDOAWATESINGTHEMACTVEASCKSOBTHEFINDHACFANVWATKHDOGCCOFETIFECTHEVPASLUNNEKECCASIMVPUTAWICEFANNERESIGNOSECTHEISWASNINGFVFEANINGCIFBMVICTHATWHATERESIHARETSIEDTODOINMIYEIHARETSIEDWITHAMMFVHEASTTODOWEMMTHATWHATERESIHAREDEROTEDFVCEMYTOIHAREDEROTEDFVCEMYTOKOFBMETEMVTHATINGSEATAIFCANDINCFAMMIHAREAMWAVCPEENTHOSOUGHMVINEASNECTYAFEICABEASMFANVDIREYOSANDONMVAYEWPSINGUBERENWHENTHEVDOITICNOTBESYEKTANDTHEVCIGHYOSFOSEANDMOCEPETTESTHINGCINCTSUGGMINGYOSTHEFWICEMVANDCMOWTHEVCTUFPMETHATSUNYACTJ

# {'J': 'E', 'X': 'T', 'N': 'A', 'S': 'I', 'I': 'N', 'P': 'O', 'O': 'U', 'U': 'W', 'Q': 'H', 'C': 'S', 'T': 'Y', 'H': 'D', 'B': 'P', 'K': 'G', 'A': 'M', 'R': 'R', 'D': 'C', 'Y': 'F', 'M': 'J', 'E': 'V', 'F': 'L', 'G': 'K', 'V': 'B'}
# MOFWDTHEMOUWDEREUHAREJEENYADEICITSYALEUHADJEENACUAIDOCYALINGTUOFJWEYALINGWICEYEANSYALINGTUOFJWEITSJFTWITTWEGOODPOFWWDOAMATEUINGTHEWASTPEAUSKUOVTHEYINDHASYANPMATKHDOGSSOYETIYESTHEPJAULFNNEKESSAUIWPJFTAMISEYANNEREUIGNOUESTHEIUMAUNINGYPYEANINGSIYVWPISTHATMHATEREUIHARETUIEDTODOINWICEIHARETUIEDMITHAWWYPHEAUTTODOMEWWTHATMHATEREUIHAREDEROTEDYPSEWCTOIHAREDEROTEDYPSEWCTOKOYVWETEWPTHATINGUEATAIYSANDINSYAWWIHAREAWMAPSJEENTHOUOFGHWPINEAUNESTCAYEISAVEAUWYANPDIRECOUANDONWPACEMJUINGFVERENMHENTHEPDOITISNOTVEUCEKTANDTHEPSIGHCOUYOUEANDWOSEJETTEUTHINGSINSTUFGGWINGCOUTHEYMISEWPANDSWOMTHEPSTFYJWETHATUFNCASTB









# txt = "HONESTPEOPLEDONTHIDETHEIRDEEDSHEATNOTAFURNACEFORYOURFOESOHOTTHATITDOSINGEYOURSELFTAKENOTHINGONITSLOOKSTAKEEVERYTHINGONEVIDENCETHERESNOBETTERRULEINHERITEDIDEASAREACURIOUSTHINGANDINTERESTINGTOOBSERVEANDEXAMINETHECOMPANIONSOFOURCHILDHOODALWAYSPOSSESSACERTAINPOWEROVEROURMINDSWHICHHARDLYANYLATERFRIENDCANOBTAINTRULYTOENJOYBODILYWARMTHSOMESMALLPARTOFYOUMUSTBECOLDFORTHEREISNOQUALITYINTHISWORLDTHATISNOTWHATITISMERELYBYCONTRASTNOTHINGEXISTSINITSELFNOBODYCANSPOILALIFEMYDEARTHATSNONSENSETHINGSHAPPENBUTWEBOBUPMYADVICEISNEVERDOTOMORROWWHATYOUCANDOTODAYPROCRASTINATIONISTHETHIEFOFTIMELAUGHTERISPOISONTOFEAR"

# alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# skey = "MROYKJGISHZETFQWVBPNXULADC"
# subskey = {}
# for i in range(len(alph)):
#     subskey[alph[i]] = skey[i]

# ciphertext = SubstitutionCipherCracker.cipher(subskey, txt)
# plaintext = SubstitutionCipherCracker.decipher(subskey, ciphertext)
# faplain = FrequencyAnalysis(txt)
# print(faplain.letter_frequencies())
# fatest = FrequencyAnalysis(ciphertext)
# print(subskey)
# print(ciphertext)
# print('--------')
# print(plaintext)
# crk = SubstitutionCipherCracker(fatest)


# naive_map = crk.crack()

# naive_soln = SubstitutionCipherCracker.cipher(naive_map, ciphertext)
print('----')
# print(naive_soln)
# print(faplain.bigram_correlation_distance())

# key, soln = crk.crack()
# print(key)
# print(soln)


# gsoln = {"Q": "O", "I": "H", "F": "N", "K": "E", "P": "S", "N": "T", "W": "P"}
# bkey, bsoln = crk.crack(gsoln)
# print(bkey)
# print(bsoln)


