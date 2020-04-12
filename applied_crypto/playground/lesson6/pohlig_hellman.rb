require_relative './chinese_remainder'
require 'openssl'

class PohligHellman


    def self.factor(num)
        factors = []
        for i in (2..(Math.sqrt(num).ceil))
    
            factors << i if num % i == 0
        end
        factors
    end
    
    attr_accessor :p, :g, :h

    def initialize(p: , g: , h: )
        @p, @g, @h = p, g, h
        @pm1_facts = PohligHellman.factor(@p - 1)
    end

    def crack
        pm1 = @p - 1
        chinese_remainder_mods = []
        @pm1_facts.each do |f|
            nexp = pm1 / f
            ngx = ->(x){ @g.to_bn.mod_exp(nexp * x,  @p).to_i }
            nh = @h.to_bn.mod_exp(nexp, @p).to_i
            for i in 0...f
                if ngx[i] == nh
                    chinese_remainder_mods << ModRemRing.new(f,i)
                    break
                end 
            end
        end
        ModRemRing.chinese_remainder(chinese_remainder_mods)
    end


    

end

p = 125301575591
g = 115813337451
h = 73973989900

# p = 31
# g = 3 
# h = 26

ph = PohligHellman.new(p: p, g: g, h: h)
a = ph.crack 
puts a

x = a.nums.next

puts g.to_bn.mod_exp(x, p)
puts h 

