package com.example.bdapp.BD;

import androidx.room.Dao;
import androidx.room.Index;
import androidx.room.Insert;
import androidx.room.Query;

import com.example.bdapp.Models.Comment;

import java.util.List;

@Dao
public interface CommentDAO {
    @Insert
    void insert (Comment c);

    @Query("Select * from Comment where taskId = :id")
    List<Comment> getCommentTask(int id);
}
