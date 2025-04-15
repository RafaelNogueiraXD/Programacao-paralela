class Numero_Primo:
    def eh_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def contar_primos(self, intervalo):
        inicio, fim = intervalo
        total = 0
        for i in range(inicio, fim):
            if self.eh_primo(i):
                total += 1
        print(f"Intervalo {inicio}-{fim} tem {total} primos")
        return total

    def contar_primos_thread(self, intervalo, resultados, idx):
        inicio, fim = intervalo
        total = 0
        for i in range(inicio, fim):
            if self.eh_primo(i):
                total += 1
        print(f"Intervalo {inicio}-{fim} tem {total} primos")
        resultados[idx] = total
