from python_resources.playfair_cipher_cracker import *
from python_resources.frequency_analysis import *

# SOLVED: 
# cipher1 - hill
# cipher2 - subs???
# cipher3 - playfair??
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

# txt = "wouldtheworldeverhavebexnmadeifitsmakerhadbeenafraidofmakingtroublemakinglifemeansmakingtroubleahmissharrietitwouldxousnoharmtorememberoftenerthanwedothatvicesaresometimesonlyvirtuescarxiedtoexcessthepraiseofafoxlisincensetothewisestofusthemindhasmanywatchdogssometimestheybarkunxecessarilybutawisemanxeverignorestheirwarningthewideworldisalxaboutyouyoucanfenceyourselvesinbutyoucannotforeverfenceitoutthelandladyloxkedathiminamotherlywayandshookherheadyouhavehadnogreattruckwiththeworldshesaidoryouwouldhavelearnedthatitisthesmallmenandnotthegreatwhoholdtheirnosesintheairfairspeechmayhideafoulheart"
# crk = PlayfairCipherCracker(FrequencyAnalysis(txt))
# key = crk.random_key()



akey= [['Q', 'V', 'X', 'Z', 'K'], ['H', 'O', 'I', 'R', 'C'], ['D', 'T', 'A', 'L', 'E'], ['N', 'Y', 'P', 'M', 'S'], ['W', 'B', 'F', 'G', 'U']]

# print(key)
# ciphertext = crk.cipher(key, crk.ciphertext.replace("J", "I"))

# fatest = FrequencyAnalysis(ciphertext)
# plaintext = crk.decipher(key, ciphertext)
# print(plaintext)

# fkey = [['X', 'K', 'F', 'W', 'B'], ['I', 'R', 'C', 'H', 'O'], ['A', 'L', 'E', 'D', 'T'], ['P', 'M', 'S', 'N', 'Y'], ['G', 'Z', 'U', 'Q', 'V']]
# fkey = [['C', 'H', 'O', 'I', 'F'], ['E', 'D', 'T', 'A', 'L'], ['S', 'N', 'Y', 'P', 'R'], ['U', 'W', 'B', 'G', 'M'], ['K', 'Z', 'V', 'X', 'Q']]
# [['C', 'H', 'O', 'I', 'F'], ['E', 'D', 'T', 'A', 'L'], ['S', 'N', 'Y', 'P', 'R'], ['U', 'W', 'B', 'G', 'M'], ['K', 'Z', 'V', 'X', 'Q']]
# WOUADTHEWOFRDEVEFHAVEBEENRADEIGITSRAKEFHADBEENAGFAIDOGRAKIGUTFOUBAERAKINQWIGEREANSRAKIGUTFOUBAEAPSISSHAFFSETITWOUALLOUSNOHAFRTOFERERBEFOGTENEFTHANWEDOTHATVICESAFESORETIRESOWLYVSFTUESCAHHIEDTOEXCESSTHEGFAISEOGAGOOLPSINCENSETOTHEWISESTOBUSTHEYPNDHASRANYWATCHDOMGSORETIRESTHEYBAFKURRECESSAFSLBHMTAICSERARREVEFLQNOFESTHESFHLFWINMTHEICDEWOFRDISADDLOOUTYOUYOUCANGENCEYOUFUELVESINBUTYOUCANNOTGOFEVEFGENCEITOUTTHELANDLADBLOOKEDATHPYINAROTHEFRYWAYANDSHOOKHEFHEADYOUHAVEHADNYMFEATTFUCKMITHTHEWOFRDSHESAIDOFYOUWOULDHAVELEAFNEDTHATITISTHESRALGBENANDNOTTHEMFEATZLOHYLDTHESFNOSESINTHEAIXPAIFUPEECPSAYFYDEAGOULNEAFT
# [['C', 'H', 'O', 'I', 'R'], ['E', 'D', 'T', 'A', 'L'], ['S', 'N', 'Y', 'P', 'F'], ['U', 'W', 'B', 'G', 'M'], ['K', 'Q', 'V', 'X', 'Z']]
# WOUADTHEWORFDEVERHAVEBEENFADEIGITSFAKERHADBEENAGRAIDOGFAKIGUTROUBAEFAKINMFIGEFEANSFAKIGUTROUBAEAHFISSHARRIETITWOUADDOUSNOHARFTOREFEFBEROGTENERTHANWEDOTHATVICESARESOFETIFESOWLYVIRTUESCARRIEDTOEXCESSTHEGRAISEOGAGOOLISINCENSETOTHEWISESTOBUSTHEFINDHASFANYWATCHDOMGSOFETIFESTHEYBARKUNNECESSARILBNMTANRSEFANNEVERZLNORESTHEIRNLRWINMTHENRDEWORFDISALLLYOUTYOUYOUCANGENCEYOURUELVESINBUTYOUCANNOTGOREVERGENCEITOUTTHELANDLADBLOOKEDATHIFINAFOTHERFYWAYANDSHOOKHERHEADYOUHAVEHADNOMREATTRUCKWITHTHEWORFDSHESAIDORYOUWOULDHAVELEARNEDTHATITISTHESFALGBENANDNOTTHEMREATWHOHOLDTHEIRNOSESINTHEAIXPAIRUPEECHFAYHIDEAGOULHEART
testcrack = PlayfairCipherCracker(fa3)

# key, faans = testcrack.crack_close_key(fkey)
# print(key)
# print(faans.ciphertext)

# key, faans = testcrack.crack()
# print(key)
# print(faans.ciphertext)

print(testcrack.decipher(akey, fa3.ciphertext))






# faobjs = [FrequencyAnalysis(txt) for txt in emails]

# faobjs[1] = FrequencyAnalysis(faobjs[1].ciphertext.replace("J", "I"))

# pfcracker = PlayfairCipherCracker(faobjs[1])
# print(pfcracker.crack())


# ([['C', 'R', 'H', 'O', 'I'], ['E', 'L', 'D', 'T', 'A'], ['S', 'M', 'N', 'Y', 'P'], ['U', 'G', 'W', 'B', 'F'], ['K', 'Z', 'Q', 'V', 'X']], 'WOULDTHEWORLDLVEIHAVEBEXNPEDEIFITSMAKEIHEDBEENAFRAIDOFMAKINGTROUBLEMAKINGLIFEMLENMMAKINGTROUBLLEHMISSHARICLTITWOULDXOUMNOHARMTOIEMEMBEIOFTENERTHANWEDOTHETVICESARESOMETIMESONLYVCITUESCARXIEDTOEXCESSTHEPRAISEOFAFOXLISINCENSETOTHEWISESTOUGSTHEMINDHAMPANYWETRHDOGSSOMETIMESTHEYBARKUNXECESSAICLYBGTEWISEMANXEVERIGNORESTHECIWARNINGTHEWIDLWORLDISALXABOUTYOUYOUCANFENCEYOURSLAVESINBUTYOUCANNOTFOIEVERFENCEITOUTTHLAANDAEDYLOXKEDETHIMINAMOTHERLYWAYANDSHOOKHEIHLEDYOUHAVEHADNOGREETTRUCKWITHTHEWORLDSHESAIDOIYOGWOUADHAVEALARNEDTHATITISTHEMPEALMENANDNOTTHEGREETWHOHOLDTHECINOSESINTHEAIRFAIRSPEECHMAYHCDLAFOULHLERT')