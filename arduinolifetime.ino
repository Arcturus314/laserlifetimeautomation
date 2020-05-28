#define LEDON 1       // each led is on for this many seconds during sampling
#define SAMPLETIME 60 // total time for one sample - delay iteration
#define NUMLEDS 8    // will break if >12

// 10 LEDs on pins 2 -> NUMLEDS+2
int photodiodePin = A0;
long waittimems    = ((long)SAMPLETIME - (long)NUMLEDS * (long)LEDON)*(long)1000;

void setup() {
  // put your setup code here, to run once:
  for (int i = 2; i < NUMLEDS+2;i++) pinMode(i, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  // turning LEDs off
  for (int lednum = 0; lednum < NUMLEDS; lednum++) {
    digitalWrite(lednum+2, HIGH) ;
  }
  // sampling LEDs
  for (int lednum = 0; lednum < NUMLEDS; lednum++) {
    digitalWrite(lednum+2, LOW);
    delay(LEDON*1000);
    Serial.print(String(5*float(analogRead(photodiodePin))/1023));
    if (lednum < NUMLEDS-1) Serial.print(",");
    digitalWrite(lednum+2, HIGH);
  }
  Serial.print("\n");
  // turning LEDs on
  for (int lednum = 0; lednum < NUMLEDS; lednum++) {
    digitalWrite(lednum+2, LOW);
  }  
  delay(waittimems);

}
