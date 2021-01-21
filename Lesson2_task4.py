st = input('Введите строку из нескольких слов разделенных пробелами ')

vs = (st.split())
dl = len(vs)

for i, vs in enumerate(vs, 1):
    print(f'{i} {vs[0:10]}')
