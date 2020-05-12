package com.example.recyclerview.Tools;

import android.content.Context;
import android.content.SharedPreferences;

import com.example.recyclerview.Models.Prof;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.ArrayList;

public class SaveRestoreData {

    Context context;


    public SaveRestoreData(Context context) {
        this.context = context;
    }

    public void saveArrayListProfs(ArrayList<Prof> lesProfs) {
        SharedPreferences sharedPreferences = context.getSharedPreferences("myData", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        Gson gson = new Gson();
        String json = gson.toJson(lesProfs);
        editor.putString("lesProfs", json);
        editor.apply();
    }

    public ArrayList<Prof> loadArrayListProfs(){
        SharedPreferences sharedPreferences = context.getSharedPreferences("myData",Context.MODE_PRIVATE);
        Gson gson = new Gson();
        String json =sharedPreferences.getString("lesProfs",null);
        Type type = new TypeToken<ArrayList<Prof>>(){}.getType();
        ArrayList<Prof> result = gson.fromJson(json,type);
        if (result == null){
            result = new ArrayList<>();
        }
        return result;
    }
}
