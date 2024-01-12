#include <vector>
#include <cstdio>
#include <cstring>

std::vector<char> G(100000);
int S, W, T;
int L = 0;
int l = 0;

void find(int p) {
    if (p < 0 || p >= S || G[p] == '#') return;
    if (p == T) {
        if (l > L) L = l;
        return;
    }
    G[p] = '#';
    ++l;
    for (int d : {1, W, -1, -W}) {
        find(p + d);
    }
    G[p] = '.';
    --l;
}

int main() {
    FILE* f = fopen("input", "r");
    if (!f) return 1;
    S = fread(G.data(), 1, G.size(), f);
    fclose(f);
    W = strchr(G.data(), '\n') - G.data() + 1;
    T = S - 3;
    find(1);
    printf("%d\n", L);
    return 0;
}
