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

__END__
n = gets.to_i
arrD = (1..n).map do |i|
  value = gets.to_i
end

print arrD.sort.uniq.length

