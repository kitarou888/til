n = gets.to_i
arrA = gets.split.map(&:to_i)

count = 0
arrA.sort.reverse.each_with_index do |x, i|
  if i % 2 == 0
    count += x
  else
    count -= x
  end
end

print count

__END__
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
