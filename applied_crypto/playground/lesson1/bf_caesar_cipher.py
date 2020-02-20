from python_resources.ciphers import bf_decrypt_cc

msg1 = "hvwgw gqozz srobv wghcf wqozq wdvsf psqoi gswhw gpfcy sbhbl"
msg2 = "sahyk iapkp daben opzwu kbpda naopk bukqn hebau"
bf_res1 = bf_decrypt_cc(msg1)
bf_res2 = bf_decrypt_cc(msg2)

print(bf_res1) # (14, 'THISISCALLEDANHISTORICALCIPHERBECAUSEITISBROKENTNX')
print("---------------------------------------")
print(bf_res2) #  (22, 'WELCOMETOTHEFIRSTDAYOFTHERESTOFYOURLIFEY')