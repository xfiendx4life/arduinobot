const int pinPump = 9;
const int Moister = A0;
const int power = 7;
int val = 0;  // for storing moisture value

void setup() {
  pinMode(pinPump, OUTPUT);
  Serial.begin(9600);
  pinMode(Moister,INPUT);
  pinMode(power, OUTPUT);
  digitalWrite(power, LOW);
  
}

int readSoil() {
    digitalWrite(power, HIGH);//turn D7 "On"
    delay(10);//wait 10 milliseconds 
    val = analogRead(Moister);//Read the SIG value form sensor 
    digitalWrite(power, LOW);//turn D7 "Off"
    return val;//send current moisture value
}
bool botMoister () {
  while(Serial.available()){
    char incomingChar = Serial.read();
    if (incomingChar == '1') {
      return true; 
      }
    return false;  
}
}
void loop() {
  int v = readSoil();
  bool botSignal = botMoister();
  Serial.print(botSignal + ' ');
  Serial.println(v);
  if (v<= 345 || botSignal) {
    analogWrite(pinPump, 255);
      delay(3000);
  }
  analogWrite(pinPump, 0);
  delay(5000);
  
}
