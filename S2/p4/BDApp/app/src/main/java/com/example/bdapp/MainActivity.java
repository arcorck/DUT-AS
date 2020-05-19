package com.example.bdapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.example.bdapp.Models.Task;
import com.example.bdapp.Tools.TaskViewModel;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    TaskViewModel taskViewModel;
    TextView tvNbTask;
    TextView tvNBTasksLD;
    TextView tvTasksLD;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        this.taskViewModel = new ViewModelProvider(this).get(TaskViewModel.class);
        this.tvNbTask = findViewById(R.id.tvNbTasks);
        this.tvNBTasksLD = findViewById(R.id.tvNbTasksLD);
        this.taskViewModel.getNbTasksLD().observe(this, new Observer<Integer>() {
            @Override
            public void onChanged(Integer integer) {
                tvNBTasksLD.setText("nb tasksLD : " + integer);
            }
        });
        this.tvTasksLD = findViewById(R.id.tvListTaskLD);
        this.taskViewModel.getTasksLD().observe(this, new Observer<List<Task>>() {
            @Override
            public void onChanged(List<Task> tasks) {
                tvTasksLD.setText(" ");
                for (Task t : tasks){
                    tvTasksLD.setText(tvTasksLD.getText().toString() + " " + t.toString());
                }
            }
        });
    }

    public void ajouter (View view){
        this.taskViewModel.insert(new Task("Task 1", "description 1", 1));
        this.taskViewModel.insert(new Task("Task 2", "description 2", 2));
        this.taskViewModel.insert(new Task("Task 3", "description 3", 3));
    }

    public void actualiser (View view) {
        this.tvNbTask.setText("Nombre de tâches : " + taskViewModel.count());
    }

    public void deleteAll (View view){
        taskViewModel.deleteAll();
    }
}
