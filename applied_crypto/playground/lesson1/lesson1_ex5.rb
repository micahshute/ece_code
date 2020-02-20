require 'digest'


phrase = "it is not the critic who counts"

hexdigest = Digest::SHA2.new(256).hexdigest(phrase)
digest = Digest::SHA2.new(256).digest(phrase)

puts hexdigest
puts digest
puts [hexdigest].pack "H*"
puts digest.bytes.map{|n| n.chr}.to_s
puts digest.bytes.map{|n| n.to_s(16)}.join

puts digest.bytes.to_s
puts hexdigest.bytes.to_s
# #pack("H*") turns ascii hex string to "actual" hex string
# #bytes turns each character into its numeric representation in base 10, outputs an array
# #chr on an integer turns that integer into its encoded character (which can be hex encoding)


# puts [digest].pack "H*"
# puts [digest].pack("H*").bytes.map{|n| n.chr}.to_s



