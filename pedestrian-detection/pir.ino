void setup() {
  Serial.begin(9600);
}
void loop() {
  int sensorDegeri = analogRead(A0); /* Arduinonun A0 ayagindaki gerilim olculuyor */
  Serial.println(sensorDegeri);
  if(sensorDegeri!=0){
  Serial.println("1");
  digitalWrite(2,HIGH);
  }
  else
  digitalWrite(2,LOW);
  Serial.println("0");
}
