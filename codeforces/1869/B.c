#include <stdio.h>
#include <limits.h>

long find_route(long a[2], long b[2]) {
    long dx = a[0] > b[0] ? a[0] - b[0] : b[0] - a[0];
    long dy = a[1] > b[1] ? a[1] - b[1] : b[1] - a[1];
    return dx + dy;
}

int main() {
    freeopen()
    int ts;
    scanf("%d", &ts);

    while (ts--) {
        int n, k;
        long a, b;
        scanf("%d %d %ld %ld", &n, &k, &a, &b);
        a--;
        b--;

        long cities[n][2];
        long x[2] = {LONG_MAX, LONG_MIN};
        long y[2] = {LONG_MAX, LONG_MIN};
        long np1 = LONG_MAX;
        long np2 = LONG_MAX;

        for (int i = 0; i < n; i++) {
            scanf("%ld %ld", &cities[i][0], &cities[i][1]);
        }

        for (int i = 0; i < k; i++) {
            long tgv = find_route(cities[i], cities[a]);
            np1 = tgv < np1 ? tgv : np1;

            tgv = find_route(cities[i], cities[b]);
            np2 = tgv < np2 ? tgv : np2;

            x[0] = cities[i][0] < x[0] ? cities[i][0] : x[0];
            x[1] = cities[i][0] > x[1] ? cities[i][0] : x[1];
            y[0] = cities[i][1] < y[0] ? cities[i][1] : y[0];
            y[1] = cities[i][1] > y[1] ? cities[i][1] : y[1];
        }

        long directx = a > b ? a - b : b - a;
        long directy = a > b ? a - b : b - a;
        long direct = directx + directy;

        long ind = np1 + np2;

        printf(">>> %ld\n", ind < direct ? ind : direct);
    }

    return 0;
}
