#include "HC_SR04.h"



double cm = 0.0;
//bool beam_status = false;

int trigPin = A0;
int echoPin = A1;

long min_dist = 2;
long max_dist = 200;


HC_SR04 rangefinder = HC_SR04(trigPin, echoPin, min_dist, max_dist );


void setup() 
{
    Spark.variable("cm", &cm, DOUBLE);
    //Time.zone(+10);
}


boolean milk_state_check(long distance){
    
    boolean milk_state;
    
    if(distance < max_dist and distance > 20 ){
        milk_state = 0;
    }
    if(distance < 20 and distance > 0 ){
        milk_state = 1;
    }
    return milk_state;
}

String milk_gone_check(long distance){
    
    String milk_has_gone;
    
    if(milk_state_check(distance) == 0){
        milk_has_gone = "Gone";
    }
    if(milk_state_check(distance) == 1){
        milk_has_gone = "Have";
    }
    return milk_has_gone;
}

void loop() 
{
    cm = rangefinder.getDistanceCM();
    
    if(cm == -1){
        Particle.publish("Nothing in the range");
    }
    else{
        
        String milk_state_now = milk_gone_check(cm);
        Particle.publish("Distance(cm)" , String(cm));
        Particle.publish("Milk" , milk_state_now);
        //Particle.publish("Time ",Time.format(Time.now()));
    }
    
    delay(5000);
}
