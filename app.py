def classificar_consumo():
    tipo_imovel = input('Digite o tipo de imóvel (comercial, casa, apartamento): ').strip().lower()

    if tipo_imovel not in ['comercial', 'casa', 'apartamento']:
        print('Erro: Tipo de imóvel inválido.')
        return

    try:
        consumo = float(input('Digite o consumo mensal de água em m³: '))
        if consumo < 0:
            print('Erro: O consumo não pode ser negativo.')
            return
    except ValueError:
        print('Erro: Insira um número decimal válido.')
        return

    # 1. Comercial
    if tipo_imovel == 'comercial':
        print('Tarifa comercial aplicada – consulte o plano corporativo.')
    
    # 2. Apartamento com consumo menor que 10 m³
    elif tipo_imovel == 'apartamento' and consumo < 10:
        print('Consumo econômico – excelente controle de água!')
    
    # 3. Apartamento (de 10 até 25) ou Casa com consumo de até 25 m³
    elif (tipo_imovel in ['apartamento', 'casa']) and consumo <= 25:
        print('Consumo moderado – dentro do padrão residencial.')
    
    # 4. Qualquer outro caso (consumo acima de 25 m³ para casa ou apartamento)
    else:
        print('Consumo excessivo – adote medidas de economia e verifique vazamentos.')

if __name__ == '__main__':
    classificar_consumo()

