package com.example.intent;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        Intent intent = getIntent();
        String message = intent.getStringExtra("message");
        TextView textView = findViewById(R.id.TextView4);
        textView.setText(message);
    }

    public void fermerApp2 (View view){
        finish();
    }

    @Override
    public void finish(){
        EditText editText = findViewById(R.id.editText);
        Intent intent = new Intent();
        intent.putExtra("reponse", editText.getText().toString());
        setResult(Activity.RESULT_OK, intent);
        super.finish();
    }
}
