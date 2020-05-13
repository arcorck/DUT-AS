package com.example.bdapp.BD;

import androidx.lifecycle.LiveData;
import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;
import androidx.room.Update;

import com.example.bdapp.Models.Task;

import java.util.List;

@Dao
public interface TaskDAO {
    @Insert
    void insert (Task task);

    @Update
    void update (Task task);

    @Delete
    void delete (Task task);

    @Query("Delete FROM Task_table")
    void deleteAll();

    @Query("SELECT count(*) FROM Task_table")
    int count();

    @Query("SELECT count(*) FROM Task_table")
    LiveData<Integer> countLD();

    @Query("SELECT * FROM Task_table order by priority desc")
    List<Task> getTasks();

    @Query("SELECT * FROM Task_table order by priority desc")
    LiveData<List<Task>> getTasksLD();
}
