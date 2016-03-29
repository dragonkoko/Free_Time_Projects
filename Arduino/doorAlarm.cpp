/*GR-SAKURA Sketch Template Version: V1.08*/
#include <rxduino.h>
int buzzer_voltage = 7;
int buzzer_gnd = 5;
#define INTERVAL 100
void setup()
{
    pinMode(PIN_LED0,OUTPUT);
    pinMode(PIN_LED1,OUTPUT);
    pinMode(buzzer_voltage, OUTPUT);
    pinMode(buzzer_gnd, OUTPUT);
}
void loop()
{
    int sensor = analogRead(A1);
    if(sensor > 600) {
        digitalWrite(PIN_LED0, 1);
        digitalWrite(PIN_LED1, 0);
        digitalWrite(buzzer_voltage, LOW);
        digitalWrite(buzzer_gnd, LOW);
    } else {
        digitalWrite(buzzer_voltage, HIGH);
        digitalWrite(buzzer_gnd, LOW);
        digitalWrite(PIN_LED0, 0);
        digitalWrite(PIN_LED1, 1);
    }
    delay(20);
}
