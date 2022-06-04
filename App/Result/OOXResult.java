package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class OOXResult extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result112);
        
        TextView OOX=findViewById(R.id.OOX);
        
        String[] OOXtxt=getResources().getStringArray(R.array.OOXtxt);
        Random random=new Random();
        int n= random.nextInt(OOXtxt.length-1);

        OOX.setText(OOXtxt[n]);
    }
}
