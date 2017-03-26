package com.example.snc19.overlay;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

/**
 * Created by snc19 on 25/3/17.
 */

public class RegisterActivity extends AppCompatActivity{
    private EditText register_email;
    private EditText register_password;
    private EditText register_confirm_password;
    private Button register_button;
    private MqttApplication application;

    @Override
    protected void onStart() {
        super.onStart();
        application.page=getApplicationContext();
        application.activity=this;
    }

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.register_layout);
        application=(MqttApplication)getApplication();
        register_button=(Button)findViewById(R.id.register_button);
        register_email=(EditText) findViewById(R.id.register_email);
        register_password=(EditText)findViewById(R.id.register_password);
        register_confirm_password=(EditText)findViewById(R.id.register_confirm_password);
        register_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(validate()){
                    application.email=register_email.getText().toString();
                    application.password=register_password.getText().toString();
                    application.subscribe(register_email.getText().toString()+"/"+register_password.getText().toString());
                    application.pub("/signup",register_email.getText().toString()+"/"+register_password.getText().toString());
                }
            }
        });
    }
    private boolean validate(){
        return true;
    }

}
