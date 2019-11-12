# COLCOANDO CORES NO TERMINAL DO PYTHON

# STYLE
# \033[0;33;44m -----> Este codigo de cores semrpe tera est padrao \033[0,33,44m
# Onde na primeira parte 0 = NONE, 1 = BOLD, 4 = UNDERLINE e 7 = NEGATIVO

# CORES DO TEXTO
# 30 - BRANCO, 31 - VERMELHO, 32 - VERDE, 33 - AMARELO, 34 - AZUL, 35 - ROXO, 36 - AZUL CLARO, 37 - CINZA

# BACKGROUND
# 40 - BRANCO, 41 - VERMELHO, 42 - VERDE, 43 - AMARELO, 44 - AZUL, 45 - ROXO, 46 - AZUL CLARO, 47 - CINZA

a = 3
b = 5
print('Os valores sao \033[1;32m{}\033[m e \033[1;33m{}\033[m'.format(a, b))