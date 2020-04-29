package com.example.recyclerview.Models;

import android.os.Parcel;
import android.os.Parcelable;

public class Prof implements Parcelable {
    private String nom, mat;

    public Prof(String nom, String mat) {
        this.nom = nom;
        this.mat = mat;
    }

    public Prof(Parcel parcel){
        this.nom = parcel.readString();
        this.mat = parcel.readString();
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getMat() {
        return mat;
    }

    public void setMat(String mat) {
        this.mat = mat;
    }

    @Override
    public int describeContents(){
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags){
        dest.writeString(nom);
        dest.writeString(mat);
    }

    public static Creator<Prof> CREATOR = new Creator<Prof>(){
        @Override
                public Prof createFromParcel(Parcel p){
            return new Prof(p);
        }

        @Override
                public Prof[] newArray(int i){
            return new Prof[i];
        }
    };
}
