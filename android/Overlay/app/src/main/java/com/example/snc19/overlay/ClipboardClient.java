package com.example.snc19.overlay;

import android.content.Context;
import android.support.annotation.Nullable;
import android.util.Log;

import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;

/**
 * Created by snc19 on 25/3/17.
 */

public class ClipboardClient {
    private MqttAndroidClient client;
    private String topic;
    public boolean isSubscribed;

    public void subscribe(String topic){
        try {
            client.subscribe(topic,0);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    public ClipboardClient(final Context context, final String url, String topic_to_subscribe, @Nullable final MqttCallback callback){
        final MqttConnectOptions options = new MqttConnectOptions();
        final String clientId = MqttClient.generateClientId();
        topic=topic_to_subscribe;
        isSubscribed=true;
        Thread thread=new Thread(){
            @Override
            public void run() {
                super.run();
                client=new MqttAndroidClient(context,url,clientId);
                try {
                    IMqttToken token = client.connect(options);
                    token.setActionCallback(new IMqttActionListener() {
                        @Override
                        public void onSuccess(IMqttToken asyncActionToken) {
                            Log.d("-Connected Service--","Connected");
                            try {
                                client.subscribe(topic,0);
                                Log.d("Subscribed",topic);
                                if(callback!=null){
                                    client.setCallback(callback);
                                }
                            } catch (MqttException e) {
                                e.printStackTrace();
                            }
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
        };

        thread.run();
    }

    public boolean isConnected(){
        return client.isConnected();
    }

    public void publish(String topic,String message){
        try {
            client.publish(topic, message.getBytes(), 0, false);
            Log.d("Publishing",message);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    public void unsubscribe(String topic){
        try{
            client.unsubscribe(topic);
            isSubscribed=false;
            Log.d("Unsubsribe ClipClient","Unsubscribed"+topic);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    public void unsubscribe(){
        if(topic!=null){
            try {
                client.unsubscribe(topic);
                isSubscribed=false;
                Log.d("Unsubsribing","Unsubscribed");
            } catch (MqttException e) {
                e.printStackTrace();
            }
        }
    }

    public void setCallback(MqttCallback callback){
        client.setCallback(callback);
    }

    @Override
    protected void finalize() throws Throwable {
        super.finalize();
        try {
            client.disconnect();
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }
}
