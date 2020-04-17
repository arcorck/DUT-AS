package com.example.intent;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void openURL(View view){
        EditText editText = findViewById(R.id.editTextURL);
        String url = editText.getText().toString();
        openWebPage("http://" + url);
    }

    public void openWebPage(String url){
        Uri webpage = Uri.parse(url);
        Intent intent = new Intent (Intent.ACTION_VIEW, webpage);
        if (intent.resolveActivity(getPackageManager()) != null){
            startActivity(intent);
        }else{
            Toast.makeText(this, "Impossible d'ouvrir un navigateur", Toast.LENGTH_SHORT).show();
        }
    }

    public void apppeler (View view){
        EditText editText = findViewById(R.id.editTextPhone);
        String phone = editText.getText().toString();
        dialPhoneNumber(phone);
    }

    public void dialPhoneNumber(String phoneNumber) {
        Intent intent = new Intent(Intent.ACTION_DIAL);
        intent.setData(Uri.parse("tel:" + phoneNumber));
        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }else{
            Toast.makeText(this, "Impossible d'ouvrir l'appli téléphone", Toast.LENGTH_SHORT).show();
        }
    }

    public void takePicture (View view){
        Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(intent, 1);
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == RESULT_OK) {
            if (requestCode == 1){
                Bitmap thumbnail = data.getParcelableExtra("data");
                ImageView imageView = findViewById(R.id.imageView);
                imageView.setImageBitmap(thumbnail);
            }
            else if (requestCode == 2) {
                //c'est activite 2 qui nous repond
                String reponse = data.getStringExtra("reponse");
                TextView textview = findViewById(R.id.textViewreponse);
                textview.setText(reponse);
            }
        }else{
            Toast.makeText(this, "Probleme", Toast.LENGTH_SHORT).show();
        }
    }

    public void Lanceact2 (View view){
        EditText editText = findViewById(R.id.editTextMessage);
        Intent intent = new Intent(this, MainActivity2.class);
        intent.putExtra("message", editText.getText().toString());
        startActivityForResult(intent, 2);
    }
}
