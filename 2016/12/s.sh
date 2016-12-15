#!/bin/sh
for c in 0 1
do
	awk 'BEGIN { print"#include <stdio.h>\nint main() {\nint a = 0, b = 1, c = '$c', d = 0;" }
	{ printf "l_%02x: ", NR }
	$1 == "jnz" { printf "if (%s) goto l_%02x;\n", $2, NR + $3 }
	$1 == "cpy" { printf "%s = %s;\n", $3, $2 }
	$1 == "inc" { printf "++%s;\n", $2 }
	$1 == "dec" { printf "--%s;\n", $2 }
	END { print"printf(\"%d\\n\", a);\n}" }' in | gcc -xc - && ./a.out
	rm -f a.out
done
