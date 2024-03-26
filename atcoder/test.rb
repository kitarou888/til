n, a, b = gets.split.map(&:to_i)

value = (1..n).select do |i|
  count = 0
  while true
    count += i % 10
    i /= 10
    break if i == 0
  end
  a <= count && count <= b
end

print value.sum
