import time


def rabinkarp(texto, padrao):
    n, m = len(texto), len(padrao)
    d, q = 256, 101
    h, p, t = 1, 0, 0
    ocorrencias = []
    comparacoes = 0

    if m > n:
        return [], 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(padrao[i])) % q
        t = (d * t + ord(texto[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                comparacoes += 1
                if texto[i + j] != padrao[j]:
                    break
            else:
                ocorrencias.append(i)

        if i < n - m:
            t = (d * (t - ord(texto[i]) * h) + ord(texto[i + m])) % q
            if t < 0:
                t += q

    return ocorrencias, comparacoes


txt_dna = "ATGC" * 25000
pat_dna = "ATGCATGC"

inicio = time.perf_counter()
indices, comps = rabinkarp(txt_dna, pat_dna)
fim = time.perf_counter()

print(f"Resultado, Rabin Karp:")
print(f"Tempo: {(fim - inicio) * 1000:.4f} ms")
print(f"Comparações: {comps}")
print(f"Ocorrências: {len(indices)}")
