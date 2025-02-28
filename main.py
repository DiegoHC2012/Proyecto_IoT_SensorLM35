import network
import urequests
import utime
import machine

# Configuración de la conexión WiFi
SSID = "Nombre_De_La_Red_Wifi"
PASSWORD = "contraseñadelared123"

# Dirección de la API de ThingSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update?api_key=AQUITUKEYDETHINGSPEAK&field1="

# Configuración del sensor LM35
adc = machine.ADC(26)  # Pin GP26 (ADC0)

def connect_wifi():
    try:
        print("Iniciando conexión WiFi...")
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        print("WiFi activado.")

        wlan.connect(SSID, PASSWORD)
        tiempo_espera = 0
        print(f"Intentando conectar a {SSID}...")

        while not wlan.isconnected():
            utime.sleep(1)
            tiempo_espera += 1
            print(f"Esperando conexión... ({tiempo_espera} s)")
            if tiempo_espera > 10:
                print("Error: No se pudo conectar a WiFi. Reiniciando...")
                machine.reset()

        print("Conectado a WiFi:", wlan.ifconfig())

    except Exception as e:
        print(f"Error en connect_wifi(): {e}")

def leer_temperatura():
    try:
        lectura = adc.read_u16()  # Valor de 0 a 65535
        voltaje = (lectura / 65535.0) * 3.3  # Convertir a voltaje (3.3V referencia)
        temperatura = voltaje * 100  # LM35: 10mV/°C → Voltaje * 100
        return round(temperatura, 2)  # Redondear la temperatura a 2 decimales
    except Exception as e:
        print("Error leyendo el sensor:", e)
        return None  # Retornar None en caso de error

def enviar_a_thingspeak(temperatura):
    if temperatura is not None:
        try:
            url = THINGSPEAK_URL + str(temperatura)
            respuesta = urequests.get(url)
            print("Enviado a ThingSpeak:", respuesta.text)
            respuesta.close()
        except Exception as e:
            print("Error enviando a ThingSpeak:", e)
    else:
        print("No se enviará a ThingSpeak debido a un error en la lectura.")

# Conectar a la red WiFi
connect_wifi()

# Loop principal
while True:
    # Verificar que la conexión WiFi sigue activa
    if not network.WLAN(network.STA_IF).isconnected():
        print("Conexión WiFi perdida, reiniciando...")
        machine.reset()

    temperatura = leer_temperatura()
    if temperatura is not None:
        print(f"Temperatura: {temperatura:.2f}°C")
    
    enviar_a_thingspeak(temperatura)
    
    utime.sleep(15)  # Esperar 15 segundos antes de la próxima lectura

