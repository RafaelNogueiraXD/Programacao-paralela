#include <iostream>
#include <unistd.h> // Para fork()

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        std::cout << "Processo filho: PID = " << getpid() << "\n";
    } else if (pid > 0) {
        std::cout << "Processo pai: PID = " << getpid() << ", filho = " << pid << "\n";
    } else {
        std::cerr << "Erro ao criar processo!\n";
    }

    return 0;
}