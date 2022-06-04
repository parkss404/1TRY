package com.example.a1try.result;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.R;

public class XXXResult extends AppCompatActivity {
    
    private Button btn_222;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result222);
        
        TextView XXX=findViewById(R.id.XXX);
        btn_222=findViewById(R.id.btn_222);
        
        String[] XXXtxt=getResources().getStringArray(R.array.XXXtxt);
        Random random=new Random();
        int n= random.nextInt(XXXtxt.length-1);

        XXX.setText(XXXtxt[n]);
        
        btn_222.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String[] XXXtxt=getResources().getStringArray(R.array.XXXtxt);
                Random random=new Random();
                int n= random.nextInt(XXXtxt.length);

                XXX.setText(XXXtxt[n]);
            }
        });
    }
}
