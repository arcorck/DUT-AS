package com.example.recyclerview.Tools;

import android.app.AlertDialog;
import android.content.ClipData;
import android.view.TextureView;
import android.view.View;
import android.widget.TextView;
import com.example.recyclerview.Models.Prof;
import com.example.recyclerview.R;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

//un ViewHolder permet de placer les objets (ici Prof) dans les cellules de la RecyclerView
public class MyViewHolder extends RecyclerView.ViewHolder implements View.OnLongClickListener{

    private TextView textViewNom, textViewMat;
    private Prof current;
    private ItemLongClickListener itemLongClickListener;

    public MyViewHolder (final View view){
        super(view);
        textViewNom = view.findViewById(R.id.textViewNom);
        textViewMat = view.findViewById(R.id.textViewMat);

        view.setOnLongClickListener(this);

        view.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new AlertDialog.Builder(view.getContext())
                        .setTitle("Informations détaillées")
                        .setMessage("Nom : " + current.getNom() + "\nMatière : " + current.getMat())
                        .show();
            }
        });
    }

    @Override
    public boolean onLongClick(View view){
        this.itemLongClickListener.onItemLongClick(view, getLayoutPosition());
        return false;
    }

    public void setItemLongClickListener (ItemLongClickListener ic){
        this.itemLongClickListener = ic;
    }

    public void display(Prof prof){
        current = prof;
        textViewNom.setText(prof.getNom());
        textViewMat.setText(prof.getMat());
    }
}
