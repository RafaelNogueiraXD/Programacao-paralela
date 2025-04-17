#include <iostream>
#include <thread>
using namespace std;

void tarefa_simples() {
    cout << "Executando tarefa na thread...\n";
}

int main() {
    thread minhaThread(tarefa_simples); // Cria e inicia a thread

    cout << "Executando no thread principal.\n";

    minhaThread.join(); // Espera a thread terminar antes de continuar

    cout << "Thread finalizada.\n";
    return 0;
}
