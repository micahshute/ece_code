require 'pry'
require_relative './ruby_resources/historic_ciphers'


phrase = "hvwgw gqozz srobv wghcf wqozq wdvsf psqoi gswhw gpfcy sbhbl"
bf_result = HistoricCiphers::CaesarCipher.brute_force_decrypt(phrase)

# puts bf_result

# 14=>"THISI SCALL EDANH ISTOR ICALC IPHER BECAU SEITI SBROK ENTNX",
# THIS IS CALLEC AN HISTORICAL CIPHER BECAUSE IT IS BROKEN TNX

phrase2 = "sahyk iapkp daben opzwu kbpda naopk bukqn hebau"

bf_result2 = HistoricCiphers::CaesarCipher.brute_force_decrypt(phrase2)

puts bf_result2

# 22=>"WELCO METOT HEFIR STDAY OFTHE RESTO FYOUR LIFEY",
# WELCOME TO THE FIRST DAY OF THE REST OF YOUR LIFE Y
binding.pry