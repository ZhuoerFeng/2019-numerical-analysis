
count = 0
for t = -16.0:0.1:0.0
    count = count + 1
    h(count) = 10. ^t
    sheru(count) = log10(2e-16) - t
    jieduan(count) = log10(h(count) / 2)
    total(count) = log10( h(count) / 2 + 2e-16 / h(count))
    real(count) =  log10(abs((sin(1 + h(count)) - sin(1)) / h(count) - cos(1)) + 10. ^jieduan(count))
    
end
sheru
jieduan
total
real
hold on
plot(log10(h), sheru)
plot(log10(h), jieduan)
plot(log10(h), total)
plot(log10(h), real)
