#!/usr/bin/env ruby

start_num = ARGV[0].to_i
count = ARGV[1].to_i

list = []

for i in 0...count do
    list.push(i * start_num)
end

sum = 0
divisible = 0

list.each do |num|
    sum += num
    if num % 10 == 0 then
        divisible += 1
    end
end

puts "#{sum} #{divisible}"
