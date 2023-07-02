import string
import itertools

# Dados do AFN - Defina os valores desejados aqui
states = {0, 1, 2}
initial_state = 0
transitions = {
    (0, 'a'): {0, 1},
    (0, 'b'): {0},
    (1, 'a'): {2},
    (2, 'a'): {2},
    (2, 'b'): {2},
}
final_states = {2}
alphabet = {'a', 'b'}

# Conversão do AFN para AFD
# Restante do código permanece igual

# Variáveis AFN
states_afn = states
states_final_afn = final_states
syms_afn = len(alphabet)
lines_afn = []
for state in states_afn:
    col = []
    for sym in alphabet:
        val = transitions.get((state, sym), set())
        col.append(val)
    lines_afn.append(col)

# Variáveis AFD
lines_afd = []
states_afd = 2 ** len(states_afn)
syms_afd = syms_afn

# Geração de combinação de estados
states_combinations_afd = []
for i in range(1, len(states_afn) + 1):
    for j in itertools.combinations(states_afn, i):
        states_combinations_afd.append(set(j))

# Criação da matriz AFD
for state in states_combinations_afd:
    arr_sym = [None] * syms_afn

    for tuple_state in state:
        for i, sym in enumerate(alphabet):
            tuple_aux = lines_afn[tuple_state][i]

            if arr_sym[i]:
                arr_sym[i] = arr_sym[i].union(tuple_aux)
            else:
                arr_sym[i] = set(tuple_aux)

    # Limpeza do array
    new_arr_sym = [tuple(aux) for aux in arr_sym]
    lines_afd.append(new_arr_sym)

# Verificação de estados inacessíveis
lines_not_using = []
for i in range(0, states_afd):
    for i_st, state in enumerate(states_combinations_afd):
        is_using = True
        for i_ln, line in enumerate(lines_afd):
            for l in line:
                if state == set(l) and i_st != i_ln and is_using and (i_ln not in lines_not_using):
                    is_using = False
        if is_using and (i_st not in lines_not_using):
            lines_not_using.append(i_st)

# Impressão do AFD
print("------------------ AFD GERADO ------------------")
def eFinal(states_final, state):
    for s1 in state:
        if s1 in states_final:
            return "(f)"
    return ""

for i_st, state in enumerate(states_combinations_afd):
    for i_ln, line in enumerate(lines_afd):
        if i_ln not in lines_not_using:
            if i_st == i_ln:
                for i, l in enumerate(line):
                    str_final1 = eFinal(states_final_afn, state)
                    str_final2 = eFinal(states_final_afn, set(l))
                    print(f'S{i_st}{str_final1}\t---{string.ascii_lowercase[i]}--->\tS{states_combinations_afd.index(set(l))}{str_final2}')
