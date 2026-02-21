import time


def sunday(texto, padrao):
    n, m = len(texto), len(padrao)
    if m > n:
        return [], 0

    saltos = {char: m + 1 for char in set(texto)}
    for j in range(m):
        saltos[padrao[j]] = m - j

    ocorrencias = []
    comparacoes = 0
    i = 0
    while i <= n - m:
        for j in range(m):
            comparacoes += 1
            if texto[i + j] != padrao[j]:
                break
        else:
            ocorrencias.append(i)

        if i + m < n:
            i += saltos.get(texto[i + m], m + 1)
        else:
            break

    return ocorrencias, comparacoes


txt_dna = "ATGC" * 25000
pat_dna = "ATGCATGC"

inicio = time.perf_counter()
indices, comps = sunday(txt_dna, pat_dna)
fim = time.perf_counter()

print(f"Resultado, Boyer Moore Sunday:")
print(f"Tempo: {(fim - inicio) * 1000:.4f} ms")
print(f"Comparações: {comps}")
print(f"Ocorrências: {len(indices)}")
