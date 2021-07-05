int in1 = 11;  //Motor A 
int in2 = 10;   //Motor A 
int in3 = 9;  // Motor B
int in4 = 8;    //Motor B 
int enA = 6; // pwm Motor A 
int enB = 5;  // pwm Motor 
#define data_a 7
#define data_b 4
#define data_c 3
int ultra_data;
uint8_t data[2];
int count = 3;
void setup() {
  // put your setup code here, to run once:
pinMode(data_a,INPUT);
pinMode(data_b, INPUT);
pinMode(data_c, INPUT);
pinMode(in1,OUTPUT);
pinMode(in2,OUTPUT);
pinMode(in3,OUTPUT);
pinMode(in4,OUTPUT);
pinMode(in4,OUTPUT);
pinMode(enA,OUTPUT);
pinMode(enB,OUTPUT);
Serial.begin(9600);
}

void loop() {
//sensor_func_l();
//sensor_func_f();
//sensor_func_r();
  bool f[]={data_func_a(),data_func_b(),data_func_c()};
  for(int i = 0; i<count; i++){
     data[i] = f[i];
     bitWrite(ultra_data,i,data[i]);
  }
  
  Serial.println(ultra_data);
  switch(ultra_data){
        case(2):
        Serial.println("Backward");
 analogWrite(enA, 100);
 analogWrite(enB, 100);
digitalWrite(in1,0);
digitalWrite(in2,1);
digitalWrite(in3,0);
digitalWrite(in4,1);
delay(500);
break;
 case(3):
 Serial.println("Left");
  analogWrite(enA, 150);
 analogWrite(enB, 150);
digitalWrite(in1,1);
digitalWrite(in2,0);
digitalWrite(in3,0);
digitalWrite(in4,0);
break;

    case(0):
    Serial.println("Stop");
 analogWrite(enA, 150);
 analogWrite(enB, 150);
digitalWrite(in1,0);
digitalWrite(in2,0);
digitalWrite(in3,0);
digitalWrite(in4,0);
break;
    case(4):
    Serial.println("Right");
 analogWrite(enA, 150);
 analogWrite(enB, 150);
digitalWrite(in1,0);
digitalWrite(in2,0);
digitalWrite(in3,1);
digitalWrite(in4,0);
break;
 case(1):
 Serial.println("Forward");
analogWrite(enA, 100);
analogWrite(enB, 100);
digitalWrite(in1,1); // Motor right
digitalWrite(in2,0); // Motor right
digitalWrite(in3,1); // Motor left
digitalWrite(in4,0); // motor left
break;
 case(7):
 Serial.println("up_front");
analogWrite(enA, 100);
analogWrite(enB, 100);
digitalWrite(in1,1); // Motor right
digitalWrite(in2,0); // Motor right
digitalWrite(in3,1); // Motor left
digitalWrite(in4,0); // motor left
break;
 case(6):
 Serial.println("upward_opposite_right");
analogWrite(enA, 120);
analogWrite(enB, 120);
digitalWrite(in1,0); // Motor right
digitalWrite(in2,0); // Motor right
digitalWrite(in3,1); // Motor left
digitalWrite(in4,0); // motor left
break;
 case(5):
 Serial.println("upward_opposite_left");
analogWrite(enA, 120);
analogWrite(enB, 120);
digitalWrite(in1,1); // Motor right
digitalWrite(in2,0); // Motor right
digitalWrite(in3,0); // Motor left
digitalWrite(in4,0); // motor left
break;
default:
analogWrite(enA, 0);
analogWrite(enB, 0);
digitalWrite(in1,0);
digitalWrite(in2,0);
digitalWrite(in3,0);
digitalWrite(in4,0);
break;
  }
  // put your main code here, to run repeatedly:
}

bool data_func_a(){
  uint8_t Sn1 = digitalRead(data_a);
  if(Sn1 == 1){
    return true;
  }return false;
}

bool data_func_b(){
  uint8_t Sn2 = digitalRead(data_b);
  if(Sn2 == 1){
    return true;
  }
  return false;
}

bool data_func_c(){
  uint8_t Sn3 = digitalRead(data_c);
  if(Sn3 == 1){
    return true;
  }
  return false;
}
