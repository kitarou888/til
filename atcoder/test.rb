n = gets.to_i
arrD = (1..n).map do |i|
  value = gets.to_i
end

print arrD.sort.uniq.length

__END__
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
