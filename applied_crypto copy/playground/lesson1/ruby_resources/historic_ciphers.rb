require 'pry'

module HistoricCiphers
    class CaesarCipher


        def self.brute_force_decrypt(txt)
            all_keys = 0..26
            cs = new(0)
            all_keys.each_with_object({}) do |k, memo|
                cs.key = k
                memo[k] = cs.decrypt(txt)
            end
        end

        attr_accessor :key

        def initialize(key)
            @key = key
        end

        def encrypt(txt)
            to_txt(to_num(txt).map{ |n| n.is_a?(Integer) ? (n + @key) % 26 : n })
        end

        def decrypt(txt)
            to_txt(to_num(txt).map{ |n| n.is_a?(Integer) ?  (n + 26 - @key) % 26 : n })
        end


        private

        def to_num(txt)
            txt.upcase.split('').map{|c| c.ord.between?(65, 90) ? c.ord - 65 : c }
        end

        def to_txt(numarr)
            numarr.map{ |n| n.is_a?(Integer) && n.between?(0, 25) ? (n + 65).chr : n }.join('')
        end

    end


    class VigenereCipher

        attr_accessor :key

        def initialize(key)
            @key = key
        end

        def encrypt(txt)
            kns = keynums
            cc = CaesarCipher.new(0)
            ct = []
            txt = txt.upcase.gsub(/[^A-Z]/, '')
            txt.each_char.with_index do |c, i|
                cc.key = kns[i % kns.length]
                ct << cc.encrypt(c)
            end
            ct.join('')
        end

        private

        def keynums
            @key.upcase.split('').map{ |c| c.upcase.ord - 65 }
        end

    end

end

class CharAnalysis

    WORD_STATS = %w{E T A H O N I S D R L W U G M F Y C B P K V J Q X Z}

    attr_accessor :text, :n

    def initialize(text, n = 1)

        @text, @n = text.upcase.gsub(/[^A-Z]+/, ''), n
    end

    def hist
        ngram.each_with_object(Hash.new(0)){ |i, mem| mem[i] += 1 }#
    end

    def hist_prcnt
        mem_hist = self.hist
        sum = mem_hist.values.sum
        mem_hist.each_with_object({}){ |(k,v), mem| mem[k] = (v.to_f / sum) }.sort{ |(k1,v1), (k2,v2)| v2 <=> v1 }
    end

    def map_to_stats
        newtxt = text.split('')
        hp = self.hist_prcnt.map{|kv| kv.first }
        newtxt.map do |c|
            i = hp.index(c)
            WORD_STATS[i]
        end.join('')
    end

    private

    def ngram
        return @text.split('') if @n == 1
        @text.split('').each.with_index.reduce([]) do  |mem, (el, i)| 
            for i in -(n-1)..-1
                mem[i] += el if mem[i]
            end
            mem << el
            mem
        end.reject{ |ngram| ngram.length < @n }
    end

end

# cc = CaesarCipher.new(0)
# phrase = "ZBYYLUKLY"
# for key in 1..25
#     cc.key = key
#     puts "For key #{key} \n #{cc.decrypt(phrase)}"
#     puts "---------------"
# end

# phrase = "ZBYYLUKLY"
# ca = CharAnalysis.new(phrase)
# puts ca.hist_prcnt.to_s
# puts "----------------"
# ca.n = 2
# puts ca.hist_prcnt.to_s
# puts "----------------"
# ca.n = 3
# puts ca.hist_prcnt.to_s

# puts ca.map_to_stats

