package com.example.snc19.overlay;

import android.app.IntentService;
import android.app.Service;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.content.SharedPreferences;
import android.os.IBinder;
import android.support.annotation.Nullable;
import android.util.Log;
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
import org.json.JSONObject;

import java.util.Timer;
import java.util.TimerTask;


/**
 * Created by snc19 on 25/3/17.
 */

public class CBManager extends Service implements LogTag{
    /*private MonitorTask mTask = new MonitorTask();
    private class MonitorTask extends Thread {

        private volatile boolean mKeepRunning = false;


        public MonitorTask() {
            super("ClipboardMonitor");
        }

        public void cancel() {
            mKeepRunning = false;
            interrupt();
        }

        @Override
        public void run() {
            mKeepRunning = true;
            while (true) {
                doTask();
                try {
                    Thread.sleep(mPrefs.getInt(AppPrefs.KEY_MONITOR_INTERVAL,
                            AppPrefs.DEF_MONITOR_INTERVAL));
                } catch (InterruptedException ignored) {
                }
                if (!mKeepRunning) {
                    break;
                }
            }
        }

        private void doTask() {
            if (mCM.hasPrimaryClip()) {
                String newClip = mCM.getPrimaryClip().getItemAt(0).getText().toString();
                if (!newClip.equals(mOldClip)) {
                    Log.i(TAG, "detect new text clip: " + newClip.toString());
                    mOldClip = newClip;
                    Log.d("Connected?", String.valueOf(client.isConnected()));
                    Log.d("Publish?", String.valueOf(toPublish));
                    if(!client.isConnected()){
                        connectClient();
                    }
                    if(client.isConnected() && toPublish){
                        pub(emailid+"/"+password+"/cc",newClip);
                    }else{
                        toPublish=true;
                    }
                }
            }
        }
    }
    */

    private SharedPreferences mPrefs;

    private static String emailid;
    private static String password;
    private static String mOldClip = null;
    private static boolean toPublish=true;
    public static ClipboardClient client;
    public static ClipboardManager mCM;
    public static boolean isRunning=false;
    public static boolean otpMode=false;
    private static ClipboardManager.OnPrimaryClipChangedListener primaryClipChangedListener;

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    public static void inOtpMode(long time,final String topic){
        otpMode=true;
        Timer t=new Timer();
        t.schedule(new TimerTask() {
            @Override
            public void run() {
                otpMode=false;
                if(topic!=null){
                    client.unsubscribe(topic);
                }

                //client.unsubscribe();
                CBManager.attachListener(emailid+"/"+password+"/cc");
                CBManager.client.subscribe(emailid+"/"+password+"/cc");
            }
        },time);
    }
    @Override
    public void onCreate() {
        super.onCreate();
        isRunning=true;
        SharedPreferences settings = getSharedPreferences(MqttApplication.PREFS_NAME, 0);
        emailid=settings.getString("emailid","-");
        password=settings.getString("password","-");
        Log.d("EMail",emailid);
        Log.d("Password",password);
        Log.d("Starting","Service");
        mCM = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
        mPrefs = getSharedPreferences(AppPrefs.NAME, MODE_PRIVATE);
        AppPrefs.operatingClipboardId = mPrefs.getInt(
                AppPrefs.KEY_OPERATING_CLIPBOARD,
                AppPrefs.DEF_OPERATING_CLIPBOARD);

        client=new ClipboardClient(CBManager.this, "tcp://139.59.79.171:1883", emailid + "/" + password+"/cc", new MqttCallback() {
            @Override
            public void connectionLost(Throwable cause) {
                Log.d("Connection Lost","Lost Connection");
            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("Self Clipboard",message.toString());
                if(!message.toString().equals(mOldClip)){
                    toPublish=false;
                    mCM.setPrimaryClip(ClipData.newPlainText("text", message.toString()));
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {}
        });
        attachListener(emailid+"/"+password+"/cc");

    }
    public static void attachListener(final String topic){
        if(primaryClipChangedListener!=null){
            mCM.removePrimaryClipChangedListener(primaryClipChangedListener);
        }
        primaryClipChangedListener=new ClipboardManager.OnPrimaryClipChangedListener() {
            @Override
            public void onPrimaryClipChanged() {
                if(client!=null){
                    Log.d("CHANGED","CLIPBOARD");
                    String newClip = mCM.getPrimaryClip().getItemAt(0).getText().toString();
                    if (!newClip.equals(mOldClip)) {
                        mOldClip = newClip;
                        Log.d("Connected?", String.valueOf(client.isConnected()));
                        Log.d("Publish?", String.valueOf(toPublish));
                        /*if(!client.isConnected()){
                            connectClient();
                        }*/
                        if(client.isConnected() && toPublish){
                            Log.d("Publishing :",topic+" "+newClip);
                            client.publish(topic,newClip);
                        }else{
                            toPublish=true;
                        }
                    }
                }
            }
        };
        mCM.addPrimaryClipChangedListener(primaryClipChangedListener);
    }

    /*private void pub(String topic,String message){
        try {
            client.publish(topic, message.getBytes(), 0, false);
            Log.d("Publishing",message);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }*/
    private void connectClient(){
       /* MqttConnectOptions options = new MqttConnectOptions();

        String clientId = MqttClient.generateClientId();
        client = new MqttAndroidClient(this, "tcp://139.59.79.171:1883", clientId);
        try {
            IMqttToken token = client.connect(options);
            token.setActionCallback(new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    Log.d("-Connected Service--","Connected");
                    try {
                        client.subscribe(emailid+"/"+password+"/cc",0);
                        Log.d("Subscribed",emailid+"/"+password+"/cc");
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
        }*/

        /*client.setCallback(new MqttCallback() {
            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("Received in Register",message.toString());
                if(!message.toString().equals(mOldClip)){
                    toPublish=false;
                    mCM.setPrimaryClip(ClipData.newPlainText("text", message.toString()));
                }

            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });*/
    }

    @Override
    public void onDestroy() {
        Log.d("Destroying","Service");
        isRunning=false;
    }
}
