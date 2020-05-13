package com.example.bdapp.Tools;

import android.app.Application;
import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import com.example.bdapp.Models.Task;
import java.util.List;

public class TaskViewModel extends AndroidViewModel {

    private TaskRepository taskRepository;
    LiveData<Integer> nbTasksLD;
    LiveData<List<Task>> tasksLD;

    public TaskViewModel(@NonNull Application application) {
        super(application);
        this.taskRepository = new TaskRepository(application);
        this.nbTasksLD = taskRepository.getNbTasksLD();
        this.tasksLD = taskRepository.getTasksLD();
    }

    public void insert(Task task){
        taskRepository.insert(task);
    }

    public void update(Task task){
        taskRepository.update(task);
    }

    public void delete(Task task){
        taskRepository.delete(task);
    }

    public void deleteAll (){
        taskRepository.deleteAll();
    }

    public Integer count (){
        return taskRepository.count();
    }

    public List<Task> getTasks(){
        return taskRepository.getTasks();
    }

    public LiveData<Integer> getNbTasksLD() {
        return nbTasksLD;
    }

    public LiveData<List<Task>> getTasksLD() {
        return tasksLD;
    }
}
