require 'bcrypt'
require 'digest'

# salt = BCrypt::Engine.generate_salt
salt = "$2a$12$5Bx/CBG3xoXor78zB8DSRe"
password = 'password'



def salted_password_hash(password, salt, r)
    hash = ''
    r.times do
        hash = Digest::SHA2.new(256).hexdigest("#{hash}#{password}#{salt}")
    end
    hash
end

def time_test(password, salt, r)
    start = Time.now
    salted_password_hash(password, salt, r)
    fin = Time.now
    fin - start
end


def find_r(password, salt, desired_time_in_seconds)
    rval = 380000
    loop do 
        seconds_to_complete = time_test(password, salt, rval)
        puts "For r = #{rval}, seconds = #{seconds_to_complete}" if rval % 10 == 0
        break if seconds_to_complete > desired_time_in_seconds
        rval += 1
    end
    rval
end




def password_hasher(password)
    salt = BCrypt::Engine.generate_salt
    r = 380000
    hash= ''
    r.times do 
        hash = Digest::SHA2.new(256).hexdigest("#{hash}#{password}#{salt}")
    end
    [salt, r, hash]
end



# puts find_r(password, salt, 1) # 380000
password = "i<3wilmy"
password_hash_info = password_hasher(password)
puts password_hash_info.to_s

password_hash_check = salted_password_hash(password, password_hash_info[0], password_hash_info[1])
puts "check"
puts password_hash_check == password_hash_info[2]


