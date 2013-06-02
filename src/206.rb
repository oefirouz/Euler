
LOWER = 1020304050607080900
x = Math.sqrt(LOWER).floor

def check(x)
	x *= x
	for i in [0,9,8,7,6,5,4,3,2,1]
		digit = x % 10
		if digit != i
			return true
		end
		x /= 100
	end
	return false
end

while check(x)
	x += 10
end

puts x