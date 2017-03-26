package com.example.snc19.overlay;

import android.app.Application;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.MqttSecurityException;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.Timer;
import java.util.TimerTask;

/**
 * Created by snc19 on 25/3/17.
 */

public class MqttApplication extends Application {
    public static final String PREFS_NAME = "Clipper";
    private MqttAndroidClient client;
    public Context page;
    public AppCompatActivity activity;
    private String subscription;
    public String email;
    public String password;
    public void destroyClient(){
        try {
            client.disconnect();
        } catch (MqttException e) {
            //e.printStackTrace();
        }
    }

    @Override
    public void onCreate() {
        super.onCreate();
        connectClient();
        setCallback();
        SharedPreferences settings=getSharedPreferences(MqttApplication.PREFS_NAME,0);
        String x=settings.getString("emailid","-");
        String y=settings.getString("password","-");
        if(!x.equals("-") && !y.equals("-")){
            email=x;
            password=y;
        }
    }

    public boolean isConnected(){
        return client.isConnected();
    }
    public void connectClient(){
        MqttConnectOptions options = new MqttConnectOptions();

        String clientId = MqttClient.generateClientId();
        client = new MqttAndroidClient(this.getApplicationContext(), "tcp://139.59.79.171:1883", clientId);
        try {
            IMqttToken token = client.connect(options);
            token.setActionCallback(new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    Log.d("-----Connected-----","Connected");
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    //String s = String.valueOf(options.getPassword());
                }
            });
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    public void unsubscribe(){
        if(subscription!=null){
            try {
                Log.d("UnsubscribingInMqtt: ",subscription);
                client.unsubscribe(subscription);
            } catch (MqttException e) {
                e.printStackTrace();
            }
        }
    }

    public void setCallback(){
        client.setCallback(new MqttCallback() {
            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                JSONObject object=new JSONObject(message.toString());
                if(email.equals("-") || password.equals("-")){

                }
                else if(topic.equals(email+"/"+password+"/otp")){
                    Log.d("Requested OTP",message.toString());
                    if(object.has("otp") && object.has("status") && object.getString("status").equals("1")){
                        Timer t=new Timer();
                        final String otp=object.getString("otp");
                        Toast.makeText(page,"Connected to OTP Clipboard for 5 Minutes",Toast.LENGTH_SHORT).show();
                        CBManager.client.unsubscribe();
                        CBManager.attachListener(email+"/"+password+"/cc");
                        CBManager.client.subscribe(email+"/"+password+"/cc");
                        CBManager.inOtpMode(60*1000,null);
                    }

                }else if(topic.equals(email+"/"+password)){
                    Log.d("Arrived",message.toString());
                    if(object.has("status") && object.getBoolean("status")){
                        setSharedPreferences(topic);
                        changetologinactivity();
                    }else{
                        Toast.makeText(page,"Emailid & Password Do not match",Toast.LENGTH_SHORT).show();
                    }
                }else{
                    Log.d("Topic:",topic);
                    Log.d("Message Aya: ",message.toString());
                    if(object.has("message") && object.getString("message").equals("matched") && object.has("topic") && object.has("diff")){
                        Timer t=new Timer();
                        CBManager.client.unsubscribe();
                        CBManager.attachListener(object.getString("topic"));
                        CBManager.client.subscribe(object.getString("topic"));
                        CBManager.inOtpMode(60*1000-(long) (Float.valueOf(object.getString("diff"))*1000),object.getString("topic"));
                    }
                }
                unsubscribe();
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }

    public void setOTPCallback(final TextView otp_text){
        client.setCallback(new MqttCallback() {
            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                otp_text.setText(message.toString());
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }

    private void changetologinactivity(){
        Intent intent=new Intent(page,LoggedIn.class);
        activity.finish();
        startActivity(intent);
    }

    private void setSharedPreferences(String topic){
        Log.d("Setting Pref","Set to : "+topic);
        String[] args=topic.split("/");
        SharedPreferences settings = getSharedPreferences(PREFS_NAME, 0);
        SharedPreferences.Editor editor = settings.edit();
        editor.putString("emailid", args[0]);
        editor.putString("password", args[1]);
        editor.apply();
    }

   /* public void setRegisterCallback(){
        client.setCallback(new MqttCallback() {
            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("Received in Register",message.toString());
                JSONObject object=new JSONObject(message.toString());
                if(object.has("status") && object.getBoolean("status")){
                    setSharedPreferences(topic);
                    changetologinactivity();
                }else{
                    client.unsubscribe(topic);
                    subscribed=false;
                    Toast.makeText(page,"User already Exists",Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }*/

    public void requestOTP(String email,String password){
        try {
            client.subscribe(email+"/"+password+"/otp",0);
            client.publish("/requestotp",(email+"/"+password).getBytes(),0,false);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }
    public void pub(String topic,String message){
        try {
            client.publish(topic, message.getBytes(), 0, false);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }
    public void subscribe(String topic){
        try {
            Log.d("Subscribing to :",topic);
            client.subscribe(topic,0);
            if(subscription!=null){
                client.unsubscribe(subscription);
            }
            subscription=topic;
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

}
