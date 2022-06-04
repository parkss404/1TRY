package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class XXOResult extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result221);
        
        TextView XXO=findViewById(R.id.XXO);
        
        String[] XXOtxt=getResources().getStringArray(R.array.XXOtxt);
        Random random=new Random();
        int n= random.nextInt(XXOtxt.length-1);

        XXO.setText(XXOtxt[n]);
    }
}
