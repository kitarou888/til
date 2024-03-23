n = gets.to_i
str = gets.chomp
arrC = gets.split.map(&:to_i)

strA = ''
strB = ''

for i in 1..n-1 do
  for j in 1..n do
    strA << 1
    strB << 0
    if j == i
      strA << 
  end
end

# n, k = gets.split.map(&:to_i)
# arrA = gets.split.map(&:to_i)

# arrA_filter = (arrA.select { |num| num <= k }).uniq

# print (1..k).sum - arrA_filter.sum
