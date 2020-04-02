package com.example.helloworld;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.TextureView;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void modifierTexte(View view){
        TextView tv1 = super.findViewById(R.id.textView1);
        TextView tv2 = super.findViewById(R.id.textView2);
        TextView tvbjr = super.findViewById(R.id.textviewbonjour);
        tvbjr.setText("On a modifie le texte");
        String aide = tv1.getText().toString();
        tv1.setText(tv2.getText().toString());
        tv2.setText(aide);
        Button button = (Button)view;
        button.setText("Mdifie aussi");
    }
}
