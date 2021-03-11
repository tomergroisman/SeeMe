/**************** Imports ****************/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

/************** Definitions **************/

#define MSG_BUFFER_SIZE  (255)
String CLASS_ID = "6047c75db313be4c8829b7d5";

/*********** Wifi Configuration **********/

// Update these with values suitable for your network.
const char* ssid = "Tomer&aya";
const char* password = "1702196060";

/*********** MQTT Configuration **********/

const char* broker = "18.133.245.223";
const char MQTT_CLIENTID[] = __DATE__ __TIME__;
char updateTopic[] = "see_me/update";
char previewTopic[] = "see_me/preview";

/************ Set Connections ************/

WiFiClient espClient;
PubSubClient mqtt(espClient);
unsigned long lastMsg = 0;
char msg[MSG_BUFFER_SIZE];
uint32_t lastReconnectAttempt = 0;

/********* Variable Declerations *********/

int lights[MSG_BUFFER_SIZE];

/********* Import Helper Classes *********/

#include "Connections.h"

/************* Sketch Logic **************/

// Setup callback
void setup() {
  
  Serial.begin(115200);
  
  connectToWifi();
  mqttConnect(false);
  
}

// Loop callback
void loop() {

  mqttLoop();
  
}
