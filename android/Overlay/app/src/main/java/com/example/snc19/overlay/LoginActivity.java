package com.example.snc19.overlay;


import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Paint;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class LoginActivity extends AppCompatActivity {

    private EditText email_id;
    private EditText password;
    private MqttApplication application;

    @Override
    protected void onStart() {
        super.onStart();
        application.page=getApplicationContext();
        application.activity=this;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_layout);
        TextView textView=(TextView) findViewById(R.id.register_text);
        email_id=(EditText) findViewById(R.id.login_email);
        password=(EditText) findViewById(R.id.login_password);
        application=((MqttApplication)getApplication());
        Log.d("Application",application.toString());
        Log.d("isConnected to MQTT", String.valueOf(application.isConnected()));
        SharedPreferences settings = getSharedPreferences(MqttApplication.PREFS_NAME, 0);
        final String emailid_val=settings.getString("emailid","-");
        final String password_val=settings.getString("password","-");

        if(!emailid_val.equals("-") && !password_val.equals("-")){
            Intent intent=new Intent(this,LoggedIn.class);
            finish();
            startActivity(intent);
        }
        findViewById(R.id.login_button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("---SENDING---","data");
                if(validate()){
                    application.email=email_id.getText().toString();
                    application.password=password.getText().toString();
                    application.subscribe(email_id.getText().toString()+"/"+password.getText().toString());
                    application.pub("/register",email_id.getText().toString()+"/"+password.getText().toString());
                }
            }
        });
        textView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(LoginActivity.this,RegisterActivity.class);
                startActivity(intent);
            }
        });
        textView.setPaintFlags(textView.getPaintFlags()| Paint.UNDERLINE_TEXT_FLAG);
    }

    private boolean validate(){
        return true;
    }

}

