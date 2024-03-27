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

__END__
n, total = gets.split.map(&:to_i)

(0..n).each do |x|
  (0..n - x).each do |y|
    if 1000 * x + 5000 * y + 10000 * (n - x - y) == total
      print "#{n - x - y} #{y} #{x}"
      exit
    end
  end
end

print '-1 -1 -1'
