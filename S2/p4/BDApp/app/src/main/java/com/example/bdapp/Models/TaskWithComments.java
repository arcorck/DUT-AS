package com.example.bdapp.Models;

import androidx.room.Embedded;
import androidx.room.Relation;
import java.util.List;

public class TaskWithComments {
    @Embedded
    private Task task;

    @Relation(
            parentColumn = "id",
            entityColumn = "taskID"
    )
    private List<Comment> commentList;

    public Task getTask() {
        return task;
    }

    public List<Comment> getCommentList() {
        return commentList;
    }
}
