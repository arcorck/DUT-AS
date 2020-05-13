package com.example.bdapp.Models;

import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity(tableName = "Task_table")
public class Task {
    @PrimaryKey(autoGenerate = true)
    private int id;

    private String titre;
    private String description;
    private int priority;

    public Task(String titre, String description, int priority) {
        this.titre = titre;
        this.description = description;
        this.priority = priority;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitre() {
        return titre;
    }

    public void setTitre(String titre) {
        this.titre = titre;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
}
