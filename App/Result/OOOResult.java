package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class OOOResult extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result111);
        
        TextView OOO=findViewById(R.id.OOO);
        
        String[] OOOtxt=getResources().getStringArray(R.array.OOOtxt);
        Random random=new Random();
        int n= random.nextInt(OOOtxt.length-1);

        OOO.setText(OOOtxt[n]);
    }
}
