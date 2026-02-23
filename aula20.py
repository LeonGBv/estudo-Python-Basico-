primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

valor1 = f"primeiro valor = {primeiro_valor} é maior que segundo valor = {segundo_valor}"
valor2 = f"segundo valor = {segundo_valor} é maior que primeiro valor = {primeiro_valor}"

if primeiro_valor > segundo_valor:
    print(valor1)
else:
    print(valor2)