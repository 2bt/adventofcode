
$_="1113222113";
for my $i (1...50) {s/1+|2+|3+/length($&).substr($&,0,1)/ge }
print length
