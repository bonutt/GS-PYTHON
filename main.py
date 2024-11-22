#RM560950
def media(consumos): #FUNÇAO QUE CALCULA A MEDIA DO CONSUMO DE ENERGIA
    return sum(consumos) / len(consumos)

def energia(consumo): #FUNÇAO QUE PASSA FEEDBACKS DO USO DE ENERGIA
    if consumo > 20:
        return "Diminua o uso de energia e considere usar mais energia solar."
    elif consumo > 10:
        return "Você está no caminho certo"
    else:
        return "Ótimo uso de energia!"

consumos = [] #LISTA

print("Digite o consumo de energia em kwh para cada dia da semana:")


for i in range(7): #COLETA DOS DADOS FORNECIDOS
    dia = input(f"Dia {i+1}: ")
    consumos.append(int(dia))

mediaConsumo = media(consumos)
print(f"\nMédia de consumo de energia durante a semana: {mediaConsumo:.2f} kWh")
print(energia(mediaConsumo))
print("\nConsumo diário de energia:")

i = 1
#ANALISE INDIVIDUAL DOS DIAS DA SEMANA
for consumo in consumos:
    print(f"Dia {i}: {consumo} kwh - {energia(consumo)}")
    i += 1
