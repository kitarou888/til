n, k = gets.split.map(&:to_i)
arrA = gets.split.map(&:to_i)

print ((arrA.select do |i|
  i % k == 0
end).map do |i|
  i / k
end).join(' ')

__END__
n = gets.to_i
arrTXY = (1..n).map do |arr|
  gets.split.map(&:to_i)
end

arrTXY.each_with_index do |n, i|
  if i > 0
    result = (n[0] - arrTXY[i - 1][0]) - ((n[1] - arrTXY[i - 1][1]).abs + (n[2] - arrTXY[i - 1][2]).abs)
  else
    result = n[0] - (n[1].abs + n[2].abs)
  end
  if !(result >= 0 && result <= n[0] - 1 && result % 2 == 0)
    print 'No'
    exit
  end
end

print 'Yes'
