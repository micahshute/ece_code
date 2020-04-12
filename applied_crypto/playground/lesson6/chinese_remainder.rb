require 'set'

class ModuloSieve

    attr_accessor :mod, :remainder, :max, :nums

    def initialize(mod, remainder, max=nil)
        @mod, @remainder, @max = mod, remainder, max
        @nums = Set.new
    end


    def include?(num)
        num % mod == remainder
    end

    def populate_nums
        (remainder..max).step(mod) do |n|
            @nums.add(n)
        end
    end

end


class SieveConglomorate

    attr_accessor :sieves, :first_set, :nums

    def initialize(*sieves)
        @sieves = sieves
        @first_set = true
        @nums = Set.new
        @sieves.each do |s|
            add_sieve(s)
        end
    end

    def add_sieve(s)
        if @first_set
            s.populate_nums
            @nums.merge(s.nums)
            @first_set = false
        else  
            throw NoAnswerError.new if @nums.empty? 
            @nums.delete_if do |n|
                !s.include?(n)
            end
        end
        
    end

    class NoAnswerError < StandardError

    end

end

# max = 5000
# s1 = ModuloSieve.new(2, 1, max)
# s2 = ModuloSieve.new(3, 0, max)
# s3 = ModuloSieve.new(4, 3, max)
# s4 = ModuloSieve.new(5, 2, max)
# s5 = ModuloSieve.new(6, 3, max)
# s6 = ModuloSieve.new(7, 5, max)
# s7 = ModuloSieve.new(8, 3, max)
# s8 = ModuloSieve.new(9, 6, max)


# cr = ChineseRemainder.new(s1, s2, s4, s6, s7, s8)
# puts cr.nums

class ModRemRing

    class NotCoprimeError < StandardError
    end
    
    #Mirror's sage's CRT; perform the chinese remainder theorem
    # by providing an array of residues and an array of mods
    def self.crt(remarr, modarr)
        raise ArgumentError.new if remarr.length != modarr.length
        rings = remarr.map.with_index {|rem, i| new(modarr[i], rem) } 
        chinese_remainder(rings)
    end

    def self.invmod(a,b)
        r, rm1 = b, a
        s, sm1 = 0, 1
        t, tm1 = 1, 0
        while r != 0
            q = rm1 / r
            rm1, r = r, rm1 % r
            sm1, s = s, sm1 - q * s
            tm1, t = t, tm1 - q * t
        end
        d = sm1 * a + tm1 * b
        return [d, sm1, tm1]
    end

    def self.coprime?(a,b)
        a.gcd(b) == 1
    end

    def self.pairwise_coprime?(rings)
        nxtrings = Array.new(rings)
        for i in (0...(rings.length - 1))
            for j in ((i+1)...rings.length)
                if !coprime?(rings[i].mod, rings[j].mod)
                    nxtrings = nxtrings.select{ |m| m != rings[j]}
                    # puts "#{rings[i]} and #{rings[j]} are NOT COPRIME!"
                    # raise NotCoprimeError.new("Modulos must be pairwise coprime!")
                end
            end
        end
        # puts rings.map(&:mod).to_s
        # puts nxtrings.map(&:mod).to_s
        nxtrings
    end

    def self.chinese_remainder(*rings)
        rings = rings.first if rings.first.is_a? Array
        rings = pairwise_coprime?(rings)
        n = rings.map(&:mod).reduce{|mem, el| el * mem}
        x = rings.reduce(0) do |mem, el|
            ai = el.remainder
            non = n / el.mod
            si = invmod(non, el.mod)[1]
            mem += ai * si * non
        end
        new(n, x % n)
    end

    attr_accessor :mod, :remainder, :nums

    def initialize(mod, remainder)
        @mod, @remainder = mod, remainder
        @nums = Enumerator.new do |g|
            start = @remainder % @mod
            loop do 
                g.yield start
                start = start + @mod
            end
        end
    end

    def include?(num)
        num % mod == remainder
    end

    def to_s
        "#{@remainder} (mod #{@mod})"
    end


end



# s1 = ModRemRing.new(2, 1)
# s2 = ModRemRing.new(3, 0)
# s3 = ModRemRing.new(4, 3)
# s4 = ModRemRing.new(5, 2)
# s5 = ModRemRing.new(6, 3)
# s6 = ModRemRing.new(7, 5)
# s7 = ModRemRing.new(8, 3)
# s8 = ModRemRing.new(9, 6)


# cr = ModRemRing.chinese_remainder(s4, s6, s7, s8)
# puts cr
# puts cr.nums.next
# puts cr.nums.next
# puts cr.nums.next


# puts r = ModRemRing.crt([2,0,1],[3,5,2])
# puts r.nums.next
# puts r.nums.next




