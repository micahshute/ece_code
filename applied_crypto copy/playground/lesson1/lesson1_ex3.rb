require 'digiproc'
require 'sqlite3'
require 'pry'

class RubySQL
    DB = {}

    def self.setup_database(name)
        system("touch #{name}.db")
        DB[:conn] = SQLite3::Database.open("#{name}.db")
        DB[:conn].results_as_hash = true
    end

    def self.run_migrations(*migrations)
        migrations.each do |m|
            m.new.change
        end
    end

end

class RubySQL::Migration
    
    def db
        RubySQL::DB[:conn]
    end
    
    def create_table(table_name)
        query = QueryManager.new("CREATE TABLE IF NOT EXISTS #{table_name} (id INTEGER PRIMARY KEY")
        yield(query)
        query.complete_query
        db.execute(query.current_query)
    end

    def add_column(table_name, col_name, col_type)
        query = QueryManager.new("ALTER TABLE #{table_name} ADD COLUMN #{col_name} #{col_type.upcase};")
        db.execute(query.current_query)
    end

    class QueryManager

        attr_reader :current_query

        def initialize(query_prefix)
            @current_query = query_prefix
        end

        def string(col_name)
            add_to_query(col_name, "TEXT")
        end

        def integer(col_name)
            add_to_query(col_name, "INTEGER")
        end

        def bigint(col_name)
            add_to_query(col_name, 'BIGINT')
        end

        def boolean(col_name)
            add_to_query(col_name, "BOOLEAN")
        end

        def complete_query
            @current_query += ");"
        end

        private 

        def add_to_query(col_name, type)
            @current_query += ", #{col_name} #{type}"
        end
    end

end






module Functions

    class CreateMemo < RubySQL::Migration
        def change
            create_table :factorial do |t|
                t.integer :input
                t.bigint :output
            end
        end
    end


    def self.get_memo(input)
        sql = "SELECT output FROM factorial WHERE input = ?"
        res = RubySQL::DB[:conn].execute(sql, input)[0]
        res ? res["output"] : res
    end

    def self.add_memo(input, output)
        sql = "INSERT INTO factorial (input, output) VALUES (? , ?);"
        RubySQL::DB[:conn].execute(sql, input, output)
    end

    def self.max_memo_input
        sql = 'SELECT MAX(input) FROM factorial'
        RubySQL::DB[:conn].execute(sql)[0]["MAX(input)"]
    end

    def self.initMemo
        RubySQL.setup_database('factorial')
        RubySQL.run_migrations(CreateMemo)
        RubySQL::DB[:conn].execute('INSERT INTO factorial (input, output) VALUES (1,1)')
    end

    def self.fact(num)
        return num if num == 1
        memoized = get_memo(num)
        return memoized if memoized
        val = num * fact(num - 1)
        add_memo(num, val)
        return val
    end

    def self.fact_and_memoize(num)
        begin
            return fact(num)
        rescue SystemStackError
            final_num = num
            for i in max_memo_input..final_num
                fact(i)
            end
            return fact(final_num)
        end
    end

    def self.num_permutations(n,k)
        return (fact_and_memoize(n)) / (fact_and_memoize(n - k))
    end

    def self.num_permutations2(n, k)
        nmk = n - k
        quotient = 1
        for i in n.downto(nmk + 1)
            quotient *= i
        end
        quotient
    end
end


Functions.initMemo

words_in_dict = 187632
sec_per_year = 60 * 60 * 24 * 366
words_per_sec = 187632 / 0.1
words_per_year = words_per_sec * sec_per_year
k = 3

permutations_no_repeats = Functions.num_permutations2(words_in_dict, k)


# puts Functions.max_memo_input


permutations = words_in_dict ** k

puts "Length of time to crack 2 hashed words from dictionary with #{words_in_dict} words: #{(words_in_dict ** 2).to_f / words_per_sec} seconds, which is #{((words_in_dict ** 2).to_f / (words_per_sec * 3600))  } hours"

puts "Words per second: #{words_per_sec}"
puts "Words per year: #{words_per_year}"
puts "WITH REPEATS"
puts "Permutations for #{k} letters chosen from dictionary: #{permutations}"
puts "Seconds to complete cracking #{k} words at a time: #{permutations.to_f / words_per_sec}"
puts "Years to complete cracking #{k} words at a time: #{permutations.to_f / words_per_year}"
puts "--------------------------------------------------------"
puts "NO REPEATS"
puts "Permutations for #{k} letters chosen from dictionary: #{permutations_no_repeats}"
puts "Seconds to complete cracking #{k} words at a time: #{permutations_no_repeats.to_f / words_per_sec}"
puts "Years to complete cracking #{k} words at a time: #{permutations_no_repeats.to_f / words_per_year}"

RubySQL::DB[:conn].close

# binding.pry