print ('Informações do carro')
carro = str(input ('Qual seu carro?'))
marca = str (input ('Qual marca?'))
km_p_litro = int (input ('Quantos Km seu carro faz por litro?'))
combustivel = float (input ('Qual o valor do combustível?'))
km_rodados = int (input ('Quantos km você rodou?'))

resultado_km = km_rodados / km_p_litro
resultado_gasto = resultado_km * combustivel

print ('Você gastou R$ {} rodando {} com combustível custando R$ {}'.format(resultado_gasto, km_rodados, combustivel))



