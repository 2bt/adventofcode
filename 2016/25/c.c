#include <stdio.h>

int count;
int success;

int out(int x) {
   if (x != (count++ & 1)) return 0;
   if (count > 30) {
      success = 1;
      return 0;
   }
   return 1;
}

void try(int a) {
   int b = 1, c = 0, d = 0;
   l_01: d = a;
   l_02: c = 15;
   l_03: b = 170;
   l_04: ++d;
   l_05: --b;
   l_06: if (b) goto l_04;
   l_07: --c;
   l_08: if (c) goto l_03;
   l_09: a = d;
   l_0a: if (0) goto l_0a;
   l_0b: b = a;
   l_0c: a = 0;
   l_0d: c = 2;
   l_0e: if (b) goto l_10;
   l_0f: if (1) goto l_15;
   l_10: --b;
   l_11: --c;
   l_12: if (c) goto l_0e;
   l_13: ++a;
   l_14: if (1) goto l_0d;
   l_15: b = 2;
   l_16: if (c) goto l_18;
   l_17: if (1) goto l_1b;
   l_18: --b;
   l_19: --c;
   l_1a: if (1) goto l_16;
   l_1b: if (0) goto l_1b;
   l_1c: if (!out(b)) return;
   l_1d: if (a) goto l_0a;
   l_1e: if (1) goto l_09;
}


int main() {
   int a = 0;
   for (; a < 999999; ++a) {
      count = 0;
      success = 0;
      try(a);
      if (success) break;
   }
   printf("%d\n", a);
   return 0;
}
