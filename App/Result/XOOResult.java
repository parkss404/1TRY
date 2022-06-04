package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class XOOResult extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result211);
        
        TextView XOO=findViewById(R.id.XOO);
        
        String[] XOOtxt=getResources().getStringArray(R.array.XOOtxt);
        Random random=new Random();
        int n= random.nextInt(XOOtxt.length-1);

        XOO.setText(XOOtxt[n]);
    }
}
