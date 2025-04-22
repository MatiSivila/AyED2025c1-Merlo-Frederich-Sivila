def radixsort(lista):
    maximo_numero = max(lista)  # Encontrar el número máximo en la lista
    exp = 1  # Inicializar el exponente para la posición actual (unidades, decenas, centenas, etc.)

    while maximo_numero // exp > 0:  # Mientras haya dígitos en el número máximo
        buckets = [[] for _ in range(10)]  # Crear 10 buckets para cada dígito (0-9)

        for numero in lista:  # Distribuir los números en los buckets según el dígito actual
            digito = (numero // exp) % 10  # Obtener el dígito en la posición actual
            buckets[digito].append(numero)

        lista = []  # Reiniciar la lista para volver a llenarla con los números ordenados por el dígito actual
        for bucket in buckets:
            lista.extend(bucket)

        exp *= 10  # Pasar al siguiente dígito (unidades,decenas,centenas, etc.)

    return lista  # Devolver la lista ordenada
    


        