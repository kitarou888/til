s = gets.chomp
n = s.length

count1 = count2 = 0

for i in 1..n-1 do
  for j in i+1..n do
    if s[i-1] != s[j-1] then
      count1 += 1
    end
    count2 += 1
  end
end

if count1 != count2 then
  count1 += 1
end

print count1
