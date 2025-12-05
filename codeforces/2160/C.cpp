#include <bits/stdc++.h>

using namespace std;

void checkPalindrome(int n) {
    string b = bitset<32>(n).to_string();
    int left = 0, right = 31;
    while (b[left] == '0') left++;
    while (b[right] == '0') right--;

    while (left < right) {
        if (b[left] == b[right]) {
            left++;
            right--;
            continue;
        }

        cout << "No" << endl;
        return;
    }

    if (left == right && b[left] != '0') {
        cout << "No" << endl;
        return;
    }

    cout << "Yes" << endl;
    return;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int a;
        cin >> a;
        checkPalindrome(a);
    }
}
