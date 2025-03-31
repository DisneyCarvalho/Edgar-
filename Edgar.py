from PIL import Image
import numpy as np


def contar_pixels_brancos(caminho_imagem):
    imagem = Image.open(caminho_imagem).convert("1") 
    
    matriz_pixels = np.array(imagem)
    
    total_brancos = np.sum(matriz_pixels)
    
    return total_brancos



def conta_pixels_area(caminho_imagem):
    imagem = Image.open(caminho_imagem).convert("RGB")      
    matriz_pixels = np.array(imagem)

    r, g, b = matriz_pixels[:, :, 0], matriz_pixels[:, :, 1], matriz_pixels[:, :, 2]
    
    total_area = np.sum((b > r) & (b > g))
    

    return total_area


Area = {"EUA": 9867000, "CANADA": 9985000, "SA" : 17840000, "TOP-AMER": 719835, "LEFT-A-EU": 40900000 , "RUSSIA": 24906880, "SH-ASIA": 4500000, "AU-NZ": 7960045}

Results = {}


for i,o in Area.items():
    caminho = f"Tif//{i}.tif"  
    quantidade_brancos = int(contar_pixels_brancos(caminho))
    pixeis_area = int(conta_pixels_area(f"Png//{i}.png"))

    km_ppixel = round(Area[i]/pixeis_area,4) #Km por pixel da area
    print(km_ppixel,f"{i} km p pixel")
    Results[i] = round(km_ppixel*quantidade_brancos,4) #Km luminozo


total_Area = 0    
for i,o in Results.items():
    total_Area += Results[i] 

for i,o in Results.items():
    print(f"{i} {round(Results[i]/total_Area*100,2)}% ")

print(Results)

