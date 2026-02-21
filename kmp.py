import time


def kmp(padrao):
    m = len(padrao)
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and padrao[k] != padrao[q]:
            k = pi[k-1]
        if padrao[k] == padrao[q]:
            k += 1
        pi[q] = k
    return pi


def kmp_busca(texto, padrao):
    n, m = len(texto), len(padrao)
    if m == 0:
        return [], 0

    pi = kmp(padrao)
    q = 0
    ocorrencias = []
    comparacoes = 0

    for i in range(n):

        comparacoes += 1
        while q > 0 and padrao[q] != texto[i]:
            q = pi[q-1]
            comparacoes += 1

        if padrao[q] == texto[i]:
            q += 1

        if q == m:
            ocorrencias.append(i - m + 1)
            q = pi[q-1]

    return ocorrencias, comparacoes


txt_dna = "ATGC" * 25000
pat_dna = "ATGCATGC"

inicio = time.perf_counter()
indices, comps = kmp_busca(txt_dna, pat_dna)
fim = time.perf_counter()

print(f"Resultado, Knuth Morris Prat: ")
print(f"Tempo: {(fim - inicio) * 1000:.4f} ms")
print(f"Comparações: {comps}")
print(f"Ocorrências: {len(indices)}")
