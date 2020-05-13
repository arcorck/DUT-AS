package com.example.bdapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.example.bdapp.Models.Task;
import com.example.bdapp.Tools.TaskViewModel;

public class MainActivity extends AppCompatActivity {

    TaskViewModel taskViewModel;
    TextView tvNbTask;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        this.taskViewModel = new ViewModelProvider(this).get(TaskViewModel.class);
        this.tvNbTask = findViewById(R.id.tvNbTasks);
    }

    public void ajouter (View view){
        this.taskViewModel.insert(new Task("Task 1", "description 1", 1));
        this.taskViewModel.insert(new Task("Task 2", "description 2", 2));
        this.taskViewModel.insert(new Task("Task 3", "description 3", 3));
    }

    public void actualiser (View view) {
        this.tvNbTask.setText("Nombre de tâches : " + taskViewModel.count());
    }
}
