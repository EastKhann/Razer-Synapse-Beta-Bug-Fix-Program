import time

import psutil
import subprocess
isimm="razer"
try:

    for xxxx in range(1, 4):

        print(f"{xxxx}. Deneme: ")

        for proc in psutil.process_iter(['pid', 'name']):

            if proc.info['name'] != "":

                if isimm.lower() in str(proc.info['name']).lower():
                    isim = str(proc.info['name']).lower()
                    print(proc.info['name'])
                    if " " in proc.info['name']:
                        komut = f'taskkill /F /IM "{isim}"'
                    else:
                        komut = f"taskkill /F /IM {isim}"

                        subprocess.run(komut, check=True, shell=True)
                        print(isim, " Kapatıldı...")
except:
    gwgw=0

time.sleep(2)

exe_path = r'C:\\Program Files\\Razer\\RazerAppEngine\\RazerAppEngine.exe'
args = '--url-params=apps=synapse'

while True:
    try:
        # subprocess.Popen kullanarak komutu çalıştırma
        command = f'"{exe_path}" {args}'
        process = subprocess.Popen(command, shell=True)

        # İsteğe bağlı: Programın PID'sini yazdır
        print("Program başlatıldı, PID:", process.pid)
        break
    except Exception as e:
        print("Bir hata oluştu:", e)
        time.sleep(5)  # Kısa bir bekleme süresi ekleyerek yeniden deneyin

time.sleep(10)



