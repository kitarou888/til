s = gets.chomp

size = s.length

result = []
(1..size).each do |i| # 何文字抜くか
  (0..size-1).each do |j| # どこから抜くか
    result.push s.slice(j, i)
  end
end

print result.uniq.length

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
