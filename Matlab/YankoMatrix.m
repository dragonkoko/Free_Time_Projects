m = 3;
n = 9;
a = zeros(m,n);
for i = 1:m
    for j = 1:n
        a(i,j) = ceil(mod(i-j,2));
    end
end

a(a == 0) = 4
a(a == 1) = 0
