import requests


ondan_birim = str(input("Değiştirmek istediğiniz para birimini giriniz: "))

buna_birim = str(input("Yukarda girdiğiniz birimi hangi birime çevirmek istediğinizi giriniz: "))

miktar = float(input("Miktarı giriniz: "))

cevap = requests.get(f"https://www.frankfurter.app/latest?amount={miktar}&from={ondan_birim}&to={buna_birim}")

print(f"{miktar} {ondan_birim} is {cevap.json()['rates'][buna_birim]} {buna_birim}")
