#include <Servo.h>        //Servo library
 #define TURN_TIME 555

 Servo servo_test;      //initialize a servo object for the connected servo  
                
 char angle = 90;    
 int potentio = A0;      // initialize the A0analog pin for potentiometer

 
 void setup() 
 { 
  Serial.begin(9600);
  servo_test.attach(9);   // attach the signal pin of servo to pin9 of arduino
  //servo_test.write(90);
 } 
 
 void loop() 
 { 
  if (Serial.available())
    {
      Serial.println("inside if statement");
      angle = Serial.read();
      Serial.println(angle,DEC);
      servo_test.write(angle);
    }

  
  //angle = analogRead(potentio);            // reading the potentiometer value between 0 and 1023 
//  Serial.println(angle);
  //angle = map(angle, 0, 1023, 0, 179);     // scaling the potentiometer value to angle value for servo between 0 and 180) 
//  Serial.println(angle);
                     //command to rotate the servo to the specified angle 
   //delay(TURN_TIME); 
   //servo_test.write(90);
   delay(10);            
 }  
