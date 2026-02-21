import time


def horspool(texto, padrao):
    n, m = len(texto), len(padrao)
    if m > n:
        return [], 0

    saltos = {char: m for char in set(texto)}
    for j in range(m - 1):
        saltos[padrao[j]] = m - 1 - j

    ocorrencias = []
    comparacoes = 0
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0:
            comparacoes += 1
            if texto[i + j] == padrao[j]:
                j -= 1
            else:
                break

        if j < 0:
            ocorrencias.append(i)

        i += saltos.get(texto[i + m - 1], m)

    return ocorrencias, comparacoes


txt_dna = "ATGC" * 25000
pat_dna = "ATGCATGC"

inicio = time.perf_counter()
indices, comps = horspool(txt_dna, pat_dna)
fim = time.perf_counter()

print(f"Resultado, Boyer Moore Horspoo:")
print(f"Tempo: {(fim - inicio) * 1000:.4f} ms")
print(f"Comparações: {comps}")
print(f"Ocorrências: {len(indices)}")
