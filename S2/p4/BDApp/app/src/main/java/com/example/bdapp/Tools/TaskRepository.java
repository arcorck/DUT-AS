package com.example.bdapp.Tools;

import android.app.Application;
import android.os.AsyncTask;
import android.util.Log;

import androidx.lifecycle.LiveData;

import com.example.bdapp.BD.TaskDAO;
import com.example.bdapp.BD.TaskDataBase;
import com.example.bdapp.Models.Task;

import java.util.List;

public class TaskRepository {
    private TaskDAO taskDao;
    private LiveData<List<Task>> tasksLD;
    private LiveData<Integer> nbTasksLD;

    public TaskRepository (Application application){
        TaskDataBase taskDataBase = TaskDataBase.getDataBase(application);
        taskDao = taskDataBase.getTaskDao();
        tasksLD = taskDao.getTasksLD();
        nbTasksLD = taskDao.countLD();
    }

    public void insert (Task task){
        new InsertAsync(taskDao).execute(task);
    }

    private static class InsertAsync extends AsyncTask<Task, Void, Void>{
        private TaskDAO taskDAO;

        public InsertAsync (TaskDAO t){
            taskDAO = t;
        }

        @Override
        protected Void doInBackground(Task... tasks){
            taskDAO.insert(tasks[0]);
            return null;
        }
    }

    public void update (final Task task){
        AsyncTask.execute(new Runnable() {
            @Override
            public void run() {
                taskDao.update(task);
            }
        });
    }

    public void delete (final Task task){
        new DeleteAsync(taskDao).execute(task);
    }

    private static class DeleteAsync extends AsyncTask<Task, Void, Void>{
        private TaskDAO taskDAO;

        public DeleteAsync (TaskDAO t){
            taskDAO = t;
        }

        @Override
        protected Void doInBackground(Task... tasks){
            taskDAO.delete(tasks[0]);
            return null;
        }
    }

    public void deleteAll (){
        new DeleteAllAsync(taskDao).execute();
    }

    private static class DeleteAllAsync extends AsyncTask<Void, Void, Void>{
        private TaskDAO taskDAO;

        public DeleteAllAsync (TaskDAO t){
            taskDAO = t;
        }

        @Override
        protected Void doInBackground(Void ... args){
            taskDAO.deleteAll();
            return null;
        }
    }

    public Integer count (){
        try {
            return new CountAsync(taskDao).execute().get();
        }catch (Exception e){
            Log.d("MesLogs", "pb count");
        }
        return null;
    }

    private static class CountAsync extends AsyncTask<Void, Void, Integer>{
        private TaskDAO taskDAO;

        public CountAsync (TaskDAO t){
            taskDAO = t;
        }

        @Override
        protected Integer doInBackground(Void ... args){
            return taskDAO.count();
        }
    }

    public LiveData<List<Task>> getTasksLD() {
        return tasksLD;
    }

    public LiveData<Integer> getNbTasksLD() {
        return nbTasksLD;
    }

    public List<Task> getTasks(){
        try{
            return new GetTasksAsync(taskDao).execute().get();
        }catch (Exception e){
            Log.d("MesLogs", "pb liste de tâches");
        }
        return null;
    }

    private static class GetTasksAsync extends AsyncTask<Void, Void, List<Task>>{
        private TaskDAO taskDAO;

        public GetTasksAsync (TaskDAO t){
            taskDAO = t;
        }

        @Override
        protected List<Task> doInBackground(Void ... args){
            return taskDAO.getTasks();
        }
    }
}