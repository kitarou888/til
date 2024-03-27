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

__END__
s = gets.chomp

s1 = 'dream'
s2 = 'dreamer'
s3 = 'erase'
s4 = 'eraser'

while true do
  if s.delete_suffix(s1) == s && s.delete_suffix(s2) == s && s.delete_suffix(s3) == s && s.delete_suffix(s4) == s
    print 'NO'
    exit
  end
  s.delete_suffix!(s1) if s.delete_suffix(s1) != s
  s.delete_suffix!(s2) if s.delete_suffix(s2) != s
  s.delete_suffix!(s3) if s.delete_suffix(s3) != s
  s.delete_suffix!(s4) if s.delete_suffix(s4) != s
  if s == ''
    print 'YES'
    exit
  end
end
