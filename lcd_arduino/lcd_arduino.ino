#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);

String text1,text2,text3,text4,text5;
int i,z,x,lengthStr;

String getValue(String data, char separator, int index){           //breaks up text with a separator in it
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;
    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;}}
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";}

void lcdDrctPrint(String text_1,String text_2){     //prints the text directly to the screen
  lcd.setCursor(0,0);
  lcd.print(text_1);
  lcd.setCursor(0,1);
  lcd.print(text_2);
}

void lcdMidPrint(String text_1,String text_2){         //prints the text in the middle of the screen
  lcd.setCursor(int((16-text_1.length())/2),0);
  lcd.print(text_1);
  lcd.setCursor(int((16-text_2.length())/2),1);
  lcd.print(text_2);
}

void lcdScrllRigth(String text_1,String text_2){      //scrolls the text to the right and the text goes back to the screen from the left
  lengthStr = text_1.length();
  if(text_2.length() > lengthStr){lengthStr = text_2.length();}
  text4="";text5="";
  for(i=0;i<16;i++){
      lcd.clear();
      lcd.setCursor(i,0);
      lcd.print(text_1);
      lcd.setCursor(i,1);
      lcd.print(text_2);
      delay(700);
      lcd.clear();}

  for(i=lengthStr;i>=0;i--){
      lcd.clear();
      text4 = String(text_1[i]) + text4;
      text5 = String(text_2[i]) + text5;
      lcd.setCursor(0,0);
      lcd.print(text4);
      lcd.setCursor(0,1);
      lcd.print(text5);
      delay(700);
      lcd.clear();}
}

void lcdOnebyOnePrint(String text_1,String text_2){                        //prints text by adding letters one by one to the screen
    text4="";text5="";
    lengthStr = text_1.length();
    if(text_2.length() > lengthStr){lengthStr = text_2.length();}
    for(i=0;i<lengthStr;i++){
      lcd.clear();
      text4 = text4 + String(text_1[i]);
      text5 = text5 + String(text_2[i]);
      lcd.setCursor(0,0);
      lcd.print(text4);
      lcd.setCursor(0,1);
      lcd.print(text5);
      delay(700);
      lcd.clear();
    }
    lcdFlashingPrint(text_1,text_2);
}

void lcdScrllLeft(String text_1,String text_2){       //shifts the text to the left to fit the lcd.
    lengthStr = text_1.length();
    if(text_2.length()> lengthStr){lengthStr = text_2.length();}
    text4="";text5="";
    for(i=0;i<lengthStr-15;i++){
        lcd.clear();
        for(x=i;x<lengthStr;x++){
            text4 = text4 + String(text_1[x]);
            text5 = text5 + String(text_2[x]);}
        lcd.setCursor(0,0);
        lcd.print(text4);
        lcd.setCursor(0,1);
        lcd.print(text5);
        delay(700);
        text4="";text5="";
    }
}

void lcdFlashingPrint(String text_1,String text_2){            //flashing intermittently
    for(i=0;i<5;i++){
    lcd.setCursor(0,0);
    lcd.print(text_1);
    lcd.setCursor(0,1);
    lcd.print(text_2);
    delay(700);
    lcd.clear();
    delay(400);
    }    
}

void setup() {
  Serial.begin(9600);
  lcd.begin();     //begin lcd
  lcd.clear();
  delay(100);
}

void loop(){
    if(Serial.available()>0){
        lcd.clear();
        String myS = Serial.readString();          // receives information from serial port
        String text2 = getValue(myS, '^', 0);      // takes 1. text
        String text3 = getValue(myS, '^', 1);      // takes 2. text
        String text4 = getValue(myS, '^', 2);      // gets the animation number

        if(text4=="1"){while(Serial.available()==0){lcdDrctPrint(text2,text3);}}         //The animations continue as long as there is no information on the serial port
        else if(text4=="2"){while(Serial.available()==0){lcdMidPrint(text2,text3);}}
        else if(text4=="3"){while(Serial.available()==0){lcdScrllRigth(text2,text3);}}
        else if(text4=="4"){while(Serial.available()==0){lcdOnebyOnePrint(text2,text3);}}
        else if(text4=="5"){while(Serial.available()==0){lcdScrllLeft(text2,text3);}}
        else if(text4=="6"){while(Serial.available()==0){lcdFlashingPrint(text2,text3);}}
        else if(text4=="7"){lcd.clear();}         
    }   
}
