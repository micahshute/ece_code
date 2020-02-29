require 'open-uri'
require 'nokogiri'
require 'httparty'

jokes_res = HTTParty.get('http://api.icndb.com/jokes?client=4&clientVersion=0.1')
# jokes_hash = JSON.parse(jokes_res, symbolize_names: true)
pg = URI.open('http://www.icndb.com/the-jokes-2/')
txt = pg.read
html = Nokogiri::HTML(txt)

jokes = html.css('p').map(&:text).filter{ |j| j.include?("Chuck Norris")}
jokes2 = jokes_res["value"].map{ |jh| jh["joke"]}
puts jokes.to_s
puts jokes2.to_s
