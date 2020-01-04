#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

unsigned int getNumLinesBetween(ifstream &ifs, size_t start, size_t end) {
    unsigned int numLines = 0;
    size_t pos = start;
    ifs.clear();
    ifs.seekg(start);
    while (ifs && pos < end) {
        string temp;
        getline(ifs, temp);
        numLines += 1;
        pos = ifs.tellg();
    }
    return numLines;
}

void printLastLines(const string &filename, unsigned int n, size_t startFrom) {
    ifstream ifs(filename);
    vector<string> circBuffer(n);
    if (ifs) {
        ifs.seekg(startFrom);
        int count = 0;
        while (ifs) {
            getline(ifs, circBuffer[count]);
            count += 1;
            count %= n;
        }

        int start = (count-1) % n;
        for (int i=0; i < n; ++i) {
            cout << circBuffer[(i+start) % n] << "\n";
        }

    } else {
        cout << "Error opening file: " << filename << "\n";
    }

}

void printLastLines(const string &filename, unsigned int n) {
    int granularity = 5;  // chars

    if (n <= 0) {
        return;
    }

    ifstream ifs(filename);
    if (ifs) {
        ifs.seekg(0, ios_base::end);
        size_t fileSize = ifs.tellg();
        size_t seekTo = fileSize;
        int totalLines = 0;
        while (seekTo > 0 && totalLines < n) {
            totalLines += getNumLinesBetween(ifs, seekTo-granularity, seekTo);
            seekTo -= granularity;
        }

        if (totalLines < n) {
            cout << "Not enough lines\n";
        }

        printLastLines(filename, n, seekTo);

    } else {
        cout << "Error opening file: " << filename << "\n";
    }
}

int main() {
    printLastLines("lines.txt", 10);
    return 0;
}