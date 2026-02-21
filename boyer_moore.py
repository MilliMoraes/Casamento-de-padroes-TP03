import time


def processar_mau_caractere(padrao):
    m = len(padrao)
    bad_char = {}
    for i in range(m):
        bad_char[padrao[i]] = i
    return bad_char


def processar_sufixo_bom(padrao):
    m = len(padrao)
    sufixo_bom = [0] * (m + 1)
    f = [0] * (m + 1)
    i = m
    j = m + 1
    f[i] = j
    while i > 0:
        while j <= m and padrao[i-1] != padrao[j-1]:
            if sufixo_bom[j] == 0:
                sufixo_bom[j] = j - i
            j = f[j]
        i -= 1
        j -= 1
        f[i] = j
    j = f[0]
    for i in range(m + 1):
        if sufixo_bom[i] == 0:
            sufixo_bom[i] = j
        if i == j:
            j = f[j]
    return sufixo_bom


def boyer_moore(texto, padrao):
    n = len(texto)
    m = len(padrao)
    if m == 0:
        return [], 0

    bad_char = processar_mau_caractere(padrao)
    sufixo_bom = processar_sufixo_bom(padrao)

    ocorrencias = []
    comparacoes = 0
    s = 0

    while s <= n - m:
        j = m - 1
        while j >= 0:
            comparacoes += 1
            if padrao[j] == texto[s + j]:
                j -= 1
            else:
                break

        if j < 0:
            ocorrencias.append(s)
            s += sufixo_bom[0]
        else:
            salto_mau_char = j - bad_char.get(texto[s + j], -1)
            salto_sufixo = sufixo_bom[j + 1]
            s += max(salto_mau_char, salto_sufixo)

    return ocorrencias, comparacoes


txt_dna = "ATGC" * 25000
pat_dna = "ATGCATGC"

inicio = time.perf_counter()
indices, comps = boyer_moore(txt_dna, pat_dna)
fim = time.perf_counter()

print(f"Resultado, Boyer Moore:")
print(f"Tempo: {(fim - inicio) * 1000:.4f} ms")
print(f"Comparações: {comps}")
print(f"Ocorrências: {len(indices)}")
