package com.example.snc19.overlay;

import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.content.SharedPreferences;
import android.os.IBinder;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class LoggedIn extends AppCompatActivity {

    private Button logoutbutton;
    private Button generateOtpButton;
    private Button connectToOtpButton;


    private EditText otpEditText;
    private TextView otpTextView;
    private String emailid;
    private String password;


    @Override
    protected void onDestroy() {
        super.onDestroy();
    }

    public TextView getOTPTextView(){
        return otpTextView;
    }

    public Button getGenerateOtpButton() {
        return generateOtpButton;
    }

    public Button getConnectToOtpButton() {
        return connectToOtpButton;
    }

    public EditText getOtpEditText() {
        return otpEditText;
    }

    @Override
    protected void onStart() {
        super.onStart();
        ((MqttApplication)getApplication()).activity=this;
        ((MqttApplication)getApplication()).page=getApplicationContext();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_logged_in2);
        logoutbutton=(Button) findViewById(R.id.logout_button);
        generateOtpButton=(Button) findViewById(R.id.generate_otp_button);
        connectToOtpButton=(Button) findViewById(R.id.connect_to_otp);
        otpEditText=(EditText) findViewById(R.id.otp_edittext);
        otpTextView=(TextView) findViewById(R.id.otp_text);
        ((MqttApplication)getApplication()).unsubscribe();

        SharedPreferences settings = getSharedPreferences(MqttApplication.PREFS_NAME, 0);
        emailid=settings.getString("emailid","-");
        password=settings.getString("password","-");
        if(!CBManager.isRunning) {
            Intent intent = new Intent(this, CBManager.class);
            startService(intent);
        }else if(!CBManager.client.isSubscribed && !emailid.equals("-") && !password.equals("-")){
            CBManager.client.subscribe(emailid+"/"+password);
        }

        logoutbutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CBManager.client.unsubscribe();
                SharedPreferences settings=getSharedPreferences(MqttApplication.PREFS_NAME,0);
                SharedPreferences.Editor editor=settings.edit();
                editor.clear();
                editor.apply();
                ((MqttApplication)getApplication()).setCallback();
                startActivity(new Intent(LoggedIn.this,LoginActivity.class));
                finish();
            }
        });

        generateOtpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!CBManager.otpMode){
                    Log.d("Clicked OTP","Clicked");
                    ((MqttApplication)getApplication()).subscribe(emailid+"/"+password+"/otp");
                    ((MqttApplication)getApplication()).pub("/requestotp",emailid+"/"+password+"/0");
                }else{
                    Toast.makeText(LoggedIn.this,"Already In OTP Mode",Toast.LENGTH_SHORT).show();
                }
            }
        });

        connectToOtpButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                if(!CBManager.otpMode){
                    String otp=otpEditText.getText().toString();
                    if(otp.length()==6){
                        ((MqttApplication)getApplication()).subscribe("/checkotp"+emailid+"/"+password);
                        ((MqttApplication)getApplication()).pub("/checkotp",emailid+"/"+password+"/"+otp);
                    }else{
                        Toast.makeText(LoggedIn.this,"Invalid OTP",Toast.LENGTH_SHORT).show();
                    }
                }else{
                    Toast.makeText(LoggedIn.this,"Already In OTP Mode",Toast.LENGTH_SHORT).show();
                }

            }
        });


    }
}
