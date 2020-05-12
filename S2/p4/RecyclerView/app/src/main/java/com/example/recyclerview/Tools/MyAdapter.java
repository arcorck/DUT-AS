package com.example.recyclerview.Tools;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.recyclerview.widget.RecyclerView;
import com.example.recyclerview.Models.Prof;
import com.example.recyclerview.R;
import java.util.ArrayList;

public class MyAdapter extends RecyclerView.Adapter<MyViewHolder> {

    private static ArrayList<Prof> lesProfs;

    public MyAdapter (ArrayList<Prof> liste){
        lesProfs = liste;
    }

    public static void setLesProfs(ArrayList<Prof> lesProfs) {
        MyAdapter.lesProfs = lesProfs;
    }

    @Override
    public int getItemCount(){
        return lesProfs.size();
    }

    //Créer de nouvelles vues pour RecyclerView (invoqué par le layoutManager)
    @Override
    public MyViewHolder onCreateViewHolder(ViewGroup parent, int ViewType){
        //creer une nouvelle vue
        LayoutInflater layoutInflater = LayoutInflater.from(parent.getContext());
        View view = layoutInflater.inflate(R.layout.cell, parent, false);
        MyViewHolder myViewHolder = new MyViewHolder(view);
        return myViewHolder;
    }

    //Remplacer le contenu d'une vue (invoqué par le layoutManager)
    public void onBindViewHolder(MyViewHolder myViewHolder, int position){
        //recuperer un element depuis la structure de données (ici ArrayList)
        Prof prof = lesProfs.get(position);
        //remplacer le contenu de la vue avec cet element
        myViewHolder.display(prof);
        myViewHolder.setItemLongClickListener(new ItemLongClickListener() {
            @Override
            public void onItemLongClick(View view, int pos) {
                lesProfs.remove(pos);
                notifyDataSetChanged();
            }
        });
    }
}
