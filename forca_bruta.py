import time


def fbruta(texto, padrao):
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    comparacoes = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparacoes += 1
            if texto[i + j] == padrao[j]:
                j += 1
                if j == m:
                    ocorrencias.append(i)
            else:
                break

    return ocorrencias, comparacoes


txt_dna = "ATGC" * 25000
pat_dna = "ATGCATGC"

inicio = time.perf_counter()
indices, comps = fbruta(txt_dna, pat_dna)
fim = time.perf_counter()

tempo_ms = (fim - inicio) * 1000

print(f"Resultado, Força Bruta:")
print(f"Tempo: {tempo_ms:.4f} ms")
print(f"Comparações: {comps}")
print(f"Ocorrências encontradas: {len(indices)}")
