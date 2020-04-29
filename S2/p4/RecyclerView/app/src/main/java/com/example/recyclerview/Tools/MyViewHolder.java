package com.example.recyclerview.Tools;

import android.view.TextureView;
import android.view.View;
import android.widget.TextView;
import com.example.recyclerview.Models.Prof;
import com.example.recyclerview.R;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

//un ViewHolder permet de placer les objets (ici Prof) dans les cellules de la RecyclerView
public class MyViewHolder extends RecyclerView.ViewHolder {

    private TextView textViewNom, textViewMat;
    private Prof current;

    public MyViewHolder (final View view){
        super(view);
        textViewNom = view.findViewById(R.id.textViewNom);
        textViewMat = view.findViewById(R.id.textViewMat);
    }

    public void display(Prof prof){
        current = prof;
        textViewNom.setText(prof.getNom());
        textViewMat.setText(prof.getMat());
    }
}
