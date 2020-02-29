require 'open-uri'
require 'nokogiri'


def extractor(tbits)
    if tbits == "01"
        "0"
    elsif tbits == "10"
        "1"
    else
        ""
    end
end

pg = URI.open('http://www.befria.nu/elias/pi/binpi.html')
txt = pg.read

html = Nokogiri::HTML(txt)

info = html.css('pre').text

byts = info.scan(/\s[10]+\s/).map(&:strip)

# puts byts.to_s

all_bytes = byts.join('')

extracted_bytes = all_bytes.split('').each_slice(2).map do |tb|
    extractor(tb.join(''))
end.join('')

puts extracted_bytes
puts extracted_bytes.length
puts all_bytes
puts all_bytes.length


