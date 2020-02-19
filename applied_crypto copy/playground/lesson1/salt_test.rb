require 'bcrypt'
require 'digest'


def hash256(password, salt, r=1)
    hash = ''
    r.times do 
        hash = Digest::SHA2.new(256).hexdigest "#{hash}#{password}#{salt}"
    end
    hash
end


# salt = BCrypt::Engine.generate_salt
salt = "$2a$12$5Bx/CBG3xoXor78zB8DSRe"
# puts "What is your password?"
# password = gets
password = 'password'

hexdigest = hash256(password, salt, 3)
puts hexdigest
# puts password + salt
x1 = Digest::SHA2.new(256).hexdigest "#{password}#{salt}"
x2 = Digest::SHA2.new(256).hexdigest "#{x1}#{password}#{salt}"
x3 = Digest::SHA2.new(256).hexdigest "#{x2}#{password}#{salt}"

puts "test: #{x3 == hexdigest ? 'passed' : 'failed'}"

