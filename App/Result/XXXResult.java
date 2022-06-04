package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class XXXResult extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result222);
        
        TextView XXX=findViewById(R.id.XXX);
        
        String[] XXXtxt=getResources().getStringArray(R.array.XXXtxt);
        Random random=new Random();
        int n= random.nextInt(XXXtxt.length-1);

        XXX.setText(XXXtxt[n]);
    }
}
