package com.example.tp2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d("MesLogs","onCreate");
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onStart(){
        super.onStart();
        Toast.makeText(this, "Onstart",Toast.LENGTH_SHORT).show();
        Log.d("MesLogs","onStart");
    }

    @Override
    protected void onResume(){
        super.onResume();
        Toast.makeText(this, "Onresume",Toast.LENGTH_SHORT).show();
        Log.d("MesLogs","onResume");
    }

    @Override
    protected void onPause(){
        super.onPause();
        Toast.makeText(this, "Onpause",Toast.LENGTH_SHORT).show();
        Log.d("MesLogs","onPause");
    }

    @Override
    protected void onStop(){
        super.onStop();
        Toast.makeText(this, "Onstop",Toast.LENGTH_SHORT).show();
        Log.d("MesLogs","onStop");
    }

    @Override
    protected void onDestroy(){
        super.onDestroy();
        Toast.makeText(this, "Ondestroy",Toast.LENGTH_SHORT).show();
        Log.d("MesLogs","onDestroy");
    }

    @Override
    protected void onRestart(){
        super.onRestart();
        Toast.makeText(this, "Onrestart",Toast.LENGTH_SHORT).show();
        Log.d("MesLogs","onRestart");
    }

    public void onSaveInstanceState(Bundle savedInstanceState){
        Log.d("MesLogs","onSaveInstanceState");
        TextView textView = findViewById(R.id.textViewNbRotations);
        Integer nbRotations = Integer.parseInt(textView.getText().toString());
        savedInstanceState.putInt("NbRotations",nbRotations);
        super.onSaveInstanceState(savedInstanceState);
    }

    public void onRestoreInstanceState(Bundle savedInstanceState){
        super.onRestoreInstanceState(savedInstanceState);
        Integer nbRotations=savedInstanceState.getInt("NbRotations");
        TextView textView = findViewById(R.id.textViewNbRotations);
        textView.setText(""+(nbRotations+1));
        Log.d("MesLogs","onRestoreInstanceState");
    }
}
