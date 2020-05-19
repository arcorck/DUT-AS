package com.example.bdapp.Models;

import androidx.room.Entity;
import androidx.room.ForeignKey;
import androidx.room.PrimaryKey;
import static androidx.room.ForeignKey.CASCADE;

@Entity(foreignKeys = @ForeignKey(entity = Task.class, parentColumns = "id", childColumns = "taskId", onDelete = CASCADE))
public class Comment {
    @PrimaryKey (autoGenerate = true)
    private int id;
    private String commentaire;
    private int taskId;

    public Comment(String commentaire, int taskId) {
        this.commentaire = commentaire;
        this.taskId = taskId;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getCommentaire() {
        return commentaire;
    }

    public void setCommentaire(String commentaire) {
        this.commentaire = commentaire;
    }

    public int getTaskId() {
        return taskId;
    }

    public void setTaskId(int taskId) {
        this.taskId = taskId;
    }
}
