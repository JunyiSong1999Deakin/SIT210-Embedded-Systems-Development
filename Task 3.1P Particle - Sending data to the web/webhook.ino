// This #include statement was automatically added by the Particle IDE.
#include <Adafruit_DHT.h>


#define DHTPIN D1
#define DHTTYPE DHT11


DHT dht(DHTPIN, DHTTYPE); // setting the instance


void setup() {
    Serial.begin(9600);
	dht.begin();
}


void loop() {
	float temp = dht.getTempCelcius();// Read temperature as Celsius
	sendData(temp);                     // sending data to Particle
    delay(15000);                       // Wait for 15 second
}

void sendData(float temp){
    if(!isnan(temp)){
        String tempstring= String(temp);    //converting float to string to avoid data conversion error
        Particle.publish("temp", tempstring, PRIVATE);
    }
}
