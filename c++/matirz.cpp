#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <thread>
using namespace std;
using namespace std::chrono;
random_device rd;
mt19937 gen(rd());
uniform_int_distribution<> distrib(1000,10000);

vector<int> cria_vetor(int tamanho){
    vector<int> vetor(tamanho);
    for (int i = 0; i < tamanho; i++)
    {
        vetor[i] = distrib(gen);
    }
    return vetor;
}

vector<vector<int>> cria_matriz_thread(int tamanho){
    vector<vector<int>> matriz(tamanho);
    vector<thread> threads;
    for (int i = 0; i < tamanho; i++)
    {
        threads.emplace_back([i, tamanho, &matriz](){
            
            matriz[i] = cria_vetor(tamanho);
        });
    }
    for(auto& t: threads){
        t.join();
    }
    return matriz;
}
vector<vector<int>> cria_matriz(int tamanho){
    vector<vector<int>> matriz(tamanho);
    for (int i = 0; i < tamanho; i++)
    {
        matriz[i] = cria_vetor(tamanho);
    }
    return matriz;
}



void mostra_vetor(vector<int>& vetor){
    for (int num : vetor)
        cout << num << " ," ;     
    cout << endl;
}
int main(){
    auto inicioT = high_resolution_clock::now();
    cout << "criando uma matriz  com thread" << endl;
    cria_matriz_thread(15000);
    auto fimT = high_resolution_clock::now();
    auto duracaoT = duration_cast<milliseconds>(fimT - inicioT);
    cout << "matriz criada!" << endl;
    cout << "Tempo de execucao: " << duracaoT.count() << " ms " <<  endl;

    auto inicio = high_resolution_clock::now();
    cout << "criando uma matriz  " << endl;
    cria_matriz(15000);
    auto fim = high_resolution_clock::now();
    auto duracao = duration_cast<milliseconds>(fim - inicio);
    cout << "matriz criada!" << endl;
    cout << "Tempo de execucao: " << duracao.count() << " ms " <<  endl;
    
}