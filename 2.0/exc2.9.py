data_digitada = input("Digite uma data no formato mm/dd/aaaa: ")

if len(data_digitada) == 10:

    if data_digitada[2] == '/' and data_digitada[5] == '/':
        mes, dia, ano = data_digitada.split('/')
        
        if mes.isdigit() and dia.isdigit() and ano.isdigit():
            mes, dia, ano = int(mes), int(dia), int(ano)

            if 1 <= mes <= 12 and 1 <= dia <= 31 and 1000 <= ano <= 9999:
                print("A data é válida!")
            else:
                print("A data não é válida.")
        else:
            print("A data não é válida.")
    else:
        print("A data não é válida.")
else:
    print("A data não é válida.")
