#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include <cstring>

const int LINHAS = 4;
const int COLUNAS = 4;

void calcularParteMatriz(int matriz[LINHAS][COLUNAS], int inicio, int fim) {
    for (int i = inicio; i < fim; ++i) {
        for (int j = 0; j < COLUNAS; ++j) {
            matriz[i][j] *= 2; // Exemplo de cálculo: multiplicar por 2
        }
    }
}

void imprimirMatriz(int matriz[LINHAS][COLUNAS]) {
    for (int i = 0; i < LINHAS; ++i) {
        for (int j = 0; j < COLUNAS; ++j) {
            std::cout << matriz[i][j] << " ";
        }
        std::cout << "\n";
    }
}

int main() {
    int matriz[LINHAS][COLUNAS] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    int pipefd[2]; // pipefd[0] = leitura, pipefd[1] = escrita
    pipe(pipefd);

    pid_t pid = fork();

    if (pid == 0) {
        // Processo filho
        close(pipefd[0]); // Fecha leitura

        calcularParteMatriz(matriz, 2, 4);

        // Escreve as linhas 2 e 3 no pipe
        write(pipefd[1], &matriz[2], sizeof(int) * COLUNAS * 2);
        close(pipefd[1]);
        _exit(0); // Encerra o processo filho
    } else if (pid > 0) {
        // Processo pai
        close(pipefd[1]); // Fecha escrita

        calcularParteMatriz(matriz, 0, 2); // Calcula linhas 0 e 1

        // Lê linhas 2 e 3 do filho
        read(pipefd[0], &matriz[2], sizeof(int) * COLUNAS * 2);
        close(pipefd[0]);

        wait(nullptr); // Espera o filho terminar

        std::cout << "Matriz final processada:\n";
        imprimirMatriz(matriz);
    } else {
        std::cerr << "Erro ao criar processo.\n";
    }

    return 0;
}
