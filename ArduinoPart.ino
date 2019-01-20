int data;

void setup() 
{ 
  Serial.begin(9600); 
  pinMode(3, OUTPUT); 
  digitalWrite (3, LOW); //initially set to low
  
}
 
void loop() 
{
while (Serial.available())
  {
    data = Serial.read();
  }

  if (data == '1')
  analogWrite(3, 75);

  else if (data == '0')
  analogWrite (3, 0);

  else if (data =='2')
  analogWrite (3, 150);

  else if (data == '3')
  analogWrite(3, 255);

}
