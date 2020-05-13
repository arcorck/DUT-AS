package com.example.bdapp.BD;

import android.content.Context;
import android.os.strictmode.InstanceCountViolation;

import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;

import com.example.bdapp.Models.Task;

@Database(entities = {Task.class}, version =1)
public abstract class TaskDataBase extends RoomDatabase {

    public abstract TaskDAO getTaskDao();

    private static TaskDataBase INSTANCE;

    public static TaskDataBase getDataBase(final Context context){
        if (INSTANCE == null){
            synchronized (TaskDataBase.class){
                if (INSTANCE == null) {
                    INSTANCE = Room.databaseBuilder(context.getApplicationContext(), TaskDataBase.class, "task _database").build();
                }
            }
        }
        return INSTANCE;
    }
}
