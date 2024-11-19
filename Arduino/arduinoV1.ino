//Este será la primera versión, que sólo enviará los datos sin dar ninguna señal de alarma ni nada por el estilo.
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>
#define DHTPIN 32
#define DHTTYPE DHT11
DHT dht(DHTPIN,DHTTYPE);
float valor_sensor;
const char* ssid = "Tec-IoT";
//Yo debo estar con el internet del Tec
const char* password = "spotless.magnetic.bridge";
// URL del servidor (cambia localhost por la IP de tu servidor)
const char* serverName = "http://10.25.124.239:5000/insert_data";
//Mi propio ip
void setup() {
 
 Serial.begin(115200);
 dht.begin();
 // Conectar a WiFi
 WiFi.begin(ssid, password);
 while (WiFi.status() != WL_CONNECTED) {
  delay(1000);
  Serial.println("Connecting to WiFi...");
 }
 Serial.println("Connected to WiFi");

}

void loop() {
 if (WiFi.status() == WL_CONNECTED) {
  valor_sensor = dht.readTemperature();
  HTTPClient http;
 // Configurar la URL y el header
  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");
 // Crear el JSON con el valor del sensor
  String nombre_sensor = "DHT11";
  String json = "{\"nombre_sensor\": \""+ nombre_sensor + "\", \"valor_sensor\": " + String(valor_sensor) + "}";
 // Hacer la solicitud POST
  int httpResponseCode = http.POST(json);
  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println(httpResponseCode);
    Serial.println(response);
 } else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
 }
  http.end();
 }
  delay(300000); // Esperar 5 minutos entre envíos
}
