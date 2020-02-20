from python_resources.frequency_analysis import * 
from python_resources.functions import *
from python_resources.vigenere_cipher_cracker import *
import time



cipher1 = "jtdjjmxlfmjhvpyhlzhzkzuwabeallvdlurzvtnloriyvmnkkkvqprimzuvikzluncvpeklhggmuvztgwzoqbevilzlhxoncduoaqsvtmghwrarslzlhxohwbsbekykzraimrznxgnradxjhpivdhjlpxvhzuidwoewihjmujmlzlhnaxvyhraimbllhzfbaooujoemxpuwopizyvdyolknaguhvrwmujplzsvjtjyfcmwaglbsaimyskymlgsilusradgramuxfpillbckgundwwfgyfptllpizhjbezbnabavtpiypxwrsakkrcqbnxvlnmwxfkzcegiugfcojdwzfdhmussjmnxyosvprmlvdrnwqrzgwfcncmqyhlziwnksvkzluwqrzfxfhblblugratgxkowxoypuiitvilzlhpuwqpbpincooatrzbnjfuchvlbhkfcjqksfioemlfhpbrzhvbeookzpicofhcnbezhfxfqbansiozkvnkywqdjfrabvigcnkfdwafhnvmuucmxvijyscklsmbrjmpilugutfjmvdkzseprwzywtgcgxmlphjtqqgceyhrwoeyv"
cipher2 = "apyuhxqjapouhjrjoqnrjmjjitnhjsdsxctnfjoqnhmjjindonshpdtnfsikxopymujtnfsikusdjtjnictnfsikxopymujsxcmyxusxxujkpphbpyuuhpnanxjosikxqjuncxbjnocgopexqjtsihqnctnibanxgqhpkccptjxstjcxqjbmnofyiijgjccnosubmyxnascjtniijrjoskipojcxqjsoanoisiktbtjnisikcsteubscxqnxaqnxjrjosqnrjxosjhxphpsiusdjsqnrjxosjhasxqnuutbqjnoxxphpajuuxqnxaqnxjrjosqnrjhjrpxjhtbcjudxpsqnrjhjrpxjhtbcjudxpgpteujxjubxqnxsikojnxnstcnihsictnuusqnrjnuanbcmjjixqpopykqubsijnoijcxdntjscnejnoutnibhsrjdponihpiubndjamosikyejrjiaqjixqjbhpsxscipxejodjgxnihxqjbcskqdpotpojnihupcjmjxxjoxqsikcsicxoykkusikdpoxqjtascjubnihcupaxqjbcxytmujxqnxoyidncxv"
cipher3 = "bhgetacdbhlmtdktcotxtuakysltacxaeyplcscoltutdspxilhaibplxcmwlocbgtlsexhpzmaxlsdlynplxcmwlocbgtdlrncpnclicrdaoabhgeaqcbnyioliyliclslsutcibadslcdodpudthdolaxoespeclycslaoslycmdborcebsuieizcatactkisuyecdmipausibpxivarpcshdsusytdoducpsuytgwyecdprwnidnsdpnblahothumycslaoslyecdbvlickpqsesupecrtmfwalfhusplpqtklcrfyhclyecdrcfdhmhpblcdfhtdbhlmahpeaztfcbybcbbtkedpuashtscbcmdektpcywbebtkedpyhabictklcuashacytbedodedpteltmtivcstldorphplptycdlmnbtpdpenoicvcdcodltncbidktidnwrbcllalokequoaodcdbhlmencdpehaicbtwbcbetidktedlisdtaidaoaoyecdnslemgdsdpnwtydolucllaqdiorttacdrcyhuspcydcdpaigpacmsaserntportdpxcbdrdlol"
cipher4 = "aobfyhrceireherrnhmttmorastohshethetaooercaaornsriatdstiwlopaehrniartyodwtaoetoodhedoeftebestesrstilueuowbsfphiounaenerneahatdivtehpbhsdrousirittrirdsiiindrgdtggoxatnahetcaottfhpaofyeornyjadefoaehhebtntiueaaaoariswtweosnuyntylrheahnabtetwewdntsortreeitnonrnowiumtinlnthcernhrysrmtietayarntdlettetktthhecihduleesoeusanknatsnentnlndseisiihdtnhgnayhtnmitwultrondnetwolptorlnieroeyitrsfndfteoethosnldriitiieetnegyondhntouerecennetgnzerensngbhoivomgefioinobothtdeidpteipeshanetwuoosjhhifehrlfascidvtnbnladjtwinahiritagnnnhnntardmwswydilhgtfioeycaoetoaghatyehcueaieuhhsinenlsauoeggigghractiao"
cipher5 = "rhzjeykdwemafgblsubspvxcyhsbvmkvyamvcgzgguavgzlokrnrltbclgnelkjkntmpgwfcsezfkzalbsdxkftngyzoglzrvteloqrvlxitjrxlrjhknrhcybpgyrukuekumguguwsycyvmabuignpmxmhwkvbywugyputkjomqydyclcyyzgnxmrebczjcytgzbaslflzvzstrzaizdjgvitqoamxvalgezvlmxgomcjhbxprjsxntvmoquklvzqcukkmzkrypuayrvzbmyknjyibcxpufmzryoqihszsukbnhpocgakygggkkzuonlmybrzamsdoktrmunnzewthyoyiyqofshzkobtppernntwqyweadxsmyguybnhgxzyhjkvteqlhpuxiydxbsfqyxajpvyrgajbvmlgntrqqgvjtvthzkywrgbrytzkdfzssxmatneghortoijuognxiikbzsixyygnxiougnpchpknzamkyvrdtxcgqytathpkdwgpoyetajlfklwkqinzmmxhqctxyrgxkttuqtztqknopqbvmxcoemyyrjgrazkrayyysgycaqiknrlvsq"

emails = [cipher1, cipher2, cipher3, cipher4, cipher5]
cracked_emails = {}
###################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################
#########    BREAK VIGENERE CIPHER      ###########################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################
print('\n\n\n')
print('###############################################')
print('###############################################')
print('#########  BREAK VIGENERE CIPHER  #############')
print('###############################################')
print('###############################################')
print('\n\n\n')


fa1 = FrequencyAnalysis(cipher1)
fa2 = FrequencyAnalysis(cipher2)
fa3 = FrequencyAnalysis(cipher3)
fa4 = FrequencyAnalysis(cipher4)
fa5 = FrequencyAnalysis(cipher5)

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

print(f"Email number {i + 1} was a Viginere Cipher with key {vctest5[0]} and ciphertext:\n{el.ciphertext}")

cracked_emails['vigenere'] = f"Email {i + 1}:\n{el.ciphertext}"
time.sleep(10)
###################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################
#########    BREAK SUBSTITUTION CIPHER      ###########################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################

print('\n\n\n')
print('###############################################')
print('###############################################')
print('#########  BREAK SUBSTITUTION CIPHER  #########')
print('###############################################')
print('###############################################')
print('\n\n\n')


emails = emails[:-1]

print(FrequencyAnalysis.unigram_autocorrelation())
print(FrequencyAnalysis.bigram_autocorrelation())

def mapping_permutations(mapping_possibilities):
    mapping_permutations = []
    queue = [dict(mapping_possibilities)]
    while len(queue) > 0:
        
        current_mapping = queue.pop()
        # print(current_mapping)
        used_letters = set()
        has_array = False
        char_to_use = None
        for letter, possible_matches in current_mapping.items():
            if(isinstance(possible_matches, str)):
                used_letters.add(possible_matches)
            else: 
                char_to_use = letter
                has_array = True
        if not has_array: 
            mapping_permutations.append(current_mapping)
            # print(f"NEW SOLN, TOTAL: {len(mapping_permutations)}")
            continue
        # print(used_letters)
        maps_to_add = []
        filtered_possible_matches = [match for match in current_mapping[char_to_use] if match not in used_letters]
        # print(char_to_use)
        # print(filtered_possible_matches)
        # if len(filtered_possible_matches) == 0: 
        #     valid_solution = False
        #     continue
        for char in filtered_possible_matches:
            map_perm = dict(current_mapping)
            map_perm[char_to_use] = char
            maps_to_add.append(map_perm)   
        # if valid_solution: queue += maps_to_add
        queue += maps_to_add

    return mapping_permutations


def swap_letter(cipher, plain, mapping):
    pass


def apply_mapping(text, mapping):
    return "".join([mapping[char] for char in text])



print('---------------------------')
print("")
mapping = {char: [] for char in fa2.ciphertext}
for _ in range(1):
    map_sol, ciphertext = fa2.crack_substitution()
    for cipher, plain in map_sol.items():
        if not plain in mapping[cipher]:
            mapping[cipher] = mapping[cipher] + [plain]

print(mapping)
product = 1
for cipher, possibilities in mapping.items():
    product *= len(possibilities)
print('---------------------------')
print(f"Number of permutations: {product}")
mapping_possibilities = mapping_permutations(mapping)
print(len(mapping_possibilities))
print('---------------------------')
# print(fa4.crack_substitution())
messages = [(f"{mapping}", apply_mapping(fa2.ciphertext, mapping)) for mapping in mapping_possibilities ]
file = open("substitution_cipher_crack.txt", "w")

for msg in messages:
    file.write('------------------------------------\n\n')

    file.write(msg[0])
    file.write(':\n')
    file.write(msg[1])
    file.write('------------------------------------\n\n')

file.close()
# {'J': 0.12794612794612795, 
# 'X': 0.09090909090909091, 
# 'N': 0.08922558922558922, 
# 'S': 0.07407407407407407, 
# 'I': 0.06565656565656566, 
# 'P': 0.05555555555555555, 
# 'O': 0.05555555555555555, 
# 'U': 0.05387205387205387, 
# 'Q': 0.05218855218855219, 
# 'C': 0.05218855218855219, 
# 'T': 0.04208754208754209, 
# 'H': 0.04040404040404041, 
# 'B': 0.03198653198653199, 
# 'K': 0.02861952861952862, 
# 'A': 0.025252525252525252, 
# 'R': 0.02356902356902357, 
# 'D': 0.02356902356902357, 
# Y': 0.020202020202020204, 
# 'M': 0.018518518518518517, 
# 'E': 0.010101010101010102, 
# 'F': 0.008417508417508417, 
# 'G': 0.008417508417508417, 
# 'V': 0.0016835016835016834}