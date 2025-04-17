#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <chrono>
#include <random>

std::mutex mtx;
int contador = 0;

void incrementarContador(int id, int vezes) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(10, 100); // milissegundos

    for (int i = 0; i < vezes; ++i) {
        std::this_thread::sleep_for(std::chrono::milliseconds(dist(gen))); // Simula trabalho
        {
            std::lock_guard<std::mutex> lock(mtx);
            ++contador;
            std::cout << "Thread " << id << " incrementou para " << contador << '\n';
        }
    }
}

int main() {
    const int numThreads = 5;
    const int incrementoPorThread = 10;
    std::vector<std::thread> threads;

    for (int i = 0; i < numThreads; ++i) {
        threads.emplace_back(incrementarContador, i + 1, incrementoPorThread);
    }

    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Valor final do contador: " << contador << '\n';
    return 0;
}
