from python_resources.frequency_analysis import *
from python_resources.hill_cipher_cracker import *
from python_resources.functions import *
import ssl
import random
from urllib.request import urlopen
from python_resources.frequency_analysis import *

def c2i(character):
    return ord(character)-ord('A')

def i2c(encoded):
    return chr(ord('a') + encoded)

def hill_enc(plain):
    found = False
    a=1
    b=1
    c=1
    d=1
    while not found:
        a,b,c,d = [random.randint(0,25) for i in range(4)]
        det = (a*d - b*c) % 26
        det2 = ((a-1)*d - b*(c-1)) % 26
        if (det % 2 != 0 )and (det % 13 != 0) and (det2 % 26 != 0):
            found = True
    a,b,c,d = [17, 25, 19, 2]
    secret = ''
    for i in range(0, len(plain) - 1, 2):
        i1 = c2i(plain[i])
        i2 = c2i(plain[i+1])
        c1 = (i1*a + i2*b) % 26
        c2 = (i1*c + i2*d) % 26
        secret += i2c(c1) + i2c(c2)
    return secret, [a,b,c,d]

key = np.matrix([[17,25], [19,2]])
enres = urlopen("https://vip.udel.edu/crypto/mobydick.txt",  context=ssl._create_unverified_context())
entxt = enres.read().decode()

enfa = FrequencyAnalysis(entxt)
ciphertest, tkey = hill_enc(enfa.ciphertext)
print(tkey)
fatest = FrequencyAnalysis(ciphertest)

cipher1 = "jtdjjmxlfmjhvpyhlzhzkzuwabeallvdlurzvtnloriyvmnkkkvqprimzuvikzluncvpeklhggmuvztgwzoqbevilzlhxoncduoaqsvtmghwrarslzlhxohwbsbekykzraimrznxgnradxjhpivdhjlpxvhzuidwoewihjmujmlzlhnaxvyhraimbllhzfbaooujoemxpuwopizyvdyolknaguhvrwmujplzsvjtjyfcmwaglbsaimyskymlgsilusradgramuxfpillbckgundwwfgyfptllpizhjbezbnabavtpiypxwrsakkrcqbnxvlnmwxfkzcegiugfcojdwzfdhmussjmnxyosvprmlvdrnwqrzgwfcncmqyhlziwnksvkzluwqrzfxfhblblugratgxkowxoypuiitvilzlhpuwqpbpincooatrzbnjfuchvlbhkfcjqksfioemlfhpbrzhvbeookzpicofhcnbezhfxfqbansiozkvnkywqdjfrabvigcnkfdwafhnvmuucmxvijyscklsmbrjmpilugutfjmvdkzseprwzywtgcgxmlphjtqqgceyhrwoeyv"
cipher2 = "apyuhxqjapouhjrjoqnrjmjjitnhjsdsxctnfjoqnhmjjindonshpdtnfsikxopymujtnfsikusdjtjnictnfsikxopymujsxcmyxusxxujkpphbpyuuhpnanxjosikxqjuncxbjnocgopexqjtsihqnctnibanxgqhpkccptjxstjcxqjbmnofyiijgjccnosubmyxnascjtniijrjoskipojcxqjsoanoisiktbtjnisikcsteubscxqnxaqnxjrjosqnrjxosjhxphpsiusdjsqnrjxosjhasxqnuutbqjnoxxphpajuuxqnxaqnxjrjosqnrjhjrpxjhtbcjudxpsqnrjhjrpxjhtbcjudxpgpteujxjubxqnxsikojnxnstcnihsictnuusqnrjnuanbcmjjixqpopykqubsijnoijcxdntjscnejnoutnibhsrjdponihpiubndjamosikyejrjiaqjixqjbhpsxscipxejodjgxnihxqjbcskqdpotpojnihupcjmjxxjoxqsikcsicxoykkusikdpoxqjtascjubnihcupaxqjbcxytmujxqnxoyidncxv"
cipher3 = "bhgetacdbhlmtdktcotxtuakysltacxaeyplcscoltutdspxilhaibplxcmwlocbgtlsexhpzmaxlsdlynplxcmwlocbgtdlrncpnclicrdaoabhgeaqcbnyioliyliclslsutcibadslcdodpudthdolaxoespeclycslaoslycmdborcebsuieizcatactkisuyecdmipausibpxivarpcshdsusytdoducpsuytgwyecdprwnidnsdpnblahothumycslaoslyecdbvlickpqsesupecrtmfwalfhusplpqtklcrfyhclyecdrcfdhmhpblcdfhtdbhlmahpeaztfcbybcbbtkedpuashtscbcmdektpcywbebtkedpyhabictklcuashacytbedodedpteltmtivcstldorphplptycdlmnbtpdpenoicvcdcodltncbidktidnwrbcllalokequoaodcdbhlmencdpehaicbtwbcbetidktedlisdtaidaoaoyecdnslemgdsdpnwtydolucllaqdiorttacdrcyhuspcydcdpaigpacmsaserntportdpxcbdrdlol"
cipher4 = "aobfyhrceireherrnhmttmorastohshethetaooercaaornsriatdstiwlopaehrniartyodwtaoetoodhedoeftebestesrstilueuowbsfphiounaenerneahatdivtehpbhsdrousirittrirdsiiindrgdtggoxatnahetcaottfhpaofyeornyjadefoaehhebtntiueaaaoariswtweosnuyntylrheahnabtetwewdntsortreeitnonrnowiumtinlnthcernhrysrmtietayarntdlettetktthhecihduleesoeusanknatsnentnlndseisiihdtnhgnayhtnmitwultrondnetwolptorlnieroeyitrsfndfteoethosnldriitiieetnegyondhntouerecennetgnzerensngbhoivomgefioinobothtdeidpteipeshanetwuoosjhhifehrlfascidvtnbnladjtwinahiritagnnnhnntardmwswydilhgtfioeycaoetoaghatyehcueaieuhhsinenlsauoeggigghractiao"
cipher5 = "rhzjeykdwemafgblsubspvxcyhsbvmkvyamvcgzgguavgzlokrnrltbclgnelkjkntmpgwfcsezfkzalbsdxkftngyzoglzrvteloqrvlxitjrxlrjhknrhcybpgyrukuekumguguwsycyvmabuignpmxmhwkvbywugyputkjomqydyclcyyzgnxmrebczjcytgzbaslflzvzstrzaizdjgvitqoamxvalgezvlmxgomcjhbxprjsxntvmoquklvzqcukkmzkrypuayrvzbmyknjyibcxpufmzryoqihszsukbnhpocgakygggkkzuonlmybrzamsdoktrmunnzewthyoyiyqofshzkobtppernntwqyweadxsmyguybnhgxzyhjkvteqlhpuxiydxbsfqyxajpvyrgajbvmlgntrqqgvjtvthzkywrgbrytzkdfzssxmatneghortoijuognxiikbzsixyygnxiougnpchpknzamkyvrdtxcgqytathpkdwgpoyetajlfklwkqinzmmxhqctxyrgxkttuqtztqknopqbvmxcoemyyrjgrazkrayyysgycaqiknrlvsq"

emails = [cipher1, cipher2, cipher3, cipher4, cipher5]


faobjs = [FrequencyAnalysis(txt) for txt in emails]

hcracker = Hill2x2CipherCracker(faobjs[0])
# print("CT BIGRAMS:")
# print(fatest.ciphertext_bigram_frequencies)
# print(hcracker.crack())
print(hcracker.crack())
# print("------------ORIGINAL TXT BIGRAMS--------------")
# print('------------------------------------')
# print(enfa.ciphertext_bigram_frequencies)
# fat = FrequencyAnalysis("ELLLTWZGNA")
# # fa1 = FrequencyAnalysis("MRBVEHZP")
# hcracker = Hill2x2CipherCracker(fat)
# txt = hcracker.decrypt2txt(key)
# print(txt)


# (matrix([[23., 17.],
#         [ 1., 12.]]), 'HONESTPEOPLEDONTHIDETHEIRDEEDSHEATNOTAFURNACEFORYOURFOESOHOTTHATITDOSINGEYOURSELFTAKENOTHINGONITSLOOKSTAKEEVERYTHINGONEVIDENCETHERESNOBETTERRULEINHERITEDIDEASAREACURIOUSTHINGANDINTERESTINGTOOBSERVEANDEXAMINETHECOMPANIONSOFOURCHILDHOODALWAYSPOSSESSACERTAINPOWEROVEROURMINDSWHICHHARDLYANYLATERFRIENDCANOBTAINTRULYTOENJOYBODILYWARMTHSOMESMALLPARTOFYOUMUSTBECOLDFORTHEREISNOQUALITYINTHISWORLDTHATISNOTWHATITISMERELYBYCONTRASTNOTHINGEXISTSINITSELFNOBODYCANSPOILALIFEMYDEARTHATSNONSENSETHINGSHAPPENBUTWEBOBUPMYADVICEISNEVERDOTOMORROWWHATYOUCANDOTODAYPROCRASTINATIONISTHETHIEFOFTIMELAUGHTERISPOISONTOFEARJ')