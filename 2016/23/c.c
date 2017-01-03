#include <stdio.h>
typedef enum { cpy, dec, inc, jnz, tgl } Opcode;
Opcode toggle[] = { jnz, inc, dec, cpy, inc };
typedef struct { Opcode o; int v1; int r1; int v2; int r2; } Cmd;
Cmd cmds[] = {
   { cpy, 0, 1, 1, 1 },
   { dec, 1, 1 },
   { cpy, 0, 1, 3, 1 },
   { cpy, 0, 0, 0, 1 },
   { cpy, 1, 1, 2, 1 },
   { inc, 0, 1 },
   { dec, 2, 1 },
   { jnz, 2, 1, -2, 0 },
   { dec, 3, 1 },
   { jnz, 3, 1, -5, 0 },
   { dec, 1, 1 },
   { cpy, 1, 1, 2, 1 },
   { cpy, 2, 1, 3, 1 },
   { dec, 3, 1 },
   { inc, 2, 1 },
   { jnz, 3, 1, -2, 0 },
   { tgl, 2, 1 },
   { cpy, -16, 0, 2, 1 },
   { jnz, 1, 0, 2, 1 },
   { cpy, 75, 0, 2, 1 },
   { jnz, 78, 0, 3, 1 },
   { inc, 0, 1 },
   { inc, 3, 1 },
   { jnz, 3, 1, -2, 0 },
   { inc, 2, 1 },
   { jnz, 2, 1, -5, 0 },
};
int r[4] = { 12, 1, 0, 0 };
int main() {
   int v;
   int i = 0;
   while (i < 26) {
      Cmd c = cmds[i];
      switch (c.o) {
      case inc:
         if (c.r1) ++r[c.v1];
         break;
      case dec:
         if (c.r1) --r[c.v1];
         break;
      case cpy:
         if (c.r2) r[c.v2] = c.r1 ? r[c.v1] : c.v1;
         break;
      case jnz:
         if (c.r1 ? r[c.v1] : c.v1) i += (c.r2 ? r[c.v2] : c.v2) - 1;
         break;
      case tgl:
         v = i + (c.r1 ? r[c.v1] : c.v1);
         if (v >= 0 && v < 26) cmds[v].o = toggle[cmds[v].o];
         break;
      }
      ++i;
   }
   printf("%d\n", r[0]);
   return 0;
}
