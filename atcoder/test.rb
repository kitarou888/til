n = gets.to_i
arrA = gets.split.map(&:to_i)

array = arrA.map do |i|
  count = 0
  while i % 2 == 0 do
    count += 1
    i /= 2
  end
  count
end

print array.min
