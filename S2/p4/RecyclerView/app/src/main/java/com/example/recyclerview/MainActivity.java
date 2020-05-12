package com.example.recyclerview;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Parcelable;
import android.view.View;
import android.widget.Adapter;
import android.widget.EditText;

import com.example.recyclerview.Models.Prof;
import com.example.recyclerview.Tools.MyAdapter;
import com.example.recyclerview.Tools.SaveRestoreData;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private ArrayList<Prof> lesProfs = new ArrayList<>();
    private MyAdapter myAdapter;
    private LinearLayoutManager linearLayoutManager;
    private Parcelable recyclerState;
    private SaveRestoreData saveRestoreData;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        RecyclerView recyclerView = findViewById(R.id.recyclerView);
        linearLayoutManager = new LinearLayoutManager(this);
        recyclerView.setLayoutManager(linearLayoutManager);

        saveRestoreData = new SaveRestoreData(this);

        SharedPreferences sharedPref = getSharedPreferences("mesinfos", Context.MODE_PRIVATE);

        myAdapter = new MyAdapter(lesProfs);
        recyclerView.setAdapter(myAdapter);

        //lesProfs = saveRestoreData.loadArrayListProfs();
    }

    public void addProf (View view){
        EditText editTextNom = findViewById(R.id.editTextNom);
        EditText editTextMat = findViewById(R.id.editTextMat);
        Prof prof = new Prof (editTextNom.getText().toString(), editTextMat.getText().toString());
        lesProfs.add(prof);
        myAdapter.notifyDataSetChanged();
    }

    protected void onSaveInstanceState(@NonNull Bundle outState) {
        super.onSaveInstanceState(outState);
        recyclerState = linearLayoutManager.onSaveInstanceState();
        outState.putParcelable("infos", recyclerState);
        outState.putParcelableArrayList("donnees", lesProfs);
    }

    protected void onRestoreInstanceState (Bundle state){
        super.onRestoreInstanceState(state);
        if (state != null){
            recyclerState = state.getParcelable("infos");
            lesProfs = state.getParcelableArrayList("donnees");
            myAdapter.setLesProfs(lesProfs);
            myAdapter.notifyDataSetChanged();
        }
    }

    @Override
    protected void onResume (){
        super.onResume();
        if (recyclerState != null){
            linearLayoutManager.onRestoreInstanceState(recyclerState);
        }
        myAdapter.notifyDataSetChanged();
    }

    public void saveData(View view){
        saveRestoreData.saveArrayListProfs(lesProfs);
    }

    public void restoreData(View view){
        lesProfs = saveRestoreData.loadArrayListProfs();
        myAdapter.setLesProfs(lesProfs);
        myAdapter.notifyDataSetChanged();
    }

    @Override
    protected void onStop(){
        super.onStop();
        saveRestoreData.saveArrayListProfs(lesProfs);
    }
}
