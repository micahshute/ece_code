# from python_resources.ciphers import *
from python_resources.frequency_analysis import *


# text_orig = "Ok, onto intuition. We want to find the shortest path in between a source node and all other nodes (or a destination node), but we don’t want to have to check EVERY single possible source-to-destination combination to do this, because that would take a really long time for a large graph, and we would be checking a lot of paths which we should know aren’t correct! So we decide to take a greedy approach! You have to take advantage of the times in life when you can be greedy and it doesn’t come with bad consequences! So what does it mean to be a greedy algorithm? It means that we make decisions based on the best choice at the time. This isn’t always the best thing to do — for example, if you were implementing a chess bot, you wouldn’t want to take the other player’s queen if it opened you up for a checkmate the next move! For situations like this, something like minimax would work better. In our case today, this greedy approach is the best thing to do and it drastically reduces the number of checks I have to do without losing accuracy. How?? Well, let’s say I am at my source node. I will assume an initial provisional distance from the source node to each other node in the graph is infinity (until I check them later). I know that by default the source node’s distance to the source node is minium (0) since there cannot be negative edge lengths. My source node looks at all of its neighbors and updates their provisional distance from the source node to be the edge length from the source node to that particular neighbor (plus 0). Note that you HAVE to check every immediate neighbor; there is no way around that. Next, my algorithm makes the greedy choice to next evaluate the node which has the shortest provisional distance to the source node. I mark my source node as visited so I don’t return to it and move to my next node. Now let’s consider where we are logically because it is an important realization. The node I am currently evaluating (the closest one to the source node) will NEVER be re-evaluated for its shortest path from the source node. Its provisional distance has now morphed into a definite distance. Even though there very well could be paths from the source node to this node through other avenues, I am certain that they will have a higher cost than the node’s current path because I chose this node because it was the shortest distance from the source node than any other node connected to the source node. So any other path to this mode must be longer than the current source-node-distance for this node. Using our example graph, if we set our source node as  we would set provisional distances for nodes because had the shortest distance from  we then visited node  Now, even though there are multiple other ways to get from I know they have higher weights than my current  distance because those other routes must go through  , which I have verified to be farther from  than  is from . My greedy choice was made which limits the total number of checks I have to do, and I don’t lose accuracy! Pretty cool. Continuing the logic using our example graph, I just do the same thing from  as I did from  I update all of  immediate neighbors with provisional distances equal to length + edge length to neighbor IF that distance is less than it’s current provisional distance, or a provisional distance has not been set. (Note: I simply initialize all provisional distances to infinity to get this functionality). I then make my greedy choice of what node should be evaluated next by choosing the one in the entire graph with the smallest provisional distance, and add  to my set of seen nodes so I don’t re-evaluate it. This new node has the same guarantee as  that its provisional distance from A is its definite minimal distance from . To understand this, let’s evaluate the possibilities (although they may not correlate to our example graph, we will continue the node names for clarity). If the next node is a neighbor of  but not of  then it will have been chosen because its provisional distance is still shorter than any other direct neighbor of  so there is no possible other shortest path to it other than through  If the next node chosen IS a direct neighbor of  then there is a chance that this node provides a shorter path to some of  neighbors than  itself does."
# text_orig = FrequencyAnalysis(text_orig).ciphertext
# text = encrypt_vc([17, 5, 13], text_orig)
# print(decrypt_vc([17, 5, 13], text))

text = 'inzba wqkls jboll dwnzh lbokn ybppu incpc pvbtf cnvlb eqwyy yjdag pgdpk faqvs emvmf ijmrn miulb fwdod ptmny zxxhm oqady zuvpm qikeu incpc pvbhm vwxlv djzzp vcrhs nwvdj iekah gmafu inwlb zczeo lbdpb pivet erxzb ltqli znnvu pzbsj nnord ylzpu lkvpb lvaps rcotz uwzty puohc pzuty tqwjb zvvpq cjvtn dbqxr vmshs ptgoj tukyd obppf dnbpb lvxpt guozg zctom reohu zqkpn ecrlr ptmny zxxve epmtw enhar fxzpr vlybq ercdy zloag pzmqt indoh ddinf elizg zctos fclle tttpi lwdpk hmpla vjxlv azmdn unxaa fbbsj rvoyh nivaj fyvlz wzmli pmskg ldmlx rhwps npunh fwxlk wivom zbzhq egrfx kmskm etqvj zccvs smgcj xxsuf ewulp vcrlt yxzph vmous plicl lvous epiey ynnbk jmtph knnwq paqoj ecyms smcyn knnzs lbmdt wjwlq tkidm fdvkh rvwcj yrcjn yabty lcsvm ltzpx gxxzh mqtty pjxki fabdn kxxoh dpiyi jdxah wbpps vgdwq paqoj ecszd wmkej ucrpr tarfx kkofn ylbsj gjvlg ldqyl xaybm okwyl inczs ziplq kjxkc zvmpa vaiag tvoem vhmhm ewkzs jckus wgcyi vawpm pivoi vvohm epmwj xrdpl lbmlz kqyyh egwqy ynoed ncbta vkbhm npzpu lkvpb lvayt nboll ombpw drxlc ewwmx kaejs epmht itsuf dwnem vcrpq ojzls tqymn fzoza vaxtd ybbzt radpb wmqtx vldpn ywnzz ilyur eqbfy zxxyd llaat nnban ywuts rcoag prcdy zlozh ddmdy vmsus smxcj jrnlm ewnem vdxps plaef knchm oixat zwdtd ybalw vvkkd hqbsy ynkku tkmls ulyur pvbzk kqozd yibpq rbddd lttnm vlulc azmdn unxan miuln jcrlo cmati vwdve epmfs zcokr eibpx ryzvh ybqyl rbewq pumnt ladqt dbqnj zbrpr azqgn cnqlz ylzpx gxxzh mqtty paowt mtqnf ebsub tlmyy ruvfz cmxzn ecsuf ewzzg vadin cszzs runyd loiyx jdzyd xmkzz icxvl tvmpb yxclm lbmoj dxmyz eaafh tncze fttjg cxmrd ojcei vvyjq lbaon uwdhm ywcyh vqybq dinej icrlu lkiyh pfkzb cmiej ujxka pnwcj rwiuz xmahj inpsn lbmoy yjdag pgezz cmeuz yquzz juiik zksls psezs tkmcj rpkuv zctos fvsuz embsj zaywo zaqen fwghr dxmnn wrmhk wgttr zcoks zjwcp rwndg pvjzw bfkza wwkvj ujxkq piols exwpm lbmof ecrvm jsmys vmiod hiafs rwstn fatjh fwppq xmlmd kqozd yibpy fmkfq pxcmq zlkur sidps kmojk lzmoy ynsyn axwdn kryus ziaaj trppb nivon ujdls smgsf mnnlb wizpi kqopq zxxzx zcsvm ewxcj jrnlm ewjlr rwyth yibts xjxfn ymazb yjdhq pxzpx zmous zjixf jxzah zvadn elood siadf zmrlv tttyt drxhs pirfx krmls znqwq kqocz nivnd rwnun ejwhy fcrpr cqlth luybr cmxfg crmhm emuaj ickus ccuxd jnxzd tappm rbddn cmiwn jcsjn abqzs jcrle tzaen jcyun xqvly vjcbo pzaef ivykd cibpy fossk epmgf tjxjx dwupt ensav tttmj mnbfo ztqen tjvsx sizok fablo fjtth rwcan zxxzx vxlch zcawd zcgvt wlpla vcyid lkiyi zmkad hpwnm vluzz wtwqy ynulx mwfpx wxbkd xwkcf kbsus pzudt wbkmd rcici zwqvq pdmyx kaouf epmyn epmvm dbqez kryuz wrccn jybbc pvkpf ixeuc ljwcy zxxyh rpbdr rabpz rmmbz rusax nwuxt ebour pocyw vbdyh nbqzs jjxkn epmch vwdyz wqadz vblbs zbppw nrclh omwwt xrmhk wgqeh fdvka pisps ennfk tbmtk pxedh wtazr vxxlv swqds fcppq xtgts vrdod cbpph fwclq gibta vxbsh mmzlq nrxnn qbpph fdbas smxct suoth dacnm rviag tkiwz ermvq ywnlx lybll pkwfw kwyth ymmxf pwyad gmvpc zbdhm oxwwn krmhk wgxcf xvkah niaaw vbskd ybwmf djszn qbmyn elvpm plbzg vaotd xjmcm vckbf sbkzs jcsat eqwyf cukdz ylppz emoyr eivox kqowq znwfs ujxkk labts xrwwz nbwqb yxwlu pzppf gyypm eaiyi zbezo pkbem rcgoh wmppr rhdhb eqklq chvlz ybwhf immvl azwxn jnyuz xibej ijcmt ylixj ecksz ylxpw djxlm eiaem zbrlr ywbts tusud obwmj txxjh wqiet ihdoz eaiti inzba wqkls jpypm rixzu cnmah nwdpw rwyag pzetx vyoye pkbwd inkzn yijwj exwpm pmiyi zwcvc zqvrm zprsh rpbts xcrlf zxapc kaoth dbdtj nbdoz eizpt lcyms zcksb zcrag pdidy djtvq tbgzk mxdlq dkwfq uyvhx bcqej nnvse zzlpr flbhs dqvem vuohc fxbzy ynosd nbqzs fkktz damnt emyws twvtx raojd daiau frxal pvbty adcar zpiau vwcag lbbsj jnxhs pqanz iaous wgqyw vlozr fvbtq wnluc hpqwj rbewq pumnt ladyt wqvrn elyur ezits vmcbb sixat zwdtd ybaem vfkfr pviej inzba wqkls jqkcd eisps kqszb fzzps kkblz vuqrm kvkrd tbxzx jrlsd qwzaw vbskd ybwmf djdvk poiwq pvkrd lviau frxal pvbqt ivyyd zvbsj grmhx fvmwj xjvkd eiqwx zwfvk gmlsj incld dkwez jkvvf zjixf yjczs cwvrb zwnhs sqadf zucan owbsn jfsag xkkzs envsz ylwem vachk cmiod unmsz cqvry ynsya wivvj kxzwn dqbtt ecyiz nsqyl rwiun xqvpj rwnpl ywbrt ewksh pqbht lunid lzmlq chzvv pznfq wdmrx zcopx kdbls zuivj kxkyd acjwn tjxwz cbgem rcrhr mmmys fcrpm rjceu ixlsd xibth ruvfo pbcwf eccpm nmwmf djdvn vwnqn tnlbs cmxfg crmhm dpigj rublz ogaxj raokn miulk faezh yomij tddpu picem fasax hpmyy ynicd mtwnp vmvlf tatly zeoyn fbmdf emdod azmdn unxal topeg vaost nbiyy kxblh ynwch vcrhs npicf tcoyh kibtt eyvbr fvlzz scokk jwvpt wcrla toopx kokjs zzaqt icrlv sqbpm fdclh dpwhf ehwhm pcdpw nxesc smtat iqeys epmpa vwdbz wlmxt takah nvwxn enomn cbpzz xqcpm nmafh yjxho awqyy dnxav zctog vcoto zzicd rwidz jivof lcytz eqklq choeo tzmly kqolm ownem zbmvm rzmdx fkktz nwcwi raqbd epiem vrcpm qikei frxnv sibcj gdlsh nivdb rwdhm oixat zwdpm rixwf tnrvk omzfs krvag pvmiy gaozh omveg fcrve epmdj fydpn yapla vkoud qqbdf embpr vajfy nqkah epqyp zbwvr eqvej incah yoqdy ynith czwcy yncvq ewnnt xwsah gmiyi kjmah nitpa fueah zvwqt sjwhr azmdn unxjx qwzsn josyr enwfw faocd yaqid vjbzh ywnqn tnzyd dqlps kxlhl leidi vnzsx nwuxn kcoks zivoj mnxjn ydqyh vmymg taimn crdfs zvign xjdls smcyu inmlc pvbpi gjbah divdm zyknz tvaem zvgps skwxu ixwpr puwcj inmlm etgqn ejvsx cmkzl erjpm rzmaz susjz yqvew rwcpf pvkpk fagoz eqbtx fkktz dbivj evyyd znbsj wdmrx zcxly yjcmn cepzy fwyth yibpn yjflm zqlpf gnbzn yitwd zmvpj pbwdj vbytd zvmwn bntbc tbpmw ffxlc tivtx fafhm tbirz gckvm epmmj elrag zcosy wdvjh gqtcn xqdzk legpw jfrvv zctog irxnz omxem fooeo pzqps tnkzo ciken kryud cabzy ynmvt cbvlr vbdoz epigj snoue wwiej unvzd hpmcj zwmst omacn jasuh gials tdbyd ybtjt ecrlt dkwfw kxpho amiwx wxbag plknn ileps lvluf enulk wgkfw inxak jwvem vcrjh ckcty txeys zniau vjvza zbphj inzyd gqwfx cheuz yquzz juijn ynqcr vmlfs smaps rcodg pvwmf djppq dbvzr zwkad obppr kxdod tzkfw inxao zabdt kqoyn abqzs jrxjk flmqt ivoyl laalh ydcls eaoza vaxvq omdlq gjdyh nsiyi dnbyh nsolw cjxkb sqmqo lmqlh ybppi tlsyb fqbhm faowt mtqnf eboun czqym rcmon ykmdf zmgvt wljph fwppq xmlet kqooh rpkzz icxvp fmaen fwdod awqyy zbdod cmicj guous jwnzz kbdhm oqvrh rwnpc lbmdj jyojh lttjf dxxns smiww vjnfb zvntw dnnvm nmjjw vyeik tkiyx taywn qkccw vwdmd omzlq adcah nmaem vzelr eqwyn jqydn miulb rwdzs zxqnp kqsze topek fuvvv ditwd fwddh ebmcb vfosb zumjt lamvl xmvex rcskd laykh fvgvv'

fa = FrequencyAnalysis(text)
keylen = fa.find_keylen(25)
fa.keylen = keylen




keys = fa.vc_freq_analysis_naive()
vc_key = [res[0] for col, res in keys.items()]

# res = FrequencyAnalysis.decrypt_vc(vc_key, fa.ciphertext)
# Res showed that M should be I and X should be T so the key is too small by 4:

refined_vc_key = list(vc_key)
refined_vc_key[6] += 4
print(f"Naive VC Key: {vc_key}")
print(f"Naive key refined: {refined_vc_key}")
# print(decrypt_vc(refined_vc_key, fa.ciphertext))

# ORRRRR DO THIS WITH CORRELATION:

keys = fa.vc_freq_analysis_correlation()
keysarr = [key for col, key in keys.items()]
print(f"VC Key Found with correlation: {keysarr}")

# print(fa.decrypt_with_vc(keysarr))
# Broken Message -- liberal rant

# REPUBLICANS SEEM SO FOCUSED ON THE PRESIDENTIAL ELECTION THAT THEYVE FORGOTTEN BARACK OBAMA WON THE ELECTION AND IS STILL IN FACT PRESIDENT 

# WHEN NEWS BROKE THAT CONSERVATIVE SUPREME COURT JUSTICE ANTONIN SCALIA DIED OVER THE WEEKEND REPUBLICAN SENATE MAJORITY LEADER MITCH MCCONNELL 
# ALMOST IMMEDIATELY DECLARED THE AMERICAN PEOPLE SHOULD HAVE A VOICE IN THE SELECTION OF THEIR NEXT SUPREME COURT JUSTICE THEREFORE THIS VACANCY 
# SHOULD NOT BE FILLED UNTIL WE HAVE A NEW PRESIDENT BUT THE AMERICAN PEOPLE ALREADY DID HAVE A SAY MITCH MCCONNELL AND HIS PARTY JUST DIDNT LIKE IT 
# SO THEYRE GOING TO MAKE THE UNPRECEDENTED ARGUMENT THAT THE DULY ELECTED PRESIDENT OF THE UNITED STATES OF AMERICA SHOULD IGNORE HIS CONSTITUTIONAL 
# RESPONSIBILITY AND JUST SIT ON HIS HANDS UNTIL THE NEXT PRESIDENT IS ELECTED THIS IS JUST BEYOND THE PALE HAVING GROUND CONGRESS TO A HALT AND 
# DONE EVERYTHING THEY CAN TO CONSTANTLY UNDERMINE AND DEMEAN THE LEGITIMATE AUTHORITY OF THE EXECUTIVE BRANCH REPUBLICANS NOW SEEM DETERMINED TO 
# OBSTRUCT THE WORKINGS OF THE THIRD BRANCH OF OUR GOVERNMENT TOO ARTICLE II SECTION OF OUR CONSTITUTION READS POWER TO NOMINATE THE JUSTICES IS 
# VESTED IN THE PRESIDENT OF THE UNITED STATES AND APPOINTMENTS ARE MADE WITH THE ADVICE AND CONSENT OF THE SENATE LAST WE ALL CHECKED PRESIDENT 
# OBAMA IS THE PRESIDENT OF THE UNITED STATES APPOINTING A SUPREME COURT JUSTICE IS HIS PRIVILEGE AND RESPONSIBILITY 

# REPUBLICANS INCIDENTALLY ARE POINTING TO ROBERT BORK RONALD REAGANS SUPREME COURT NOMINEE WHO SENATE DEMOCRATS SUCCESSFULLY BLOCKED BUT DEMOCRATS 
# DIDNT ANNOUNCE HOURS AFTER THE VACANCY WAS CREATED AND BEFORE ANY NAMES WERE FLOATED THAT THEY WOULD UNANIMOUSLY BLOCK ANY JUSTICE REAGAN 
# WOULD NOMINATE THEIR OPPOSITION WAS SPECIFICALLY LIMITED TO BORK AND WHEN BORK WAS BLOCKED AND REAGAN NOMINATED ANTHONY KENNEDY HE WAS U
# NANIMOUSLY CONFIRMED BY THE SENATE 

# TODAY REPUBLICANS HAVENT DECLARED THEIR OPPOSITION TO A SPECIFIC CANDIDATE THEY HAVE DECLARED THEIR OPPOSITION TO PRESIDENT OBAMA NOMINATING 
# ANYONE SO WHAT ARE PRESIDENT OBAMAS OPTIONS SINCE HE HAS SAID HE WILL NOMINATE A JUSTICE TO FILL THE VACANCY AND NOT BOW TO THIS RIDICULOUS 
# REPUBLICAN TEMPER TANTRUM MY SENSE IS HE HAS TWO REALISTIC OPTIONS 

# THE FIRST IS TO NOMINATE A SUPERSTAR MODERATE TO FILL THE VACANCY SOMEONE IT WILL BE VERY POLITICALLY HARD FOR REPUBLICANS TO OPPOSE 

# OBVIOUSLY IT WOULD HAVE TO BE A CANDIDATE WHO CHECKS ALL OF THE KEY BOXES FOR DEMOCRATS IN TERMS OF SAFEGUARDING OR EVEN STRENGTHENING 
# CONSTITUTIONAL JURISPRUDENCE AROUND ABORTION RIGHTS MARRIAGE EQUALITY COMMON SENSE GUN RESTRICTIONS AND OTHER CENTRAL ISSUES BUT OTHERWISE 
# IDEOLOGICALLY IT COULD BE A KENNEDY LITE IF YOU WILL 


# SOMEONE WHO IS NOT FIRMLY IN EITHER THE CONSERVATIVE OR LIBERAL WING OF THE COURT THE PROBLEM IS SUCH A MYTHICAL UNICORN OF A SUPREME 
# COURT NOMINEE MAY NOT EVEN EXIST AND POLITICALLY PRAGMATIC AS PRESIDENT OBAMA IS OFTEN INCLINED TO BE 

# REMEMBER HE TAUGHT CONSTITUTIONAL LAW AND HE UNDERSTANDS THE PROFOUND AND LASTING IMPACT OF WHOMEVER HE APPOINTS AND I SUSPECT THAT WHILE HE MAY 
# TACTICALLY LEAN TOWARD COMPROMISE ON A MATTER AS FUNDAMENTAL AND PERMANENTAST HIS HES NOT INCLINED TO BE CONCILIATORY THAT SAID REPUBLICANS GOING A 
# POPLECTICOVER ANOTHER WISE PERFECTLY REASONABLE NOMINEE AND INSODOING HIGHLIGHTING THE GOPS EXTREMIST VIEWS THAT ARE OUT OF TOUCH WITH THE VAST
# MAJORITY OF VOTERS COULD PLAY QUITE WELL FOR DEMOCRATS IN THE LEADUP TO THE ELECTION 

# OBAMAS SECOND OPTION IS A RECESS APPOINTMENT IT JUST SO HAPPENS THAT THE SENATE IS CURRENTLY IN RECESS UNTIL FEB ND WHILE A SUPREME COURT RULING 
# INCONSTRAINED SUCH APPOINTMENTS THE WAY SENATE REPUBLICANS HAVE TAKEN THIS CURRENT BREAK MIGHT MAKE IT POSSIBLE FOR PRESIDENT OBAMA TO LEGALLY MAKE
# AN APPOINTMENT FOR MORE ON THE PICAY UNELEGAL DETAILS INVOLVED HERE SEES COTUSBLOG OBAMA HAS STRONG WIND AT HIS SAILS TO DO THIS WITH MCCONNELL AND 
# OTHERS ALREADY DECLARING THEIR BLANKET OPPOSITION TO BACKING ANY NOMINEE AND IM NOT GONNA LIE IT WOULD BE A REALLY POWERFUL FUCK YOU GESTURE TO MAKE 
# TO A REPUBLICAN PARTY THAT HAS BEEN NOTHING BUT PROBLEMATICALLY PETULANT SINCE OBAMA TOOK OFFICE BUT REPUBLICANS HAVE ALREADY SMEARED OBAMA FOR 
# USING EXECUTIVE AUTHORITY WHEN THEYVE BLOCKED LEGISLATIVE ROUTES AND THE PRESIDENT MIGHT BE RELUCTANT TO REINFORCE THAT CHARACTERIZATION PLUS 
# UNDOUBTEDLY ONE OF THE BIGGEST FACTORS FOR THE WHITE HOUSE IS HOW ANY MAN EUVER WOULD HELP OR HURT THE EVENTUAL DEMOCRATIC NOMINEE FOR THOUGH 
# SINCE SUCH AN APPOINTMENT WOULD BE TEMPORARY ANYWAY AND AUTOMATICALLY EXPIRE AT THE END OF THIS CONGRES S OBAMA COULD ARGUE THAT HE IS IN FACT 
# DOING WHAT REPUBLICANS WANT AND APPOINTING A PLACEHOLDER UNTIL THE NEXT PRESIDENT BOTH OF THESE OPTIONS HAVE BENEFITS AND RISKS BUT WHAT I THINK
#  IS MOST INTERESTING IS THEY MIRROR THE SORT OF COGNITIVE AND TACTICAL EVOLUTION OF OBAMAS PRESIDENCY FOR HIS FIRST FOUR OR EVEN SIX YEARS IN OFFICE 

# PRESIDENT OBAMA WAS DEEPLY COMMITTED TO AND EVEN CONVINCED OF HIS ABILITY TO NAVIGATE THE UNPRECEDENTED PARTISANSHIP AGAINST HIM WITH COMPROMISE 
# MORE RECENTLY FINALLY RECOGNIZING REPUBLICAN INTRANSIGENCE FOR WHAT IT IS OBAMAS TAKEN MORE OF THE FUCK YOU PATH AS FOR WHO TO NOMINATE I HAVE NO 
# IDEA PERSONALLY ID LIKE TO SEE SOMEONE LIKE JUDITH BROWNE DIAN ISORVANITA GUPTA ON THE BENCH THOUGHTFUL CIVIL RIGHTS LAWYERS WHO WOULD BRING A 
# DEPTH OF EXPERIENCE AS PRACTITIONERS TO THE COURT 

# NAMES THAT HAVE BEEN FLOATED ELSEWHERE INCLUDES RISRINIVASAN CURRENTLY ON THE US COURT OF APPEALS FOR THE DC CIRCUIT AND JANE KELLY CURRENTLY 
# ON THE TH CIRCUIT COURT OF APPEALS BOTH WERE PREVIOUSLY UNANIMOUSLY CONFIRMED BY THE SENATE WHEN OBAMA FIRST NOMINATED THEM TO THEIR CURRENT 
# POST SO THER OPTIONS INCLUDE FORMER MASSACHUSETTS GOVERNOR DEVAL PATRICK AND MERRICK GARLAND CHIEF JUDGE IN THE DC CIRCUIT WHO REPUBLICAN SENOR 
# RINHATCHONCE SAID WOULD BE CONFIRMED TO THE HIGH COURT NO QUESTION THE POINT IS THERE ARE PLENTY OF OUTSTANDING CANDIDATES ESPECIALLY AMONG THE 
# ALREADY CONFIRMED ONCE BY REPUBLICANS CROP OF CURRENT FEDERAL JUSTICES THE QUESTION IS HOW OBAMA WANTS TO PICK THIS FIGHT FOLLOW SALLY ON 
# TWITTER WE WELCOME YOUR COMMENTS AT IDEAS QZCOMWOW
